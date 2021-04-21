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

print (overall_deaths(mon=3))
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

[Data](http://data.gdeltproject.org/events/)

```python
import pandas as pd, zipfile
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth',-1)

with zipfile.ZipFile('/tmp/20210420.export.CSV.zip', 'r') as z:
     df = pd.read_csv(z.open('20210420.export.CSV'),sep='\t',header=None)
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
g = df3.groupby(['Actor1CountryCode','Actor1Name','Actor2Name']).size()
g = g[g>1]
print (g)
```

```text
58
Actor1CountryCode  Actor1Name      Actor2Name             
AFR                AFRICA          VILLAGE                    2 
AUS                AUSTRALIA       GOVERNMENT                 4 
                   PERTH           SCHOOL                     3 
                   VICTORIA        UNITED STATES              2 
COD                CONGOLESE       RUSSIA                     2 
EUR                EUROPE          SERBIA                     2 
GBR                BRITISH         UNITED KINGDOM             2 
                   UNITED KINGDOM  UNITED KINGDOM             4 
IND                CHHATTISGARH    POLITICIAN                 3 
ISR                ISRAEL          PALESTINIAN                2 
NGA                NIGERIA         AFRICA                     3 
                                   POLICEMAN                  3 
PAK                PAKISTAN        POLICE                     2 
RUS                RUSSIA          FINLAND                    3 
                                   UKRAINE                    3 
SYR                SYRIA           CIVILIAN                   2 
                                   RICHMOND                   2 
TWN                TAIPEI          TAIWAN                     2 
                   TAIWAN          TAIWAN                     2 
UKR                UKRAINE         RUSSIA                     2 
                                   RUSSIAN                    5 
                   UKRAINIAN       MEXICO                     2 
USA                AUSTIN          CIVILIAN                   2 
                   BOSTON          CRIMINAL                   2 
                   FLORIDA         SENATE                     2 
                   INDIANA         POLICE                     3 
                   KENTUCKY        PRISON                     2 
                   LOS ANGELES     DETECTIVE                  3 
                   NEW YORK        KILLERS                    3 
                                   UYGHUR                     3 
                   TEXAS           UNIVERSITY                 2 
                   THE US          JOURNALIST                 2 
                   UNITED STATES   ATTORNEY                   6 
                                   AUSTRALIA                  2 
                                   FELON                      3 
                                   JOURNALIST                 3 
                                   LAW ENFORCEMENT OFFICER    2 
                                   NASSAU                     2 
                                   NAVAJO                     2 
                                   NAVY                       4 
                                   NEWSPAPER                  2 
                                   POLICE                     8 
                                   POLICE OFFICER             2 
                                   POLICEMAN                  2 
                                   PRISON                     4 
                                   SAUDI ARABIA               2 
                                   UNITED STATES              12
                   VIRGINIA        AUTHORITIES                2 
ZWE                ZIMBABWE        GAZA                       2 
                                   VILLAGE                    2 
dtype: int64
```
















