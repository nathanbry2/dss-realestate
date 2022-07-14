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

app.layout = html.Div()