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
from .data.dataframes_ftr import get_df
from app import app, cache
#get_df = __import__("dataframes_ftr").get_df

# PLACE THE COMPONENTS IN THE LAYOUT
df_c = get_df()

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

available_indicators = ['transaction_card_type',
                        'merchant_classification',
                        'category_hour',
                        'category_paymentmethod_franchise',
                        'category_response_code']
                        
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
            y=(df_c[df_c['cluster_predicted']==0]).value_counts(),
            name="cluster 0",
            marker_color="tomato",
        )
    )
    fig.add_trace(
        go.Bar(
            x=df_c["{}".format(select)],
            y=(df_c[df_c['cluster_predicted']==1]).value_counts(),
            name="cluster 1",
            marker_color="slategray",
        )
    )
    fig.update_layout(barmode="group")

    return fig
