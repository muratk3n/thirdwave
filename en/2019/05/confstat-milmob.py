from scipy import sin, cos, tan, arctan, arctan2, arccos, pi
import pandas as pd, datetime, numpy as np
from zipfile import ZipFile
from io import BytesIO
import urllib.request as urllib2
import folium

#base_conflict_url = "http://data.gdeltproject.org/events"
base_conflict_url = "http://localhost:5000/static"

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
dfs = []

clat,clon=33.01136975577918, 40.98527636859822

m = folium.Map(location=[clat, clon], zoom_start=3, tiles="Stamen Terrain")

for i in range(3):
    d = now - datetime.timedelta(days=i+1)
    sd = "%d%02d%02d" % (d.year, d.month, d.day)
    url = base_conflict_url + "/%s.export.CSV.zip" % sd
    r = urllib2.urlopen(url).read()
    file = ZipFile(BytesIO(r))
    csv = file.open("%s.export.CSV" % sd)
    df = pd.read_csv(csv,sep='\t',header=None)    
    urls = df[57]        
    df2 = df[range(len(conf_cols))]
    df2 = pd.concat((df2,urls),axis=1)    
    df2.columns = conf_cols + ['url']
    df3 = df2[(df2.EventCode==154) & (df2['Actor1Type1Code']=='MIL')]
    dft = df3[['EventCode','Actor1CountryCode','Actor1Name','Actor2Name','Actor2Geo_Lat','Actor2Geo_Long','url']].copy()
    dfs.append(dft)

df4 = pd.concat(dfs,axis=0)

for index, row in df4.iterrows():
    if str(row['Actor2Geo_Lat'])=='nan': continue
    if str(row['Actor1CountryCode'])=='nan': continue
    folium.Marker(
        [row['Actor2Geo_Lat'], row['Actor2Geo_Long']], popup="<a href='%s' target='_blank' rel='noopener noreferrer'>Link</a>" % (row['url']), tooltip=row['Actor1CountryCode']
    ).add_to(m)

m.save('conflict-milmob.html')

