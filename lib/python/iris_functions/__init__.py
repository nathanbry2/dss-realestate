import json
from shapely.geometry import Polygon, Point


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