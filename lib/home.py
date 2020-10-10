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
                html.H1("Transactional Analytics Platform",style={'color':'#A569BD'}),
                html.P("Place to pay analytical platform for the analysis of the transactional behavior of your customers",style={'color':'#8190A5','font-weight': 'bold'}),
            ],
            style={'background-color':'#F8F6F6','border':'0px'},
        ),
        html.Div([
            html.Div(dcc.Input(id='input-on-submit', type='text')), 
            html.Button('Submit', id='submit-val', n_clicks=0),
            html.Div(id='container-button-basic', children='Enter a value and press submit'),
            dcc.Graph(
        id='example-graph1'
    )
        ])
    ]
)

