import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc,html,callback,Output,Input
import dash.dependencies as dd
import pandas as pd


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP,"/assets/style.css"])

# Define the navigation bar with custom styling
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink(page["name"], href=page["path"], active="exact", className="nav-link"))
                    for page in dash.page_registry.values()
                ],
                className="ml-auto",
                navbar=True,
                
            ),
        ],
        fluid=True,
    ),
    color="light",
)

app.layout = html.Div(
    [
        dbc.Row([
            dbc.Col([
        # Place the title at the top
        dbc.Card([
                dbc.CardBody([
                html.Div("Labor Force Survey 2022", style={'fontSize': '50px', 'textAlign': 'left', 'padding': '10px'}),
            ], className="border-start border-success border-5")
        ],className="text-center m-4"),
        ],width=5,className="mx-auto"),
        ]),
        
        # Add some space between the title and the navigation bar
        html.Br(),
        
        # Place the custom navbar in the middle
        dbc.Container(navbar, className="mt-3"),
        
        dash.page_container
    ]
)
if __name__ == "__main__":
    app.run(debug=True)
    
