import json
from shapely.geometry import Polygon, Point


'''
    This functions creates a dictionary with iris codes as keys and polygon shapes as values.
    It takes as inputs the iris code and polygon columns of a dataframe, and returns a dictionary.
'''

def create_iris_polygon_dict(iris_code_column,polygon_column):
    
    start = '['
    end = ']'

    polygon_list = []


    for polygon in polygon_column.to_list():

        coords_raw = polygon[polygon.find(start)+len(start):polygon.rfind(end)].replace(']]], [[[','], [').replace(']], [[','], [')

        coords_list = json.loads(coords_raw)

        if len(coords_list)==1:
            coords_list=coords_list[0]  

        poly = Polygon([tuple(i) for i in coords_list])

        polygon_list.append(poly)
        
    iris_coords_codes = dict(zip(iris_code_column.to_list(),polygon_list))
    
    return iris_coords_codes 

'''
    This functions creates GeoPoints from latitude and longitude coordinates, and finds the iris corresponding to these points.
    It takes as inputs the latitude and longitude columns of a dataframe, the dictionary and returns a dictionary.
'''


def find_iris(latitude_column, longitude_column, iris_coords_codes_dict):
    lat_list = latitude_column.to_list()
    long_list = longitude_column.to_list()

    points_list = []

    for i in range(len(lat_list)):
        coords_point = Point(long_list[i],lat_list[i])

        points_list.append(coords_point)
        
        
    points_iris_code_list = []

    for point in points_list:

        is_within_polygon = False

        for iris,coords in iris_coords_codes_dict.items():

            test = point.within(coords)

            if test == True:

                points_iris_code_list.append(iris)
                is_within_polygon = True

                break

        if is_within_polygon==False:

            points_iris_code_list.append('None')
            
    return points_iris_code_list