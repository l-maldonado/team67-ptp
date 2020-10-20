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
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

=======
>>>>>>> 9841020fcdef8153e13c908d099d065074d7defe
layout = html.Div(
    [
        dbc.Alert(
            [
<<<<<<< HEAD
                html.H1("Recommender System",style={'color':'#F37126'}),
                html.P("Place to pay analytical platform for the analysis of the transactional behavior of your customers",style={'color':'#8190A5','font-weight': 'bold'}),
            ],
            style={'background-color':'#F8F6F6','border':'0px'},
        ),
        dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
=======
                html.H3("Recommender System", style={"color": "#F37126"}),
                html.P(
                    "Recommendation system that gives you the list of products that each of yur clienes are model likely to buy",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        ),
>>>>>>> 9841020fcdef8153e13c908d099d065074d7defe
    ]
)
