# Conflict Statistics

Based on UCDP/PRIO Armed Conflict Dataset

[Data](https://ucdp.uu.se/downloads/)

### Deaths, Incidences, Globally

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

print (overall_deaths(mon=2))
```

```text
                          incidents  deaths
country                                    
Afghanistan                     272    1592
Nigeria                          74     364
Yemen (North Yemen)              52     133
Syria                            61      95
Somalia                          29      78
Mali                             21      58
DR Congo (Zaire)                 47      52
Iraq                             16      41
Cameroon                         26      30
Pakistan                         28      26
Philippines                      11      15
Burkina Faso                     16      15
India                            21      12
Mozambique                       13      12
Ukraine                          16       8
Libya                             1       7
Mexico                          167       6
Iran                              4       2
Burundi                           7       2
Indonesia                         3       1
South Sudan                       8       1
Sierra Leone                      1       1
United States of America          3       0
Uganda                            1       0
Tunisia                           1       0
Thailand                          2       0
Central African Republic          7       0
Sudan                             6       0
Chile                             1       0
Colombia                          3       0
Papua New Guinea                  1       0
Ecuador                           3       0
Bangladesh                        4       0
Niger                             9       0
Myanmar (Burma)                  16       0
Egypt                             6       0
Morocco                           4       0
Ethiopia                         28       0
Haiti                             2       0
Azerbaijan                        2       0
Kenya                             1       0
Honduras                          1       0
Brazil                           14       0
```

### Details for Specific Country

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

print (country_attacked(mon=2, 'Syria'))
```

```text
                              incidents  deaths
side_b               country                   
IS                   Syria           19      66
Syrian insurgents    Syria           23      11
Government of Syria  Syria            2       9
SDF                  Syria            9       9
Civilians            Syria            7       0
Government of Israel Syria            1       0
```

<a name='gdelt'/>

### GDELT

[Codes](http://data.gdeltproject.org/documentation/CAMEO.Manual.1.1b3.pdf)

[Data](https://www.gdeltproject.org/data.html#rawdatafiles)

```python
import pandas as pd, zipfile
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth',-1)

with zipfile.ZipFile('/tmp/20210418.export.CSV.zip', 'r') as z:
     df = pd.read_csv(z.open('20210418.export.CSV'),sep='\t',header=None)
print (len(df.columns))
urls = df[57]
cols = ['GlobalEventID', 'Day', 'MonthYear', 'Year', 'FractionDate',\
       'Actor1Code', 'Actor1Name', 'Actor1CountryCode', 'Actor1KnownGroupCode',\
       'Actor1EthnicCode', 'Actor1Religion1Code', 'Actor1Religion2Code',\
       'Actor1Type1Code', 'Actor1Type2Code', 'Actor1Type3Code', \
       'Actor2Code', 'Actor2Name', 'Actor2CountryCode', 'Actor2KnownGroupCode',
       'Actor2EthnicCode', 'Actor2Religion1Code', 'Actor2Religion2Code',
       'Actor2Type1Code', 'Actor2Type2Code', 'Actor2Type3Code', \
       'IsRootEvent','EventCode', 'EventBaseCode']
df2 = df[range(len(cols))]
df2.columns = cols
flt = (df2.EventCode==180)
df3 = df2[flt]
#print (df3[['Actor1Name','Actor1CountryCode','Actor2Name','EventCode']])
urls[flt].to_csv('/tmp/gdelturl.csv')
g = df3.groupby(['Actor1CountryCode','Actor1Name','Actor2Name'])
print (g.size())
```

```text
58
Actor1CountryCode  Actor1Name     Actor2Name   
AFG                TALIBAN        AFGHANISTAN      1
                                  GOVERNOR         1
AFR                AFRICA         AMERICAN         2
                                  POPULATION       2
                                  UNITED STATES    1
                                                  ..
USA                UNITED STATES  PROTESTER        1
                                  UNITED STATES    6
                   WASHINGTON     ABBOT            1
                                  JOE BIDEN        2
                                  UNITED STATES    2
Length: 89, dtype: int64
```
















