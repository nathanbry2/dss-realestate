import numpy as np
from math import sin, cos, sqrt, atan2, radians, pi
from geopy.geocoders import Nominatim

''' R = approximate radius of earth in km,
    centre cordinates correspond to Place Dauphine coordinates (which is considered as Paris surface centre).
    
    This functions computes the distance (in km) between a location and Paris centre. 
    It takes as inputs the latitude and longitude columns of a pandas dataframe, and returns a distance list.
'''

def distance_to_centre(lat, long, R = 6373.0, lat_centre = 48.8565, long_centre = 2.3424):
   
    dlon = np.radians(long) - np.radians(long_centre)
    dlat = np.radians(lat) - np.radians(lat_centre)

    a = np.sin(dlat / 2)**2 + np.cos(np.radians(lat)) * np.cos(np.radians(lat_centre)) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distance = R * c
   
    return distance

'''
    This functions computes the direction between a location and Paris centre (Place Dauphine). 
    The direction is the one FROM Paris centre TO the destination location.
    It takes as inputs the latitude and longitude columns of a pandas dataframe, and returns a direction list.
'''

def direction_from_centre(destination_long, destination_lat, origin_lat = 48.853, origin_long = 2.35):
    deltaX = destination_long - origin_long
    deltaY = destination_lat - origin_lat
    degrees_temp = atan2(deltaX, deltaY)/pi*180
    if degrees_temp < 0:
        degrees_final = 360 + degrees_temp
    else:
        degrees_final = degrees_temp

    compass_brackets = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    compass_lookup = round(degrees_final / 45)

    return compass_brackets[compass_lookup]#, degrees_final


'''
    This functions finds the latitude and longitude of a location (address).
    It takes as inputs the address column of a pandas dataframe, and returns the latitude and longitude lists.
'''

def find_location(address_column):
    
    latitude_list = []
    longitude_list = []
    address_list = address_column.to_list()
    locator = Nominatim(user_agent="myGeocoder")
    
    for address in address_list:
        location = locator.geocode(address)
        latitude_list.append(location.latitude)
        longitude_list.append(location.longitude)
    
    return latitude_list,longitude_list