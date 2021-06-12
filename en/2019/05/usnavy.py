import requests, re, bs4

#https://www.vesselfinder.com/vessels?type=7&flag=US
headers = { 'User-Agent': 'UCWEB/2.0 (compatible; Googlebot/2.1; +google.com/bot.html)'}
def all_urls():
    #for i in range(18):
    urls = []
    for i in range(2):
        url = 'https://www.vesselfinder.com/vessels?page=%d&type=7&flag=US' % i
        resp = requests.get(url, headers=headers)  
        soup = bs4.BeautifulSoup(resp.text,"lxml");
        tds = soup.find_all("td", {"class": "v1"})
        for x in tds:
            urls.append(x.a.attrs['href'])
    return urls

#url = 'https://www.vesselfinder.com/vessels/WARSHIP-69-IMO-0-MMSI-368962000'
url = 'https://www.vesselfinder.com/vessels/USNS-GORDON-IMO-7234430-MMSI-367834000'
resp = requests.get(url, headers=headers)  
#print (resp.text)
res = re.findall(r'Course / Speed</td><td class="v3">(.*?)&deg; / (.*?) kn</td>',resp.text)
course,speed = res[0]
print (course,speed)
res = re.findall(r'Position received.*?"red">(.*?) ago',resp.text,re.DOTALL)
if len(res)>0:
    ago = res[0]
    if 'mins' in ago: ago=0
    ago = ago.replace('days','')
else:
    ago = ''
print (ago)
res = re.findall(r'The current position of <strong>(.*?)</strong>',resp.text)
name = res[0]
print (name)
res = re.findall(r'at .*?coordinates (.*?) \/ (.*?)\) reported',resp.text)
lat,lon = res[0]
print (lat,lon)
flat = float(lat[:-2])
flon = float(lon[:-2])
if "S" in lat: flat = flat*-1
if "W" in lon: flon = flon*-1
print (flat,flon)

