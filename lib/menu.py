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

# DS4A_Img = html.Div(
#    children=[html.Img(src=app.get_asset_url("ds4a-img.svg"), id="ds4a-image",)],
# )
DS4A_LOGO = "../static/images/correlation-one.png"

#############################################################################
# Menu Layout
#############################################################################


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Recommender System", href="/recommender_system")),
            dbc.NavItem(
                dbc.NavLink("Clustering Analysis", href="/clustering_analysis")
            ),
            dbc.NavItem(
                dbc.NavLink("Descriptive Analytics", href="/descriptive_analytics")
            ),
            dbc.NavItem(dbc.NavLink("About Us", href="/about_us")),
        ],
        brand="Home",
        brand_href="/home",
        sticky="top",
        color="#FEFEFE",
    )
    return navbar