# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
<<<<<<< HEAD
import plotly.express as px
import pandas as pd 
=======
>>>>>>> 9841020fcdef8153e13c908d099d065074d7defe

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# PLACE THE COMPONENTS IN THE LAYOUT

<<<<<<< HEAD
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


=======
>>>>>>> 9841020fcdef8153e13c908d099d065074d7defe
layout = html.Div(
    [
        dbc.Alert(
            [
<<<<<<< HEAD
                html.H1("Clustering Analysis",style={'color':'#F37126'}),
                html.P("Place to pay analytical platform for the analysis of the transactional behavior of your customers",style={'color':'#8190A5','font-weight': 'bold'}),
            ],
            style={'background-color':'#F8F6F6','border':'0px'},
        ),
        dcc.Graph(
        id='example-graph',
        figure=fig
    )
=======
                html.H3("Clustering Analysis", style={"color": "#F37126"}),
                html.P(
                    "You will find an analysis of how your clients relate to"
                    " each other based on their transaction behavior",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        ),
>>>>>>> 9841020fcdef8153e13c908d099d065074d7defe
    ]
)
