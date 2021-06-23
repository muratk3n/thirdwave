# US Bases and Navy Locations

<a name='navy'/>

Navy

Locations for a few US aircraft carriers, and destroyers. To see the map
click on the Output at the bottom.

```python
import requests, re
import folium

headers = { 'User-Agent': 'UCWEB/2.0 (compatible; Googlebot/2.1; +google.com/bot.html)'}

ships = [
    [338912000, 'USS Shiloh (CG-67)', 'NA-IMO-0-MMSI-338912000'],
    [338967000, 'USS Port Royal (CG-73)', 'US-GOV-VESSEL-IMO-0-MMSI-338967000'],
    [368776000, 'USS Chancellorsville (CG-62)', 'US-WARSHIP-62-IMO-0-MMSI-368776000'],
    [338834000, 'USS Antietam (CG-54)', 'NA-IMO-0-MMSI-338834000'],
    [368926053, 'USS Rafael Peralta (DDG-115)', 'NA-IMO-0-MMSI-368926053'],
    [366996000, 'USS Mitscher (DDG-57)','MITSCHER-IMO-0-MMSI-366996000'],
    [338807000, 'USS John Paul Jones (DDG-53)', 'US-GOV-VESSEL-IMO-0-MMSI-338807000'],
    [338821000, 'USS WINSTON S. CHURCHILL (DDG-81)','GOVTVESSEL-IMO-0-MMSI-338821000'],
    [367198000, 'USS The Sullivans (DDG-68)','US-WARSHIP-IMO-0-MMSI-367198000'],
    [369921000, 'USS Mustin (DDG-89)','NA-IMO-0-MMSI-369921000'],
    [367199000, 'USS Milius (DDG-69)','US-GOV-SHIP-IMO-0-MMSI-367199000'],
    [369962000, 'USS James E. Williams (DDG-95)','US-GOVT-VESSEL-95-IMO-0-MMSI-369962000'],
    [369970407, 'USS Halsey (DDG-97)','US-GOV-VESSEL-IMO-0-MMSI-369970407'],
    [369952000, 'USS Chung-Hoon (DDG-93)','US-WARSHIP-IMO-0-MMSI-369952000'],
    [338813000, 'USS Iwo Jima (LHD-7)','US-GOVT-VESSEL-IMO-0-MMSI-338813000'],
    [368938000, 'USS Ross (DDG-71)','US-GOV-VESSEL-IMO-0-MMSI-368938000'],
    [366992000, 'USS Barry (DDG-52)','USGOVT-VESSEL--IMO-0-MMSI-366992000'],
    [366986000, 'USS Arleigh Burke (DDG-51)','US-GOV-VESSEL-IMO-8406286-MMSI-366986000'],
    [338822000, 'USS Roosevelt (DDG-80)', 'US-GOVERNMENT-VESSEL-IMO-0-MMSI-338822000'],
    [369970410, 'USS RONALD REAGAN (CVN-76)', 'US-GOV-VSL-IMO-0-MMSI-369970410'],
    [368962000, 'USS Dwight D. Eisenhower (CVN-69)', 'WARSHIP-69-IMO-0-MMSI-368962000'],
    [303981000, 'USS NIMITZ (CVN-68)', 'NAVY-UNIT-78-IMO-0-MMSI-303981000'],
    [366984000, 'USS Theodore Roosevelt (CVN-71)', 'US-GOV-VESSEL-IMO-0-MMSI-366984000'],
    [369970406, 'USS Abraham Lincoln (CVN-72)', 'WARSHIP-72-IMO-0-MMSI-369970406'],
    [338803000, 'USS Gerald R. Ford (CVN-78)', 'US-GOV-VESSEL-IMO-0-MMSI-338803000'],
    [369970739, 'USS AMERICA (LHA-6)', 'US-AIRCRAFTCARRIER-6-IMO-0-MMSI-369970739'],
]

def ship_detail(url):
    resp = requests.get(url, headers=headers)  
    res = re.findall(r'Course / Speed</td><td class="v3">(.*?)&deg; / (.*?) kn</td>',resp.text)
    course,speed = res[0]
    res = re.findall(r'Position received.*?"red">(.*?) ago',resp.text,re.DOTALL)
    name = ''
    flat=0
    flon=0
    if len(res)>0:
        ago = res[0]
        if 'mins' in ago: ago=0
        ago = ago.replace('days','')
    else:
        ago = ''
    res = re.findall(r'The current position of <strong>(.*?)</strong>',resp.text)
    name = res[0]
    res = re.findall(r'.*?coordinates (.*?) \/ (.*?)\) reported',resp.text)
    lat,lon = res[0]
    flat = float(lat[:-2])
    flon = float(lon[:-2])
    if "S" in lat: flat = flat*-1
    if "W" in lon: flon = flon*-1
    
    return course,speed,ago,name,flat,flon

m = folium.Map(location=[30, 30], zoom_start=2, tiles="Stamen Terrain")

base = 'https://www.vesselfinder.com/vessels/'

for s in ships:
    url = s[2]
    if len(url)>0: 
        course,speed,ago,name,flat,flon = ship_detail(base + url)
        ttext = "%s (%s deg, %s kn) %s days ago" % (s[1],course,speed,ago)
        tpop = "<a href='%s' target='_blank' rel='noopener noreferrer'>Link</a>" % (base+url)
        folium.Marker(
            [flat, flon], popup=tpop, tooltip=ttext
        ).add_to(m)
        
m.save('navy-out.html')
```

[Output](navy-out.html)

<a name='bases'/>

Bases

```python
import pandas as pd, folium

clat,clon=33.01136975577918, 40.98527636859822

m = folium.Map(location=[clat, clon], zoom_start=7, tiles="Stamen Terrain")

df = pd.read_csv("https://raw.githubusercontent.com/meflynn/troopdata/master/data-raw/basedata.csv",encoding = "ISO-8859-1", engine='python')
df = df[['countryname','lat','lon']]
df = df.dropna()

for index, row in df.iterrows():
    folium.CircleMarker(location=[row['lat'], row['lon']],
                        radius=6,
			color='red',
                        weight=1).add_to(m)


m.save('usbases-out.html')
```
