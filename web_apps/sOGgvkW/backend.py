import plotly.express as px
import dataiku
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output, State

# DEFINE CLUES

clue1 = 'clue1'
clue2 = 'clue2'
clue3 = 'clue3'
clue4 = 'clue4'

# DEFINE STYLES

main_style = {
    'background': '#FFFFFF',
    'font-family': "Arial"
}

title_style = {
    #'background': '#5473FF',
    'text': '#00B2A9'
}

desc_style = {
    'background': '#FFFFFF',
    'text': '5473FF'
}

#logo_path = "/local-static/DKU_LOGO.png"
#encoded_logo = base64.b64encode(open(logo_path, 'rb').read())


# DEFINE APP LAYOUT
app.layout = html.Div(
    ## Step 1: Define App Style
    style={
        'backgroundColor': main_style['background'],
        'font-family': main_style['font-family']
    },
    ## Step 2: Create Title & Description
    children=[
        html.Div(html.H1(
            children='Dataiku Real Estate Estimator',
            style={
                #'backgroundColor': title_style['background'],
                'color': title_style['text'],
                'textAlign': 'center'}
        )),
        html.Div(html.H2(
            children='Welcome! Please fill in the following fields to get an astimation of your property.',
            style={
                'backgroundColor': desc_style['background'],
                'color': desc_style['text'],
                'textAlign': 'center'}
        ),html.Br(),html.Br(),
        
        ## Step 3: Create clues inputs
        dbc.Label("Clue n°1", html_for="input1"),html.Br(),html.Br(),
        dcc.Input(
            id="input1",
            type='text',
            value='',
            placeholder="Please fill in clue n°1",
        ),html.Br(),html.Br(),html.Br(),
        dbc.Label("Clue n°2", html_for="input2"),html.Br(),html.Br(),
        dcc.Input(
            id="input2",
            type='text',
            placeholder="Please fill in clue n°2",
        ),html.Br(),html.Br(),html.Br(),
        dbc.Label("Clue n°3", html_for="input3"),html.Br(),html.Br(),
        dcc.Input(
            id="input3",
            type='text',
            placeholder="Please fill in clue n°3",
        ),html.Br(),html.Br(),html.Br(),
        dbc.Label("Clue n°4", html_for="input3"),html.Br(),html.Br(),
        dcc.Input(
            id="input4",
            type='text',
            placeholder="Please fill in clue n°4",
        ),
        
        ## Step 3: Submit button
        html.Br(),html.Br(),html.Br(),
        html.Div(dbc.Col(dbc.Button(children="Submit answers", id="submit",n_clicks=0))),
        html.Br(),
        html.Div(id='output')
        #html.Img(src='data:image/png;base64,{}'.format(encoded_logo))
    ]
)


'''@app.callback(
    Output(component_id='output', component_property='children'),
    Input(component_id='input1', component_property='value'))
def update_output_div(input_value):
    if input_value==clue1:
        return "Correct"
    else: 
        return "Incorrect"
    #return f'Output: {input_value}'''

@app.callback(
    Output('output', 'children'),
    [Input('submit', 'n_clicks')],
    [State('input1', 'value')]
)

def output_function(n_clicks, number):
    
    if number == '':
        return ""
    elif number == clue1:
        return "Correct"
    else:
        return "Incorrect"


