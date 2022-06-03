# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
new_inputs = dataiku.Dataset("new_inputs")
new_inputs_df = new_inputs.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

inputs_located_df = new_inputs_df # For this sample code, simply copy input to output


# Write recipe outputs
inputs_located = dataiku.Dataset("inputs_located")
inputs_located.write_with_schema(inputs_located_df)
