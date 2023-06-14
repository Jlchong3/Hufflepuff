import plotly.express as px
import pandas as pd
import numpy as np

import dash
from dash import Dash, dcc, html, dash_table

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from app import app
import plotly.graph_objects as go
df = pd.read_csv('pages/NBA_Team_Stats.csv')
def filterteams(equipo):
    dfnew = df[df["Team"]== equipo] 
    return dfnew
df_suma_eficiencia=df.groupby("Team").sum().reset_index()
df_suma_eficiencia=df_suma_eficiencia.drop(axis=1,columns=["No","Pct","Pct.1","Pct.2"])
df_suma_eficiencia=df_suma_eficiencia.sort_values(by="Eff",ascending=False)
top5=df_suma_eficiencia.head(5)
analize_teams=[]
for i in top5['Team']:
    analize_teams.append(i)
analize_teams
df_GoldenState=filterteams("Golden State")
df_SanAntonio=filterteams("San Antonio")
df_Denver=filterteams("Denver")
df_Dallas=filterteams("Dallas")
df_Utah=filterteams("Utah")
Fgm=[]
Fga=[]
for i in (df_GoldenState["Fgm-a"]):
    list1=i.split("-")
    Fgm.append(list1[0])
    Fga.append(list1[1])
Tgm=[]
Tga=[]
for i in (df_GoldenState["3gm-a"]):
    list1=i.split("-")
    Tgm.append(list1[0])
    Tga.append(list1[1])
Ftm=[]
Fta=[]
for i in (df_GoldenState["Ftm-a"]):
    list1=i.split("-")
    Ftm.append(list1[0])
    Fta.append(list1[1])
df_GoldenState["Fgm"]=(Fgm)
df_GoldenState["Fga"]=(Fga)
df_GoldenState["Tgm"]=(Tgm)
df_GoldenState["Tga"]=(Tga)
df_GoldenState["Ftm"]=(Ftm)
df_GoldenState["Fta"]=(Fta)
df_GoldenState=df_GoldenState.drop(axis=1,columns=["Ftm-a","Fgm-a","3gm-a","Year","No"])
df_GoldenState["Fgm"]=df_GoldenState["Fgm"].astype(float)
df_GoldenState["Fga"]=df_GoldenState["Fga"].astype(float)
df_GoldenState["Tgm"]=df_GoldenState["Tgm"].astype(float)
df_GoldenState["Tga"]=df_GoldenState["Tga"].astype(float)
df_GoldenState["Ftm"]=df_GoldenState["Ftm"].astype(float)
df_GoldenState["Fta"]=df_GoldenState["Fta"].astype(float)
Fgm=[]
Fga=[]
for i in (df_SanAntonio["Fgm-a"]):
    list1=i.split("-")
    Fgm.append(list1[0])
    Fga.append(list1[1])
Tgm=[]
Tga=[]
for i in (df_SanAntonio["3gm-a"]):
    list1=i.split("-")
    Tgm.append(list1[0])
    Tga.append(list1[1])
Ftm=[]
Fta=[]
for i in (df_SanAntonio["Ftm-a"]):
    list1=i.split("-")
    Ftm.append(list1[0])
    Fta.append(list1[1])
df_SanAntonio["Fgm"]=(Fgm)
df_SanAntonio["Fga"]=(Fga)
df_SanAntonio["Tgm"]=(Tgm)
df_SanAntonio["Tga"]=(Tga)
df_SanAntonio["Ftm"]=(Ftm)
df_SanAntonio["Fta"]=(Fta)
df_SanAntonio=df_SanAntonio.drop(axis=1,columns=["Ftm-a","Fgm-a","3gm-a","Year","No"])
df_SanAntonio["Fgm"]=df_SanAntonio["Fgm"].astype(float)
df_SanAntonio["Fga"]=df_SanAntonio["Fga"].astype(float)
df_SanAntonio["Tgm"]=df_SanAntonio["Tgm"].astype(float)
df_SanAntonio["Tga"]=df_SanAntonio["Tga"].astype(float)
df_SanAntonio["Ftm"]=df_SanAntonio["Ftm"].astype(float)
df_SanAntonio["Fta"]=df_SanAntonio["Fta"].astype(float)
Fgm=[]
Fga=[]
for i in (df_Denver["Fgm-a"]):
    list1=i.split("-")
    Fgm.append(list1[0])
    Fga.append(list1[1])
Tgm=[]
Tga=[]
for i in (df_Denver["3gm-a"]):
    list1=i.split("-")
    Tgm.append(list1[0])
    Tga.append(list1[1])
Ftm=[]
Fta=[]
for i in (df_Denver["Ftm-a"]):
    list1=i.split("-")
    Ftm.append(list1[0])
    Fta.append(list1[1])
df_Denver["Fgm"]=(Fgm)
df_Denver["Fga"]=(Fga)
df_Denver["Tgm"]=(Tgm)
df_Denver["Tga"]=(Tga)
df_Denver["Ftm"]=(Ftm)
df_Denver["Fta"]=(Fta)
df_Denver=df_Denver.drop(axis=1,columns=["Ftm-a","Fgm-a","3gm-a","Year","No"])
df_Denver["Fgm"]=df_Denver["Fgm"].astype(float)
df_Denver["Fga"]=df_Denver["Fga"].astype(float)
df_Denver["Tgm"]=df_Denver["Tgm"].astype(float)
df_Denver["Tga"]=df_Denver["Tga"].astype(float)
df_Denver["Ftm"]=df_Denver["Ftm"].astype(float)
df_Denver["Fta"]=df_Denver["Fta"].astype(float)
Fgm=[]
Fga=[]
for i in (df_Dallas["Fgm-a"]):
    list1=i.split("-")
    Fgm.append(list1[0])
    Fga.append(list1[1])
Tgm=[]
Tga=[]
for i in (df_Dallas["3gm-a"]):
    list1=i.split("-")
    Tgm.append(list1[0])
    Tga.append(list1[1])
Ftm=[]
Fta=[]
for i in (df_Dallas["Ftm-a"]):
    list1=i.split("-")
    Ftm.append(list1[0])
    Fta.append(list1[1])
df_Dallas["Fgm"]=(Fgm)
df_Dallas["Fga"]=(Fga)
df_Dallas["Tgm"]=(Tgm)
df_Dallas["Tga"]=(Tga)
df_Dallas["Ftm"]=(Ftm)
df_Dallas["Fta"]=(Fta)
df_Dallas=df_Dallas.drop(axis=1,columns=["Ftm-a","Fgm-a","3gm-a","Year","No"])
df_Dallas["Fgm"]=df_Dallas["Fgm"].astype(float)
df_Dallas["Fga"]=df_Dallas["Fga"].astype(float)
df_Dallas["Tgm"]=df_Dallas["Tgm"].astype(float)
df_Dallas["Tga"]=df_Dallas["Tga"].astype(float)
df_Dallas["Ftm"]=df_Dallas["Ftm"].astype(float)
df_Dallas["Fta"]=df_Dallas["Fta"].astype(float)
Fgm=[]
Fga=[]
for i in (df_Utah["Fgm-a"]):
    list1=i.split("-")
    Fgm.append(list1[0])
    Fga.append(list1[1])
Tgm=[]
Tga=[]
for i in (df_Utah["3gm-a"]):
    list1=i.split("-")
    Tgm.append(list1[0])
    Tga.append(list1[1])
Ftm=[]
Fta=[]
for i in (df_Utah["Ftm-a"]):
    list1=i.split("-")
    Ftm.append(list1[0])
    Fta.append(list1[1])
df_Utah["Fgm"]=(Fgm)
df_Utah["Fga"]=(Fga)
df_Utah["Tgm"]=(Tgm)
df_Utah["Tga"]=(Tga)
df_Utah["Ftm"]=(Ftm)
df_Utah["Fta"]=(Fta)
df_Utah=df_Utah.drop(axis=1,columns=["Ftm-a","Fgm-a","3gm-a","Year","No"])
df_Utah["Fgm"]=df_Utah["Fgm"].astype(float)
df_Utah["Fga"]=df_Utah["Fga"].astype(float)
df_Utah["Tgm"]=df_Utah["Tgm"].astype(float)
df_Utah["Tga"]=df_Utah["Tga"].astype(float)
df_Utah["Ftm"]=df_Utah["Ftm"].astype(float)
df_Utah["Fta"]=df_Utah["Fta"].astype(float)
first_variable_eff=[]
for i,j,k,l,m in zip(top5["Pts"],top5["Reb"],top5["Ast"],top5["Stl"],top5["Blk"]):
    fst_va_eff=i+j+k+l+m
    fst_va_eff=round(fst_va_eff)
    first_variable_eff.append(fst_va_eff)
top5["1 variable eff"]=first_variable_eff
Fga_teams=[]
Fga_GoldenState=0
for i in df_GoldenState["Fga"]:
    Fga_GoldenState+=i
    Fga_GoldenState=round(Fga_GoldenState)
Fga_teams.append(Fga_GoldenState)
Fga_SanAntonio=0
for i in df_SanAntonio["Fga"]:
    Fga_SanAntonio+=i
    Fga_SanAntonio=round(Fga_SanAntonio)
Fga_teams.append(Fga_SanAntonio)
Fga_Denver=0
for i in df_Denver["Fga"]:
    Fga_Denver+=i
    Fga_Denver=round(Fga_Denver)
Fga_teams.append(Fga_Denver)
Fga_Dallas=0
for i in df_Dallas["Fga"]:
    Fga_Dallas+=i
    Fga_Dallas=round(Fga_Dallas)
Fga_teams.append(Fga_Dallas)
Fga_Utah=0
for i in df_Utah["Fga"]:
    Fga_Utah+=i
    Fga_Utah=round(Fga_Utah)
Fga_teams.append(Fga_Utah)
top5["Fga"]=Fga_teams
Fgm_teams=[]
Fgm_GoldenState=0
for i in df_GoldenState["Fgm"]:
    Fgm_GoldenState+=i
    Fgm_GoldenState=round(Fgm_GoldenState)
Fgm_teams.append(Fgm_GoldenState)
Fgm_SanAntonio=0
for i in df_SanAntonio["Fgm"]:
    Fgm_SanAntonio+=i
    Fgm_SanAntonio=round(Fgm_SanAntonio)
Fgm_teams.append(Fgm_SanAntonio)
Fgm_Denver=0
for i in df_Denver["Fgm"]:
    Fgm_Denver+=i
    Fgm_Denver=round(Fgm_Denver)
Fgm_teams.append(Fgm_Denver)
Fgm_Dallas=0
for i in df_Dallas["Fgm"]:
    Fgm_Dallas+=i
    Fgm_Dallas=round(Fgm_Dallas)
Fgm_teams.append(Fgm_Dallas)
Fgm_Utah=0
for i in df_Utah["Fgm"]:
    Fgm_Utah+=i
    Fgm_Utah=round(Fgm_Utah)
Fgm_teams.append(Fgm_Utah)
top5["Fgm"]=Fgm_teams
Tga_teams=[]
Tga_GoldenState=0
for i in df_GoldenState["Tga"]:
    Tga_GoldenState+=i
    Tga_GoldenState=round(Tga_GoldenState)
Tga_teams.append(Tga_GoldenState)
Tga_SanAntonio=0
for i in df_SanAntonio["Tga"]:
    Tga_SanAntonio+=i
    Tga_SanAntonio=round(Tga_SanAntonio)
Tga_teams.append(Tga_SanAntonio)
Tga_Denver=0
for i in df_Denver["Tga"]:
    Tga_Denver+=i
    Tga_Denver=round(Tga_Denver)
Tga_teams.append(Tga_Denver)
Tga_Dallas=0
for i in df_Dallas["Tga"]:
    Tga_Dallas+=i
    Tga_Dallas=round(Tga_Dallas)
Tga_teams.append(Tga_Dallas)
Tga_Utah=0
for i in df_Utah["Tga"]:
    Tga_Utah+=i
    Tga_Utah=round(Tga_Utah)
Tga_teams.append(Tga_Utah)
top5["Tga"]=Tga_teams
Tgm_teams=[]
Tgm_GoldenState=0
for i in df_GoldenState["Tgm"]:
    Tgm_GoldenState+=i
    Tgm_GoldenState=round(Tgm_GoldenState)
Tgm_teams.append(Tgm_GoldenState)
Tgm_SanAntonio=0
for i in df_SanAntonio["Tgm"]:
    Tgm_SanAntonio+=i
    Tgm_SanAntonio=round(Tgm_SanAntonio)
Tgm_teams.append(Tgm_SanAntonio)
Tgm_Denver=0
for i in df_Denver["Tgm"]:
    Tgm_Denver+=i
    Tgm_Denver=round(Tgm_Denver)
Tgm_teams.append(Tgm_Denver)
Tgm_Dallas=0
for i in df_Dallas["Tgm"]:
    Tgm_Dallas+=i
    Tgm_Dallas=round(Tgm_Dallas)
Tgm_teams.append(Tgm_Dallas)
Tgm_Utah=0
for i in df_Utah["Tgm"]:
    Tgm_Utah+=i
    Tgm_Utah=round(Tgm_Utah)
Tgm_teams.append(Tgm_Utah)
top5["Tgm"]=Tgm_teams
Fta_teams=[]
Fta_GoldenState=0
for i in df_GoldenState["Fta"]:
    Fta_GoldenState+=i
    Fta_GoldenState=round(Fta_GoldenState)
Fta_teams.append(Fta_GoldenState)
Fta_SanAntonio=0
for i in df_SanAntonio["Fta"]:
    Fta_SanAntonio+=i
    Fta_SanAntonio=round(Fta_SanAntonio)
Fta_teams.append(Fta_SanAntonio)
Fta_Denver=0
for i in df_Denver["Fta"]:
    Fta_Denver+=i
    Fta_Denver=round(Fta_Denver)
Fta_teams.append(Fta_Denver)
Fta_Dallas=0
for i in df_Dallas["Fta"]:
    Fta_Dallas+=i
    Fta_Dallas=round(Fta_Dallas)
Fta_teams.append(Fta_Dallas)
Fta_Utah=0
for i in df_Utah["Fta"]:
    Fta_Utah+=i
    Fta_Utah=round(Fta_Utah)
Fta_teams.append(Fta_Utah)
top5["Fta"]=Fta_teams
Ftm_teams=[]
Ftm_GoldenState=0
for i in df_GoldenState["Ftm"]:
    Ftm_GoldenState+=i
    Ftm_GoldenState=round(Ftm_GoldenState)
Ftm_teams.append(Ftm_GoldenState)
Ftm_SanAntonio=0
for i in df_SanAntonio["Ftm"]:
    Ftm_SanAntonio+=i
    Ftm_SanAntonio=round(Ftm_SanAntonio)
Ftm_teams.append(Ftm_SanAntonio)
Ftm_Denver=0
for i in df_Denver["Ftm"]:
    Ftm_Denver+=i
    Ftm_Denver=round(Ftm_Denver)
Ftm_teams.append(Ftm_Denver)
Ftm_Dallas=0
for i in df_Dallas["Ftm"]:
    Ftm_Dallas+=i
    Ftm_Dallas=round(Ftm_Dallas)
Ftm_teams.append(Ftm_Dallas)
Ftm_Utah=0
for i in df_Utah["Ftm"]:
    Ftm_Utah+=i
    Ftm_Utah=round(Ftm_Utah)
Ftm_teams.append(Ftm_Utah)
top5["Ftm"]=Ftm_teams
second_variable_eff=[]
for i,j,k,l,m in zip(Fga_teams,Fgm_teams,Fta_teams,Ftm_teams,top5["To"]):
    scd_va_eff=(i-j)+(k-l)+m
    scd_va_eff=round(scd_va_eff)
    second_variable_eff.append(scd_va_eff)
top5["2 variable eff"]=second_variable_eff
eff_teams=[]
for i,j in zip(first_variable_eff,second_variable_eff):
    eff=(i-j)
    eff=round(eff)
    eff_teams.append(eff)
top5["Eficiencia"]=eff_teams
Min_5=[]
for i in top5["Min"]:
    i=round(i)
    Min_5.append(i)
top5["Min"]=(Min_5)
Pts_5=[]
for i in top5["Pts"]:
    i=round(i)
    Pts_5.append(i)
top5["Pts"]=(Pts_5)
Reb_5=[]
for i in top5["Reb"]:
    i=round(i)
    Reb_5.append(i)
top5["Reb"]=(Reb_5)
Oreb_5=[]
for i in top5["Oreb"]:
    i=round(i)
    Oreb_5.append(i)
top5["Oreb"]=(Oreb_5)
Dreb_5=[]
for i in top5["Dreb"]:
    i=round(i)
    Dreb_5.append(i)
top5["Dreb"]=(Dreb_5)
Ast_5=[]
for i in top5["Ast"]:
    i=round(i)
    Ast_5.append(i)
top5["Ast"]=(Ast_5)
Stl_5=[]
for i in top5["Stl"]:
    i=round(i)
    Stl_5.append(i)
top5["Stl"]=(Stl_5)
Blk_5=[]
for i in top5["Blk"]:
    i=round(i)
    Blk_5.append(i)
top5["Blk"]=(Blk_5)
To_5=[]
for i in top5["To"]:
    i=round(i)
    To_5.append(i)
top5["To"]=(To_5)
Eff_5=[]
for i in top5["Eff"]:
    i=round(i)
    Eff_5.append(i)
top5["Eff"]=(Eff_5)
Deff_5=[]
for i in top5["Deff"]:
    i=round(i)
    Deff_5.append(i)
top5["Deff"]=(Deff_5)
Pf_5=[]
for i in top5["Pf"]:
    i=round(i)
    Pf_5.append(i)
top5["Pf"]=(Pf_5)
Fgp_teams=[]
for i,j in zip(top5["Fgm"],top5["Fga"]):
    Fgp=(i/j)*100
    Fgp=round(Fgp,1)
    Fgp_teams.append(Fgp)
top5["Fg%"]=(Fgp_teams)
Tgp_teams=[]
for i,j in zip(top5["Tgm"],top5["Tga"]):
    Tgp=(i/j)*100
    Tgp=round(Tgp,1)
    Tgp_teams.append(Tgp)
top5["Tg%"]=(Tgp_teams)
Ftp_teams=[]
for i,j in zip(top5["Ftm"],top5["Fta"]):
    Ftp=(i/j)*100
    Ftp=round(Ftp,1)
    Ftp_teams.append(Fgp)
top5["Ft%"]=(Ftp_teams)
top5=top5.sort_values("Eficiencia",ascending=False)

layout = dbc.Container([html.Div([
            dbc.Container([
                dbc.Row([
                    dbc.Col(html.H1("Casa Hufflepuff",className="text-center"),
                            className="mb-5 mt-5")
                ]),
            ]),
            dbc.Row([]),
            html.Div([html.H1("NBA Teams Stats"),
                html.Div([
            html.H3("Los 5 equipos con más eficiencia",style={'margin-top':'4vw'}),
            dcc.Dropdown(
                id="topeff",
                options=["Eff","1 variable eff","2 variable eff"],
                value="Eff",
                placeholder="Seleccione una opcion",
                clearable=False,
            ),
            dcc.Graph(id="grafico_barras"),
            html.Br(),
            ]),
            html.Div([
                html.H2("Distribución de los stats de la 1° variable eff",style={'margin-top':'4vw'}),
                dcc.Dropdown(
                    id="scattervar",
                    options=["Pts","Reb","Ast","Stl","Blk"],
                    value="Pts",
                    placeholder="Seleccione una variable",
                    clearable=False,
                ),
                dcc.Graph(id="scatter_1°eff"),
                html.Br(),
            ]),
            html.Div([
                html.H2("Porcentajes de los tiros de cada equipo"),
                dcc.Dropdown(
                    id="Fg%",
                    options=["Fg%","Tg%","Ft%"],
                    value="Fg%",
                    placeholder="Seleccione un procentaje de tiro",
                    clearable=False,
                ),
                dcc.Graph(id="%"),
                html.Br(),
            ]),
            html.Div([
                html.H2("Informacion de los goles de campo de cada equipo"),
                dcc.Dropdown(
                    id="Fg",
                    options=["Fgm","Fga","Fg%"],
                    value="Fgm",
                    placeholder="Seleccione una informacion",
                    clearable=False,
                ),
                dcc.Graph(id="Fgg"),
                html.Br(), 
            ]),
            html.Div([
                html.H2("Informacion de los goles de tres puntos de cada equipo"),
                dcc.Dropdown(
                    id="Tg",
                    options=["Tgm","Tga","Tg%"],
                    value="Tgm",
                    placeholder="Seleccione una informacion",
                    clearable=False,
                ),
                dcc.Graph(id="Tgg"),
                html.Br(), 
            ]),
            html.Div([
                html.H2("Informacion de los tiros libres de cada equipo"),
                dcc.Dropdown(
                    id="Ft",
                    options=["Ftm","Fta","Ft%"],
                    value="Ftm",
                    placeholder="Seleccione una informacion",
                    clearable=False,
                ),
                dcc.Graph(id="Ftg"),
                html.Br(), 
            ]),
            html.Div([
                html.H2("Distribución de los stats de la 2° variable eff",style={'margin-top':'4vw'}),
                dcc.Dropdown(
                id="scattervar2",
                options=["Fgm","Fga","Ftm","Fta","To"],
                value="Fgm",
                placeholder="Seleccione una variable",
                clearable=False,
                ),
                dcc.Graph(id="scatter_2°eff"),
                html.Br(),
            ]),
            html.Div([
                html.H2("Eficiencia y diferencia de eficiencia de cada equipo"),
                dcc.Dropdown(
                    id="Eff_Deff",
                    options=["Eff","Deff"],
                    value="Eff",
                    placeholder="Seleccione una opcion",
                    clearable=False,
                ),
                dcc.Graph(id="Eff_Deff_g"),
                html.Br(),
            ]),
            html.Div([
                html.H2("Informacion de los rebotes de cada equipo"),
                dcc.Dropdown(
                    id="Rebs",
                    options=["Reb","Oreb","Dreb"],
                    value="Reb",
                    placeholder="Seleccione una informacion",
                    clearable=False,
                ),
                dcc.Graph(id="Rebg"),
                html.Br(), 
            ]),
        ]),
    ])
])
@app.callback(
    Output("grafico_barras","figure"),
    Input("topeff","value")
)
def update_graph(selected_value):
    fig=go.Figure()
    fig.add_trace(go.Bar(
        x=top5["Team"],
        y=top5[selected_value],
        name=selected_value,
        marker_color="#025464",
    ))
    fig.update_layout(barmode="group",xaxis_tickangle=-45)
    return fig

@app.callback(
    Output("scatter_1°eff","figure"),
    Input("scattervar","value")
)
def update_graph(selected_value):
    fig=px.scatter(top5,y=selected_value,x="1 variable eff",color="Team")
    fig.update_traces(marker_size=30)
    return fig

@app.callback(
    Output("%","figure"),
    Input("Fg%","value")
)
def update_graph(selected_value):
    fig=go.Figure()
    fig.add_trace(go.Bar(
        x=top5["Team"],
        y=top5[selected_value],
        name=selected_value,
        marker_color="#025464",
    ))
    fig.update_layout(barmode="group",xaxis_tickangle=-45)
    return fig

@app.callback(
    Output("Fgg","figure"),
    Input("Fg","value")
)
def update_graph(selected_value):
    fig=go.Figure()
    fig.add_trace(go.Scatter(
        x=top5["Team"],
        y=top5[selected_value],
        name=selected_value,
        marker_color='#025464',
    ))
    fig.update_layout(barmode="group",xaxis_tickangle=-45)
    return fig
@app.callback(
    Output("Tgg","figure"),
    Input("Tg","value")
)
def update_graph(selected_value):
    fig=go.Figure()
    fig.add_trace(go.Scatter(
        x=top5["Team"],
        y=top5[selected_value],
        name=selected_value,
        marker_color='#025464',
    ))
    fig.update_layout(barmode="group",xaxis_tickangle=-45)
    return fig

@app.callback(
    Output("Ftg","figure"),
    Input("Ft","value")
)
def update_graph(selected_value):
    fig=go.Figure()
    fig.add_trace(go.Scatter(
        x=top5["Team"],
        y=top5[selected_value],
        name=selected_value,
        marker_color='#025464',
    ))
    fig.update_layout(barmode="group",xaxis_tickangle=-45)
    return fig

@app.callback(
    Output("scatter_2°eff","figure"),
    Input("scattervar2","value")
)
def update_graph(selected_value):
    fig=px.scatter(top5,y=selected_value,x="2 variable eff",color="Team")
    fig.update_traces(marker_size=30)
    return fig

@app.callback(
    Output("Eff_Deff_g","figure"),
    Input("Eff_Deff","value")
)
def update_graph(selected_value):
    fig=go.Figure()
    fig.add_trace(go.Bar(
        x=top5["Team"],
        y=top5[selected_value],
        name=selected_value,
        marker_color="#025464",
    ))
    fig.update_layout(barmode="group",xaxis_tickangle=-45)
    return fig

@app.callback(
    Output("Rebg","figure"),
    Input("Rebs","value")
)
def update_graph(selected_value):
    fig=go.Figure()
    fig.add_trace(go.Scatter(
        x=top5["Team"],
        y=top5[selected_value],
        name=selected_value,
        marker_color='#025464',
    ))
    fig.update_layout(barmode="group",xaxis_tickangle=-45)
    return fig