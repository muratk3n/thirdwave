# Conflict Statistics

### UCDP/PRIO Armed Conflict Dataset

[Data](https://ucdp.uu.se/downloads/)

Deaths, Incidences, Globally

```python
import pandas as pd

def overall_deaths(mon):
   url = 'https://ucdp.uu.se/downloads/candidateged/GEDEvent_v21_0_%d.csv' % mon
   df = pd.read_csv(url)
   g = df[['country','deaths_b']].\
       groupby(['country']).\
       agg({'country':'count', 'deaths_b': 'sum'})
   g.columns = ['incidents','deaths']
   return g.sort_values('deaths',ascending=False)

print (overall_deaths(mon=4))
```

```text
                          incidents  deaths
country                                    
Afghanistan                     304    1350
Nigeria                         122     409
Somalia                          26     101
Syria                            86      95
Yemen (North Yemen)              61      89
DR Congo (Zaire)                 86      50
Philippines                      18      42
Iraq                             19      39
Cameroon                         30      37
Mali                             26      36
Pakistan                         14      21
India                            26      19
Burkina Faso                     16      14
Mozambique                       11      13
Colombia                          3      10
Ukraine                          15       9
Mexico                          296       9
Ethiopia                         46       4
South Sudan                      10       4
Central African Republic          7       3
Niger                            11       3
Ivory Coast                       2       3
Russia (Soviet Union)             2       2
Libya                             2       2
Egypt                             8       2
Tunisia                           2       2
Burundi                           7       2
Sudan                             8       1
Indonesia                         2       1
Thailand                          4       1
Iran                              3       1
Spain                             1       0
Switzerland                       1       0
South Africa                      3       0
Malaysia                          1       0
Papua New Guinea                  1       0
Myanmar (Burma)                  83       0
Austria                           1       0
Malawi                            1       0
Kenya                             2       0
Germany                           1       0
Chad                              4       0
Canada                            1       0
Bangladesh                        1       0
Azerbaijan                        1       0
Zimbabwe (Rhodesia)               1       0
```

Details for Specific Country

```python
def country_attacked(mon, country):
   url = 'https://ucdp.uu.se/downloads/candidateged/GEDEvent_v21_0_%d.csv' % mon
   df = pd.read_csv(url)
   df1 = df[df.country == country]
   g = df1[['country','deaths_b','side_b']].\
       groupby(['side_b','country']).\
       agg({'side_b':'count', 'deaths_b': 'sum'})
   g.columns = ['incidents','deaths']
   return g.sort_values('deaths',ascending=False)

print (country_attacked(3, 'Syria'))
```

```text
                           incidents  deaths
side_b            country                   
IS                Syria           19      61
SDF               Syria           28      25
Syrian insurgents Syria           20       6
HTS               Syria            2       3
Civilians         Syria           17       0
```

<a name='gdelt'/>

### GDELT

GDELT uses natural language processing ("AI") to extract Actor -
Action - Actor triplets. The result is not curated, there can be
mistakes, but as an overall outlook, it can be useful.

[Codes](http://data.gdeltproject.org/documentation/CAMEO.Manual.1.1b3.pdf)

[Data](http://data.gdeltproject.org/events)

```python
import pandas as pd, datetime
from zipfile import ZipFile
from io import BytesIO
import urllib.request as urllib2
import folium

base_url = "http://data.gdeltproject.org/events"

cols = ['GlobalEventID', 'Day', 'MonthYear', 'Year', 'FractionDate',\
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
m = folium.Map(location=[34.933582413578954, 42.04398758620605], zoom_start=7, tiles="Stamen Terrain")

for i in range(7):
    d = now - datetime.timedelta(days=i+1)
    sd = "%d%02d%02d" % (d.year, d.month, d.day)
    r = urllib2.urlopen(base_url + "/%s.export.CSV.zip" % sd).read()
    file = ZipFile(BytesIO(r))
    csv = file.open("%s.export.CSV" % sd)
    df = pd.read_csv(csv,sep='\t',header=None)
    urls = df[57]        
    df2 = df[range(len(cols))]
    df2 = pd.concat((df2,urls),axis=1)
    df2.columns = cols + ['url']
    flt1 = ((df2.Actor2Name == 'IRAQ')|(df2.Actor2Name == 'SYRIA'))
    flt2 = ((df2.EventCode==190)|(df2.EventCode==195)|(df2.EventCode==194))
    flt = flt1 & flt2
    df3 = df2[flt]
    dft = df3[['EventCode','Actor1CountryCode','Actor1Name','Actor2Name','Actor2Geo_Lat','Actor2Geo_Long','url']].copy()
    dfs.append(dft)

df4 = pd.concat(dfs,axis=0)

for index, row in df4.iterrows():
    if str(row['Actor2Geo_Lat'])=='nan': continue
    if str(row['Actor1CountryCode'])=='nan': continue
    folium.Marker(
        [row['Actor2Geo_Lat'], row['Actor2Geo_Long']], popup="<a href='%s'>Link</a>" % (row['url']), tooltip=row['Actor1CountryCode']
    ).add_to(m)

m.save('conflict-out.html')
```

The output of the code is below

[Output](conflict-out.html)

