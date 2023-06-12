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

df= pd.read_csv("pages\\NBA_Team_Stats.csv")
dfmig = df.copy
def filterteams(equipo):
    dfnew = dfmig[dfmig["Team"]== equipo] 
    return dfnew
O = []
for elem in dfmig[r"3gm-a"]:
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
fig = px.line_polar(dfc, r='r', theta='theta', line_close=True)
fig.show()
app = dash.Dash()
app.layout = html.Div([dcc.graph(figure=fig)])

layout = dbc.Container()