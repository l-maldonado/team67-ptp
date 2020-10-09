# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html


# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import json
from datetime import datetime as dt


# Recall app
from app import app


####################################################################################
# Add the DS4A_Img
####################################################################################

#DS4A_Img = html.Div(
#    children=[html.Img(src=app.get_asset_url("ds4a-img.svg"), id="ds4a-image",)],
#)

#############################################################################
# Menu Layout
#############################################################################

def Navbar():
    navbar = dbc.Navbar(
        [
            dbc.Col(dbc.NavbarBrand("Home", href="/home"), sm=3, md=2, className="mr-auto flex-nowrap mt-3 mt-md-0",),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Col(
                dbc.Nav(dbc.NavItem(dbc.NavLink("Recommender System", href="/recommender_system")), navbar=True),
                width="auto"
            ),
            dbc.Col(
                dbc.Nav(dbc.NavItem(dbc.NavLink("Clustering Analysis", href="/clustering_analysis")), navbar=True),
                width="auto"
            ),
            dbc.Col(
                dbc.Nav(dbc.NavItem(dbc.NavLink("Descriptive Analytics", href="/descriptive_analytics")), navbar=True),
                width="auto"
            ),
            dbc.Col(
                dbc.Nav(dbc.NavItem(dbc.NavLink("About Us", href="/about_us")), navbar=True),
                width="auto"
            ),
        ],
        color="#FEFEFE",
    )

    return navbar
