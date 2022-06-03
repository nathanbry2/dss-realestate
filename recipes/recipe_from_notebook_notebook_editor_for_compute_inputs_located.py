# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from geoloc_functions import find_location,distance_to_centre, direction_from_centre
from openlocationcode import openlocationcode as olc
from pluscode_functions import convert_pluscode
from iris_functions import create_iris_polygon_dict, find_iris

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
new_inputs = dataiku.Dataset("new_inputs")
new_inputs_df = new_inputs.get_dataframe()
iris_75 = dataiku.Dataset("iris_75")
iris_75_df = iris_75.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_inputs_df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_inputs_df['latitude'] = find_location(new_inputs_df['adresse'])[0]
new_inputs_df['longitude'] = find_location(new_inputs_df['adresse'])[1]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_inputs_df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_inputs_df['distance_to_centre']= distance_to_centre(new_inputs_df['latitude'],new_inputs_df['longitude'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_inputs_df['direction_from_centre'] = np.vectorize(direction_from_centre)(new_inputs_df['longitude'],new_inputs_df['latitude'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_inputs_df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_inputs_df['pluscode_16_first'] = np.vectorize(olc.encode)(new_inputs_df['latitude'],new_inputs_df['longitude'],17)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_inputs_df['pluscode_10'] = [code[:11] for code in new_inputs_df['pluscode_16_first'].to_list()]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_inputs_df['v_coordinate'],new_inputs_df['h_coordinate'],new_inputs_df['reduced_v_coordinate'],new_inputs_df['reduced_h_coordinate'],new_inputs_df['reduced_coordinates_couple'] = convert_pluscode(new_inputs_df['pluscode_10'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
iris_coords_codes = create_iris_polygon_dict(iris_75_df['CODE_IRIS'],iris_75_df['Geo Shape'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_inputs_df['iris_code'] = find_iris(new_inputs_df['latitude'],new_inputs_df['longitude'],iris_coords_codes)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
def correct_date(date_column):
    
    dates_list = date_column.to_list()
    new_dates_list = []
    
    for date in dates_list:
        if date > 2021:
            new_date = 2021
        elif date < 2014:
            new_date = 2014
        else:
            new_date = date
            
        new_dates_list.append(new_date)
    
    return new_dates_list

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_inputs_df['date_mutation_year'] = correct_date(new_inputs_df['date_mutation_year'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

inputs_located_df = new_inputs_df # For this sample code, simply copy input to output


# Write recipe outputs
inputs_located = dataiku.Dataset("inputs_located")
inputs_located.write_with_schema(inputs_located_df)