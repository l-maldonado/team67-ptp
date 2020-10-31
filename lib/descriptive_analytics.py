# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from .data.dataframes import df_t

# from .data.postgresql.process_db import test
# from .data.dataframes_ftr import df_t
# Dash Bootstrap Components

import dash_bootstrap_components as dbc


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

descriptive_map = "https://app.powerbi.com/view?r=eyJrIjoiMmI1MzkwNmEtZThkNi00ZTk3LThjZWYtYjgwOGI0NDQ5ZmVjIiwidCI6ImZhYmQwNDdjLWZmNDgtNDkyYS04YmJiLThmOThiOWZiOWNjYSIsImMiOjR9"
descriptive_1 = "https://app.powerbi.com/view?r=eyJrIjoiOGQ3NmRjOGEtZDExNi00OGRiLWJhNzQtNzE1NzAzZDRlMzg0IiwidCI6ImZhYmQwNDdjLWZmNDgtNDkyYS04YmJiLThmOThiOWZiOWNjYSIsImMiOjR9"
######## TABS #########
tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("DESCRIPTION", className="card-text"),
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
            html.P("DESCRIPTION", className="card-text"),
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
        dbc.Tab(tab2_content, label="Geospatial information by merchant and industry"),
    ]
)