
```python
from quakefeeds import QuakeFeed
import requests, time, datetime
import numpy as np, math

def get_eq3(minx,maxx,miny,maxy):
    today = datetime.datetime.now()
    days = 100
    start = today - datetime.timedelta(days=days)

    req = 'https://earthquake.usgs.gov/fdsnws'
    req+='/event/1/query.geojson?starttime=%s&endtime=%s'
    req+='&minlatitude=%d&maxlatitude=%d&minlongitude=%d&maxlongitude=%d'
    req+='&minmagnitude=4.5&orderby=time&limit=2000'
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

lat,lon = 30.1,20.1
print (lat,lon)
D = 1000
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
30.1 20.1
                         mag  ...  ago
0                             ...     
2021-04-03 09:10:14.176  4.8  ...   20
2021-06-04 04:05:26.498  4.6  ...   82

[2 rows x 5 columns]
```





