# US Bases and Navy Locations

<a name='navy'/>

Navy

Locations for a few US aircraft carriers, and destroyers. To see the map
click on the Output at the bottom.

[Script](usnavy.py)

[Output](navy-out.html)

<a name='bases'/>

US Bases around the World

Data from [here](https://github.com/meflynn/troopdata), itself based
on David Vine's work.

```python
import pandas as pd, folium

clat,clon=33.01136975577918, 40.98527636859822

m = folium.Map(location=[clat, clon], zoom_start=7, tiles="Stamen Terrain")

df = pd.read_csv("https://raw.githubusercontent.com/meflynn/troopdata/master/data-raw/basedata.csv",encoding = "ISO-8859-1", engine='python')
df = df[['countryname','basename','lat','lon']]
df = df.dropna()

for index, row in df.iterrows():
    folium.Marker([row['lat'], row['lon']],tooltip=row['basename'] + " " + row['countryname']
                  ).add_to(m)


m.save('usbases-out.html')
```

[Output](usbases-out.html)

