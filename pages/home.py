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

layout = dbc.Container([
    html.Hr(style = {'height':'2px','backgroundColor':'black','width':'100%'}),
    html.Div(
        [
            html.Div(
                html.H1('Bienvenidos a NBA analytics', 
                        style={'fontFamily':'monospace','fontWeight':'bold','fontSize':'40px'}
                        ),
            style={'margin':'25px','marginLeft':'0px'}
            ),

    html.Div([
        dbc.Carousel(
            items=[
                {'key':'1','src':'../assets/home/slide1.png'},
                {'key':'2','src':'../assets/home/Slide2.jpg'},
                {'key':'3','src':'../assets/home/slide3.jpg'},
                ],
                controls=False,
                interval=3000,
                indicators = True,
                style = {'width':'60vw'}
                ),
        html.Div(
            [
            html.Div(
                html.Img(alt='Suns vs Nuggets',src='../assets/home/juego1.jpg',style={'height':'100%', 'width':'100%'}), 
            ),
            html.Div(
                html.Img(alt='Lakers vs Warriors',src='../assets/home/juego2.jpg',style={'height':'100%', 'width':'100%'}),
                style={'borderTop':'1px solid black',}
            ),
            html.Div(
                html.Img(alt='Heat vs Nuggets',src='../assets/home/juego3.jpg',style={'height':'100%', 'width':'100%'}),
                style={'borderTop':'1px solid black'}
            )
            ],
                style={'display':'grid','gridTemplateRows':'repeat(3, 1fr)','width':'32%','marginLeft':'2vw'})
        ],
            style = {'display':'flex','flexDirection':'row','width':'100%'})
    ],
    style = {'display':'flex','flexDirection':'column','alignItems':'flex-start','marginBottom':'4vw','border-style':'black'}
    )
])