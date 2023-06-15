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
    dfnew = dfmig[dfmig["Team"== equipo]] 
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
L = ['1997-1998', '1998-1999', '1999-2000', '2000-2001', '2001-2002',
       '2002-2003', '2003-2004', '2004-2005', '2005-2006', '2006-2007',
       '2007-2008', '2008-2009', '2009-2010', '2010-2011', '2011-2012',
       '2012-2013', '2013-2014', '2014-2015', '2015-2016', '2016-2017',
       '2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022']

H = ["G","Min","Pts","Reb","Ast","Stl","Blk","To","Pf","Dreb","Oreb","Pct","Eff","Deff"]

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



def top5año(temporada):
    dfb = dfmig[dfmig["Year"]==temporada]
    n=0
    L=[]
    M=[]
    X=[]
    frames=[]
    for i in range(len(dfb)):
        L.append(dfb["Eff"].iloc[i])
        L.sort()
    for elem in reversed(L):
        M.append(elem)
    for elem in M[:3]:
        a = pd.DataFrame(dfb[dfb["Eff"]==elem])
        b= a["Team"].iloc[0]
        X.append((b,elem))
    for elem in X:
        equipo,eff = elem
        df1 = dfmig[dfmig["Year"]==temporada]
        df2= df1[df1["Team"]== equipo]
        df3 = df2[df2["Eff"]==eff]
        frames.append(df3)
        result = pd.concat(frames)
    return result

layout = dbc.Container(
    html.Div([
        html.Div([
            html.H1("Estadísticas relevantes por equipo y temporada")
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
        
        html.Div([html.H2("Histórico de relación entre Dribles y Faltas Cometidas"),dcc.Graph(figure=fig)]),

        html.Div([html.Div([html.H2("Relación de estadísticas por equipo con respecto al tiempo")])]),

        html.Div([
            html.Div([html.H2("Estadística 1"), dcc.Dropdown(H, value= "G", id="ejex")], style={"width":"47%","marginRight":"1vw"}),
            html.Div([html.H2("Estadística 2"), dcc.Dropdown(H, value="Pf", id="ejey")])
        ],style={"display":"flex","flexDirection":"row","justifyContent":"center"}),
        html.Div([
            html.Div(
                [html.H2("Equipo"),
                 dcc.Dropdown(dfmig["Team"].unique(),value="Golden State",id="equipo")], 
                 style={'width':'95%'}
                 ),
            ],
        style={"display":"flex","flexDirection":"row","justifyContent":"flexStart"}),
            
        html.Div([dcc.Graph(id="linear")]),

        html.Div([html.H2("Estadísticas Top 3 equipos por efectividad"),dcc.Dropdown(L, value = "2021-2022", id ="tabladrop")]),

        html.Div(dbc.Table(id="table", color = "info", hover=True), style={"width":"100%"}),
            
            
            
            ]))

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

@app.callback(
    Output("linear","figure"),
    Input("ejex","value"),
    Input("ejey","value"),
    Input("equipo","value"),
    )

def graflinea(var1,var2,equi):
    x1 = pd.DataFrame(dfmig[dfmig["Team"]== equi] )
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dfmig["Year"].unique(),y=x1[var1],name=var1,
                             marker_color="#025464"))
    fig.add_trace(go.Scatter(x=dfmig["Year"].unique(),y=x1[var2],name=var2,
                             marker_color="#E57C23"))
    return fig


@app.callback(
    Output("table","children"),
    Input("tabladrop","value")
)

def top5año(temporada):
    dfb = dfmig[dfmig["Year"]==temporada]
    n=0
    L=[]
    M=[]
    X=[]
    frames=[]
    for i in range(len(dfb)):
        L.append(dfb["Eff"].iloc[i])
        L.sort()
    for elem in reversed(L):
        M.append(elem)
    for elem in M[:3]:
        a = pd.DataFrame(dfb[dfb["Eff"]==elem])
        b= a["Team"].iloc[0]
        X.append((b,elem))
    for elem in X:
        equipo,eff = elem
        df1 = dfmig[dfmig["Year"]==temporada]
        df2= df1[df1["Team"]== equipo]
        df3 = df2[df2["Eff"]==eff]
        frames.append(df3)
    result = pd.concat(frames)
    result = result.drop(["No","Year","Min"], axis = 1)
    header = [html.Thead(html.Tr([html.Td(i) for i in result.columns]),style={'fontWeight':'Bold','fontSize':'17px'})]
    rows = []
    for i in range(result.shape[0]):
        player = []
        for data in result.iloc[i]:
            player.append(html.Td(data))
        rows.append(html.Tr(player))
    return header + [html.Tbody(rows)]
