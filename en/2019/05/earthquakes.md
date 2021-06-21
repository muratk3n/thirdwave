
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

[Output](equake-out.html)


