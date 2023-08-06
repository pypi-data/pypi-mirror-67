"""NQontrol UI: AutoLock Widget"""
# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code
# ----------------------------------------------------------------------------------------
# For documentation please read the comments. For information about Dash and Plotly go to:
#
# https://dash.plot.ly/
# ----------------------------------------------------------------------------------------
import dash_core_components as dcc
import dash_html_components as html
from dash import callback_context
from dash.dependencies import Input, Output

from nqontrol.gui.dependencies import app
from nqontrol.gui.widgets.nqWidget import NQWidget

from . import _callbacks


class AutoLockWidget(NQWidget):
    """Widget for the autolock in the servo sections.
    """

    def __init__(self, servoNumber):
        self._servoNumber = servoNumber

    @property
    def layout(self):
        """Return the elements' structure to be passed to a Dash style layout, usually with html.Div() as a top level container. For additional information read the Dash documentation at https://dash.plot.ly/.

        Returns
        -------
        html.Div
            The html/dash layout.

        """
        return html.Details(
            children=[
                html.Summary(
                    children=[
                        html.H3("Autolock", className="col-6"),
                        html.P(
                            _callbacks.getLockString(self._servoNumber),
                            id=f"lockFeedback_{self._servoNumber}",
                            className="col-6 text-right mt-0 mb-0 pt-0 pb-0",
                        ),
                    ],
                    className="row justify-content-between align-items-center",
                    # style={
                    #     "background-color": "#4C78A8",
                    #     "border": ".5px solid #4C78A8",
                    #     "border-radius": "4.5px",
                    # }
                ),
                html.Div(
                    children=[
                        html.P(
                            "Threshold (V)",
                            className="col-3 mb-0",
                            id=f"lockThresholdInfo_{self._servoNumber}",
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    "Analyse",
                                    className="w-100 btn btn-primary",
                                    id=f"lockThresholdAnalysisButton_{self._servoNumber}",
                                )
                            ],
                            className="col-3 ml-auto",
                        ),
                    ],
                    className="row p-0 justify-content-between align-items-center",
                ),
                # current values
                html.Div(
                    children=[
                        html.Span(
                            id=f"current_lock_ramp_{self._servoNumber}",
                            className="col-auto",
                        )
                    ],
                    className="row pl-0 justify-content-between align-items-center",
                ),
                # Amplitude label and slider
                html.Div(
                    children=[
                        html.P("Amplitude (V)", className="col-3"),
                        dcc.Slider(
                            id=f"lock_amplitude_slider_{self._servoNumber}",
                            min=0,
                            max=10,
                            step=0.05,
                            value=_callbacks.getLockAmplitude(self._servoNumber),
                            marks={i: f"{i}" for i in range(0, 11, 1)},
                            className="col-9",
                            updatemode="drag",
                        ),
                    ],
                    className="row p-0 justify-content-center",
                ),
                # Offset label and slider
                html.Div(
                    children=[
                        html.P("Offset (V)", className="col-3"),
                        dcc.Slider(
                            id=f"lock_offset_slider_{self._servoNumber}",
                            min=-10,
                            max=10,
                            step=0.05,
                            value=_callbacks.getLockOffset(self._servoNumber),
                            marks={i: f"{i}" for i in range(-12, 11, 2)},
                            className="col-9",
                            updatemode="drag",
                        ),
                    ],
                    className="row p-0 justify-content-center",
                ),
                # Frequency label and slider
                html.Div(
                    children=[
                        html.P("Frequency (Hz)", className="col-3"),
                        dcc.Slider(
                            id=f"lock_frequency_slider_{self._servoNumber}",
                            min=1,
                            max=100,
                            step=1,
                            value=_callbacks.getLockFrequency(self._servoNumber),
                            marks={
                                1: 1,
                                10: 10,
                                20: 20,
                                30: 30,
                                40: 40,
                                50: 50,
                                60: 60,
                                70: 70,
                                80: 80,
                                90: 90,
                                100: 100,
                            },
                            className="col-9",
                            updatemode="drag",
                        ),
                    ],
                    className="row p-0 justify-content-center",
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dcc.Checklist(
                                    options=[
                                        {"label": "Relock", "value": "relock"},
                                        {"label": "Rampmode", "value": "rampmode"},
                                    ],
                                    value=_callbacks.getLockRelockRampmode(
                                        self._servoNumber
                                    ),
                                    className="w-100 pl-0",
                                    inputClassName="form-check-input",
                                    labelClassName="form-check form-check-inline",
                                    persistence=True,
                                    id=f"lockRelockChecklist_{self._servoNumber}",
                                ),
                                dcc.Store(
                                    id=f"lockRelockChecklistStore_{self._servoNumber}"
                                ),
                            ],
                            className="col-3",
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    f"{_callbacks.callLockButtonLabel(self._servoNumber)}",
                                    className="w-100 btn btn-primary",
                                    id=f"lockStateButton_{self._servoNumber}",
                                ),
                                dcc.Store(
                                    id=f"lockStateButtonStore_{self._servoNumber}"
                                ),
                            ],
                            className="col-3 ml-auto",
                        ),
                    ],
                    className="row p-0 pb-2 justify-content-between align-items-center",
                ),
            ],
            className="col-12 d-inline mt-1 mr-2",
            style={
                "background-color": "#f2f4f5",
                "border": ".5px solid #f2f4f5",
                "border-radius": "4.5px",
            },
        )

    def setCallbacks(self):
        """Initialize all callbacks for the given element."""

        # Feedback label updater
        app.callback(
            Output(f"lockFeedback_{self._servoNumber}", "children"),
            [Input(f"update", "n_intervals")],
        )(self._lockStringCallback)

        # Threshold feedback label, callback for direction, threshold value and analysis
        app.callback(
            Output(f"lockThresholdInfo_{self._servoNumber}", "children"),
            [Input(f"lockThresholdAnalysisButton_{self._servoNumber}", "n_clicks")],
        )(self._lockThresholdInfoCallback)

        # Callback of the trigger button
        app.callback(
            Output(f"lockStateButtonStore_{self._servoNumber}", "data"),
            [Input(f"lockStateButton_{self._servoNumber}", "n_clicks")],
        )(self._lockStateCallback)

        # Both button and change of ADwin internal state can change the label of the button
        app.callback(
            Output(f"lockStateButton_{self._servoNumber}", "children"),
            [
                Input(f"lockStateButtonStore_{self._servoNumber}", "data"),
                Input(f"lockFeedback_{self._servoNumber}", "children"),
            ],
        )(self._lockButtonLabelCallback)

        # Relock checkbox
        app.callback(
            Output(f"lockRelockChecklistStore_{self._servoNumber}", "data"),
            [Input(f"lockRelockChecklist_{self._servoNumber}", "value")],
        )(self._lockRelockRampmodeCallback)

        # Slider callbacks
        app.callback(
            Output(f"current_lock_ramp_{self._servoNumber}", "children"),
            [
                Input(f"lock_amplitude_slider_{self._servoNumber}", "value"),
                Input(f"lock_offset_slider_{self._servoNumber}", "value"),
                Input(f"lock_frequency_slider_{self._servoNumber}", "value"),
            ],
        )(self._lockRampCallback)

    #######################################################################################################
    # All callbacks need to return a function to be bound to that callback, defined below
    #######################################################################################################

    def _lockThresholdInfoCallback(self, analyse_clicks):
        return _callbacks.callLockThresholdInfo(analyse_clicks, self._servoNumber)

    def _lockStateCallback(self, n_clicks):
        return _callbacks.callLockState(n_clicks, self._servoNumber)

    def _lockButtonLabelCallback(self, _data, _children):
        return _callbacks.callLockButtonLabel(self._servoNumber)

    def _lockRelockRampmodeCallback(self, values):
        return _callbacks.callLockRelockRampmode(values, self._servoNumber)

    def _lockStringCallback(self, _n_interval):
        return _callbacks.getLockString(self._servoNumber)

    # Callback for the Lock widget's amplitude, offset and frequency slider
    def _lockRampCallback(self, amplitude, offset, frequency):
        ctxt = callback_context
        return _callbacks.callLockRamp(
            amplitude, offset, frequency, ctxt, self._servoNumber
        )
