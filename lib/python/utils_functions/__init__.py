import ast
import plotly.graph_objects as go


'''
    This function correct dates that are not in the [2014-2021] range.
    It takes as input the date column of a dataframe and outputs a list of corrected dates.'''

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


'''
    This function converts a dataframe to the geojson format.
    It takes as input the dataframe to convert, a list of columns that need to be stored in the geojson (properties), the column containing the geo information (geo_col),
    and outputs a list of corrected dates.'''


def convert_df_to_geojson(df, properties, geo_col):
    # create a new python dict to contain our geojson data, using geojson format
    geojson = {'type':'FeatureCollection', 'features':[]}

    # loop through each row in the dataframe and convert each row to geojson format
    for _, row in df.iterrows():
        # create a feature template to fill in
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{}}

        # fill in the coordinates
        feature['geometry'] = ast.literal_eval(row[geo_col])
        
        feature['id'] = row['NOM_IRIS_first']

        # for each column, get the value and add it as a new feature property
        for prop in properties:
            feature['properties'][prop] = row[prop]
        
        # add this feature (aka, converted dataframe row) to the list of features inside our dict
        geojson['features'].append(feature)
    
    return geojson


'''
    This function creates a plotly blank figure.'''

def blank_figure():
    b_fig = go.Figure(go.Scatter(x=[], y = []))
    b_fig.update_layout(template = None)
    b_fig.update_xaxes(showgrid = False, showticklabels = False, zeroline=False)
    b_fig.update_yaxes(showgrid = False, showticklabels = False, zeroline=False)
    
    return b_fig