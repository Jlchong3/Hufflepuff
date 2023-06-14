import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go 

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash import dash_table

from app import app

df= pd.read_csv(r"pages\NBA_Team_Stats.csv")
dfmig = df.copy()
def filterteams(equipo):
    dfnew = dfmig[dfmig["Team"]== equipo] 
    return dfnew
O = []
"""
for elem in dfmig["3gm-a"]:
    a,b = elem.split("-")
    O.append((float(a)+float(b))/2)
dfmig["3gma"]= O
def tabob2 (criteria):
    tab = dfmig.groupby("Team")[criteria].sum()
    return tab
tab3 = tabob2("3gma")

H = []
for elem in dfmig["3gm-a"]:
    a,b = elem.split("-")
    a = float(a)
    b = float(b)
    H.append(round(a/b,2))

dfmig["3gmper"] = H

M=[]
for elem in dfmig["Fgm-a"]:
    a,b = elem.split("-")
    a = float(a)
    b = float(b)
    M.append(round(a/b,2))
dfmig["Fgmper"] = M

Z = []
for elem in dfmig["Ftm-a"]:
    a,b = elem.split("-")
    a = float(a)
    b = float(b)
    Z.append(round(a/b,2))
dfmig["Ftmper"]= Z
"""

teams = dfmig["Team"].unique()
def filterteams2(equipo):
    dfnew = dfmig[dfmig["Team"]== equipo] 
    return dfnew

S = []
for elem in teams:
    dfg = filterteams2(elem)
    a = np.array(dfg["Eff"])
    pos = np.argmax(a)
    b = [elem,dfg.iloc[pos]["Year"],dfg.iloc[pos]["Eff"]]
    S.append(b)

a = dfmig[dfmig["Team"]=="Golden State"][dfmig["Eff"]==144.2]
b = dfmig[dfmig["Team"]=="Golden State"][dfmig["Eff"]==142.0]
c = dfmig[dfmig["Team"]=="Milwaukee"][dfmig["Eff"]==140.0]
d = dfmig[dfmig["Team"]=="Golden State"][dfmig["Eff"]==139.4]
e = dfmig[dfmig["Team"]=="Golden State"][dfmig["Eff"]==148.9]


dfc = pd.DataFrame(dict(
    r=[14.0, 42.8, 15.4, 7.1, 29.5],
    theta=['To','Reb','Ast',
           'Stl', 'Dreb']))
"""
fig = px.line_polar(dfc, r='r', theta='theta', line_close=True)
fig.show()
app = dash.Dash()
app.layout = html.Div([dcc.Graph(figure=fig)])
"""

dfouls = pd.DataFrame(dfmig.groupby("Year")["Pf"].sum())
dfdrib = pd.DataFrame(dfmig.groupby("Year")["Dreb"].sum())


fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df["Year"].unique(),
    y=dfouls["Pf"],
    name='Fouls',
    marker_color='#025464'
))
fig.add_trace(go.Scatter(
    x=df["Year"].unique(),
    y=dfdrib["Dreb"].unique(),
    name='Dribbles',
    marker_color='#E57C23'
))

fig.update_layout(barmode='group', xaxis_tickangle=-45)

layout = dbc.Container(
    html.Div([
        html.Div([
            html.H1("Estadisticas relevantes por equipo y temporada")
            ]),
        html.Br(),
        html.Div([
            html.Div([
                dcc.Dropdown(teams,"Golden State", id="Teams drop")
                ],
                style={'width':'47%','marginRight':'1vw'}
                ),
            html.Div([
                dcc.Dropdown(dfmig["Year"].unique(), value = "2021-2022", id="Year")
                ],
                style={'width':'47%'}
                )
            ],
            style={'display':'flex','flexDirection':'row','justifyContent':'center'}
            ),

        html.Div([
            dcc.Graph(id="Radial-Graph")
            ]),

        html.Div([
            html.H2("Relacion de Dribles y Faltas cometidas con respecto al tiempo"),dcc.Graph(figure=fig)
            ])
        ])
    )

@app.callback(
    Output("Radial-Graph","figure"),
    Input("Teams drop","value"),
    Input("Year", "value"),
    )

def grafico2(nombre,año):
    lindf = pd.DataFrame(dfmig[dfmig["Year"]==año])
    lindf2 = pd.DataFrame(lindf[lindf["Team"]==nombre])
    To1 = lindf2["To"].iloc[0]
    Reb1 = lindf2["Reb"].iloc[0]
    Ast1 = lindf2["Ast"].iloc[0]
    Stl1 = lindf2["Stl"].iloc[0]
    Dreb1 = lindf2["Dreb"].iloc[0]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r = [To1,Reb1,Ast1,Stl1,Dreb1], theta = ['To','Reb','Ast',
           'Stl', 'Dreb'], fill="toself", name = nombre))
    fig.update_layout(
    polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 50])),
    showlegend=False)
    return fig


"""
def update_graph(year,team):
    linea = dfmig[dfmig["Year"]==year][dfmig["Team"]==team]
    To = linea["To"].values[0]
    Reb = linea["Reb"].values[0]
    Ast = linea["Ast"].values[0]
    Stl = linea["Stl"].values[0]
    Dreb = linea["Dreb"].values[0]
    dfc = pd.DataFrame(dict(r=[To,Reb,Ast,Stl,Dreb],
    theta=['To','Reb','Ast',
           'Stl', 'Dreb']))
    fig = px.line_polar(dfc, r='r', theta='theta', line_close=True)
    return fig
"""