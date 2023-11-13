import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc,html
import dash.dependencies as dd
import pandas as pd
import plotly.graph_objects as go

dash.register_page(__name__, path='/Agriculture')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Link to the dataset on GitHub
econoagri_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Econoagri.xlsx'

# Load the dataset
Econoagri = pd.read_excel(econoagri_url, engine='openpyxl')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Load the dataset for employed population IN/NOT in agriculture
# Link to the dataset on GitHub
EmployAgri_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/EmployAgri.xlsx'

# Load the dataset
EmployAgri = pd.read_excel(EmployAgri_url, engine='openpyxl')

# Filter data for those in agriculture and not in agriculture
in_agriculture = EmployAgri[EmployAgri['Type'] == 'In Agriculture']
not_in_agriculture = EmployAgri[EmployAgri['Type'] == 'Not in Agriculture']

# Create a radar chart for those in agriculture
figEmplAgr = go.Figure()

figEmplAgr.add_trace(go.Scatterpolar(
    r=in_agriculture['Population'],
    theta=in_agriculture['CategoryAgri'],
    # fill='toself',
    name='In Agriculture'
))

# Create a radar chart for those not in agriculture
figEmplAgr.add_trace(go.Scatterpolar(
    r=not_in_agriculture['Population'],
    theta=not_in_agriculture['CategoryAgri'],
    # fill='toself',
    name='Not in Agriculture'
))

# Update layout for better visualization
figEmplAgr.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, max(EmployAgri['Population'])])
    ),
    showlegend=True,
    title='Empoyed Population Distribution Among Categories in Agriculture and Not in Agriculture',
)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Load the dataset for tained populatiion in agriculture and not in agriculture
# Link to the dataset on GitHub
training_data_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/training.xlsx'

# Load the dataset
training_data = pd.read_excel(training_data_url, engine='openpyxl')

#bar chart creation
figTrainAgr = px.bar(training_data, x=['in agriculture', 'not in agriculture'], y='period',
             labels={'value': 'Population'},
             title='Population Distribution by Training Period and Status in Agriculture/Not in Agriculture',
             orientation='h')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Link to the dataset on GitHub
age_pop_agri_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/agerangeagri.xlsx'

# Load the dataset
AgePopAgri = pd.read_excel(age_pop_agri_url, engine='openpyxl')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
layout = dbc.Container([
     # Link to CSS file for this page
        html.Link(
             # the path to CSS file
        ),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Employed Population by Branch of Economic Activity ", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
            ],
            style={'text-align': 'center'}
        ),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='horizontal-bar-chart',
                    figure=px.bar(
                        Econoagri,
                        y='Economic Activities',
                        x=['In agriculture', 'Not in agriculture'],
                        orientation='h',
                        labels={'value': 'Employed Population'},
                        title='Employed Population Distribution Across Economic Activities with a Focus on Agriculture',
                        hover_data={'value': ':,.0f'},
                    )
                    .update_layout(
                        legend_title_text=''  # Change 'Your New Legend Title' to your desired title
                    ),
                ),
            ],width=12, style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
        ]),
        html.Br(),
        dbc.Row([
            html.Div(
                [
                    html.H3("Employed population by status in employment and Population who Attended Training who are(Not) involved in Agriculture", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
                ],
                style={'text-align': 'center'}
            ),            
            dbc.Col([
                html.Div([
                dcc.Graph(figure=figEmplAgr)
            ], style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),                
            ],width=6),
            dbc.Col([
                html.Div([
                    dcc.Graph(figure=figTrainAgr)
                ], style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'})
            ],width=6)


        ]),
        html.Br(),
        html.Div(
                [
                    html.H3("Population Distribution by Age/Participation in Agriculture", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
                ],
                style={'text-align': 'center'}
            ),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Graph(
                            id='grouped-bar-chart',
                            figure={
                                'data': [
                                    go.Bar(
                                        x=AgePopAgri['In agriculture'],
                                        y=AgePopAgri['Age Range'],
                                        orientation='h',
                                        name='In agriculture'
                                    ),
                                    go.Bar(
                                        x=AgePopAgri['Not in agriculture'],
                                        y=AgePopAgri['Age Range'],
                                        orientation='h',
                                        name='Not in agriculture'
                                    )
                                ],
                                'layout': go.Layout(
                                    barmode='group',
                                    title='Population Distribution by Age_group',
                                    xaxis=dict(title='Population'),
                                    yaxis=dict(title='Age Range'),
                                    showlegend=True
                                )
                            }
                        )
                    ], style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'})
                ])
            ])
],
fluid=True
)