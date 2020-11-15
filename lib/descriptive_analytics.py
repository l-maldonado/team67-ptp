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

descriptive_map = "https://app.powerbi.com/view?r=eyJrIjoiMmI1MzkwNmEtZThkNi00ZTk3LThjZWYtYjgwOGI0NDQ5ZmVjIiwidCI6ImZhYmQwNDdjLWZmNDgtNDkyYS04YmJiLThmOThiOWZiOWNjYSIsImMiOjR9&pageName=ReportSection8e92f1ee166027c23cfa"
descriptive_1 = "https://app.powerbi.com/view?r=eyJrIjoiMTAzMDk0ZmMtMjk1NC00ZjE3LThjZWQtYjUwMjE0YTE4MWUzIiwidCI6ImZhYmQwNDdjLWZmNDgtNDkyYS04YmJiLThmOThiOWZiOWNjYSIsImMiOjR9"

# Tabs description for analytics
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

descriptive_tab = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Transactions and Merchants information"),
        dbc.Tab(tab2_content, label="Geospatial information \
            by merchant and industry"),
    ]
)


@app.callback(
    Output("alert-fade", "is_open"),
    [Input("alert-toggle-fade", "n_clicks")],
    [State("alert-fade", "is_open")],
)
def toggle_alert(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("alert-no-fade", "is_open"),
    [Input("alert-toggle-no-fade", "n_clicks")],
    [State("alert-no-fade", "is_open")],
)
def toggle_alert_no_fade(n, is_open):
    if n:
        return not is_open
    return is_open
