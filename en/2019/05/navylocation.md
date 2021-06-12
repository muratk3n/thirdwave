# Navy Location



```python
def all_urls():
    urls = []
    for i in range(2):
        url = 'https://www.vesselfinder.com/vessels?page=%d&type=7&flag=US' % i
        resp = requests.get(url, headers=headers)  
        soup = bs4.BeautifulSoup(resp.text,"lxml");
        tds = soup.find_all("td", {"class": "v1"})
        for x in tds:
            urls.append(x.a.attrs['href'])
    return urls
```


```python
import requests, re, bs4
import folium

headers = { 'User-Agent': 'UCWEB/2.0 (compatible; Googlebot/2.1; +google.com/bot.html)'}

ships = [
    [369970410, 'USS RONALD REAGAN (CVN-76)', 'https://www.vesselfinder.com/vessels/US-GOV-VSL-IMO-0-MMSI-369970410'],
    [369970663, 'USS George H.W. Bush (CVN-77)]',''],
    [368913000, 'USS GEORGE WASHINGTON (CVN-73)]',''],
    [368962000, 'USS Dwight D. Eisenhower (CVN-69)', 'https://www.vesselfinder.com/vessels/WARSHIP-69-IMO-0-MMSI-368962000'],
    [303981000, 'USS NIMITZ (CVN-68)', 'https://www.vesselfinder.com/vessels/NAVY-UNIT-78-IMO-0-MMSI-303981000'],
    [369970409, 'USS CARL VINSON (CVN-70)',''],
    [366984000, 'USS Theodore Roosevelt (CVN-71)', 'https://www.vesselfinder.com/vessels/US-GOV-VESSEL-IMO-0-MMSI-366984000'],
    [369970406, 'USS Abraham Lincoln (CVN-72)', 'https://www.vesselfinder.com/vessels/WARSHIP-72-IMO-0-MMSI-369970406'],
    [368912000, 'USS John C. Stennis (CVN-74)',''],
    [338803000, 'USS Gerald R. Ford (CVN-78)', 'https://www.vesselfinder.com/vessels/US-GOV-VESSEL-IMO-0-MMSI-338803000'],
    [369970739, 'USS AMERICA (LHA-6)', 'https://www.vesselfinder.com/vessels/US-AIRCRAFTCARRIER-6-IMO-0-MMSI-369970739']
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

for s in ships:
    url = s[2]
    if len(url)>0: 
        course,speed,ago,name,flat,flon = ship_detail(url)
    folium.Marker(
        [flat, flon], popup="<a href='%s'>Link</a>" % url
    ).add_to(m)
    
m.save('navy-out.html')
```












