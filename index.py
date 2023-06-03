import plotly.express as px
import pandas as pd

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from pages import equipos, analisis, home, jose, miguel, darwin
from pages.teams import Atlanta, Boston, Brooklyn, Charlotte, Chicago, Cleveland, Dallas, Denver, Detroit, Golden_State, Houston, Indiana, LAClippers, LALakers, Memphis,Miami, Milwaukee, Minnesota, New_Orleans, New_York,Oklahoma_City, Orlando, Philadelphia, Phoenix, Portland, Sacramento, San_Antonio, Toronto, Utah, Washington

from app import server
from app import app

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href = "/home", id = 'home',),
        dbc.DropdownMenuItem("Equipos", href = "/equipos", id = 'equipos'),
        dbc.DropdownMenuItem("Analisis", href = "/analisis", id = 'analisis'),
        dbc.DropdownMenuItem("Darwin", href = '/darwin', id = 'darwin'),
        dbc.DropdownMenuItem("Miguel", href = '/miguel', id = 'miguel')
    ],
    nav = True,
    in_navbar = True,
    label = "Secciones",
    style={'fontSize':'20px'},


)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/nba.png", height="100px")),
                    ],
                    align="center",
                    justify='center',
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
                style={'justifyContent':'flex-end'}
            ),
        ]
    ),
    color="#1d418b",
    dark=True,
    className="mb-3",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Output('equipos', 'active'),
              Output('analisis', 'active'),
              Output('darwin', 'active'),
              Output('miguel', 'active'),
              Output('home', 'active'),
               [Input('url', 'pathname')])
def display_page(pathname):
      if  pathname == '/equipos':
          return equipos.layout, True, False, False, False, False
      elif pathname == '/analisis':
          return analisis.layout, False, True, False, False, False
      elif pathname == '/darwin':
          return darwin.layout, False, False, True, False, False
      elif pathname == '/miguel':
          return miguel.layout, False, False, False, True, False
      elif pathname == '/jose':
          return jose.layout, False, False, False, False, False
      elif pathname[8:] == '/Atlanta':
        return Atlanta.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Boston':
        return Boston.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Brooklyn':
        return Brooklyn.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Charlotte':
        return Charlotte.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Chicago':
        return Chicago.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Cleveland':
        return Cleveland.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Dallas':
        return Dallas.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Denver':
        return Denver.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Detroit':
        return Detroit.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Golden State':
        return Golden_State.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Houston':
        return Houston.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Indiana':
        return Indiana.layout, False, False, False, False, False
    
      elif pathname[8:] == '/L.A.Clippers':
        return LAClippers.layout, False, False, False, False, False
    
      elif pathname[8:] == '/L.A.Lakers':
        return LALakers.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Memphis':
        return Memphis.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Miami':
        return Miami.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Milwaukee':
        return Milwaukee.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Minnesota':
        return Minnesota.layout, False, False, False, False, False
    
      elif pathname[8:] == '/New Orleans':
        return New_Orleans.layout, False, False, False, False, False
    
      elif pathname[8:] == '/New York':
        return New_York.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Oklahoma City':
        return Oklahoma_City.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Orlando':
        return Orlando.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Philadelphia':
        return Philadelphia.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Phoenix':
        return Phoenix.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Portland':
        return Portland.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Sacramento':
        return Sacramento.layout, False, False, False, False, False
    
      elif pathname[8:] == '/San Antonio':
        return San_Antonio.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Toronto':
        return Toronto.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Utah':
        return Utah.layout, False, False, False, False, False
    
      elif pathname[8:] == '/Washington':
        return Washington.layout, False, False, False, False, False
      else:
          return home.layout, False, False, False, False, True


if __name__ == '__main__':
    app.run_server(debug=True)