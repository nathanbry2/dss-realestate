# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
v75_2014_2021_transactions_partial_pluscode = dataiku.Dataset("75_2014_2021_transactions_partial_pluscode")
v75_2014_2021_transactions_partial_pluscode_df = v75_2014_2021_transactions_partial_pluscode.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_df = v75_2014_2021_transactions_partial_pluscode_df # For this sample code, simply copy input to output


# Write recipe outputs
test = dataiku.Dataset("test")
test.write_with_schema(test_df)