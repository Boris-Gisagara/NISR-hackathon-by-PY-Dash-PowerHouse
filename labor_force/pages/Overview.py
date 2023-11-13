# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import plotly.express as px
# import numpy as np
# import plotly.graph_objects as go
# import dash
# from dash import dcc, html
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc,html,callback
import dash.dependencies as dd
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output



dash.register_page(__name__, path='/')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

dataLF = {
    "Status": ["Employed", "Unemployed", "Outside Labor Force"],
    "Male": [1977704, 429744, 1346420],
    "Female": [1568648, 487200, 2153870],
    "Urban": [851356, 217769, 567892],
    "Rural": [2694996, 699175, 2932398]
}

df1 = pd.DataFrame(dataLF)
# Create a spider chart
fig = go.Figure()

for index, row in df1.iterrows():
    fig.add_trace(go.Scatterpolar(
        r=[row["Male"], row["Female"], row["Urban"], row["Rural"], row["Male"]],  # Close the loop
        theta=["Male", "Female", "Urban", "Rural", "Male"],  # Close the loop
        # fill="toself",
        name=row["Status"]
    ))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, df1[["Male", "Female", "Urban", "Rural"]].max().max()],
            showgrid=True,       # Show the radial grid lines
            gridwidth=1,         # Set the width of the grid lines
            gridcolor='#233336'    # Set the color of the grid lines to black
        )
    )
)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

dataTP = {
    'Age_Range': [
        '0-4', '5-9', '10-14 ', '15-19 ', '20-24 ', '25-29 ',
        '30-34 ', '35-39 ', '40-44 ', '45-49 ', '50-54 ', '55-59 ',
        '60-64 ', '65-69 ', '70-74 ', '75+'
    ],
    'Total': [
        1553553, 1628364, 1600085, 1661630, 1157947, 896904, 860513, 820692,
        707625, 490542, 419950, 343320, 333960, 246318, 164846, 191780
    ],
    'Male': [
        776063, 823677, 804702, 820717, 580976, 413564, 422771, 387942,
        326904, 216429, 184435, 164035, 151138, 105437, 71231, 69883
    ],
    'Female': [
        777490, 804687, 795383, 840913, 576971, 483339, 437742, 432749,
        380721, 274113, 235516, 179285, 182822, 140881, 93616, 121898
    ],
    'Urban': [
        298673, 277015, 241973, 291405, 277902, 227985, 221883, 180065,
        146620, 91497, 68406, 57024, 44635, 34132, 19807, 24061
    ],
    'Rural': [
        1254880, 1351348, 1358113, 1370225, 880045, 668919, 638630, 640626,
        561004, 399045, 351544, 286296, 289325, 212186, 145039, 167719
    ]
}
# Create a DataFrame from the sample data
df2 = pd.DataFrame(dataTP)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# data for disabilities table
# Creating the Sankey diagram
dataDS = {
    "source": ["Seeing", "Hearing", "Walking", "Remembering", "Washing, dressing", "Communicating"],
    "target": ["Male", "Female", "Urban", "Rural", "5-15 yrs", "16+ yrs"],
    "value": [
        [21345, 26575, 8443, 39478, 6280, 41641],
        [19486, 21599, 4843, 36242, 5737, 35348],
        [52857, 60618, 18003, 95471, 15877, 97598],
        [32182, 29020, 6714, 54489, 11167, 50036],
        [16669, 20454, 5903, 31220, 10115, 27008],
        [17829, 9648, 3478, 23998, 14048, 13429]
    ]
}

# Create the Sankey diagram
fig6 = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=dataDS["source"] + dataDS["target"]
    ),
    link=dict(
        source=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],
        target=[6, 7, 8, 9, 10, 11, 6, 7, 8, 9, 10, 11, 6, 7, 8, 9, 10, 11, 6, 7, 8, 9, 10, 11, 6, 7, 8, 9, 10, 11, 6, 7, 8, 9, 10, 11],
        value=sum(dataDS["value"], []),
        
    )
))

# Update the layout and appearance
fig6.update_layout(
    title="Disabled persons by Type of Disability/Gender/Residence/Age group",
    font=dict(size=10),
    title_x=0.5,
    title_y=0.9,
)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data for the pie chart on employment status among disabled persons
# Link to the dataset on GitHub
disability2_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/disability2.xlsx'

# Load the dataset
Disability2 = pd.read_excel(disability2_url, engine='openpyxl')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#load the dataset for migration
# Link to the dataset on GitHub
migrants_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Migrants.xlsx'

# Load the dataset
Migrants = pd.read_excel(migrants_url, engine='openpyxl')

# Link to the dataset on GitHub
internal_migrants_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Internal_migrants.xlsx'

# Load the dataset
Internal_migrants = pd.read_excel(internal_migrants_url, engine='openpyxl')

# Link to the dataset on GitHub
international_migrants_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/International_migrants.xlsx'

# Load the dataset
International_migrants = pd.read_excel(international_migrants_url, engine='openpyxl')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
df3_url='https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/labor.xlsx'
df3 = pd.read_excel(df3_url, engine='openpyxl')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data for the bar chart on employment status in disabled persons
# Link to the dataset on GitHub
migrants_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/df_migrants.xlsx'

# Load the dataset
migrants = pd.read_excel(migrants_url, engine='openpyxl')

# Link to the dataset on GitHub
internal_migrants_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/df_internal_migrants.xlsx'

# Load the dataset
internal_migrants = pd.read_excel(internal_migrants_url, engine='openpyxl')

# Link to the dataset on GitHub
international_migrants_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/df_international_migrants.xlsx'

# Load the dataset
international_migrants = pd.read_excel(international_migrants_url, engine='openpyxl')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Define the content for the Overview page
layout = dbc.Container(
    [
         # Link to CSS file for this page
        html.Link(
            rel="stylesheet",
            href="/assets/overview.css"  # the path to CSS file
        ),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Total Population Overview", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
            ],
            style={'text-align': 'center'}
        ),
        # Four cards for labor force statistics in a grid layout
        dbc.Row([
            # Card 1: Total Population
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.Div("13,078,028", style={'fontSize': '20px'}),
                        html.Div("Total Population", style={'fontSize': '16px'}),
                    ],className="border-start border-info border-5")
                ],className="text-center m-4"),
                width=3
            ),

            # Card 2: Working Age Population
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.Div("7,963,586", style={'fontSize': '20px'}),
                        html.Div("Working Age Population", style={'fontSize': '16px'}),
                    ],className="border-start border-info border-5")
                ],className="text-center m-4"),
                width=3
            ),

            # Card 3: Labor Force
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.Div("4,463,296", style={'fontSize': '20px'}),
                        html.Div("Labor Force", style={'fontSize': '16px'}),
                    ],className="border-start border-info border-5")
                ],className="text-center m-4"),
                width=3
            ),

            # Card 4: Outside Labor Force Population
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.Div("3,500,290", style={'fontSize': '20px'}),
                        html.Div("Outside Labor Force Population", style={'fontSize': '16px'}),
                    ],className="border-start border-info border-5")
                ],className="text-center m-4"),
                width=3
            ),
        ], className="mt-4"),
        html.Br(),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
        # Graphs Section
        dbc.Row([
            # Graph 1: Total Population by Age Group
            dbc.Col(
                html.Div([
                    dcc.Graph(
                    figure=px.bar(df2, x='Age_Range', y='Total', title="Total Population by Age Group"),
                    style={'height': '400px'}
                ),                    
                ], style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
                
                width=4
            ),

            # Graph 2: Total Population by Gender
            dbc.Col(
                html.Div([
                    dcc.Graph(
                    figure=px.bar(df2, x='Age_Range', y=['Male', 'Female'], title="Total Population by Gender"),
                    style={'height': '400px'}
                ),
                ], style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
                
                width=4
            ),

            # Graph 3: Total Population by Residence Area
            dbc.Col(
                html.Div([
                    dcc.Graph(
                    figure=px.bar(df2, x='Age_Range', y=['Urban', 'Rural'], title="Total Population by Residence Area"),
                    style={'height': '400px'}
                ),
                ], style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
                
                width=4
            ),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        ], className="mt-4"),
        html.Br(),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("The Labor Force", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
            ],
            style={'text-align': 'center'}
        ),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H3("Population in Total by Categories",style={ 'textAlign': 'center'}),
                    dcc.Graph(figure=fig),
                ], style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
                
                ],width=6
            ),
            dbc.Col([
                html.Div([
                    html.H3("Population Comparison by Age Group, Employment Status, and Gender/Residence",style={'fontSize': '20px', 'textAlign': 'center'}),
                dcc.Dropdown(
                    id='dropdown-input',
                    options=[
                        {'label': 'Employed', 'value': 'Employed'},
                        {'label': 'Unemployed', 'value': 'Unemployed'},
                        {'label': 'Outside The Labor', 'value': 'Outside The Labor'}
                    ],
                    value='Employed',  # Default selection
                    style={
                        'width': '70%',
                        'text-align': 'center',
                        'font-size': '15px',  # Adjust font size
                        'border-radius': '8px',  # Add rounded corners 
                    },
                    clearable=False,
                    searchable=False
                    
                ),
                html.Br(),
                dcc.RadioItems(
                     id='radio-input',
                     options=[
                         {'label': 'Gender', 'value': 'gender'},
                         {'label': 'Residence', 'value': 'Residence'}
                    ],
                    value='gender',  # Default selection
                    labelStyle={'display': 'inline-block'}
                ),
                dcc.Graph(id='bar-chart'),
                ], style={'border': '2px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
                
                ], width=6            
            ),
        ]),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        html.Br(),
        dbc.Row([
            # Horizontal frame for the title for "Disabled Persons" section
            html.Div(
                [
                    html.H3("Disabled Persons by Gender/Residence/Age Group", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
                ],
                style={'text-align': 'center'}
            ),
            dbc.Col([
                html.Div([
                    dcc.Graph(figure=fig6),
                ], style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),            
                ],width=7
            ),
            # Updated layout with a dropdown 
            dbc.Col([
                html.Div([
                    dcc.Dropdown(
                        id='employment-dropdown',
                        options=[
                            {'label': 'Employed', 'value': 'Employed'},
                            {'label': 'Unemployed', 'value': 'Unemployed'},
                            {'label': 'Outside labor force', 'value': 'Outside labour force'}
                        ],
                        value='Employed',  # Default selected option
                        style={'width': '100%','textAlign': 'center'},
                        clearable=False,
                        searchable=False
                    ),
                    html.Div([
                        dcc.Graph(id='pie-chart'),
                    ], style={'display': 'inline-block'}),
                ], style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
            ], width=5)
        ]),
        html.Br(),
        # Horizontal frame for the title for "Disabled Persons" section
            html.Div(
                [
                    html.H3("Migrant Population by Reason for moving and Employment Status", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
                ],
                style={'text-align': 'center'}
            ),
        dbc.Row([
            dbc.Col([
                html.Div([
                    dcc.Dropdown(
                        id='Mig-dropdown',
                        options=[
                            {'label': 'Migrants', 'value': 'Migrants'},
                            {'label': 'Internal migrants', 'value': 'Internal migrants'},
                            {'label': 'International migrants', 'value': 'International migrants'}
                        ],
                        value='Migrants',
                        style={
                            'width': '70%',
                            'text-align': 'center',
                            'font-size': '15px',  # Adjust font size
                            'border-radius': '8px',  # Add rounded corners                            
                            },
                            clearable=False,
                            searchable=False
                    ),
                    dcc.Graph(id='Mig-barChart'),
                ], style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'})
            ],width=6),
            dbc.Col([
                html.Div([
                    # Dropdown to select dataset
                    dcc.Dropdown(
                        id='migadataset-dropdown',
                        options=[
                            {'label': 'Migrants', 'value': 'migrants'},
                            {'label': 'Internal Migrants', 'value': 'internal_migrants'},
                            {'label': 'International Migrants', 'value': 'international_migrants'}
                        ],
                        value='migrants',  # Default selected dataset
                        style={
                            'width': '50%',
                            'text-align': 'center',
                            'font-size': '15px',  # Adjust font size
                            'border-radius': '8px',  # Add rounded corners
                            },
                        clearable=False,
                        searchable=False
                    ),

                    # Graph to display the horizontal grouped bar chart
                    dcc.Graph(id='employment1-bar-chart')
                ], style={'border': '1px solid #ccc', 'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'})

            ],width=6)
        ]),
        html.Br(),   
    ],
    
    fluid=True
),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Callback to update the pie chart based on the slider value
# Updated callback using the dropdown value
@callback(
    Output('pie-chart', 'figure'),
    [Input('employment-dropdown', 'value')]
)
def update_pie_chart(selected_value):
    selected_data = Disability2[['Type of disability', selected_value]].copy()

    # Convert values to numeric
    selected_data.loc[:, selected_value] = pd.to_numeric(
        selected_data[selected_value], errors='coerce'
    )

    # Create pie chart
    fig = px.pie(
        selected_data,
        names='Type of disability',
        values=selected_value,
        title=f'Distribution of {selected_value} population among Types of Disability'
    )

    return fig

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Callback to update the bar chart based on the selected dataset for migration
@callback(
    Output('Mig-barChart', 'figure'),
    [Input('Mig-dropdown', 'value')]
)
def update_graph(selected_dataset):
    if selected_dataset == 'Migrants':
        migri = Migrants
    elif selected_dataset == 'Internal migrants':
        migri = Internal_migrants
    elif selected_dataset == 'International migrants':
        migri = International_migrants

    figure = {
        'data': [
            {'y': migri['Reasons'], 'x': migri['Employed'], 'type': 'bar', 'name': 'Employed', 'orientation': 'h'},
            {'y': migri['Reasons'], 'x': migri['Unemployed'], 'type': 'bar', 'name': 'Unemployed', 'orientation': 'h'},
            {'y': migri['Reasons'], 'x': migri['Outside Labour Force'], 'type': 'bar', 'name': 'Outside Labour Force', 'orientation': 'h'}
        ],
        'layout': {
            'title': f'{selected_dataset} Distribution with reasons',
            'barmode': 'group',
            'hovermode': 'closest',
            'yaxis': {'title': '', 'tickfont': {'size': 6}, 'fontcolor': 'black'},
            'xaxis': {'title': 'Population'},
            'hoverlabel': {'bgcolor': 'white'},
            'legend': {'x': 1, 'y': 1.0}
        }
    }

    return figure
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Callback to update the bar chart based on the selected dataset for Employment status 
@callback(
    Output('bar-chart', 'figure'),
    Input('radio-input', 'value'),
    Input('dropdown-input', 'value')
)
def update_bar_chart(selected_radio, selected_dropdown):
    df3_url='https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/labor.xlsx'
    df3 = pd.read_excel(df3_url, engine='openpyxl')
    # df3=pd.read_excel(r'C:\Users\user\OneDrive\Documents\python works\labor_force\dataset\labor.xlsx')
    if selected_radio == 'gender':
        # Filter the data for the selected gender (male/female)
        filtered_data = df3[df3['Status'] == selected_dropdown][['Age Groups', 'Male Pop', 'Female Pop']]
        x = 'Age Groups'
        y1 = 'Male Pop'
        y2 = 'Female Pop'
        title = f"{selected_dropdown} Population by Age Group and Gender"
        hover_text = ['Male', 'Female']
        legend_labels = {'Male': 'Male', 'Female': 'Female'}
    else:
        # Filter the data for the selected residence (urban/rural)
        filtered_data = df3[df3['Status'] == selected_dropdown][['Age Groups', 'Urban Pop', 'Rural Pop']]
        x = 'Age Groups'
        y1 = 'Urban Pop'
        y2 = 'Rural Pop'
        title = f"{selected_dropdown} Population by Age Group and Residence"
        hover_text = ['Urban', 'Rural']
        legend_labels = {'Urban': 'Urban', 'Rural': 'Rural'}

    # Create the bar chart
    figure = {
        'data': [
            {'x': filtered_data[x], 'y': filtered_data[y1], 'type': 'bar', 'name': legend_labels[hover_text[0]], 'hovertext': hover_text[0]},
            {'x': filtered_data[x], 'y': filtered_data[y2], 'type': 'bar', 'name': legend_labels[hover_text[1]], 'hovertext': hover_text[1]}
        ],
        'layout': {
            'title': title,
            'xaxis': {'title': 'Age Groups'},
            'yaxis': {'title': 'Population'},
            'barmode': 'group'
        }
    }

    return figure
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Define callback to update the graph based on the selected dataset
@callback(
    Output('employment1-bar-chart', 'figure'),
    [Input('migadataset-dropdown', 'value')]
)
def update_graph(selected_dataset):
    if selected_dataset == 'migrants':
        df = migrants
    elif selected_dataset == 'internal_migrants':
        df = internal_migrants
    elif selected_dataset == 'international_migrants':
        df = international_migrants
    else:
        df = migrants  # Default to the first dataset if an invalid option is selected

    # Create horizontal grouped bar chart
    figure = {
        'data': [
            go.Bar(x=df['Employed'], y=df['Category'], orientation='h', name='Employed'),
            go.Bar(x=df['Unemployed'], y=df['Category'], orientation='h', name='Unemployed'),
            go.Bar(x=df['Outside Labour Force'], y=df['Category'], orientation='h', name='Outside Labour Force')
        ],
        'layout': go.Layout(
            title=f'{selected_dataset} distribution by employment status',
            barmode='group',
            #hovermode='closest',
            xaxis=dict(title='Population'),
            # yaxis=dict(title='Category'),
            hoverlabel=dict(bgcolor='white'),
            #hoverinfo='x+y'
        )
    }

    return figure

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
