# Basics Requirements
import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
from app import app



# PLACE THE COMPONENTS IN THE LAYOUT
layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("Clustering Analysis", style={"color": "#F37126"}),
                html.P(
                    "You will find an analysis of how your clients relate to"
                    " each other based on their transaction behavior",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        ),
    ]
)

cluster_bar = "https://tinyurl.com/yyv9j6yl"
# Tab1 of the descriptive dashboard
cluster_tab = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    dbc.Button("More Info", id="alert-toggle-fade",
                               className="mr-1"),
                    html.Hr(),
                    dbc.Alert(
                        "You can see the clusters by merchants \
                            acording the number of transactions",
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
                                        src=cluster_bar,
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