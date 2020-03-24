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
Total Confirmed 396236.0

Updated: 2020-03-24 18:08:27.625802
```

Death Rate

```python
recov = df['Recovered'].str.replace(",","").astype(np.float).sum() 
death = df['Deaths'].str.replace(",","").astype(np.float).sum()
print ( 'Death Rate =', np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
Death Rate = 14.26 %
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
China                     81,171  3,277    73,159
Italy                     63,927  6,077     7,432
United States             46,285    588       295
Spain                     39,673  2,696     3,794
Germany                   31,370    133       749
Iran                      24,811  1,934     8,913
France                    19,856    860     2,200
Switzerland                9,117    122       131
South Korea                9,037    120     3,507
United Kingdom             6,735    337       135
Netherlands                5,560    276         2
Austria                    4,971     28         9
Belgium                    4,269    122       461
Norway                     2,753     12         6
Portugal                   2,362     30        22
Sweden                     2,286     36        16
Australia                  2,144      8       118
Canada                     2,091     24       112
Brazil                     1,967     34         2
Israel                     1,656      2        49
Malaysia                   1,624     15       183
Denmark                    1,577     32         1
Turkey                     1,529     37         -
Czech Republic             1,289      2         8
Japan                      1,140     42       285
Ireland                    1,125      6         5
Ecuador                      981     18         3
Pakistan                     958      7        13
Chile                        922      2        17
Luxembourg                   875      8         6
Thailand                     827      4        52
Poland                       799      9         1
Finland                      792      1        10
Saudi Arabia                 767      1        28
Romania                      762      8        79
Diamond Princess             712     10       587
Greece                       695     19        29
Indonesia                    686     55        30
Iceland                      648      2        51
Singapore                    558      2       156
South Africa                 554      -         4
Philippines                  552     35        20
India                        519     10        40
Qatar                        501      -        37
Russia                       495      1        22
Slovenia                     480      4         3
Peru                         395      5         1
Bahrain                      390      3       164
Hong Kong                    386      4       102
Estonia                      369      -         7
Mexico                       367      4         4
Egypt                        366     19        68
Croatia                      361      1         5
Panama                       345      6         1
Iraq                         316     27        75
Dominican Republic           312      6         3
Colombia                     306      3         6
Lebanon                      304      4         8
Serbia                       303      3        15
Argentina                    301      4        51
Armenia                      235      -         2
Algeria                      230     17        65
Taiwan                       216      2        29
Slovakia                     204      -         7
Lithuania                    203      1         1
Bulgaria                     202      3         3
United Arab Emirates         198      2        41
Latvia                       197      -         1
Kuwait                       191      -        39
San Marino                   187     21         4
Hungary                      187      9        21
Andorra                      164      1         1
Uruguay                      162      -         -
Costa Rica                   158      2         2
New Zealand                  155      -        12
Bosnia and Herzegovina       150      2         2
North Macedonia              148      2         1
Morocco                      143      4         5
Vietnam                      134      -        17
Jordan                       127      -         1
Albania                      123      5        10
Faeroe Islands               122      -        23
Cyprus                       116      1         3
Burkina Faso                 114      4         7
Tunisia                      114      3         1
Malta                        110      -         2
Moldova                      109      1         2
Brunei                       104      -         2
Sri Lanka                    102      -         2
Ukraine                       97      3         1
Cambodia                      91      -         4
Azerbaijan                    87      1        10
Senegal                       86      -         8
Oman                          84      -        17
Venezuela                     84      -        15
Belarus                       81      -        22
Réunion                       75      -         1
Kazakhstan                    68      -         -
Georgia                       67      -         9
Cameroon                      66      -         2
Guadeloupe                    62      1         -
Palestine                     60      -        16
Martinique                    53      1         -
Ghana                         52      2         -
Trinidad and Tobago           52      -         -
Liechtenstein                 51      -         -
Uzbekistan                    50      -         -
DRC                           45      2         -
Afghanistan                   42      1         1
Nigeria                       42      1         2
Kyrgyzstan                    42      -         -
Cuba                          40      1         -
Bangladesh                    39      4         5
Puerto Rico                   39      2         1
Mauritius                     36      2         -
Channel Islands               36      -         -
Mayotte                       36      -         -
Rwanda                        36      -         -
Guam                          32      1         -
Honduras                      30      -         -
Montenegro                    29      1         -
Bolivia                       28      -         -
Paraguay                      27      2         -
Macao                         26      -        10
Ivory Coast                   25      -         2
Kenya                         25      -         -
Monaco                        23      -         1
French Guiana                 23      -         6
French Polynesia              23      -         -
Jamaica                       21      1         2
Guatemala                     20      1         -
Guyana                        20      1         -
Isle of Man                   20      -         -
Togo                          20      -         1
Barbados                      17      -         -
Madagascar                    17      -         -
U.S. Virgin Islands           17      -         -
Gibraltar                     15      -         5
Maldives                      13      -         5
Aruba                         12      -         1
Ethiopia                      12      -         -
Tanzania                      12      -         -
Mongolia                      10      -         -
New Caledonia                 10      -         -
Equatorial Guinea              9      -         -
Uganda                         9      -         -
Saint Martin                   8      -         -
Seychelles                     7      -         -
Gabon                          6      1         -
Benin                          6      -         -
Bermuda                        6      -         -
Haiti                          6      -         -
Suriname                       6      -         -
Cayman Islands                 5      1         -
El Salvador                    5      -         -
Curaçao                        4      1         -
Bahamas                        4      -         -
Congo                          4      -         -
Fiji                           4      -         -
Greenland                      4      -         2
Guinea                         4      -         -
Namibia                        4      -         -
Eswatini                       4      -         -
Cabo Verde                     3      1         -
Sudan                          3      1         -
Zimbabwe                       3      1         -
Angola                         3      -         -
Antigua and Barbuda            3      -         -
CAR                            3      -         -
Chad                           3      -         -
Djibouti                       3      -         -
Liberia                        3      -         -
Mozambique                     3      -         -
Niger                          3      -         -
St. Barth                      3      -         -
Saint Lucia                    3      -         -
Zambia                         3      -         -
Gambia                         2      1         -
Nepal                          2      -         1
Bhutan                         2      -         -
Dominica                       2      -         -
Laos                           2      -         -
Mauritania                     2      -         -
Myanmar                        2      -         -
Nicaragua                      2      -         -
Sint Maarten                   2      -         -
Belize                         1      -         -
Eritrea                        1      -         -
Grenada                        1      -         -
Vatican City                   1      -         -
Montserrat                     1      -         -
Papua New Guinea               1      -         -
St. Vincent Grenadines         1      -         -
Somalia                        1      -         -
Syria                          1      -         -
Timor-Leste                    1      -         -
Turks and Caicos               1      -         -
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

