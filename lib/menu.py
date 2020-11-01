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


# PTP_LOGO = app.get_asset_url("placetopay.png")
# PTP_LOGO1 = app.get_asset_url("correlation_one1.png")

PTP_LOGO = "../static/images/placetopay.png"
PTP_LOGO1 = "../static/images/correlation_one1.png"

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 12,
    "left": 0,
    "width": "0rem",
    "background-color": "#ffffff",
}
SIDEBAR_STYLE1 = {
    "position": "fixed",
    "top": 10,
    "left": 165,
    "width": "0rem",
    "background-color": "#ffffff",
}
#   "bottom": 0,
# 20

# PTP_LOGO = "../static/images/placetopay.png"
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            html.A(
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(src=PTP_LOGO, height="35px"),
                            style=SIDEBAR_STYLE,
                        ),
                        dbc.Col(
                            html.Img(src=PTP_LOGO1, height="20px"),
                            style=SIDEBAR_STYLE1,
                        ),
                    ],
                    justify="start",
                    no_gutters=False,
                    # href="/home",
                ),
                href="/home",
            ),
            dbc.NavItem(
                dbc.NavLink("Recommender System", href="/recommender_system"),
            ),
            dbc.NavItem(
                dbc.NavLink("Clustering Analysis", href="/clustering_analysis")
            ),
            dbc.NavItem(
                dbc.NavLink("Descriptive Analytics", href="/descriptive_analytics")
            ),
            dbc.NavItem(dbc.NavLink("About Us", href="/about_us")),
        ],
        # brand="Home",
        # brand_href="/home",
        sticky="top",
        color="#FEFEFE",
    )
    return navbar
