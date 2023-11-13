import dash
import dash_bootstrap_components as dbc
from dash import dcc, html,callback
import dash.dependencies as dd
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output


dash.register_page(__name__, path='/Youth&Education')

#Labor Forcee sunburst
# Link to the dataset on GitHub
youth_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Youth.xlsx'

# Load the dataset
dfSun = pd.read_excel(youth_url, engine='openpyxl')

#Scatter plot for NEET
# Link to the dataset on GitHub
neet_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/neet.xlsx'

# Load the dataset
df = pd.read_excel(neet_url, engine='openpyxl')

figScatter1 = px.scatter(df, y="Gender/Residence", x="Pop", color="Category", symbol="Category")
figScatter1.update_traces(marker_size=10)
# Sample data for NEET
EdField = {
    'Field': ['General program', 'Education', 'Humanities and arts', 'Social sciences, business and law', 'Science', 'Engineering, manufacturing and construction', 'Agriculture', 'Health and welfare', 'Services', 'No Education'],
    'Total': [5596521, 145570, 111448, 303031, 506331, 173683, 45989, 66434, 57432, 957147]
}
#data for the second card Tchnical training
# Link to the dataset on GitHub
technical_training_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/Technical%20training.xlsx'

# Load the dataset
TechT = pd.read_excel(technical_training_url, engine='openpyxl')

# Dropdown options
dropdown_options_tech = [{'label': skill, 'value': skill} for skill in TechT['Technical skills']]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# the dataset for the radar chart on the education attainment
# Link to the dataset on GitHub
education_attainment_url = 'https://github.com/Boris-Gisagara/NISR-hackathon-by-PY-Dash-PowerHouse/raw/main/dataset/education_attainment.xlsx'

# Load the dataset
EdAtt = pd.read_excel(education_attainment_url, engine='openpyxl')

# Create a spider chart
figSpid = go.Figure()

for index, row in EdAtt.iterrows():
    figSpid.add_trace(go.Scatterpolar(
        r=row[["Male", "Female", "Urban", "Rural", "In agriculture", "Not in agriculture", "Male"]].tolist(),  # Close the loop
        theta=["Male", "Female", "Urban", "Rural", "In agriculture", "Not in agriculture", "Male"],  # Close the loop       
        name=row["Level"]
    ))

figSpid.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, EdAtt[["Male", "Female", "Urban", "Rural", "In agriculture", "Not in agriculture"]].max().max()],
            showgrid=True,       # Show the radial grid lines
            gridwidth=1,         # Set the width of the grid lines
            gridcolor='#233336'    # Set the color of the grid lines to black
        )
    )
)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
layout = dbc.Container([
     # Link to CSS file for this page
        html.Link(
             # the path to CSS file
        ),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Youth Employment Status in Rwanda & Field of study/Technical training ", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
            ],
            style={'text-align': 'center'}
        ),
        dbc.Row([
            dbc.Col([
                html.Div([
               html.H3("Youth/Young Population by Gender/Residence/In&Not in Agriculture", style={'fontSize': '20px', 'textAlign': 'center'}),
                dcc.Dropdown(
                    id='category-dropdown',
                    options=[
                        {'label': 'Gender', 'value': 'Gender'},
                        {'label': 'Residence', 'value': 'Residence'},
                        {'label': 'Agriculture', 'value': 'Agriculture'}
                    ],
                    value='Gender',
                    style={
                        'width': '70%',
                        'text-align': 'center',
                        'font-size': '15px',  # Adjust font size
                        'border-radius': '8px',  # Add rounded corners 
                        },
                    clearable=False,
                    searchable=False
                ),
                dcc.Graph(id='sunburst-chart')
                ],style={'borderRadius': '15px', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc'}),  
            ],width=6),
            dbc.Col([
                html.Div([
#card 1---------------------------------------------------------------------------------------------------------------------------------------------------------- 
                html.H3("Population 16 years old and by field of education and Technical Training", style={'fontSize': '20px', 'textAlign': 'center'}),
                dcc.Dropdown(
                    id='field-dropdown',
                    options=[{'label': field, 'value': field} for field in EdField['Field']],
                    value='General program',
                    style={
                        'width': '70%',
                        'text-align': 'center',
                        'font-size': '15px',  # Adjust font size
                        'border-radius': '8px',  # Add rounded corners 
                           },  # Add margin-bottom for space
                    clearable=False,
                    searchable=False
                ),
                html.Br(),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Field of Education", className="card-title text-center", style={'textAlign': 'center', 'fontSize': '20px'}),
                        
                        html.P(id='card-output', className="card-text text-center", style={'textAlign': 'center', 'fontSize': '16px'}),
                    ],className="border-start border-info border-5"),
                    className="mb-3",
                    style={'borderRadius': '15px', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc','width':'100%'}  # Increased box-shadow size
                ),
#card 2----------------------------------------------------------------------------------------------------------------------------------------------------------                
                dcc.Dropdown(
                    id='tech-dropdown',
                    options=dropdown_options_tech,
                    value=dropdown_options_tech[0]['value'],  # Initial value
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
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Technical Training", className="card-title text-center", style={'textAlign': 'center', 'fontSize': '20px'}),
                        
                        html.P(id='tech-total-counts', className="card-text text-center", style={'textAlign': 'center', 'fontSize': '16px'}),
                    ],className="border-start border-info border-5"),
                    className="mb-3",
                    style={'borderRadius': '15px', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc','width':'100%'},  # Increased box-shadow size
                    # className="text-center m-4"
                )
                ]),
            ],width=6,className="mx-auto"
            )
        ]
        ),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        dbc.Row([
            html.Div(
                [
                    html.H3("Youth NEET (Not in Employment, Education, or Training and Education Attainment", style={'color': 'black', 'background-color': '#2fc2df', 'padding': '10px'}),
                ],
                style={'text-align': 'center'}
            ),
            dbc.Col([
                html.Div([
                html.H3("Youth Population NEET", style={'fontSize': '20px', 'textAlign': 'center'}),
                dcc.Graph(figure=figScatter1)       
                ],style={'borderRadius': '15px', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc'}),         
            ],width=7),
            dbc.Col([
                html.Div([
                html.H3("Youth Population by Education Attainment ", style={'fontSize': '20px', 'textAlign': 'center'}),
                dcc.Graph(figure=figSpid)
                ],style={'borderRadius': '15px', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc'}),
            ],width=5)


        ]),
     
],
fluid=True
)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Callback to update the total counts based on the selected technical skill 
@callback(
    Output('tech-total-counts', 'children'),
    [Input('tech-dropdown', 'value')]
)
def update_tech_total_counts(selected_skill):
    total_counts = TechT[TechT['Technical skills'] == selected_skill]['Total'].values[0]
    return f"Total Counts: {total_counts}"
#------------------------------------------------------------------------------------------------------------------------------------------
# Callback to update card text based on dropdown selection for field of education
@callback(
    Output('card-output', 'children'),
    [Input('field-dropdown', 'value')]
)
def update_card(selected_field):
    total_count = EdField['Total'][EdField['Field'].index(selected_field)]
    return f"Total Counts:{total_count:,}"
#------------------------------------------------------------------------------------------------------------------------------------------
# Define callback to update the chart(sunburst) for youth population based on dropdown selection
@callback(
    Output('sunburst-chart', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_sunburst_chart(selected_category):
    # Update the chart based on the selected category
    if selected_category == 'Gender':
        fig = px.sunburst(data_frame=dfSun, path=['Status', 'Age Group', 'Gender'], values='Gpop')
    elif selected_category == 'Residence':
        fig = px.sunburst(data_frame=dfSun, path=['Status', 'Age Group', 'Residence'], values='Rpop')
    elif selected_category == 'Agriculture':
        fig = px.sunburst(data_frame=dfSun, path=['Status', 'Age Group', 'Agriculture'], values='Apop')
    else:
        # Default to Gender if the selected category is not recognized
        fig = px.sunburst(data_frame=dfSun, path=['Status', 'Age Group', 'Gender'], values='Gpop')

    return fig
#------------------------------------------------------------------------------------------------------------------------------------------------