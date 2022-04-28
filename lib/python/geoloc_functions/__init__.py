import numpy as np
from math import sin, cos, sqrt, atan2, radians

# R = approximate radius of earth in km,
# centre cordinates correspond to Place Dauphine coordinates (which is considered as Paris surface centre)

def distance_to_centre(lat, long, R = 6373.0, lat_centre = 48.8565, long_centre = 2.3424):
   
    dlon = np.radians(long) - np.radians(long_centre)
    dlat = np.radians(lat) - np.radians(lat_centre)

    a = np.sin(dlat / 2)**2 + np.cos(np.radians(lat)) * np.cos(np.radians(lat_centre)) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distance = R * c
   
    return distance