from collections import defaultdict
import numpy.linalg as lin, numpy as np
import pandas as pd, re, mygeo
from scipy import sin, cos, tan, arctan, arctan2, arccos, pi
import pandas as pd, datetime, numpy as np
from zipfile import ZipFile
from io import BytesIO
import urllib.request as urllib2
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request, folium, re, requests

headers = { 'User-Agent': 'UCWEB/2.0 (compatible; Googlebot/2.1; +google.com/bot.html)'}

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


url = "https://news.antiwar.com/2021/07/02/report-china-india-move-tens-of-thousands-of-troops-to-disputed-border/"
resp = requests.get(url, headers=headers, timeout=2)
s = text_from_html(resp.text)

s = s[:1000]

countries = pd.read_csv('countries.csv')
countries['latlon'] = countries.apply(lambda x: list(x[['latitude','longitude']]),axis=1)
cdict = countries.set_index('name')['latlon'].to_dict()

tokens = re.split("\s|(?<!\d)[,.](?!\d)",s)
print (tokens)
c_in_tokens = defaultdict(int)
for t in tokens: c_in_tokens[t] += 1

res = {}
for t in c_in_tokens: 
    if t in cdict: res[t] = c_in_tokens[t]
    
total = []
for c in res:
    lat,lon = cdict[c]
    newcoord = mygeo.latlon2vec(lat,lon)
    total.append(list(newcoord * res[c]))

total = np.array(total)
m = np.mean(total,axis=0)
m = m / lin.norm(m)
lat,lon = mygeo.vec2latlon(m)
print (lat,lon)
