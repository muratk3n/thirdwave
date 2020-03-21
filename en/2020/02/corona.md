# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 20, 50, 100, 200, 1000, 2000, 100000]
colors = ["mistyrose","lightsalmon","salmon",
          "lightcoral","tomato","red","firebrick"]	      
df, col_dict = util.retrieve_cor_data(bins,colors)
```

```python
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import cartopy.feature as cfeature

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
shp = shpreader.natural_earth(resolution='10m',category='cultural',
                              name='admin_0_countries')
reader = shpreader.Reader(shp)
for n in reader.records() :
    if n.attributes['ADM0_A3'] in col_dict:
        c = col_dict[n.attributes['ADM0_A3']]
        if ('str' in str(type(c))): ax.add_geometries(n.geometry, ccrs.PlateCarree(), facecolor=col_dict[n.attributes['ADM0_A3']])
plt.savefig('corworld.png')
```

![](corworld.png)

```python
import datetime
print ('Total Confirmed', df['Confirmed'].str.replace(",","").astype(np.float).sum() )
print ('\nUpdated:',datetime.datetime.now())
```

```text
Total Confirmed 259684.0

Updated: 2020-03-20 20:08:40.818544
```

Death Rate

```python
recov = df['Recovered'].str.replace(",","").astype(np.float).sum() 
death = df['Deaths'].str.replace(",","").astype(np.float).sum()
print ( 'Death Rate =', np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
Death Rate = 10.5 %
```

```python
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10000)
pd.set_option('precision', 2)
pd.set_option('display.float_format', lambda x: '%.3f' % x) 
print (df.set_index('Country').fillna('-'))
```

```text
                       Confirmed Deaths Recovered
Country                                          
China                     80,967  3,248    71,150
Italy                     41,035  3,405     4,440
Spain                     20,412  1,041     1,588
Iran                      19,644  1,433     6,745
Germany                   18,794     53       180
United States             16,315    220       125
France                    10,995    372     1,295
South Korea                8,652     94     2,233
Switzerland                5,164     54        15
United Kingdom             3,269    184        65
Netherlands                2,994    106         2
Austria                    2,491      6         9
Belgium                    2,257     37       204
Norway                     1,906      7         1
Sweden                     1,639     16        16
Denmark                    1,255      9         1
Malaysia                   1,030      3        87
Portugal                   1,020      6         5
Japan                        963     33       215
Canada                       924     12        11
Australia                    876      7        46
Czech Republic               833      -         4
Diamond Princess             712      7       527
Israel                       705      -        15
Brazil                       654      7         2
Ireland                      557      3         5
Pakistan                     500      3        13
Greece                       495      9        19
Luxembourg                   484      5         6
Qatar                        460      -        10
Finland                      450      -        10
Chile                        434      -         6
Poland                       411      5        13
Iceland                      409      -         5
Singapore                    385      -       131
Indonesia                    369     32        17
Ecuador                      367      5         3
Turkey                       359      4         -
Slovenia                     341      1         -
Thailand                     322      1        42
Romania                      308      -        31
Bahrain                      291      1       112
Estonia                      283      -         1
Saudi Arabia                 274      -         8
Egypt                        256      7        42
Hong Kong                    256      4        98
Russia                       253      1        12
India                        249      5        23
Peru                         234      3         1
Philippines                  230     18         8
South Africa                 202      -         -
Iraq                         192     13        49
Mexico                       164      1         4
Lebanon                      163      4         4
Kuwait                       159      -        22
Colombia                     145      -         1
San Marino                   144     14         4
United Arab Emirates         140      -        31
Panama                       137      1         1
Slovakia                     137      -         -
Armenia                      136      -         1
Taiwan                       135      2        28
Bulgaria                     129      3         1
Argentina                    128      3         3
Croatia                      128      1         5
Serbia                       118      -         2
Latvia                       111      -         1
Uruguay                       94      -         -
Vietnam                       91      -        17
Algeria                       90     11        32
Costa Rica                    89      2         -
Hungary                       85      3         7
Faeroe Islands                80      -         3
Brunei                        78      -         1
Andorra                       75      -         1
Cyprus                        75      -         -
Morocco                       74      3         2
Sri Lanka                     73      -         3
Dominican Republic            72      2         -
Albania                       70      2         -
North Macedonia               70      -         1
Belarus                       69      -        15
Jordan                        69      -         1
Bosnia and Herzegovina        69      -         2
Moldova                       66      1         1
Malta                         64      -         2
Tunisia                       54      1         1
Kazakhstan                    52      -         -
Cambodia                      51      -         1
Lithuania                     51      -         1
Oman                          48      -        13
Palestine                     48      -        17
Guadeloupe                    45      -         -
Azerbaijan                    44      1         7
Georgia                       44      -         1
Venezuela                     42      -         -
Burkina Faso                  40      1         4
New Zealand                   39      -         -
Senegal                       38      -         2
Uzbekistan                    33      -         -
Martinique                    32      1         -
Liechtenstein                 28      -         -
Réunion                       28      -         -
Ukraine                       26      3         1
Afghanistan                   24      -         1
Honduras                      24      -         -
Bangladesh                    20      1         3
Cameroon                      20      -         2
DRC                           18      -         -
Macao                         17      -        10
Cuba                          16      1         -
Jamaica                       16      1         2
Bolivia                       16      -         -
Ghana                         16      -         -
Guyana                        15      1         -
French Guiana                 15      -         -
Guam                          14      -         -
Maldives                      13      -         -
Montenegro                    13      -         -
Paraguay                      13      -         -
Guatemala                     12      1         -
Nigeria                       12      -         1
Mauritius                     12      -         -
Monaco                        11      -         -
Channel Islands               11      -         -
French Polynesia              11      -         -
Rwanda                        11      -         -
Gibraltar                     10      -         2
Ivory Coast                    9      -         1
Ethiopia                       9      -         -
Togo                           9      -         -
Trinidad and Tobago            9      -         -
Puerto Rico                    8      -         -
Kenya                          7      -         -
Seychelles                     7      -         -
Equatorial Guinea              6      -         -
Kyrgyzstan                     6      -         -
Mayotte                        6      -         -
Mongolia                       6      -         -
Tanzania                       6      -         -
Aruba                          5      -         1
Barbados                       5      -         -
Saint Martin                   4      -         -
Suriname                       4      -         -
Cayman Islands                 3      1         -
Curaçao                        3      1         -
Gabon                          3      1         -
Bahamas                        3      -         -
CAR                            3      -         -
Congo                          3      -         -
Namibia                        3      -         -
St. Barth                      3      -         -
U.S. Virgin Islands            3      -         -
Sudan                          2      1         -
Benin                          2      -         -
Bermuda                        2      -         -
Bhutan                         2      -         -
Greenland                      2      -         -
Guinea                         2      -         -
Haiti                          2      -         -
Isle of Man                    2      -         -
Liberia                        2      -         -
Mauritania                     2      -         -
New Caledonia                  2      -         -
Saint Lucia                    2      -         -
Zambia                         2      -         -
Nepal                          1      -         1
Angola                         1      -         -
Antigua and Barbuda            1      -         -
Cabo Verde                     1      -         -
Chad                           1      -         -
Djibouti                       1      -         -
El Salvador                    1      -         -
Fiji                           1      -         -
Gambia                         1      -         -
Vatican City                   1      -         -
Montserrat                     1      -         -
Nicaragua                      1      -         -
Niger                          1      -         -
Papua New Guinea               1      -         -
St. Vincent Grenadines         1      -         -
Sint Maarten                   1      -         -
Somalia                        1      -         -
Eswatini                       1      -         -
```

Time Series


```python
! wget https://raw.githubusercontent.com/datasets/covid-19/master/time-series-19-covid-combined.csv
! zip corona-time.zip time-series-19-covid-combined.csv
! rm time-series-19-covid-combined.csv
```

```python
import pandas as pd
import zipfile
with zipfile.ZipFile('corona-time.zip', 'r') as z:
    df =  pd.read_csv(z.open('time-series-19-covid-combined.csv'),parse_dates=['Date'])
df = df[['Date','Confirmed']]
df = df.set_index('Date')
confirmed = df.groupby('Date').sum()
confirmed.plot()
plt.savefig('timeseries.png')
```

![](timeseries.png)

Files - [corona.csv](corona.csv), [corona-time.zip](corona-time.zip), [alpha3country.csv](alpha3country.csv), [util.py](util.py)

[Reference](https://www.worldometers.info/coronavirus/)

