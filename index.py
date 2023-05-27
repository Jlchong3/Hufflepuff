import plotly.express as px
import pandas as pd

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from pages import equipos, analisis, home

from app import server
from app import app

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        dbc.DropdownMenuItem("Equipos", href="/equipos"),
        dbc.DropdownMenuItem("Analisis", href="/analisis"),
    ],
    nav = True,
    in_navbar = True,
    label = "Secciones",
    style={'fontSize':'20px'}

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
               [Input('url', 'pathname')])
def display_page(pathname):
      if pathname == '/equipos':
          return equipos.layout
      elif pathname == '/analisis':
          return analisis.layout
      else:
          return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)