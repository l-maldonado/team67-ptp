# Basics Requirements
import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
from .data.dataframes_ftr import df_c, cl_0, cl_1
from app import app, cache

# PLACE THE COMPONENTS IN THE LAYOUT

layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("Clustering Analysis", style={"color": "#F37126"}),
                html.P(
                    "You will find an analysis of how your clients relate to"
                    " each other based on their transaction behavior",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        ),
    ]
)

available_indicators = df_c.columns
cluster_tab = dbc.Row(
    dbc.Col(
        [
            html.Div(
                [
                    html.P("Choose a category", className="choose_category"),
                ],
            ),
            dbc.Select(
                id="select",
                options=[{"label": i, "value": i} for i in available_indicators],
                value="transaction_card_type",
            ),
            dcc.Graph(id="indicator-graphic"),
        ],
        width={"size": 6, "offset": 3},
    )
)


@app.callback(
    dash.dependencies.Output("indicator-graphic", "figure"),
    [
        dash.dependencies.Input("select", "value"),
    ],
)
@cache.memoize(timeout=120)
def update_graph(select):
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=df_c["{}".format(select)],
            y=(cl_0).value_counts(),
            name="cluster 0",
            marker_color="tomato",
        )
    )
    fig.add_trace(
        go.Bar(
            x=df_c["{}".format(select)],
            y=(cl_1).value_counts(),
            name="cluster 1",
            marker_color="slategray",
        )
    )
    fig.update_layout(barmode="group")

    return fig
