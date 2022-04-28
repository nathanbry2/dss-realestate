# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from math import sin, cos, sqrt, atan2, radians
from geoloc_functions import distance_to_centre

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
v75_2014_2021_transactions_partial_pluscode = dataiku.Dataset("75_2014_2021_transactions_partial_pluscode")
v75_2014_2021_transactions_partial_pluscode_df = v75_2014_2021_transactions_partial_pluscode.get_dataframe()
iris_75 = dataiku.Dataset("iris_75")
iris_75_df = iris_75.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# R = approximate radius of earth in km,
# centre cordinates correspond to Place Dauphine coordinates (which is considered as Paris surface centre)

def distance_to_centre(lat, long, R = 6373.0, lat_centre = 48.8565, long_centre = 2.3424):
   
    dlon = np.radians(long) - np.radians(long_centre)
    dlat = np.radians(lat) - np.radians(lat_centre)

    a = np.sin(dlat / 2)**2 + np.cos(np.radians(lat)) * np.cos(np.radians(lat_centre)) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distance = R * c
   
    return distance


raw_data['distance_to_centre']= distance_to_centre(raw_data['latitude'],raw_data['longitude'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

transactions_enriched_df = ... # Compute a Pandas dataframe to write into transactions_enriched


# Write recipe outputs
transactions_enriched = dataiku.Dataset("transactions_enriched")
transactions_enriched.write_with_schema(transactions_enriched_df)