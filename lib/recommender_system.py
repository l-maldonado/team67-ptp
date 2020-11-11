# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = __import__("app").app
# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# PLACE THE COMPONENTS IN THE LAYOUT

layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("Recommender System", style={"color": "#F37126"}),
                html.P(
                    "Recommendation system that gives you the list of products that each of your clients are model likely to buy",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        ),
    ]
)


input_form = dbc.Row(
    dbc.Col(
        html.Div(
            [
                html.P("Type payer id"),
                dbc.InputGroup(
                    [
                        html.Div(id="target"),
                        # dbc.InputGroupAddon("CO000000", addon_type="prepend"),
                        dbc.Input(
                            id="input",
                            placeholder="Enter transaction payer id code",
                            type="text",
                            value="",
                            # max="9999",
                            # min="0",
                            maxLength="8",
                            minLength="2",
                        ),
                        html.Br(),
                        html.P(id="target"),
                        dbc.Button(
                            "Submit",
                            outline=True,
                            color="link",
                            style={"color": "#F37126"},
                            id="submit",
                        ),
                    ],
                    html.Div(html.P(id="target")),
                    className="sm-3",
                ),
            ],
        ),
        width={"size": 6, "offset": 3},
    )
)


@app.callback(
    Output(component_id="target", component_property="children"),
    [Input(component_id="input", component_property="value")],
    # [State(component_id="button", component_property="n_clicks")],
)
def input_payer(value):
    return value
