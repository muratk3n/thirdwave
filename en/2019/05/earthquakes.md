
```python
from quakefeeds import QuakeFeed
import requests, time, datetime
import numpy as np, math

def get_eq3(minx,maxx,miny,maxy):
    today = datetime.datetime.now()
    days = 7
    start = today - datetime.timedelta(days=days)

    req = 'https://earthquake.usgs.gov/fdsnws'
    req+='/event/1/query.geojson?starttime=%s&endtime=%s'
    req+='&minlatitude=%d&maxlatitude=%d&minlongitude=%d&maxlongitude=%d'
    req+='&minmagnitude=3.0&orderby=time&limit=300'
    req = req % (start.isoformat(), today.isoformat(),miny,maxy,minx,maxx)
    #print (req)
    qr = requests.get(req).json()
    res = []
    for i in range(len(qr['features'])):
        lat = qr['features'][i]['geometry']['coordinates'][1]
        lon = qr['features'][i]['geometry']['coordinates'][0]
        rad = qr['features'][i]['geometry']['coordinates'][2]
        d = datetime.datetime.fromtimestamp(qr['features'][i]['properties']['time']/1000.0)
        s = np.float(qr['features'][i]['properties']['mag'])
        diff = (d-start).days
        res.append([d,s,lat,lon,rad,diff])

    import pandas as pd
    #print (res)
    df = pd.DataFrame(res).sort_values(by=0)
    #df.drop_duplicates(inplace=True)
    df = df.set_index(0)
    df.columns = ['mag','lat','lon','rad','ago']
    return df

def to_bearing(lat,lon,brng,d):
    R = 6378.1 #Radius of the Earth
    lat1 = math.radians(lat) #Current lat point converted to radians
    lon1 = math.radians(lon) #Current long point converted to radians    
    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
         math.cos(lat1)*math.sin(d/R)*math.cos(brng))
    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                 math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)
    return lat2,lon2
```

```python
lat,lon = 36.61626063822746, -56.04276502632696
print (lat,lon)
D = 5000
lat1,lon1 = to_bearing(lat,lon,np.deg2rad(45),D)
lat2,lon2 = to_bearing(lat,lon,np.deg2rad(225),D)
minx=np.min((lon1,lon2))
maxx=np.max((lon1,lon2))
miny=np.min((lat1,lat2))
maxy=np.max((lat1,lat2))
df = get_eq3(minx,maxx,miny,maxy)
print (df)
```

```text
36.61626063822746 -56.04276502632696
                          mag  ...  ago
0                              ...     
2021-06-14 23:05:23.784  4.50  ...    0
2021-06-15 04:30:57.420  3.21  ...    0
2021-06-15 08:33:59.680  3.62  ...    0
2021-06-15 09:39:57.460  3.68  ...    0
2021-06-15 10:51:49.150  3.59  ...    0
2021-06-15 12:02:33.440  3.15  ...    0
2021-06-15 13:50:35.150  3.70  ...    0
2021-06-15 13:57:57.150  3.59  ...    0
2021-06-15 23:46:04.150  3.18  ...    1
2021-06-16 01:27:27.763  4.80  ...    1
2021-06-16 01:41:15.190  3.08  ...    1
2021-06-16 04:35:33.080  3.41  ...    1
2021-06-16 15:52:34.510  4.24  ...    1
2021-06-16 16:00:19.490  3.87  ...    1
2021-06-16 17:40:00.260  3.62  ...    1
2021-06-16 20:02:42.730  3.66  ...    2
2021-06-16 23:20:18.310  3.15  ...    2
2021-06-17 04:56:52.220  3.37  ...    2
2021-06-17 05:15:10.850  3.70  ...    2
2021-06-17 05:28:35.040  3.22  ...    2
2021-06-17 07:43:51.080  3.21  ...    2
2021-06-17 12:23:42.710  4.43  ...    2
2021-06-17 22:33:53.920  3.12  ...    3
2021-06-18 05:53:40.990  3.19  ...    3
2021-06-18 05:54:55.240  3.17  ...    3
2021-06-18 09:35:41.460  3.39  ...    3
2021-06-18 11:35:28.110  3.73  ...    3
2021-06-18 15:30:08.970  4.03  ...    3
2021-06-18 16:57:26.248  4.70  ...    3
2021-06-18 17:48:15.450  3.92  ...    4
2021-06-18 17:52:05.400  3.93  ...    4
2021-06-18 20:51:26.746  4.40  ...    4
2021-06-18 22:48:39.544  3.90  ...    4
2021-06-18 23:00:09.900  4.01  ...    4
2021-06-19 03:57:28.340  3.77  ...    4
2021-06-19 05:43:45.920  3.32  ...    4
2021-06-19 06:23:06.965  4.70  ...    4
2021-06-19 15:32:12.130  3.62  ...    4
2021-06-19 22:44:57.300  3.55  ...    5
2021-06-20 00:59:19.090  3.52  ...    5
2021-06-20 10:50:46.540  3.16  ...    5
2021-06-20 13:03:32.880  3.03  ...    5
2021-06-20 13:39:05.610  3.42  ...    5
2021-06-20 14:24:17.100  3.49  ...    5
2021-06-20 19:24:13.850  3.16  ...    6
2021-06-20 21:01:31.190  3.04  ...    6
2021-06-21 12:58:16.950  3.29  ...    6
2021-06-21 13:14:05.510  3.10  ...    6

[48 rows x 5 columns]
```

```python
m = folium.Map(location=[lat, lon], zoom_start=3, tiles="Stamen Terrain")

import folium
for index, row in df.iterrows():
    folium.Marker(
        [row['lat'], row['lon']], tooltip=str(row['mag']) + " " + str(row['ago']) + " days ago"
    ).add_to(m)
    
m.save('equake-out.html')
```




