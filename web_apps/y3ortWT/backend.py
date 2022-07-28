import dataiku
import dataikuapi
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import Dash, dash_table, html, dcc
import base64
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from utils_functions import convert_df_to_geojson, blank_figure



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

mydataset = dataiku.Dataset("transactions_by_iris_code_year_windows_prepared")
df = mydataset.get_dataframe()




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
                            value='17 rue Saulnier',
                            placeholder="Address, e.g. 17 rue Saulnier",
                            size='md',
                            ),html.Br(),
                        
                        dbc.Input(
                            id="input2",
                            type='number',
                            value='75009',
                            placeholder="Postal Code, e.g. 75009",
                            size='md',
                            min=75001,
                            max=75020,
                            ),html.Br(),
                        
                        dbc.Input(
                            id="input3",
                            type='number',
                            value='80',
                            placeholder="Surface (in m²), e.g. 80",
                            size='md',
                            min=1,
                            ),html.Br(),
                        
                        dbc.Input(
                            id="input4",
                            type='number',
                            value='4',
                            placeholder="Number of main rooms, e.g. 4",
                            size='md',
                            min=1
                            ),html.Br(),
                        
                        dbc.Input(
                            id="input5",
                            type='number',
                            value='2021',
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
                                    'width':'40%',
                                    'height':'40%',
                                }
                            ), 
                            id="submit",
                            n_clicks=0,
                            color='secondary',
                            outline=True,
                            style = {
                                'width':'40%',
                                'height':'40%',
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
        
        
        ),html.Br(),html.Br(),html.Br(),html.Br(),
        
        
        
        
        dbc.Row(
            
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dcc.Markdown(
                                    id='output',
                                    style = {
                                        #'font-weight':'bold',
                                        'text-align':'center',  
                                        'font-size': "25px",
                                    }
                                ),html.Br(),html.Br(),
                                dcc.Markdown(
                                    id='output2',
                                    style = {
                                        #'font-weight':'bold',
                                        'text-align':'center',  
                                        'font-size': "22px",

                                    }
                                ),html.Br(),
                                html.Ul(id='list_output',style={
                                    "display": "grid",
                                    'gap': "15px",
                                    'font-size': "20px",
                                    'justify-content': 'center'}),
                                html.Br(),html.Br(),
                                html.Br(),html.Br(),
                                #html.Div(id='output8',style={'width': 'auto','height':'300px','border':'none'}),html.Br(),html.Br(),
                                
                            ]
                        )
                    ],
                    
                    style = {
                        #'text-align':'center',
                        #"margin-left":"5%",
                        #"margin-right":"20%",
                       
                    },
                
                ),
                
                
                dbc.Col(
                    [
                        html.Div(id='output7')
                        
                    ],
                    style = {
                        'text-align':'center'
                    },
                
                ),
                
            ]
        
        
        ),
        
        
        
        
        
        html.Div(
            [
                
                dcc.Graph(id='output8',figure = blank_figure(),style={'width': '60%','height':'650px','border':'none',})
            ],style={'text-align':'center',
                     "margin-left":"20%",
                     "margin-right":"20%",}
        )
        
        
        
        
    ]


)



@app.callback(
    Output('output', 'children'),
    Output('output2', 'children'),
    Output('list_output','children'),
    Output('output7','children'),
    Output('output8','figure'),
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
    
    text1 = '➡ Your property is worth between **' + str("{:,}".format(estim_low)) + '€** and **' + str("{:,}".format(estim_high)) + '€**'
    
    df_filtered = df[df['iris_code']==result.get('response')['iris_code']].sort_values(by=['date_mutation_year'])
    #iris_code_name = df_filtered.iloc[0]['NOM_IRIS_first']

    text2 = "📍 A few current metrics about your area **" + df_filtered.iloc[0]['NOM_IRIS_first'] + '**:'
    text3 = "🤝 On average, there are **" + str(round(df_filtered['count'].mean())) + "** transactions per year in your area 🤝"
    text4 = "📐 The average surface in your area is **" + str(round(df_filtered['surface_m2_not_null_avg'].mean())) + 'm² 📐**'
    text5 = "💵 The average m² price in your area is currently **" + str(round(df_filtered.iloc[-1]['prix_m2_not_null_avg'])) + "€ 💵**"
    text6 = "📈 It has grown **" +  str(round(df_filtered.iloc[-1]['Growth%_7years'])) + "%** in the last 7 years, or about **" + str(round(df_filtered.iloc[-1]['CAGR%_7years'],1)) + "%** per year 📈"

    text_list = [text3,text4,text5,text6]
    
    ### CREATE PRICE TRANSAC CHART
        
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
            x=df_filtered['date_mutation_year'],
            y=df_filtered['prix_m2_not_null_avg'].round(0),
            name="Average m2 price",
            marker = {'color' : 'black'},
        ),
        secondary_y=True,
    )

    fig.add_trace(
        go.Bar(
            x=df_filtered['date_mutation_year'],
            y=df_filtered['count'],
            name="Transactions count",
            marker = {'color' : '#00B2A9'},
        ),
        secondary_y=False,
    )


    # Add figure title
    fig.update_layout(
        margin={"r":30,"t":50,"l":30,"b":0},
        title_text="<i>Transactions Count</i> and <i>Average m² Price</i> evolution in zone <b>"+df_filtered.iloc[0]['NOM_IRIS_first']+"</b>",
        plot_bgcolor='rgba(0,0,0,0)',
    )

    # Set x-axis title
    fig.update_xaxes(title_text="<b>Year</b>")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Average m² price</b>", secondary_y=True,ticksuffix='€')
    fig.update_yaxes(title_text="<b>Transactions count</b>", secondary_y=False)
    
    
    ### CREATE MAP CHART
    
    df_filtered2 = df[df['date_mutation_year']==2021].sort_values(by=['date_mutation_year'])
    geojson = convert_df_to_geojson(df_filtered2[['NOM_IRIS_first','iris_GeoShape_first']], properties=['NOM_IRIS_first'],geo_col = 'iris_GeoShape_first')
    
    sub_df = df_filtered2[['NOM_IRIS_first','prix_m2_not_null_avg','surface_m2_not_null_avg','count','Growth%_7years']]
    sub_df['prix_m2_not_null_avg'] = sub_df['prix_m2_not_null_avg'].astype('int')
    sub_df['surface_m2_not_null_avg'] = sub_df['surface_m2_not_null_avg'].astype('int')
    sub_df['Growth%_7years'] = sub_df['Growth%_7years'].round(1)
    
    

    fig2 = px.choropleth_mapbox(sub_df, geojson=geojson, locations='NOM_IRIS_first', color='prix_m2_not_null_avg',
                               color_continuous_scale="rdylgn_r",
                               range_color=(6000, 16000),
                               mapbox_style="carto-positron",
                               zoom=11.25, center = {"lat": 48.8565, "lon": 2.3424},
                               opacity=0.5,
                               labels={
                                   'prix_m2_not_null_avg':'Average m² price (€)',
                                   'surface_m2_not_null_avg':'Average surface (m²)',
                                   'NOM_IRIS_first':"Area name",
                                   'count':"Transactions count",
                                   'Growth%_7years':"Growth % in last 7 years",

                               },
                               hover_name='NOM_IRIS_first',
                               hover_data={
                                   'NOM_IRIS_first':False,
                                   'prix_m2_not_null_avg':':,',
                                   'surface_m2_not_null_avg':True,
                                   'count':True,
                                   'Growth%_7years':True,
                               }
                              )


    fig2.add_scattermapbox(lat = [float(df_filtered.iloc[-1].iris_GeoPoint_first.split(',')[0])],
                          lon = [float(df_filtered.iloc[-1].iris_GeoPoint_first.split(',')[1])],
                          mode = 'markers+text',
                          text = [df_filtered.iloc[-1].NOM_IRIS_first],  #a list of strings, one  for each geographical position  (lon, lat)              
                          below='',marker=dict(size=10, color='#221C35',symbol='circle'),               
                          )
    fig2.update_layout(margin={"r":10,"t":50,"l":20,"b":20},
                      title={
                          'text': "<b>Average m² price (€) in Paris areas - 2021</b>",
                      })
    #fig2.show()
    #,style={'width': 'auto','height':'300px','border':'none'}
    
    return text1, text2, [html.Li(dcc.Markdown(i)) for i in text_list], dcc.Graph(figure=fig), fig2
