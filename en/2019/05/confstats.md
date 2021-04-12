# Conflict Statistics

Based on UCDP/PRIO Armed Conflict Dataset

[Data](https://ucdp.uu.se/downloads/)

### Overall Deaths Globally, Specific Month

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

















