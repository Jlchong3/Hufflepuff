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
    
df_1 = pd.read_csv(r'pages/teams/NBA-P.csv')

df_1.drop(columns=['Unnamed: 0.1','Unnamed: 0'], inplace=True)       
            
df = df_1[df_1['Tm'] == 'Philadelphia']
df.drop(columns=['Tm'], inplace = True)
df.drop(columns=['Tm'], inplace = True)
dropdown = dcc.Dropdown(['2021-22','2020-21','2019-20','2018-19','2017-18',
                         '2016-17','2015-16','2014-15','2013-14','2012-13',
                         '2011-12','2010-11','2009-10','2008-09','2007-08',
                         '2006-07','2005-06','2004-05','2003-04','2002-03',
                         '2001-02', '2000-01','1999-00','1998-99','1997-98'],
                         value = '2021-22' , id = 'Philadelphia-players', style={'marginTop':'1vw','marginBottom':'2vw'})

layout = dbc.Container([
    html.Div([
        html.H1('Philadelphia 76ers', 
                style={'fontFamily':'monospace','fontWeight':'550'})
    ]),
    html.Div([dropdown]),
    html.Div(
        dbc.Table(id = "76ers-table", color = "info", hover = True),
)])

@app.callback(
    Output('76ers-table', 'children'),
    Input('Philadelphia-players','value'))
def filter_year(value):
    df_year = df[value == df['Season']]
    if 'Season' in df_year.columns:
        df_year.drop(columns=['Season'], inplace=True)
    header = [html.Thead(html.Tr([html.Td(i) for i in df_year.columns]),style={'fontWeight':'Bold','fontSize':'17px'})]
    rows = []
    for i in range(df_year.shape[0]):
        player = []
        for data in df_year.iloc[i]:
            player.append(html.Td(data))
        rows.append(html.Tr(player))
    return header + [html.Tbody(rows)]