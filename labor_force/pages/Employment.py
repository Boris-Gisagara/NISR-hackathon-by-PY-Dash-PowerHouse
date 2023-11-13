import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc,html,callback
import dash.dependencies as dd
import pandas as pd
import plotly.graph_objects as go
from math import pi
import matplotlib.pyplot as plt
from dash.dependencies import Input, Output
from mpldatacursor import datacursor
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

dash.register_page(__name__, path='/Employment')

#All datasets used in this panel
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data for formal and informal sector 
# Link to the dataset on GitHub
forsec_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Formal_Sector.xlsx'

# Load the dataset
ForSec = pd.read_excel(forsec_url, engine='openpyxl')

# Link to the dataset on GitHub
forsec_ag_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Formal_Sector_Out_Of_Agriculture.xlsx'

# Load the dataset
ForSecAg = pd.read_excel(forsec_ag_url, engine='openpyxl')

# Link to the dataset on GitHub
infsec_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Informal_Sector.xlsx'

# Load the dataset
InfSec = pd.read_excel(infsec_url, engine='openpyxl')

# Link to the dataset on GitHub
infsec_ag_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Informal_Sector_Out_Of_Agriculture.xlsx'

# Load the dataset
InfSecAg = pd.read_excel(infsec_ag_url, engine='openpyxl')


datasets = {
    'Formal Sector': ForSec,
    'Formal Sector out of Agriculture': ForSecAg,
    'Informal Sector': InfSec,
    'Informal Sector out of Agriculture': InfSecAg
}
# Get unique categories from the dataset
categories = InfSec['Categories'].unique()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data for the employment status in rwanda for the heatmap
# Link to the dataset on GitHub
economic_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Economic.xlsx'

# Load the dataset
Economic = pd.read_excel(economic_url, engine='openpyxl')

# Link to the dataset on GitHub
age_range1_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Age_range.xlsx'

# Load the dataset
Age_range1 = pd.read_excel(age_range1_url, engine='openpyxl')

# Link to the dataset on GitHub
occupations_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Occupations.xlsx'

# Load the dataset
Occupations = pd.read_excel(occupations_url, engine='openpyxl')


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data for job creation and working time
# Link to the dataset on GitHub
job_creation_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Job_creation.xlsx'

# Load the dataset
Job_creation = pd.read_excel(job_creation_url, engine='openpyxl')

# Define income ranges for dropdown options
income_ranges = Job_creation['Income'].tolist()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data for the income section
# Link to the dataset on GitHub
age_range_inc_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/IncAge_range.xlsx'

# Load the dataset
Age_rangeInc = pd.read_excel(age_range_inc_url, engine='openpyxl')

# Link to the dataset on GitHub
education_level_inc_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/IncEducation_level.xlsx'

# Load the dataset
Education_levelInc = pd.read_excel(education_level_inc_url, engine='openpyxl')

# Link to the dataset on GitHub
occupation_inc_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/IncOccupation.xlsx'

# Load the dataset
OccupationInc = pd.read_excel(occupation_inc_url, engine='openpyxl')

datasetsIncome = {
    'Age_range': Age_rangeInc,
    'Education_level':Education_levelInc,
    'Occupation': OccupationInc,
    
}
# Define dataset options for dropdown
dataset_options = [{'label': dataset, 'value': dataset} for dataset in datasetsIncome.keys()]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data and chart creation for the working time 
# Link to the dataset on GitHub
working_time_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/working_Time.xlsx'

# Load the dataset
workingTime = pd.read_excel(working_time_url, engine='openpyxl')

# Melt the DataFrame to have a tidy format
workingTime_melted = pd.melt(workingTime, id_vars=["Time"], var_name=["Location_Gender"], value_name="Population")

# Split the Location_Gender column into separate Location and Gender columns
workingTime_melted[['Location', 'Gender']] = workingTime_melted['Location_Gender'].str.split('_', expand=True)

# Create sunburst chart
figwork = px.sunburst(workingTime_melted, path=["Time", "Location", "Gender"], values="Population", title="Employed population with working time in Rwanda-Rural Urban")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
layout = dbc.Container([
     # Link to CSS file for this page
        html.Link(
             # the path to CSS file
        ),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Employment Status in Rwanda", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
            ],
            style={'text-align': 'center','border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}, 
        ),
        dbc.Row([
            dbc.Col([
                # Dropdown for selecting dataset
                dcc.Dropdown(
                    id='dataset-dropdownEmploy',
                    options=[
                        {'label': 'Employed Population by Economic Branches', 'value': 'dataset1'},
                        {'label': 'Employed population By Age_range', 'value': 'dataset2'},
                        {'label': 'Employed Population by Occupations', 'value': 'dataset3'}
                    ],
                    value='dataset1',  # Default selected value
                    style={
                        'width': '50%',
                        'text-align': 'center',
                        'font-size': '15px',  # Adjust font size
                        'border-radius': '8px',  # Add rounded corners 
                        },
                    clearable=False,
                    searchable=False
                ),
                html.Div([
                    # Heatmap figure
                    dcc.Graph(id='heatmap-graph'),
                ], style={'border': '2px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),               
            ],width=12),
            
        ]),
        html.Br(),
        dbc.Row([
            html.Div(
                [
                    html.H3("Formal & Informal Sector", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
                ],
                style={'text-align': 'center'}
            ),
            dbc.Col([
                html.Div([
                dcc.Dropdown(
                    id='scatter-dropdown',
                    options=[{'label': 'Formal Sector', 'value': 'formSec'},
                            {'label': 'Formal Sector out of Agriculture', 'value': 'formSecA'},
                            {'label': 'Informal Sector', 'value': 'InforSec'},
                            {'label': 'Informal Sector out of Agriculture', 'value': 'InforSecA'}],  # Add more datasets as needed
                    value='formSec',  # Default selected dataset
                    style={
                        'width': '50%',
                        'text-align': 'center',
                        'font-size': '15px',  # Adjust font size
                        'border-radius': '8px',  # Add rounded corners 
                        },
                    clearable=False,
                    searchable=False
                ),
                dcc.Graph(id='scatter-plot')
                ], style={'border': '2px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
            ],width=12
            ),
            
        ]),
        html.Br(),
        dbc.Row([
            html.Div(
                [
                    html.H3("Job creation and Working Time", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
                ],
                style={'text-align': 'center'}
            ),
            dbc.Col([
                # Dropdown for selecting income range
                dcc.Dropdown(
                    id='income-dropdown',
                    options=[{'label': income, 'value': income} for income in income_ranges],
                    value=income_ranges[0],  # Default selected value
                    style={
                        'width': '50%',
                        'text-align': 'center',
                        'font-size': '15px',  # Adjust font size
                        'border-radius': '8px',  # Add rounded corners 
                        },
                    clearable=False,
                    searchable=False
                ),

                # Card to display total
                html.Div([
                    html.H4('Labour Force '),
                    html.P(id='total-value', style={'fontSize': 24})
                ], style={'textAlign': 'center', 'border': '3px solid #ddd', 'padding': '5px', 'margin-top': '10px'}),

                # Gauges for percentages in the same row
                html.Div([
                    # Rwanda Gauge
                    html.Div([
                        html.H4("Rates in Rwanda by Income", style={'textAlign': 'center'}),
                        dcc.Graph(id='rwanda-gauge', figure={}),
                    ], style={'flex': '0.5'}),
                    
                    # Urban Gauge
                    html.Div([
                        html.H4("Rates in Urban by Income", style={'textAlign': 'center'}),
                        dcc.Graph(id='urban-gauge', figure={}),
                    ], style={'flex': '0.5'}),
                    
                    # Rural Gauge
                    html.Div([
                        html.H4("Rates in Rural by Income", style={'textAlign': 'center'}),
                        dcc.Graph(id='rural-gauge', figure={}),
                    ], style={'flex': '0.5'}),
                ], style={'display': 'flex', 'justifyContent': 'space-around', 'margin-top': '10px'}),                
            ],width=7),
            dbc.Col([
                html.Div([
                    dcc.Graph(figure=figwork),
                ], style={'border': '2px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
            ], width=5)

        ]),
        html.Br(),
        dbc.Row([
            html.Div(
                [
                    html.H3("Incomes from employment ", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
                ],
                style={'text-align': 'center'}
            ),
            dbc.Col([
                html.Div([
                # Dropdown for selecting dataset
                dcc.Dropdown(
                    id='dataset-dropdown',
                    options=dataset_options,
                    value=list(datasetsIncome.keys())[0],  # Default selected value
                    style={
                        'width': '50%',
                        'text-align': 'center',
                        'font-size': '15px',  # Adjust font size
                        'border-radius': '8px',  # Add rounded corners 
                        },
                    clearable=False,
                    searchable=False
                ),

                # Stacked bar chart
                dcc.Graph(id='stacked-bar-chart')
                ], style={'border': '2px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
            ],width=12),
        ]),
        html.Br(),

],
fluid=True
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Define callback to update scatter plot based on selected dataset in The formal/informal sector
@callback(
    Output('scatter-plot', 'figure'),
    [Input('scatter-dropdown', 'value')]
)
def update_plot(selected_dataset):
    # Load the corresponding dataset based on selected value
    if selected_dataset == 'formSec':
        dataset = ForSec
        title = 'Labour Force in Formal Sector'
    # Add more conditions for additional datasets if needed
    elif selected_dataset == 'formSecA':
        dataset = ForSecAg
        title = 'Labour Force in Formal Sector out of Agriculture'
    elif selected_dataset == 'InforSec':
        dataset = InfSec
        title = 'Informal Sector'
    elif selected_dataset == 'InforSecA':
        dataset = InfSecAg
        title = 'Informal Sector out of Agriculture'  
    else:
        dataset = ForSec  # Default to formSec
        title = 'Informal Sector out of Agriculture'

    # Create scatter plot based on the selected dataset
    fig = px.scatter(dataset, x='Categories', y='Labor Force', color='Occupation',
                     size='Labor Force', hover_name='Occupation',
                     labels={'Labor Force': 'Labor Force'},
                     title=title,
                     height=600, size_max=50)  # Set minimum point size to 40

    # Customize axis labels and tick angle
    fig.update_xaxes(tickangle=45, tickmode='array', tickvals=categories, title_text='Categories')
    fig.update_yaxes(title_text='Labor Force')

    return fig
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Callback to update heatmap based on selected dataset
@callback(
    Output('heatmap-graph', 'figure'),
    [Input('dataset-dropdownEmploy', 'value')]
)
def update_heatmap(selected_dataset):
    if selected_dataset == 'dataset1':
        df = Economic
        title = 'Employed Population by Economic Branches'
    elif selected_dataset == 'dataset2':
        df = Age_range1
        title = 'Employed population By age range'
    elif selected_dataset == 'dataset3':
        df = Occupations
        title = 'Employed Population by Occupations'
    else:
        # Default to dataset 1 if none selected
        df = Economic
        title = 'Employed Population by Economic Branches'

    # Create a heatmap with plotly
    fig = go.Figure(data=go.Heatmap(
        z=df.drop(columns=['Category']),
        x=df.columns[1:],  # Exclude the 'Branches' column from x-axis
        y=df['Category'],
        colorscale='viridis',
        colorbar=dict(title='Employed people')
    ))

    # Update the layout for hover annotation
    fig.update_layout(
        xaxis=dict(ticks='', showgrid=False),  # Hide x-axis ticks and grid
        yaxis=dict(showgrid=False),  # Hide y-axis grid
        title=title,  # Display selected dataset in the title
    )

    # Add hover information
    fig.update_traces(hovertemplate='Category: %{y}<br>%{x}: %{z:.0f}')

    return fig

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Callback to update card and gauges based on selected income range for the income section
@callback(
    [Output('total-value', 'children'),
     Output('rwanda-gauge', 'figure'),
     Output('urban-gauge', 'figure'),
     Output('rural-gauge', 'figure')],
    [Input('income-dropdown', 'value')]
)
def update_display(selected_income):
    # Filter DataFrame based on selected income range
    selected_row = Job_creation[Job_creation['Income'] == selected_income].squeeze()

    # Update card with total value
    total_value = selected_row['Total']

    # Update gauges with percentage values
    rwanda_percentage = selected_row['Rwanda']
    urban_percentage = selected_row['Urban']
    rural_percentage = selected_row['Rural']

    # Create gauge figures
    rwanda_fig = create_gauge('Rwanda', rwanda_percentage)
    urban_fig = create_gauge('Urban', urban_percentage)
    rural_fig = create_gauge('Rural', rural_percentage)

    return total_value, rwanda_fig, urban_fig, rural_fig

# Function to create a gauge figure
def create_gauge(label, value):
    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': label, 'font': {'size': 14}},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "darkblue"},
               'bgcolor': "white",
               'borderwidth': 2,
               'bordercolor': "gray",
               'steps': [{'range': [0, 100], 'color': "lightgray"}],
               'threshold': {'line': {'color': "red", 'width': 2}, 'thickness': 0.75, 'value': 60}}))

    fig.update_layout(height=150, margin=dict(l=10, r=10, t=10, b=10))
    return fig
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Callback to update the stacked bar chart based on selected dataset
@callback(
    Output('stacked-bar-chart', 'figure'),
    [Input('dataset-dropdown', 'value')]
)
def update_stacked_bar_chart(selected_dataset):
    selected_data = datasetsIncome[selected_dataset]

    fig = go.Figure()

    for column in ['Urban', 'Rural']:
        fig.add_trace(go.Bar(
            x=selected_data['Category'],
            y=selected_data[column],
            name=column,
            marker_color='rgb(26, 118, 255)' if column == 'Urban' else 'rgb(55, 83, 109)',
        ))

    fig.update_layout(
        barmode='group',
        title=f'Income Distribution by {selected_dataset}',
        xaxis_title=f'{selected_dataset}',
        yaxis_title='Income(in Rwf)',
        showlegend=True,
        legend=dict(x=1, y=1.0, bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'),
    )

    return fig
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
