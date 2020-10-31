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
#    children=[
#        html.Img(
#            src=app.get_asset_url("placetopay.png"),
#            id="logo",
#        )
#    ],
# )
# DS4A_LOGO = "../static/images/correlation-one.png"

#############################################################################
# Menu Layout
#############################################################################
PTP_LOGO = app.get_asset_url("placetopay.png")
PTP_LOGO1 = app.get_asset_url("correlation_one.png")

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


"""
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PTP_LOGO, height="30px")),
                    ],
                    justify="start",
                    no_gutters=False,
                ),
                href="/home",
            ),
            dbc.Col(html.Img(src=PTP_LOGO, height="30px"), width="auto"),
            dbc.NavItem(dbc.NavLink("Recommender System", href="/recommender_system")),
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
"""

"""
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.Col(html.Img(src=PTP_LOGO, height="30px"), width="auto", align="start"),
            dbc.NavItem(dbc.NavLink("Recommender System", href="/recommender_system")),
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
        align="start",
        sticky="top",
        color="#FEFEFE",
    )
    return navbar

"""
"""
def Navbar():
    navbar = dbc.Navbar(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PTP_LOGO, height="30px")),
                    ],
                    align="start",
                    no_gutters=False,
                ),
                href="/home",
            ),
            # dbc.Col(
            #    html.Img(src=PTP_LOGO, height="30px"),
            #    style={"float": "left"},
            #    id="logo",
            # ),
            dbc.NavItem(
                dbc.NavLink("Recommender System", href="/recommender_system"),
                style={"foat": "left"},
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
"""

"""
def Navbar():
    navbar = dbc.Nav(
        children=[
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PTP_LOGO, height="30px")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            # dbc.Col(
            #    html.Img(src=PTP_LOGO, height="30px"),
            #    style={"float": "left"},
            #    id="logo",
            # ),
            dbc.Nav(
                dbc.NavLink(
                    "Recommender System", active=True, href="/recommender_system"
                ),
                dbc.NavLink(
                    "Clustering Analysis", active=True, href="/clustering_analysis"
                ),
                dbc.NavLink(
                    "Descriptive Analytics", active=True, href="/descriptive_analytics"
                ),
                dbc.NavLink("About Us", active=True, href="/about_us"),
            ),
        ],
        # brand="Home",
        # brand_href="/home",
        sticky="top",
        color="#FEFEFE",
    )
    return navbar
    """