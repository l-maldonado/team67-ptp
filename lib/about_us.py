# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html

# Dash Bootstrap Components
import dash_bootstrap_components as dbc
from app import app

# PLACE THE COMPONENTS IN THE LAYOUT

dalvarez = {
    "border-radius": "225px",
    "background-color": "#F8F6F6",
    # "border": "0px",
    # "position": "fixed",
    # "float": "right",
    "margin": "10px auto",
    "display": "block",
}


SIDEBAR = {
    "border-radius": "125px",
    "background-color": "#F8F6F6",
    # "border": "0px",
    # "position": "fixed",
    # "left": 53,
    # "float": "right",
    "margin": "10px auto",
    "display": "block",
}


layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("About Us", style={"color": "#F37126"}),
                html.P(
                    "Meet the team",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={
                "background-color": "#F8F6F6",
                "border": "0px",
            },
        ),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("LuisM.jpg"),
                                    height="250px",
                                    style=dalvarez,
                                ),
                                html.H5(
                                    "Luis Gustavo Maldonado Archila",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "20px",
                                        "text-align": "center",
                                    },
                                ),
                                html.P(
                                    "Mechatronics Engineer",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "0px",
                                        "text-align": "center",
                                    },
                                ),
                            ],
                            # style={"left": 100},
                        ),
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("ed.jpeg"),
                                    height="250px",
                                    style=SIDEBAR,
                                ),
                                html.H5(
                                    "Edward Ortiz",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "20px",
                                        "text-align": "center",
                                    },
                                ),
                                html.P(
                                    "Product Manager | SWE - ML |",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "0px",
                                        "text-align": "center",
                                    },
                                ),
                            ],
                            # style={"left": 100},
                        ),
                    ],
                    style={"height": "22rem"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("jdarboleda.jpg"),
                                    height="250px",
                                    style=SIDEBAR,
                                ),
                                html.H5(
                                    "Juan D. Arboleda A.",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "20px",
                                        "text-align": "center",
                                    },
                                ),
                                html.P(
                                    "Industrial engineering",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "0px",
                                        "text-align": "center",
                                    },
                                ),
                            ],
                            # style={"left": 100},
                        ),
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("daniel.jpg"),
                                    height="250px",
                                    style=SIDEBAR,
                                ),
                                html.H5(
                                    "Daniel Salazar Castañeda",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "20px",
                                        "text-align": "center",
                                    },
                                ),
                                html.P(
                                    "Finances and international relations",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "0px",
                                        "text-align": "center",
                                    },
                                ),
                            ],
                            # style={"left": 100},
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("LuisH_.jpg"),
                                    height="250px",
                                    style=SIDEBAR,
                                ),
                                html.H5(
                                    "Luis Hernando Vanegas",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "20px",
                                        "text-align": "center",
                                    },
                                ),
                                html.P(
                                    "Statistic",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "0px",
                                        "text-align": "center",
                                    },
                                ),
                            ],
                            # style={"left": 100},
                        ),
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("ximena.jpg"),
                                    height="250px",
                                    style=SIDEBAR,
                                ),
                                html.H5(
                                    "Ximena Astrid Borda Casallas",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "20px",
                                        "text-align": "center",
                                    },
                                ),
                                html.P(
                                    "Statistics",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "0px",
                                        "text-align": "center",
                                    },
                                ),
                            ],
                            # style={"left": 100},
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("dalvarez_.jpg"),
                                    height="250px",
                                    style=SIDEBAR,
                                ),
                                html.H5(
                                    "Diego Alvarez Monroy",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "20px",
                                        "text-align": "center",
                                    },
                                ),
                                html.P(
                                    "Computer and Telecommunications Engineering",
                                    style={
                                        "color": "#8190A5",
                                        "margin-top": "0px",
                                        "text-align": "center",
                                    },
                                ),
                            ],
                            # style={"left": 100},
                        ),
                    ]
                ),
            ]
        ),
    ]
)
