import dataiku
import dataikuapi
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import Dash, dash_table, html, dcc
import base64
import os

client = dataikuapi.APINodeClient("http://localhost:12000/", "full_real_estate")

app.config.external_stylesheets=[dbc.themes.FLATLY]

address = ''
postal_code = 0
surface = 0
nb_main_rooms = 0
year = 0

images_folder = dataiku.Folder("OMmeZS75")
estimate_logo = os.path.join(images_folder.get_path(), "estimate.png")
estimate_logo_encoded = base64.b64encode(open(estimate_logo, 'rb').read()) 


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
    "margin-left":"50px"
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
            style={
                'backgroundColor': main_style['background'],
                'font-family': main_style['font-family']
            },
            children=[
                html.Div(
                    html.H2(
                        children='Dataiku Real Estate Estimator 🏡',
                        style={
                            #'backgroundColor': title_style['background'],
                            'color': title_style['text'],
                            'textAlign': 'center',
                            'font-weight':'bold'
                        }
                    )
                ),html.Br(),
                
                html.Div(
                    html.H4(
                        children='Welcome to the Dataiku Real Estate Estimator! Follow the instructions to have an estimation of how much your property is worth 💰',
                        style={
                            #'backgroundColor': desc_style['background'],
                            'color': desc_style['text'],
                            'textAlign': 'center',
                            'margin-left':'20%',
                            'margin-right':'20%',
                        }
                    )
                )
            ]
        ),html.Br(),html.Br(),
        
        dbc.Row(
            
            [
                dbc.Col(
                    [
                        dbc.Input(
                            id="input1",
                            type='text',
                            value='',
                            placeholder="Address, e.g. 17 rue Saulnier",
                            size='md',
                            ),html.Br(),
                        
                        dbc.Input(
                            id="input2",
                            type='number',
                            value='',
                            placeholder="Postal Code, e.g. 75009",
                            size='md',
                            min=75001,
                            max=75020,
                            ),html.Br(),
                        
                        dbc.Input(
                            id="input3",
                            type='number',
                            value='',
                            placeholder="Surface (in m²), e.g. 80",
                            size='md',
                            min=1,
                            ),html.Br(),
                        
                        dbc.Input(
                            id="input4",
                            type='number',
                            value='',
                            placeholder="Number of main rooms, e.g. 4",
                            size='md',
                            min=1
                            ),html.Br(),
                        
                        dbc.Input(
                            id="input5",
                            type='number',
                            value='',
                            placeholder="Year, e.g. 2021",
                            size='md',
                            min=2014,
                            max=2021,
                            )
                    ],
                    
                    style = {
                        'text-align':'center',
                        "margin-left":"5%",
                        #"margin-right":"20%",
                    },
                
                ),
                
                
                dbc.Col(
                    children = [
                        html.H4(
                            children='Click logo to get an estimation 🔽',
                        ),html.Br(),html.Br(),
                        dbc.Button(
                            html.Img(
                                src='data:image/png;base64,{}'.format(estimate_logo_encoded.decode()),         
                                style={
                                    'width':'100%',
                                    'height':'1000%',
                                }
                            ), 
                            id="submit",
                            n_clicks=0,
                            color='secondary',
                            outline=True,
                            style = {
                                'width':'100%',
                                'height':'100%',
                                'text-align':'center',
                                #"margin-left":"40%",
                                #"margin-right":"40%",
                            }
                        ),html.Br(),html.Br(),html.Br(),
                        
                    ],
                    style = {
                        'text-align':'center'
                    },
                
                ),
                
            ]
        
        
        ),html.Br(),html.Br(),
        
        html.Div(
            [
                html.H4(
                    id='output',
                    style = {
                        'font-weight':'bold',
                        'text-align':'center',                        
                    }
                ),
            ]
        )
        
        
        
        
    ]


)



@app.callback(
    Output('output', 'children'),
    Input('submit', 'n_clicks'),
    State('input1', 'value'),
    State('input2', 'value'),
    State('input3', 'value'),
    State('input4', 'value'),
    State('input5', 'value'),prevent_initial_call=True)

def output_function(n_clicks,input1,input2,input3,input4,input5):
    
    

    

    result = client.run_function("full",
            address = input1,
            postal_code = int(input2),
            surface = int(input3),
            nb_main_rooms = int(input4),
            year = int(input5))
    
    estim_low = int(round(result.get('response')['estimation_final_lower_bound'],-4))
    estim_high = int(round(result.get('response')['estimation_final_higher_bound'],-4))
    
    return 'Your property is worth between ',str("{:,}".format(estim_low)),'€ and ',str("{:,}".format(estim_high)),'€'

