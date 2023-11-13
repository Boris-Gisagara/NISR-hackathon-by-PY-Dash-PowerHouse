import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc,html, callback
import dash.dependencies as dd
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output


dash.register_page(__name__, path='/Outside_the_labor')
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Load the dataset for self reported status
# Link to the dataset on GitHub
self_rep_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/selfRep.xlsx'

# Load the dataset
selfRep = pd.read_excel(self_rep_url, engine='openpyxl')

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Load the data for livelihood source
# Link to the dataset on GitHub
livelihood_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/livelihoodSource.xlsx'

# Load the dataset
livelihood = pd.read_excel(livelihood_url, engine='openpyxl')

# Melt the dataframe to reshape it for plotting
livelihood_melted = pd.melt(livelihood, id_vars='Source', var_name='Category', value_name='Count')
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Load the dataset for donut chart on reasond for being out of labor force
# Link to the dataset on GitHub
reasons_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/ReasonsOut.xlsx'

# Load the dataset
Reasons = pd.read_excel(reasons_url, engine='openpyxl')

#-----------------------------------------------------------------------------------------------------------------------------------------------------
layout = dbc.Container([
        html.Link(
             # the path to CSS file
        ),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Population Outside the Labor Force in Rwanda", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
            ],
            style={'text-align': 'center'}
        ),
        html.Br(),
        html.Br(),
        dbc.Row([
            dbc.Col([
                html.H3("Self Reported Status", style={'fontSize': '20px', 'textAlign': 'left'}),
                dcc.Dropdown(
                    id='status-dropdown',
                    options=[
                        {'label': status, 'value': status} for status in selfRep['Status']
                    ],
                    value=selfRep['Status'][0],  # Default selected option
                    style={
                        'width': '60%',
                        'text-align': 'center',
                        'font-size': '15px',  # Adjust font size
                        'border-radius': '8px',  # Add rounded corners 
                        },
                    clearable=False,
                    searchable=False
                ),
                html.Br(),
                html.Br(),
                html.Div([                
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader("Male", style={'textAlign': 'center', 'fontSize': '20px'},className="border-start border-info border-5"),
                            dbc.CardBody(id='male-card', style={'textAlign': 'center', 'fontSize': '25px'},className="border-start border-info border-5"),
                        ],style={'borderRadius': '15px', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc'}),
                    ], width=3),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader("Female", style={'textAlign': 'center', 'fontSize': '20px'},className="border-start border-info border-5"),
                            dbc.CardBody(id='female-card', style={'textAlign': 'center', 'fontSize': '25px'},className="border-start border-info border-5"),
                        ],style={'borderRadius': '15px', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc'}),
                    ], width=3),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader("Urban", style={'textAlign': 'center', 'fontSize': '20px'},className="border-start border-info border-5"),
                            dbc.CardBody(id='urban-card', style={'textAlign': 'center', 'fontSize': '25px'},className="border-start border-info border-5"),
                        ],style={'borderRadius': '15px', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc'}),
                    ], width=3),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader("Rural", style={'textAlign': 'center', 'fontSize': '20px'},className="border-start border-info border-5"),
                            dbc.CardBody(id='rural-card', style={'textAlign': 'center', 'fontSize': '25px'},className="border-start border-info border-5"),
                        ],style={'borderRadius': '15px', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc'}),
                    ], width=3),
                ]),
            ], 
            style={'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
            ],width=12),
        ]),
        html.Br(),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        dbc.Row([
            html.Div(
                [
                    html.H3("Population outside the labour force by main source of livelihood", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
                ],
                style={'text-align': 'center'}
            ),
            dbc.Col([
                html.Div([
                    dcc.Dropdown(
                        id='liveli-dropdown',
                        options=[
                            {'label': source, 'value': source} for source in livelihood['Source']
                        ],
                        value=livelihood['Source'][0],  # Default selected option
                        style={
                            'width': '100%',
                            'text-align': 'center',
                            'font-size': '15px',  # Adjust font size
                            'border-radius': '8px',  # Add rounded corners 
                            },
                    ),
                    dcc.Graph(id='liveli-barChart'),  # Updated to bar chart
                ], style={'border': '2px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',},),
            ], width=6),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
            dbc.Col([
                html.Div([
                    dcc.Dropdown(
                        id='reason-dropdown',
                        options=[
                            {'label': reason, 'value': reason} for reason in Reasons['Reason']
                        ],
                        value=Reasons['Reason'][0],  # Default selected option
                        style={
                            'width': '100%',
                            'text-align': 'center',
                            'font-size': '15px',  # Adjust font size
                            'border-radius': '8px',  # Add rounded corners 
                            },
                        clearable=False,
                        searchable=False
                    ),
                    dcc.Graph(id='reason-donut-chart'),
                ], style={'border': '2px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
            ], width=6),
        ]),
        html.Br(),
],
fluid=True
)
#---------------------------------------------------------------------------------------------------------------------------------
# Define callback to update card values
@callback(
    [Output('male-card', 'children'),
     Output('female-card', 'children'),
     Output('urban-card', 'children'),
     Output('rural-card', 'children')],
    [Input('status-dropdown', 'value')]
)
def update_cards(selected_status):
    selected_data = selfRep[selfRep['Status'] == selected_status]

    male_value = selected_data['Male'].values[0]
    female_value = selected_data['Female'].values[0]
    urban_value = selected_data['Urban'].values[0]
    rural_value = selected_data['Rural'].values[0]

    return f"{male_value:,}", f"{female_value:,}", f"{urban_value:,}", f"{rural_value:,}"
#---------------------------------------------------------------------------------------------------------------------------------
# define callback for the linechart on livelihood sources
# Define callback to update bar chart
@callback(
    Output('liveli-barChart', 'figure'),  # Updated to bar chart
    [Input('liveli-dropdown', 'value')]
)
def update_bar_chart(selected_source):
    selected_data = livelihood_melted[livelihood_melted['Source'] == selected_source]

    fig = px.bar(selected_data, x='Count', y='Category',
                 orientation='h',  # horizontal bar chart
                 title=f'Livelihood Source Distribution for {selected_source}',
                 labels={'Count': 'Population'},
                 color_discrete_sequence=px.colors.qualitative.Set1)  # Set color sequence

    return fig
#---------------------------------------------------------------------------------------------------------------------------------
# Define callback to update donut chart
@callback(
    Output('reason-donut-chart', 'figure'),
    [Input('reason-dropdown', 'value')]
)
def update_donut_chart(selected_reason):
    selected_data = Reasons[Reasons['Reason'] == selected_reason].iloc[0]

    # Create a donut chart
    fig = px.pie(
        selected_data,
        names=['Male', 'Female', 'Urban', 'Rural', 'In agriculture', 'Not in agriculture'],
        values=[selected_data['Male'], selected_data['Female'],
                selected_data['Urban'], selected_data['Rural'],
                selected_data['In agriculture'], selected_data['Not in agriculture']],
        hole=0.5,
        labels={'names': 'Category', 'values': 'Count'},
        title=f'Distribution of {selected_reason} by Category',
        height=400
    )

    return fig