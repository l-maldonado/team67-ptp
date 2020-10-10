# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json

# Recall app
from app import app


###########################################################
#
#           APP LAYOUT:
#
###########################################################

# LOAD THE DIFFERENT FILES
from lib import menu, home, clustering_analysis, descriptive_analytics, recommender_system

# PLACE THE COMPONENTS IN THE LAYOUT

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    
app.layout = html.Div([
    dcc.Tabs([
    dcc.Tab(label='Home', children= home.layout, className="tab"),
    dcc.Tab(label='Recommender system', children= recommender_system.layout, className="tab"),
    dcc.Tab(label='Descriptive analytics', children= descriptive_analytics.layout, className="tab"),
    dcc.Tab(label='Clustering analysis', children= clustering_analysis.layout, className="tab")
    ], id="app-tabs")
    #className="ds4a-app",  # You can also add your own css files by locating them into the assets folder
])


@app.callback(
    dash.dependencies.Output('example-graph1', 'figure'),
    [dash.dependencies.Input('submit-val', 'n_clicks')])
def update_output(n_clicks):
    if n_clicks%2==1:
        figura=fig
    return figura

###############################################
#
#           APP INTERACTIVITY:
#
###############################################



if __name__ == "__main__":
    app.run_server( debug=True)
