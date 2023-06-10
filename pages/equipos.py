import plotly.express as px
import pandas as pd
import numpy as np

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

from app import app

df = pd.read_csv('pages/NBA_Team_Stats.csv')
teams = np.sort(df['Team'].unique()[np.isin(df['Team'].unique(),np.array(['Seattle','New Jersey','Vancouver']),invert = True)])

nombres = ['Hawks','Celtics','Nets','Hornets','Bulls','Cavaliers','Mavericks',
           'Nuggets','Pistons','Warriors','Rockets','Pacers','Clippers','Lakers',
           'Grizzlies','Heat','Bucks','Timberwolfs','Pelicans','Knicks','Thunder',
           'Magic','76ers','Suns','TrailBlazers','Kings','Spurs','Raptors','Jazz','Wizards']
l = []
for team,nombre in zip(teams,nombres):
    l.append(html.A(
                dbc.Card(
                    [
                    dbc.CardImg(src=f'../assets/equipos/{team}.png'),
                    dbc.CardBody(f'{team} {nombre}' if nombre not in ['Clippers','Lakers'] else f'L.A {nombre}', 
                                 style={'fontSize':'1.1vw','textAlign':'center','fontWeight':'550'}),
                    ],
                    color='dark',
                    style={'height':'100%','padding':'20px'},
                    outline=True,
                    ),
                href=f'/teams/{team}',
                style={'color':'black','textDecoration':'none'}
                )
            )

cards = dbc.Row([
            dbc.Col(i, width=3, style={'marginBottom':'20px'}) for i in l
            ])

layout = dbc.Container([
    html.Hr(style = {'height':'2px','backgroundColor':'black','width':'100%'}),
    html.Div(
        [
        html.H1('Equipos Actuales', 
                style={'fontFamily':'monospace','fontWeight':'bold','fontSize':'40px'}
                )
        ],
        style={'margin':'25px','marginLeft':'0px'}
        ),

    html.Div(
        [cards])],
        id='team-container'
        )

    

