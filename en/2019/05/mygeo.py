from scipy import sin, cos, tan, arctan, arctan2, arccos, pi

def spherical_distance(lat1, long1, lat2, long2):
    phi1 = 0.5*pi - lat1
    phi2 = 0.5*pi - lat2
    r = 0.5*(6378137 + 6356752) # mean radius in meters
    t = sin(phi1)*sin(phi2)*cos(long1-long2) + cos(phi1)*cos(phi2)
    return r * arccos(t) / 1000.

