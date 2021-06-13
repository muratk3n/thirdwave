# US Navy Location

Locations for a few US aircraft carriers, and destroyers. To see the map
click on the Output at the bottom.

```python
import requests, re, bs4
import folium

headers = { 'User-Agent': 'UCWEB/2.0 (compatible; Googlebot/2.1; +google.com/bot.html)'}

ships = [
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
    if len(res)>0:
        ago = res[0]
        if 'mins' in ago: ago=0
        ago = ago.replace('days','')
    else:
        ago = ''
    res = re.findall(r'The current position of <strong>(.*?)</strong>',resp.text)
    name = res[0]
    res = re.findall(r'at .*?coordinates (.*?) \/ (.*?)\) reported',resp.text)
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
    folium.Marker(
        [flat, flon], popup="<a href='%s' target='_blank' rel='noopener noreferrer'>Link</a>" % url, tooltip=s[1] + ' ' + ago + ' days ago'
    ).add_to(m)
    
m.save('navy-out.html')
```

[Output](navy-out.html)


