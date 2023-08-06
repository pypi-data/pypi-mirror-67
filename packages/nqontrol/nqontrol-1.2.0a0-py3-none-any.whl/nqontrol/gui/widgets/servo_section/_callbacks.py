import logging as log

import numpy as np
from dash.exceptions import PreventUpdate
from fastnumbers import fast_real

from nqontrol.general import settings
from nqontrol.gui.dependencies import DEVICE

############################################################
#################### Autolock Widget #######################
############################################################


#################### Getters ###############################


def getLockString(servo):
    """Return a string description of the autolock state. This will be updated on a by-second interval. Contains information for the GUI on search state, relock and locked state.

    Parameters
    ----------
    servo : :obj:`int`
        The servo index.

    Returns
    -------
    :obj:`String`
        The description string.

    Raises
    ------
    TypeError
        `servo` needs to be an integer.
    ValueError
        `servo` has to be in the correct range fom 1 to the max number of servos (depends on your settings).
    """
    if not isinstance(servo, int):
        raise TypeError(f"servo parameter needs to be an integer, was {servo}")
    if not servo in range(1, settings.NUMBER_OF_SERVOS + 1):
        raise ValueError(
            f"servoNumber has to be in range 1 to (including) {settings.NUMBER_OF_SERVOS}."
        )
    servo = DEVICE.servo(servo)
    lockstatus = servo.lockSearch
    locked = servo.locked
    relock = servo.relock
    rampmode = servo.lockRampmode
    return f"search {int(lockstatus)} ramp {int(rampmode)} relock {int(relock)} locked {int(locked)}"


def getLockRelockRampmode(servo):
    """Return whether auto-relock is on or off for a given servo and whether rampmode is on or off for a given servo. Return values are used in a dash Checklist component, meaning the boxes will be ticked if their related value is in the value list. List will contain "rampmode" if autolock is in rampmode and "relock" if in relock mode.

    Parameters
    ----------
    servo : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`list`
        Empty list means False for both options, else "rampmode" for `lockRampmode=True` and "relock" for `relock=True`.

    """
    result = []
    if DEVICE.servo(servo).relock:
        result.append("relock")
    if DEVICE.servo(servo).lockRampmode:
        result.append("rampmode")
    return result


def getLockAmplitude(servoNumber):
    """Return the lock ramp amplitud for a specified :obj:`servo`. Load from save or default to 1 V.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        Float from 0 to 10.
    """
    return np.round(DEVICE.servo(servoNumber).lockAmplitude, 2)


def getLockOffset(servoNumber):
    """Return the lock ramp offset for a specified :obj:`servo`. Load from save or default to 0 V.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        Float value from -10 to 10.
    """
    return np.round(DEVICE.servo(servoNumber).lockOffset, 2)


def getLockFrequency(servoNumber):
    """Return the lock ramp frequency setting for specified :obj:`servo`.
    Load from save or default to `1`.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        Frequency as a float. Default uses frequencies from 1 to 100 Hz.

    """
    return DEVICE.servo(servoNumber).lockFrequency


#################### Callbacks #############################


def callLockState(n_clicks, servoNumber):
    """Enables the auto-lock feature on given servo on button trigger.

    GUI wise, the button is located in the individual autolock section.

    Parameters
    ----------
    n_clicks : :obj:`bool`
        Times the button has been clicked, only needed right now to raise PreventUpdate on startup (None trigger).
    servo : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        Return the new button label.

    """
    # check whether list is empty
    servo = DEVICE.servo(servoNumber)
    if n_clicks is None:
        raise PreventUpdate()
    search = servo.lockSearch
    locked = servo.locked
    if search or locked:
        servo.lockSearch = 0
        servo.locked = 0
    else:
        servo.lockAnalysis()
        servo.lockSearch = 1  # setting state to 1 starts searching for peak
    return servo.lockSearch


def callLockButtonLabel(servoNumber):
    """Callback handle for the autolock button. Only sets the label of the button according to the current search status.

    Parameters
    ----------
    servoNumber : :obj:`int`
        The servo index.

    Returns
    -------
    :obj:`String`
        Button Label.
    """
    servo = DEVICE.servo(servoNumber)
    if servo.lockSearch or servo.locked:
        s = "Turn off lock"
    else:
        s = "Trigger lock"
    return s


def callLockThresholdInfo(analyse_clicks, servoNumber):
    """Return a string for the UI containing information on threshold and threshold direction (`lockGreater`). Triggers the `servo.lockAnalysis` feature.


    Parameters
    ----------
    analyse_clicks: :obj:`int`
        Number of clicks on the analysis button. Indicates the callback trigger.
    servoNumber : :obj:`int`
        The servo index.

    Returns
    -------
    :obj:`String`
        The label string.
    """
    servo = DEVICE.servo(servoNumber)

    # might be None at startup
    if analyse_clicks is not None:
        servo.lockAnalysis()

    if servo.lockGreater:  # pylint: disable=protected-access
        greaterstring = ">"
    else:
        greaterstring = "<"
    return f"Threshold {greaterstring}{servo.lockThreshold:.2f} V"


def callLockRelockRampmode(values, servoNumber):
    """Set whether the AutoLock should relock automatically whenever falling above/below threshold for a given servo and whether the rampmode of the servo is on. Values come from a dash Checklist component, meaning the boxes will be ticked if their related value is in the `values` list. List will contain "rampmode" if autolock is in rampmode and "relock" if in relock mode.

    Parameters
    ----------
    values : :obj:`list`
        As with all Dash checklists the callback input is a list.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        The values in a string description, since the UI requires a return.

    """
    servo = DEVICE.servo(servoNumber)
    if "relock" in values:
        servo.relock = True
    else:
        servo.relock = False
    if "rampmode" in values:
        servo.lockRampmode = True
    else:
        servo.lockRampmode = False
    return f"Relock: {int(servo.relock)} | Rampmode: {int(servo.lockRampmode)}"


def callLockRamp(amplitude, offset, freq, context, servoNumber):
    """Send lock ramping parameters entered in servo control section of the UI to
    the corresponding :obj:`nqontrol.Servo`.

    Parameters
    ----------
    amplitude : :obj:`float`
        Lock ramp search amplitude.
    offset : :obj:`float`
        Lock ramp search offset.
    freq : :obj:`float`
        Lock ramp frequency.
    context : :obj:'json'
        Dash callback context. Please check the dash docs for more info. Used to determine input.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        UI label string describing current lock ramp state.

    """
    servo = DEVICE.servo(servoNumber)
    triggered = context.triggered[0]["prop_id"].split(".")[0]
    log.debug(context.triggered)
    if "lock_amplitude" in triggered:
        servo.lockAmplitude = amplitude
    if "lock_offset" in triggered:
        servo.lockOffset = offset
    if "lock_freq" in triggered:
        servo.lockFrequency = freq
    return f"Amplitude {servo.lockAmplitude:.2f} V | Offset {servo.lockOffset:.2f} V | Frequency {servo.lockFrequency:.2f} Hz"


############################################################
################## Servo Switches Widget ###################
############################################################


#################### Getters ###############################


def getInputStates(servoNumber):
    """Return a list of enabled input channels. Either from save or default (empty).

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`list`
        List containing names as strings.

    """
    if not isinstance(servoNumber, int):
        raise TypeError(f"servoNumber needs to be an integer, was {servoNumber}")
    if not servoNumber in range(1, settings.NUMBER_OF_SERVOS + 1):
        raise ValueError(
            f"servoNumber has to be in range 1 to (including) {settings.NUMBER_OF_SERVOS}."
        )
    checklist = []
    servo = DEVICE.servo(servoNumber)
    if servo.inputSw:
        checklist.append("input")
    if servo.offsetSw:
        checklist.append("offset")
    return checklist


def getOffset(servoNumber):
    """Return the servo's saved or default offset.

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        :obj:`servo.offset`

    """
    if not isinstance(servoNumber, int):
        raise TypeError(f"servoNumber needs to be an integer, was {servoNumber}")
    if not servoNumber in range(1, settings.NUMBER_OF_SERVOS + 1):
        raise ValueError(
            f"servoNumber has to be in range 1 to (including) {settings.NUMBER_OF_SERVOS}."
        )
    return DEVICE.servo(servoNumber).offset


def getGain(servoNumber):
    """Return servo's saved or default gain.

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        :obj:`servo.gain`

    """
    if not isinstance(servoNumber, int):
        raise TypeError(f"servoNumber needs to be an integer, was {servoNumber}")
    if not servoNumber in range(1, settings.NUMBER_OF_SERVOS + 1):
        raise ValueError(
            f"servoNumber has to be in range 1 to (including) {settings.NUMBER_OF_SERVOS}."
        )
    return DEVICE.servo(servoNumber).gain


def getActiveFilters(servoNumber):
    """Return list of active filters for filter-checklist.
    Load from save file or default empty list.
    The checklist is part of the servo section.
    Filter labels are loaded in :obj:`controller.getFilterLabels()`.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`list`
        List containing indices of active filters.

    """
    filters = DEVICE.servo(servoNumber).servoDesign.filters
    active = []
    for i, fil in enumerate(filters):
        if fil is not None and fil.enabled:
            active.append(i)
    return active


def getFilterLabels(servoNumber):
    """List containing filter-checklist labels (objects) as used by `Dash`.

    The checklist labels contain the short description of filters or default to `Filter {index}`.
    The checklist is part of the servo section.
    Filter states are loaded in :obj:`controller.getActiveFilters()`.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`list`
        List of labels.

    """
    labels = []
    servo = DEVICE.servo(servoNumber)
    servoDesign = servo.servoDesign
    for i in range(servoDesign.MAX_FILTERS):
        fil = servoDesign.get(i)
        if fil is not None:
            labels.append(fil.description)
        else:
            labels.append(f"Filter {i}")
    return [{"label": labels[i], "value": i} for i in range(servoDesign.MAX_FILTERS)]


def getOutputStates(servoNumber):
    """Return a list of enabled output channels. Either from save or default (empty).

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`list`
        List containing names as strings.
    """
    checklist = []
    servo = DEVICE.servo(servoNumber)
    if servo.auxSw:
        checklist.append("aux")
    # if servo.snapSw:
    #     checklist.append('snap')
    if servo.outputSw:
        checklist.append("output")
    return checklist


def getInputSensitivity(servoNumber):
    """Return :obj:`servo.inputSensitivity`.
    Since each servo outputs 16 bit this basically relates to 'accuracy'.
    Please read the official docs for more information on how-to-use.

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        :obj:`servo.inputSensitivity`

    """
    servo = DEVICE.servo(servoNumber)
    return servo.inputSensitivity


def getAuxSensitivity(servoNumber):
    """Return :obj:`servo.auxSensitivity`.
    Since each servo outputs 16 bit this basically relates to 'accuracy'.
    Please read the official docs for more information on how-to-use.

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`float`
        :obj:`servo.auxSensitivity`

    """
    servo = DEVICE.servo(servoNumber)
    return servo.auxSensitivity


#################### Callbacks ##########################


def callOffset(servoNumber, offset):
    """Handle the servo offset input callback for the UI's servo input section.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    offset : :obj:`String`
        String from the input field.

    Returns
    -------
    :obj:`String`
        The offset embedded in a string for the html.P label.

    """
    servo = DEVICE.servo(servoNumber)
    try:
        offset = fast_real(offset, raise_on_invalid=True)
    except (ValueError, TypeError):
        raise PreventUpdate("Empty or no real number input.")
    # Please note that servo checks for correct value.
    servo.offset = offset
    return f"Offset ({servo.offset:.2f} V)"


def callGain(context, servoNumber, gain):
    """Handle the servo gain input callback for the UI's servo input section.

    Parameters
    ----------
    context : :obj:'json'
        Dash callback context. Please check the dash docs for more info.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    gain : :obj: `String`
        String from the input field.

    Returns
    -------
    :obj:`String`
        The gain embedded in a string for the html.P label.

    """
    servo = DEVICE.servo(servoNumber)

    # determining context of input
    triggered = context.triggered[0]["prop_id"].split(".")[0]
    if f"gain_{servoNumber}" in triggered:
        # case when gain is changed by submitting the input with Enter
        try:
            gain = fast_real(gain, raise_on_invalid=True)
        except (ValueError, TypeError):
            raise PreventUpdate("Empty or no real number input.")
        if servo.gain != gain:
            servo.gain = gain
    return f"Gain ({servo.gain:.2f})"


def callServoChannels(servoNumber, inputValues):
    """Handle the checklists for both the input and output section of servo controls.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    inputValues : :obj:`list`
        List for either input or output section.
        Labels for input section are 'input', 'offset'.
        For output section 'aux' and 'output'.

    Returns
    -------
    type
        Description of returned object.

    """
    servo = DEVICE.servo(servoNumber)
    if "input" in inputValues:
        servo.inputSw = True
    else:
        servo.inputSw = False

    if "offset" in inputValues:
        servo.offsetSw = True
    else:
        servo.offsetSw = False

    if "aux" in inputValues:
        servo.auxSw = True
    else:
        servo.auxSw = False

    # if 'snap' in inputValues:
    #     servo.snapSw = True
    # else:
    #     servo.snapSw = False

    if "output" in inputValues:
        servo.outputSw = True
    else:
        servo.outputSw = False

    return ""


def callToggleServoFilters(servoNumber, values):
    """Handle callback of the filter checklist in the servo section of the UI.
    Passes a list of active filters to the :obj:`servo`.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    values : :obj:`list`
        List containing the indices of active filters.

    Returns
    -------
    :obj:`String`
        Just an empty string since UI callback needs an output.

    """
    servoDesign = DEVICE.servo(servoNumber).servoDesign
    changed = False
    for i in range(servoDesign.MAX_FILTERS):
        f = servoDesign.get(i)
        if f is not None:
            old = f.enabled
            if i in values:
                f.enabled = True
            else:
                f.enabled = False
            if not old == f.enabled:
                changed = True
    if changed:
        log.debug("Changed filter enabled states.")
        DEVICE.servo(servoNumber).applyServoDesign()
    return ""


def callInputSensitivity(selected, servoNumber):
    """Apply the input sensitivity as specified by the dropdown
    of the servo section's input options to :obj:`servo.inputSensitivity`
    and return information as a string to update UI.

    Parameters
    ----------
    selected : :obj:`int`
        One of the dropdown options. The mode is specified with ints from `0` to `3`.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        Information formatted for the `html.P()` above the dropdown.
    """
    servo = DEVICE.servo(servoNumber)
    servo.inputSensitivity = selected
    limits = [10, 5, 2.5, 1.25]
    return f"Input sensitivity (Limit: {limits[selected]} V, Mode: {selected})"


def callAuxSensitivity(selected, servoNumber):
    """Apply the aux sensitivity as specified by the dropdown
    of the servo section's output options to :obj:`servo.auxSensitivity`
    and return information as a string to update UI.

    Parameters
    ----------
    selected : :obj:`String`
        One of the dropdown options. The mode is specified with ints from `0` to `3`.
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        Information formatted for the `html.P()` above the dropdown.

    """
    servo = DEVICE.servo(servoNumber)
    servo.auxSensitivity = selected
    limits = [10, 5, 2.5, 1.25]
    return f"Aux sensitivity (Limit: {limits[selected]} V, Mode: {selected})"


############################################################
######################## Servo Widget ######################
############################################################


#################### Getters ###############################


def getServoName(servoNumber):
    """Return name attribute of servo: :obj:`servo.name` from Save or if specified in `settings.py`.

    Concerns the servo section of the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`

    Returns
    -------
    :obj:`String`
        :obj:`servo.name`

    """
    if not isinstance(servoNumber, int):
        raise TypeError(f"servoNumber needs to be an integer, was {servoNumber}")
    if not servoNumber in range(1, settings.NUMBER_OF_SERVOS + 1):
        raise ValueError(
            f"servoNumber has to be in range 1 to (including) {settings.NUMBER_OF_SERVOS}."
        )
    servo = DEVICE.servo(servoNumber)
    return servo.name


#################### Callbacks #############################


def callServoName(servoNumber, submit, name):
    """Apply the name specified in the servo section's name input
    to the targeted :obj:`servo.name` and return the name string to update the UI.

    Parameters
    ----------
    servoNumber : :obj:`int`
        Servo index :obj:`servo.channel`
    submit : :obj:`int`
        Number of times the input's submit event occured (pressing Enter while in input).
        None on startup.
    name : :obj:`String`
        Name for the :obj:`servo` and the UI's servo section.

    Returns
    -------
    :obj:`String`
        :obj:`servo.name`
    """
    if submit is None:
        raise PreventUpdate()
    servo = DEVICE.servo(servoNumber)
    servo.name = name
    return servo.name
