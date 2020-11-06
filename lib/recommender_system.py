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

# PLACE THE COMPONENTS IN THE LAYOUT

layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("Recommender System", style={"color": "#F37126"}),
                html.P(
                    "Recommendation system that gives you the list of products that each of your clienes are model likely to buy",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        ),
    ]
)
