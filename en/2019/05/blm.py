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


base_conflict_url = "http://data.gdeltproject.org/events"

conf_cols = ['GlobalEventID', 'Day', 'MonthYear', 'Year', 'FractionDate',\
       'Actor1Code', 'Actor1Name', 'Actor1CountryCode', 'Actor1KnownGroupCode',\
       'Actor1EthnicCode', 'Actor1Religion1Code', 'Actor1Religion2Code',\
       'Actor1Type1Code', 'Actor1Type2Code', 'Actor1Type3Code', \
       'Actor2Code', 'Actor2Name', 'Actor2CountryCode', 'Actor2KnownGroupCode',
       'Actor2EthnicCode', 'Actor2Religion1Code', 'Actor2Religion2Code',
       'Actor2Type1Code', 'Actor2Type2Code', 'Actor2Type3Code', \
       'IsRootEvent','EventCode', 'EventBaseCode','EventRootCode',\
       'QuadClass', 'GoldsteinScale','NumMentions','NumSources', \
       'NumArticles', 'AvgTone','Actor1Geo_Type', 'Actor1Geo_FullName',\
       'Actor1Geo_CountryCode', 'Actor1Geo_ADM1Code','Actor1Geo_Lat', \
       'Actor1Geo_Long', 'Actor1Geo_FeatureID','Actor2Geo_Type', \
       'Actor2Geo_FullName','Actor2Geo_CountryCode', 'Actor2Geo_ADM1Code',\
       'Actor2Geo_Lat', 'Actor2Geo_Long']

now = datetime.datetime.now()
#now = datetime.date(2021,6,18)
dfs = []

clat,clon=40.74832401970278, -98.51347361480249
how_far = 3200

m = folium.Map(location=[clat, clon], zoom_start=3, tiles="Stamen Terrain")

def spherical_distance(lat1, long1, lat2, long2):
    phi1 = 0.5*pi - lat1
    phi2 = 0.5*pi - lat2
    r = 0.5*(6378137 + 6356752) # mean radius in meters
    t = sin(phi1)*sin(phi2)*cos(long1-long2) + cos(phi1)*cos(phi2)
    return r * arccos(t) / 1000.

def dist(x):
    return spherical_distance(np.deg2rad(clat),np.deg2rad(clon),np.deg2rad(x['Actor2Geo_Lat']),np.deg2rad(x['Actor2Geo_Long']))

for i in range(30):
    d = now - datetime.timedelta(days=i+1)
    print (d)
    sd = "%d%02d%02d" % (d.year, d.month, d.day)
    url = base_conflict_url + "/%s.export.CSV.zip" % sd
    print  (url)
    r = urllib2.urlopen(url).read()
    file = ZipFile(BytesIO(r))
    csv = file.open("%s.export.CSV" % sd)
    df = pd.read_csv(csv,sep='\t',header=None)    
    urls = df[57]        
    df2 = df[range(len(conf_cols))]
    df2 = pd.concat((df2,urls),axis=1)    
    df2.columns = conf_cols + ['url']
    df3 = df2[(df2.EventCode==193)]
    df3.drop_duplicates('url',inplace=True)
    df3.loc[:,'dist'] = df3.apply(dist, axis=1)
    df3 = df3[df3.dist < how_far]    
    for idx, row in df3.iterrows():
        url = row['url']
        if 'black' not in url: continue
        print (url)
        try:
            resp = requests.get(url, headers=headers, timeout=2)
            s = text_from_html(resp.text)
            filt = 'black man' in s.lower() and \
                   ('police' in s.lower() or 'deput' in s.lower()) and \
                   ('shoot' in s.lower() or 'fatally' in s.lower() or 'killed' in s.lower() or 'shot' in s.lower())            
            if filt:
                #print (s)
                folium.Marker(
                    [row['Actor2Geo_Lat'], row['Actor2Geo_Long']], popup="<a href='%s' target='_blank' rel='noopener noreferrer'>Link</a>" % url
                ).add_to(m)
                
        except:
            continue
        
m.save('blm-out.html')
