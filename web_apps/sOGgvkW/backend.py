import dataiku
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import base64
import os

app.config.external_stylesheets=[dbc.themes.FLATLY]

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

clue_style = {
    "margin-left":"15px"
}

input_style = {
    "margin-left":"65px"
}

check_button_style = {
    "margin-left":"20px"
}

clue_output_style = {
    "margin-left":"30px"
}

submit_button_style = {
    "margin-left":"50px"
}

submit_output_style = {
    "margin-left":"100px",
    "margin-right":"100px"
}


app.layout = html.Div(
    [
        html.Div(
    ## Step 1: Define App Style
    style={
        'backgroundColor': main_style['background'],
        'font-family': main_style['font-family']
    },
    ## Step 2: Create Title & Description
    children=[
        html.Div(html.H2(
            children='Dataiku Real Estate Estimator',
            style={
                #'backgroundColor': title_style['background'],
                'color': title_style['text'],
                'textAlign': 'center',
                'font-weight':'bold'})),
        html.Br(),html.Div(html.H4(
            children='Welcome to the Dataiku Real Estate Estimator! Follow the instructions to have an estimation of how much your property is worth 💰',
            style={
                #'backgroundColor': desc_style['background'],
                'color': desc_style['text'],
                'textAlign': 'center',
                'margin-left':'20%',
                'margin-right':'20%',
                }))
            ]
        ),html.Br(),html.Br(),
        
        dbc.Row([
            dbc.Col(html.Div(
        
        children = [
            html.Div(
        
        children = [      
        html.Div(
            
            children = [
                dbc.Label("1️⃣ What percentage of all customers have been part of a marketing campaign?", 
                          style = {
                              'margin-left':clue_style['margin-left']
                          }),
            ]
        ),
        html.Div(
            
            children=[
            
            dcc.Input(
                id="input1",
                type='text',
                value='',
                placeholder="Please fill in answer 1",
                style = {
                              'margin-left':input_style['margin-left']
                          }),
                
            dbc.Button(children="Check answer n°1", id="check1",n_clicks=0,
                       style = {
                           'margin-left':check_button_style['margin-left'],
                           'background-color':'#00B2A9',
                           'border-color':'#FFFFFF',
                       }),
                
            #html.Br(),
            html.B(id='output1',style = {
                'margin-left':clue_output_style['margin-left']
            }),
            ]
        ),
            
            
        ],
        style={
        'font-family': main_style['font-family']
    }
    
    
    ),html.Br(),
    
    html.Div(
        
        children = [      
        html.Div(
            
            children = [
                dbc.Label("2️⃣ Which customer has the highest lifetime value (highest total amount spent - all time)? Type in their customer_id.", 
                          style = {
                              'margin-left':clue_style['margin-left']
                          }),
            ]
        ),
        html.Div(
            
            children=[
            
            dcc.Input(
                id="input2",
                type='text',
                value='',
                placeholder="Please fill in answer 2",
                style = {
                              'margin-left':input_style['margin-left']
                          }),
                
            dbc.Button(children="Check answer n°2", id="check2",n_clicks=0,color='secondary',
                       style = {
                           'margin-left':check_button_style['margin-left'],
                           'background-color':'#00B2A9',
                           'border-color':'#FFFFFF',
                       }),
                
            #html.Br(),
            html.B(id='output2',style = {
                'margin-left':clue_output_style['margin-left']
            }),
            ]
        ),
        ],
        style={
        'font-family': main_style['font-family']
    }
    
    
    ),html.Br(),
    
    html.Div(
        
        children = [      
        html.Div(
            
            children = [
                dbc.Label("3️⃣ What was the total revenue generated from sales of Limited Collection items in 2011?", 
                          style = {
                              'margin-left':clue_style['margin-left']
                          }),
            ]
        ),
        html.Div(
            
            children=[
            
            dcc.Input(
                id="input3",
                type='text',
                value='',
                placeholder="Please fill in answer 3",
                style = {
                              'margin-left':input_style['margin-left']
                          }),
                
            dbc.Button(children="Check answer n°3", id="check3",n_clicks=0,color='info',style = {
                              'margin-left':check_button_style['margin-left'],
                              'background-color':'#00B2A9',
                              'border-color':'#FFFFFF',
                          }),
                
            #html.Br(),
            html.B(id='output3',style = {
                'margin-left':clue_output_style['margin-left']
            }),
            ]
        ),
            
            
        ],
        style={
        'font-family': main_style['font-family']
    }
    ),html.Br(),
    
    html.Div(
        
        children = [      
        html.Div(
            
            children = [
                dbc.Label("4️⃣ What is the second most purchased product among men between the ages of 30 and 45 in 2011?", 
                          style = {
                              'margin-left':clue_style['margin-left']
                          }),
            ]
        ),
        html.Div(
            
            children=[
            
            dcc.Input(
                id="input4",
                type='text',
                value='',
                placeholder="Please fill in answer 4",
                style = {
                              'margin-left':input_style['margin-left']
                          }),
                
            dbc.Button(children="Check answer n°4", id="check4",n_clicks=0,style = {
                              'margin-left':check_button_style['margin-left'],
                              'background-color':'#00B2A9',
                              'border-color':'#FFFFFF',
                          }),
                
            #html.Br(),
            html.B(id='output4',style = {
                'margin-left':clue_output_style['margin-left']
            }),
            ]
        ),
            
            
        ],
        style={
        'font-family': main_style['font-family']
    }
    ),html.Br(),
    
    html.Div(
        
        children = [      
        html.Div(
            
            children = [
                dbc.Label("5️⃣ What is the country with the 5th highest number of orders in 2010?", 
                          style = {
                              'margin-left':clue_style['margin-left']
                          }),
            ]
        ),
        html.Div(
            
            children=[
            
            dcc.Input(
                id="input5",
                type='text',
                value='',
                placeholder="Please fill in answer 5",
                style = {
                              'margin-left':input_style['margin-left']
                          }),
                
            dbc.Button(children="Check answer n°5", id="check5",n_clicks=0,style = {
                              'margin-left':check_button_style['margin-left'],
                              'background-color':'#00B2A9',
                              'border-color':'#FFFFFF',
                          }),
                
            #html.Br(),
            html.B(id='output5',style = {
                'margin-left':clue_output_style['margin-left']
            }),
            ]
        ),
            
            
        ],
        style={
        'font-family': main_style['font-family']
    }
    ),html.Br(),html.Br(),
                          
        ])
                   ,style={'margin-left':'15px'}
                   ),
                        
            
            dbc.Col(
                html.Div(
        
        children = [
            html.H4(
            children='Click logo to escape 🔽',
            ),html.Br(),html.Br(),
            dbc.Button(children=[
            #html.Img(src='https://cdn-icons-png.flaticon.com/512/747/747315.png',
            html.Img(src='data:image/png;base64,{}'.format(escape_logo_encoded.decode()),         
                     style={
                'width':'50%',
                'height':'50%',})], id="submit",n_clicks=0,color='secondary',outline=True,style = {
                #'margin-left':submit_button_style['margin-left'],
                'width':'40%',
                'height':'50%',
                #'background': '#FFFFFF',
                #'border':'2px',
                
            }),
            html.Br(),html.Br(),html.Br(),
            html.H4(id='output',style = {
                'margin-left':submit_output_style['margin-left'],
                'margin-right':submit_output_style['margin-right'],
                #'marginBottom':'125px',
                #'font_size': '86px',
                'font-weight':'bold',
            }),
                    
        
        ],style={'text-align':'center',
                'margin-top': '17%'}),
        style={
        'font-family': main_style['font-family']
    })            
            
            ])
                       
                      ])
