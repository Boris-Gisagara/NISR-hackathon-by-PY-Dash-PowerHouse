import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc,html, callback
import dash.dependencies as dd
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output


dash.register_page(__name__, path='/Unemployment')


# Load the data for unemployment population 
# Link to the dataset on GitHub
unemployment_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/unemployment.xlsx'

# Load the dataset
dfUnempl = pd.read_excel(unemployment_url, engine='openpyxl')

# Load the data for underutilization by age group
# Link to the dataset on GitHub
underutilization1_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/underutilizatoin1.xlsx'

# Load the dataset
dfunder1 = pd.read_excel(underutilization1_url, engine='openpyxl')

# Load the data for underutilization by underutilisation
# Link to the dataset on GitHub
underutilization2_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/underutilization2.xlsx'

# Load the dataset
dfUnder2 = pd.read_excel(underutilization2_url, engine='openpyxl')


layout = dbc.Container([
     # Link to CSS file for this page
        html.Link(
             # the path to CSS file
        ),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Unemployed population by Age Group/Education Level", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
            ],
            style={'text-align': 'center'}
        ),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.RadioItems(
                    id='category-radio',
                    options=[
                        {'label': 'Gender', 'value': 'Gender'},
                        {'label': 'Residence', 'value': 'Residence'}
                    ],
                    value='Gender',  # Set an initial value
                    labelStyle={'display': 'inline-block', 'margin-right': '10px'}
                ),dcc.Graph(id='bar-chartp2',style={'height': '60vh'})
            ])
        ]),
        dbc.Row([
            html.Div(
                [
                    html.H3("Labor Underutilization", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
                ],
                style={'text-align': 'center'}
            ),
            dbc.Col([
                html.Div([
                dcc.RadioItems(
                    id='toggle-radio',
                    options=[
                        {'label': 'Gender', 'value': 'gender'},
                        {'label': 'Residence', 'value': 'residence'}
                    ],
                    value='gender',
                    labelStyle={'display': 'inline-block', 'margin-right': '10px'}
                    
                ),
                
                dcc.Graph(id='pyramid-chart')
                ],style={'border': '2px solid #ccc'}),
            ],width=7),
            dbc.Col([
                html.Div(
                [
                    html.H3(" Time-related underemployment by branches of economic activities", style={'color': 'black', 'padding': '10px'}),
                ],
                style={'text-align': 'center'}
            ),
                dcc.Dropdown(
                    id='isic-dropdown',
                    options=[{'label': i, 'value': i} for i in dfUnder2['ISIC High level'].unique()],
                    value=dfUnder2['ISIC High level'].unique()[0],
                    style={
                        'width': '100%',
                        'text-align': 'center',
                        'font-size': '15px',  # Adjust font size
                        'border-radius': '8px',  # Add rounded corners 
                        },
                    clearable=False,
                    searchable=False
                ),
                html.Br(),
                html.Br(),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                        html.H4("Male Counts"),
                        html.P(id='male-count', style={'font-size': '20px'})
                        ],className="border-start border-info border-5")
                    ], style={'margin': '10px', 'border': '2px solid #ccc', 'width': 'auto'})
                    ]),
                    dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                        html.H4("Female Counts"),
                        html.P(id='female-count', style={'font-size': '20px'})
                        ],className="border-start border-info border-5")
                    ], style={'margin': '10px', 'border': '2px solid #ccc', 'width': 'auto'})
                    ])
                ], justify='center'),
                dbc.Row([
                    dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                        html.H4("Urban Counts"),
                        html.P(id='urban-count', style={'font-size': '20px'})
                        ],className="border-start border-info border-5")
                    ], style={'margin': '10px', 'border': '2px solid #ccc', 'width': 'auto'})
                    ]),
                    dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                        html.H4("Rural Counts"),
                        html.P(id='rural-count', style={'font-size': '20px'})
                        ],className="border-start border-info border-5")
                    ], style={'margin': '10px', 'border': '2px solid #ccc', 'width': 'auto'})
                    ])
                ], justify='center')
                ], width=5)



        ])
],
fluid=True
)
#------------------------------------------------------------------------------------------------------------------------------------------------
# Define callback to update the chart based on radio selection
@callback(
    Output('bar-chartp2', 'figure'),
    [Input('category-radio', 'value')]
)
def update_bar_chart(selected_category):
    if selected_category == 'Gender':
        fig = px.bar(dfUnempl, x='Categories', y=['Male', 'Female'], color_discrete_sequence=['blue', 'orange'],
                     labels={'Male': 'Male', 'Female': 'Female', 'Categories': 'Age Group'})
    elif selected_category == 'Residence':
        fig = px.bar(dfUnempl, x='Categories', y=['Urban', 'Rural'], color_discrete_sequence=['green', 'red'],
                     labels={'Urban': 'Urban', 'Rural': 'Rural', 'Categories': 'Age Group'})
    
    fig.update_layout(barmode='stack')  # Stack the bars for each category

    return fig
#------------------------------------------------------------------------------------------------------------------------------------------------
# Define the callback to update the chart based on the radio button selection
@callback(
    Output('pyramid-chart', 'figure'),
    [Input('toggle-radio', 'value')]
)
def update_pyramid_chart(selected_option):
    if selected_option == 'gender':
        labels = ['16-24 yrs', '25-34 yrs', '35-54 yrs', '55-64 yrs', '65+ yrs']
        male_data = dfunder1['Male'].tolist()
        female_data = [-1 * value for value in dfunder1['Female'].tolist()]  # Negative values for females
        title = 'Time related under employment by Age Group/sex'
    else:
        labels = ['16-24 yrs', '25-34 yrs', '35-54 yrs', '55-64 yrs', '65+ yrs']
        urban_data = dfunder1['Urban'].tolist()
        rural_data = [-1 * value for value in dfunder1['Rural'].tolist()]  # Negative values for rural
        title = 'Time related under employment by Age Group/Residence area'

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=labels,
        x=male_data if selected_option == 'gender' else urban_data,
        orientation='h',
        name='Male' if selected_option == 'gender' else 'Urban',
        marker=dict(color='#e8422c')
    ))

    fig.add_trace(go.Bar(
        y=labels,
        x=female_data if selected_option == 'gender' else rural_data,
        orientation='h',
        name='Female' if selected_option == 'gender' else 'Rural',
        marker=dict(color='#e8b92c')
    ))

    fig.update_layout(barmode='relative', title=title)

    return fig
#------------------------------------------------------------------------------------------------------------------------------------------------
# Define the callback to update the cards based on the dropdown selection
@callback(
    [Output('male-count', 'children'),
     Output('female-count', 'children'),
     Output('urban-count', 'children'),
     Output('rural-count', 'children')],
    [Input('isic-dropdown', 'value')]
)
def update_cards(selected_option):
    filtered_df = dfUnder2[dfUnder2['ISIC High level'] == selected_option]

    male_count = f"Total: {filtered_df['Male'].values[0]:,}"
    female_count = f"Total: {filtered_df['Female'].values[0]:,}"
    urban_count = f"Total: {filtered_df['Urban'].values[0]:,}"
    rural_count = f"Total: {filtered_df['Rural'].values[0]:,}"

    return male_count, female_count, urban_count, rural_count
#------------------------------------------------------------------------------------------------------------------------------------------------
