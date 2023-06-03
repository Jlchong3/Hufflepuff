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
    
df_1 = pd.read_csv('NBA_P.csv')

df_1.drop(columns=['Unnamed: 0.1','Unnamed: 0'])       
            
df = df_1[df_1 == 'Denver']
df.drop(columns=['Tm'])
dropdown = dcc.Dropdown(['2021-2022','2020-2021','2019-2020','2018-2019','2017-2018',
                         '2016-2017','2015-2016','2014-2015','2013-2014','2012-2013',
                         '2011-2012','2010-2011','2009-2010','2008-2009','2007-2008',
                         '2006-2007','2005-2006','2004-2005','2003-2004','2002-2003',
                         '2001-2002', '2000-2001','1999-2000','1998-1999','1997-1998'],
                         value = '2021-2022' , label = 'Seleccione Temporada', id = 'Denver-players')

layout = dbc.Container([
    html.Div([
        html.H1('Denver Nuggets')
    ]),
    html.Div(
        dbc.Table(id = "Nuggets-table"),
)])

@app.callback(
    Output('Nuggets-table', 'children'),
    Input('Denver-players','value'))
def filter_year(value):
    df_year = df[value == 'Season']
    df_year.drop(columns=['Season'])
    header = html.Thead(html.Tr([html.Td(i) for i in df_year.columns]))
    rows = []
    for i in range(df_year.size):
        player = []
        for data in df_year.loc[i]:
            player.append(html.Td(data))
        rows.append(html.Tr(player))
    return dbc.Table(header + html.Tbody(rows), bordered=True)