from scipy import sin, cos, tan, arctan, arctan2, arccos, pi
import numpy as np, numpy.linalg as lin

E = np.array([[0, 0, 1],[0, 1, 0],[-1, 0, 0]])

def spherical_distance(lat1, long1, lat2, long2):
    phi1 = 0.5*pi - lat1
    phi2 = 0.5*pi - lat2
    r = 0.5*(6378137 + 6356752) # mean radius in meters
    t = sin(phi1)*sin(phi2)*cos(long1-long2) + cos(phi1)*cos(phi2)
    return r * arccos(t) / 1000.

def latlon2vec(latitude,longitude):
    res = [np.sin(np.deg2rad(latitude)),
           np.sin(np.deg2rad(longitude)) * np.cos(np.deg2rad(latitude)),
           -np.cos(np.deg2rad(longitude)) * np.cos(np.deg2rad(latitude))]
    return np.dot(E.T,np.array(res))

def vec2latlon(n_E):
    n_E = np.dot(E, n_E)
    longitude=np.arctan2(n_E[1],-n_E[2]);
    equatorial_component = np.sqrt(n_E[1]**2 + n_E[2]**2 );
    latitude=np.arctan2(n_E[0],equatorial_component);
    return np.rad2deg(latitude), np.rad2deg(longitude)

def average(coords):
    res = []
    for lat,lon in coords:
        res.append(latlon2vec(lat,lon))
    res = np.array(res)
    m = np.mean(res,axis=0)
    m = m / lin.norm(m)
    return vec2latlon(m)
