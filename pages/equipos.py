import plotly.express as px
import pandas as pd
import numpy as np

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash import dash_table

from app import app

df = pd.read_csv('pages/NBA_Team_Stats.csv')
teams = np.sort(df['Team'].unique()[np.isin(df['Team'].unique(),np.array(['Seattle','New Jersey','Vancouver']),invert = True)])

nombres = ['Hawks','Celtics','Nets','Hornets','Bulls','Cavaliers','Mavericks',
           'Nuggets','Pistons','Warriors','Rockets','Pacers','Clippers','Lakers',
           'Grizzlies','Heat','Bucks','Timberwolfs','Pelicans','Knicks','Thunder',
           'Magic','76ers','Suns','TrailBlazers','Kings','Spurs','Raptors','Jazz','Wizards']
l = []
for team,nombre in zip(teams,nombres):
    l.append(dbc.Card(
        [
        dbc.CardImg(src=f'../assets/equipos/{team}.png'),
        dbc.CardBody(f'{team} {nombre}' if nombre not in ['Clippers','Lakers'] else f'L.A {nombre}'),
        ],
        style={'height':'100%','padding':'20px'}
    ))

cards = dbc.Row([dbc.Col(i, width=3) for i in l],style={'margin':'20px'})

layout = dbc.Container([html.Div(
    [cards],
    style={'marg':'40px'}
    )])