# import plotly.express as px
# import plotly.graph_objects as go 
# import pandas as pd
# import numpy as np

# import dash
# from dash import Dash, dcc, html, dash_table
# from dash.dependencies import Input, Output, State
# from dash.exceptions import PreventUpdate
# import dash_bootstrap_components as dbc


# from app import app
# df_tendency = pd.read_csv('pages/tendencies_analysis.csv')
# df_tendency.drop(columns=['Unnamed: 0'], inplace=True)

# layout = dbc.Container([
#     html.Div([
#         html.H1('Tendencia Ofensiva de la Liga')
#     ]),
#     html.Br(),
#     html.Div([
#         dcc.Dropdown(['Eff','PTS','3PM-A','2PM-A','FTM-A','3P%','2P%','FT%'], value = 'Eff',id='ofensive-filter')
#     ]),
#     html.Br(),
#     html.Div(dcc.Graph(id='tendency-graph'))
# ])

# @app.callback(
#     Output('tendency-graph','figure'),
#     Input('ofensive-filter','value'))
# def generate_graph(value):
#     fig = go.Figure()
#     if '-' in value:
#         shottypem,attemps = value.split('-')
#         shottypea = shottypem[:2] + attemps
#         fig.add_trace(go.Scatter(x = df_tendency['Year'], y = df_tendency[shottypea], name = 'Attempts'))
#         fig.add_trace(go.Scatter(x = df_tendency['Year'], y = df_tendency[shottypem], name = 'Makes'))
#         fig = fig.update_layout(xaxis_title='Year', yaxis_title=f'Average {shottypem[:2]} Shots')
#     else:
#         fig.add_trace(go.Scatter(x = df_tendency['Year'], y = df_tendency[value]))
#         fig = fig.update_layout(xaxis_title='Year',yaxis_title=f'Average {value}')
#     return fig

