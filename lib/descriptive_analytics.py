# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd 
import seaborn as sns


# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# PLACE THE COMPONENTS IN THE LAYOUT
user_cols = ['transaction_processing_amount','isic_section_name']
bd=pd.read_csv('data/bdfn.csv', usecols=user_cols)
bd['transaction_processing_amount'] = bd['transaction_processing_amount'].str.replace(',','.').astype('float64')
bd_bounded_10000 = bd[(bd["transaction_processing_amount"]>=1000) & (bd["transaction_processing_amount"]<10000)]

fig = px.box(bd_bounded_10000, x="isic_section_name", y="transaction_processing_amount")

layout = html.Div(
    [
        dbc.Alert(
            [
                html.H1("Descriptive Analytics",style={'color':'#F37126'}),
                html.P("Place to pay analytical platform for the analysis of the transactional behavior of your customers",style={'color':'#8190A5','font-weight': 'bold'}),
            ],
            style={'background-color':'#F8F6F6','border':'0px'},
        ),
         dcc.Graph(
        id='boxplot-graph',
        figure=fig
         )
    ]
)
