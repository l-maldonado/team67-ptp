# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

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

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")

grap = dbc.Container(
    [
        html.H1("Iris k-means clustering"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig)), md=6),
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id="example-graph",
                            figure={
                                "data": [
                                    {
                                        "x": [1, 2, 3],
                                        "y": [4, 1, 2],
                                        "type": "bar",
                                        "name": "SF",
                                    },
                                    {
                                        "x": [1, 2, 3],
                                        "y": [2, 4, 5],
                                        "type": "bar",
                                        "name": u"Montréal",
                                    },
                                    {
                                        "x": [1, 2, 3],
                                        "y": [1, 3, 6],
                                        "type": "bar",
                                        "name": u"Colombia",
                                    },
                                ],
                                "layout": {"title": "Test Histogram"},
                            },
                        )
                    ),
                    md=6,
                ),
            ],
            align="center",
        ),
    ],
    fluid=True,
)

