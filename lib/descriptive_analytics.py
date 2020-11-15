# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
app = __import__("app").app

# PLACE THE COMPONENTS IN THE LAYOUT
layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("Descriptive Analytics", style={"color": "#F37126"}),
                html.P(
                    "You will be able to found some important insights about "
                    "your clients and their transactions",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        )
    ]
)

descriptive_map = "https://tinyurl.com/y52pgpd2"
descriptive_1 = "https://tinyurl.com/y6qby2zo"

# Tab1 of the descriptive dashboard
tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    dbc.Button("More Info", id="alert-toggle-fade",
                               className="mr-1"),
                    html.Hr(),
                    dbc.Alert(
                        "Select the merchant_id and the division \
                            name to see the specific information about them",
                        id="alert-fade",
                        dismissable=True,
                        is_open=True,
                    ),
                ]
            ),
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    html.Iframe(
                                        src=descriptive_1,
                                        width="110%",
                                        height="780px",
                                    )
                                )
                            )
                        ],
                        align="start",
                    ),
                ],
            ),
        ],
    ),
    className="mt-3",
)

# Tab2 of the geographical map
tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    dbc.Button(
                        "More Info", id="alert-toggle-no-fade",
                        className="mr-1"
                    ),
                    html.Hr(),
                    dbc.Alert(
                        "Select the merchant_id and the division name \
                            to see purchase behavior in geospatial context",
                        id="alert-no-fade",
                        dismissable=True,
                        fade=False,
                        duration=4000,
                    ),
                ]
            ),
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    html.Iframe(
                                        src=descriptive_map,
                                        width="110%",
                                        height="780px",
                                    )
                                )
                            )
                        ],
                        align="start",
                    ),
                ],
            ),
        ]
    ),
    className="mt-3",
)

# Component to call dashboard in tabs
descriptive_tab = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Transactions and Merchants information"),
        dbc.Tab(tab2_content, label="Geospatial information \
            by merchant and industry"),
    ]
)


# Callback function for message info
@app.callback(
    Output("alert-fade", "is_open"),
    [Input("alert-toggle-fade", "n_clicks")],
    [State("alert-fade", "is_open")],
)
def toggle_alert(n, is_open):
    if n:
        return not is_open
    return is_open


# Callback function for message info
@app.callback(
    Output("alert-no-fade", "is_open"),
    [Input("alert-toggle-no-fade", "n_clicks")],
    [State("alert-no-fade", "is_open")],
)
def toggle_alert_no_fade(n, is_open):
    if n:
        return not is_open
    return is_open
