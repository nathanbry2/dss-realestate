# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from geoloc_functions import distance_to_centre, direction_from_centre
from openlocationcode import openlocationcode as olc
from pluscode_functions import convert_dic, convert_pluscode

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
v75_2014_2021_transactions_partial_pluscode = dataiku.Dataset("75_2014_2021_transactions_partial_pluscode")
v75_2014_2021_transactions_partial_pluscode_df = v75_2014_2021_transactions_partial_pluscode.get_dataframe()
iris_75 = dataiku.Dataset("iris_75")
iris_75_df = iris_75.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
v75_2014_2021_transactions_partial_pluscode_df['distance_to_centre']= distance_to_centre(v75_2014_2021_transactions_partial_pluscode_df['latitude'],v75_2014_2021_transactions_partial_pluscode_df['longitude'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
v75_2014_2021_transactions_partial_pluscode_df['direction_from_centre'] = np.vectorize(direction_from_centre)(v75_2014_2021_transactions_partial_pluscode_df['longitude'],v75_2014_2021_transactions_partial_pluscode_df['latitude'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
v75_2014_2021_transactions_partial_pluscode_df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
data_encoded = v75_2014_2021_transactions_partial_pluscode_df[v75_2014_2021_transactions_partial_pluscode_df['pluscode_16_first'].isnull() == False]
data_to_encode = v75_2014_2021_transactions_partial_pluscode_df[v75_2014_2021_transactions_partial_pluscode_df['pluscode_16_first'].isnull() == True]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
data_to_encode['pluscode_16_first'] = np.vectorize(olc.encode)(data_to_encode['latitude'],data_to_encode['longitude'],17)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
full_data = pd.concat([data_encoded,data_to_encode])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
full_data['pluscode_10'] = [code[:11] for code in full_data['pluscode_16_first'].to_list()]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
full_data['v_coordinate'],full_data['h_coordinate'],full_data['reduced_v_coordinate'],full_data['reduced_h_coordinate'],full_data['reduced_coordinates_couple'] = convert_pluscode(full_data['pluscode_10'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
full_data

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

transactions_enriched_df = ... # Compute a Pandas dataframe to write into transactions_enriched


# Write recipe outputs
transactions_enriched = dataiku.Dataset("transactions_enriched")
transactions_enriched.write_with_schema(transactions_enriched_df)