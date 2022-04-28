# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from geoloc_functions import distance_to_centre, direction_from_centre

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
# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

transactions_enriched_df = ... # Compute a Pandas dataframe to write into transactions_enriched


# Write recipe outputs
transactions_enriched = dataiku.Dataset("transactions_enriched")
transactions_enriched.write_with_schema(transactions_enriched_df)