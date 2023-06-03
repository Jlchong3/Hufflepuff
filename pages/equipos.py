import plotly.express as px
import pandas as pd
import numpy as np

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from pages.teams import Atlanta, Boston, Brooklyn, Charlotte, Chicago, Cleveland, Dallas, Denver, Detroit, Golden_State, Houston, Indiana, LAClippers, LALakers, Memphis,Miami, Milwaukee, Minnesota, New_Orleans, New_York,Oklahoma_City, Orlando, Philadelphia, Phoenix, Portland, Sacramento, San_Antonio, Toronto, Utah, Washington

from app import app

df = pd.read_csv('pages/NBA_Team_Stats.csv')
teams = np.sort(df['Team'].unique()[np.isin(df['Team'].unique(),np.array(['Seattle','New Jersey','Vancouver']),invert = True)])

nombres = ['Hawks','Celtics','Nets','Hornets','Bulls','Cavaliers','Mavericks',
           'Nuggets','Pistons','Warriors','Rockets','Pacers','Clippers','Lakers',
           'Grizzlies','Heat','Bucks','Timberwolfs','Pelicans','Knicks','Thunder',
           'Magic','76ers','Suns','TrailBlazers','Kings','Spurs','Raptors','Jazz','Wizards']
l = []
for team,nombre in zip(teams,nombres):
    l.append(html.A(dbc.Card(
        [
        dbc.CardImg(src=f'../assets/equipos/{team}.png'),
        dbc.CardBody(f'{team} {nombre}' if nombre not in ['Clippers','Lakers'] else f'L.A {nombre}', style={'fontSize':'1.1vw','textAlign':'center','fontWeight':'550'}),
        ],
        color='dark',
        style={'height':'100%','padding':'20px'},
        outline=True,
    ),href=f'/equipos/{team}',style={'color':'black'}), id='team-links')

cards = dbc.Row([dbc.Col(i, width=3, style={'marginBottom':'20px'}) for i in l])

layout = dbc.Container([html.Div(
    [cards])],id='team-container')

@app.callback(
    Output('team-container','children'),
    input('team-links','href')
)
def team_tables(path):
    if path[8:] == '/Atlanta':
        return Atlanta.layout
    
    elif path[:8] == '/Boston':
        return Boston.layout
    
    elif path[:8] == '/Brooklyn':
        return Brooklyn.layout
    
    elif path[:8] == '/Charlotte':
        return Charlotte.layout
    
    elif path[:8] == '/Chicago':
        return Chicago.layout
    
    elif path[:8] == '/Cleveland':
        return Cleveland.layout
    
    elif path[:8] == '/Dallas':
        return Dallas.layout
    
    elif path[:8] == '/Denver':
        return Denver.layout
    
    elif path[:8] == '/Detroit':
        return Detroit.layout
    
    elif path[:8] == '/Golden State':
        return Golden_State.layout
    
    elif path[:8] == '/Houston':
        return Houston.layout
    
    elif path[:8] == '/Indiana':
        return Indiana.layout
    
    elif path[:8] == '/L.A.Clippers':
        return LAClippers.layout
    
    elif path[:8] == '/L.A.Lakers':
        return LALakers.layout
    
    elif path[:8] == '/Memphis':
        return Memphis.layout
    
    elif path[:8] == '/Miami':
        return Miami.layout
    
    elif path[:8] == '/Milwaukee':
        return Milwaukee.layout
    
    elif path[:8] == '/Minnesota':
        return Minnesota.layout
    
    elif path[:8] == '/New Orleans':
        return New_Orleans.layout
    
    elif path[:8] == '/New York':
        return New_York.layout
    
    elif path[:8] == '/Oklahoma City':
        return Oklahoma_City.layout
    
    elif path[:8] == '/Orlando':
        return Orlando.layout
    
    elif path[:8] == '/Philadelphia':
        return Philadelphia.layout
    
    elif path[:8] == '/Phoenix':
        return Phoenix.layout
    
    elif path[:8] == '/Portland':
        return Portland.layout
    
    elif path[:8] == '/Sacramento':
        return Sacramento.layout
    
    elif path[:8] == '/San Antonio':
        return San_Antonio.layout
    
    elif path[:8] == '/Toronto':
        return Toronto.layout
    
    elif path[:8] == '/Utah':
        return Utah.layout
    
    elif path[:8] == '/Washington':
        return Washington.layout
    

