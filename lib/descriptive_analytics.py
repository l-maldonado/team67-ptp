# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# df_ci = __import__("./data/dataframes").df_ci

# from dataframes import df_ci

# from .data.dataframes import df_ci
from .data.dataframes_ftr import data_20

# Dash Bootstrap Components
import dash_bootstrap_components as dbc


# PLACE THE COMPONENTS IN THE LAYOUT

layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("Descriptive Analytics", style={"color": "#F37126"}),
                html.P(
                    "You will be able to found some important insights about "
                    "your clients and their transactions",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        )
    ]
)

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")

grap = dbc.Container(
    [
        html.H1("Iris k-means clustering"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig)), md=6),
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id="example-graph",
                            figure={
                                "data": [
                                    {
                                        "x": [1, 2, 3],
                                        "y": [4, 1, 2],
                                        "type": "bar",
                                        "name": "SF",
                                    },
                                    {
                                        "x": [1, 2, 3],
                                        "y": [2, 4, 5],
                                        "type": "bar",
                                        "name": u"Montréal",
                                    },
                                    {
                                        "x": [1, 2, 3],
                                        "y": [1, 3, 6],
                                        "type": "bar",
                                        "name": u"Colombia",
                                    },
                                ],
                                "layout": {"title": "Test Histogram"},
                            },
                        )
                    ),
                    md=6,
                ),
            ],
            align="center",
        ),
    ],
    fluid=True,
)
"""
######### TRANSACTION CARD ID ##################
fig_df_ci = go.Figure()
fig_df_ci.add_trace(go.Histogram(x=df_ci["transaction_card_installments"]))
fig_df_ci.update_layout(
    title_text="Transactions vs card installments",  # title of plot
    xaxis_title_text="Number of card Installments",  # xaxis label
    yaxis_title_text="Amount transactions",  # yaxis label
)
card_installment = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig_df_ci)), md=4),
            ],
            align="center",
        ),
    ],
    fluid=True,
)
"""
######### BLOXPLOT TEST #########
fig_x = go.Figure()
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "J-INFORMACIÓN Y COMUNICACIONES"
        ],
        quartilemethod="linear",
        name="J-INFORMACIÓN Y COMUNICACIONES",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "K-ACTIVIDADES FINANCIERAS Y DE SEGUROS"
        ],
        quartilemethod="linear",
        name="K-ACTIVIDADES FINANCIERAS Y DE SEGUROS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "N-ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO"
        ],
        quartilemethod="linear",
        name="N-ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "H-TRANSPORTE Y ALMACENAMIENTO"
        ],
        quartilemethod="linear",
        name="H-TRANSPORTE Y ALMACENAMIENTO",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "R-ACTIVIDADES ARTÍSTICAS, DE ENTRETENIMIENTO Y RECREACIÓN"
        ],
        quartilemethod="linear",
        name="R-ACTIVIDADES ARTÍSTICAS, DE ENTRETENIMIENTO Y RECREACIÓN",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][data_20["isic_section_name"] == "P-EDUCACIÓN"],
        quartilemethod="linear",
        name="P-EDUCACIÓN",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "Q-ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL"
        ],
        quartilemethod="linear",
        name="Q-ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "O-ADMINISTRACIÓN PÚBLICA Y DEFENSA; PLANES DE SEGURIDAD SOCIAL DE AFILIACIÓN OBLIGATORIA"
        ],
        quartilemethod="linear",
        name="O-ADMINISTRACIÓN PÚBLICA Y DEFENSA; PLANES DE SEGURIDAD SOCIAL DE AFILIACIÓN OBLIGATORIA",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "S-OTRAS ACTIVIDADES DE SERVICIOS"
        ],
        quartilemethod="linear",
        name="S-OTRAS ACTIVIDADES DE SERVICIOS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "G-COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACIÓN DE VEHÍCULOS AUTOMOTORES Y MOTOCICLETAS"
        ],
        quartilemethod="linear",
        name="G-COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACIÓN DE VEHÍCULOS AUTOMOTORES Y MOTOCICLETAS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "L-ACTIVIDADES INMOBILIARIAS"
        ],
        quartilemethod="linear",
        name="L-ACTIVIDADES INMOBILIARIAS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "M-ACTIVIDADES PROFESIONALES, CIENTÍFICAS Y TÉCNICAS"
        ],
        quartilemethod="linear",
        name="M-ACTIVIDADES PROFESIONALES, CIENTÍFICAS Y TÉCNICAS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "C-INDUSTRIAS MANUFACTURERAS"
        ],
        quartilemethod="linear",
        name="C-INDUSTRIAS MANUFACTURERAS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "I-ALOJAMIENTO Y SERVICIOS DE COMIDA"
        ],
        quartilemethod="linear",
        name="I-ALOJAMIENTO Y SERVICIOS DE COMIDA",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "D-SUMINISTRO DE ELECTRICIDAD, GAS, VAPOR Y AIRE ACONDICIONADO"
        ],
        quartilemethod="linear",
        name="D-SUMINISTRO DE ELECTRICIDAD, GAS, VAPOR Y AIRE ACONDICIONADO",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "A-AGRICULTURA, GANADERÍA, CAZA, SILVICULTURA Y PESCA"
        ],
        quartilemethod="linear",
        name="A-AGRICULTURA, GANADERÍA, CAZA, SILVICULTURA Y PESCA",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][data_20["isic_section_name"] == "F-CONSTRUCCIÓN"],
        quartilemethod="linear",
        name="F-CONSTRUCCIÓN",
    )
)

""" Boxplot con for 
fig_x= go.Figure()

cats = data_20["isic_section_name"]

for cat in cats:
    fig.add_trace(
        go.Box(
            y=data_20["logarithm"][data_20['isic_section_name'] 
            == cat],
            quartilemethod="linear", 
            name=cat
        )
    )
"""

# fig_x.add_trace(go.Box(x=bd[bd['isic_section_name']=='ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL']["logarithm"], quartilemethod="linear", name='ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL'))
boxplot_1 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig_x)), md=4),
            ],
            align="center",
        ),
    ],
    fluid=True,
)