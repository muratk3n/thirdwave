# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 20, 50, 100, 200, 1000, 2000, 10000, 100000,200000]
colors = ["mistyrose","lightsalmon","salmon",\
          "lightcoral", "tomato","red",\
	  "indianred","firebrick","maroon"]
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
Total Confirmed 489547.0

Updated: 2020-03-26 16:07:11.719646
```

Death Rate

```python
recov = df['Recovered'].str.replace(",","").astype(np.float).sum() 
death = df['Deaths'].str.replace(",","").astype(np.float).sum()
print ( 'Death Rate =', np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
Death Rate = 15.85 %
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
China                     81,285  3,287    74,051
Italy                     74,386  7,503     9,362
United States             68,742  1,037       428
Spain                     56,188  4,089     7,015
Germany                   39,502    222     3,547
Iran                      29,406  2,234    10,457
France                    25,233  1,331     3,900
Switzerland               11,316    171       131
United Kingdom             9,529    465       135
South Korea                9,241    131     4,144
Netherlands                7,431    434         3
Belgium                    6,235    220       675
Austria                    6,001     42       112
Portugal                   3,544     60        43
Canada                     3,409     36       185
Norway                     3,246     14         6
Australia                  2,806     13       170
Israel                     2,666      8        68
Brazil                     2,563     60         6
Sweden                     2,554     64        16
Turkey                     2,433     59        26
Malaysia                   2,031     23       199
Denmark                    1,851     41         1
Czech Republic             1,775      6        10
Ireland                    1,564      9         5
Luxembourg                 1,333      8         6
Japan                      1,307     45       310
Ecuador                    1,211     29         3
Chile                      1,142      3        22
Pakistan                   1,123      8        21
Poland                     1,120     14         7
Thailand                   1,045      4        88
Romania                    1,029     18        94
Saudi Arabia               1,012      3        33
Finland                      928      5        10
Indonesia                    893     78        35
Russia                       840      3        38
Greece                       821     23        36
Iceland                      737      2        56
India                        716     14        45
Diamond Princess             712     10       597
South Africa                 709      -        12
Philippines                  707     45        28
Singapore                    631      2       160
Panama                       558      8         2
Estonia                      538      1         8
Qatar                        537      -        41
Slovenia                     528      5        10
Argentina                    502      8        52
Croatia                      481      2        22
Peru                         480      9         1
Mexico                       475      6         4
Colombia                     470      4         8
Bahrain                      457      4       204
Egypt                        456     21        95
Hong Kong                    453      4       110
Dominican Republic           392     10         3
Serbia                       384      6        15
Iraq                         382     36       105
Lebanon                      368      6        20
United Arab Emirates         333      2        52
Algeria                      302     21        65
Lithuania                    290      4         1
Armenia                      290      -        18
New Zealand                  283      -        27
Hungary                      261     10        28
Taiwan                       252      2        29
Latvia                       244      -         1
Bulgaria                     243      3         4
Slovakia                     226      -         2
Morocco                      225      6         7
Andorra                      224      3         1
Uruguay                      217      -         -
San Marino                   208     21         4
Kuwait                       208      -        49
North Macedonia              201      3         3
Costa Rica                   201      2         2
Bosnia and Herzegovina       185      3         2
Albania                      174      6        17
Tunisia                      173      6         2
Jordan                       172      -         1
Ukraine                      162      5         1
Vietnam                      153      -        17
Moldova                      149      1         2
Burkina Faso                 146      4        10
Faeroe Islands               140      -        47
Malta                        134      -         2
Ghana                        132      4         1
Cyprus                       132      3         4
Azerbaijan                   122      3        15
Réunion                      115      -         1
Brunei                       114      -         5
Kazakhstan                   109      -         2
Oman                         109      -        23
Venezuela                    106      -        15
Senegal                      105      -         9
Sri Lanka                    102      -         7
Cambodia                      96      -        10
Belarus                       86      -        29
Afghanistan                   84      2         2
Palestine                     84      1        17
Ivory Coast                   80      -         3
Georgia                       79      -        10
Cameroon                      75      1         2
Guadeloupe                    73      1         -
Montenegro                    67      1         -
Martinique                    66      1         -
Uzbekistan                    65      -         -
Trinidad and Tobago           60      1         -
Cuba                          57      1         1
Mauritius                     52      2         -
Honduras                      52      -         -
DRC                           51      3         -
Nigeria                       51      1         2
Liechtenstein                 51      -         -
Channel Islands               46      1         -
Bangladesh                    44      5        11
Kyrgyzstan                    44      -         -
Paraguay                      41      3         -
Rwanda                        41      -         -
Bolivia                       39      -         -
Mayotte                       36      -         -
Macao                         31      -        10
Monaco                        31      -         1
Kenya                         31      -         1
French Guiana                 28      -         6
Jamaica                       26      1         2
Gibraltar                     26      -         5
French Polynesia              25      -         -
Isle of Man                   25      -         -
Guatemala                     24      1         4
Madagascar                    23      -         -
Togo                          23      -         1
Aruba                         19      -         1
Barbados                      18      -         -
New Caledonia                 14      -         -
Uganda                        14      -         -
El Salvador                   13      -         -
Maldives                      13      -         8
Tanzania                      13      -         -
Ethiopia                      12      -         -
Zambia                        12      -         -
Djibouti                      11      -         -
Dominica                      11      -         -
Mongolia                      11      -         -
Saint Martin                  11      -         -
Equatorial Guinea              9      -         -
Cayman Islands                 8      1         -
Haiti                          8      -         -
Suriname                       8      -         -
Gabon                          7      1         -
Niger                          7      1         -
Bermuda                        7      -         2
Namibia                        7      -         2
Seychelles                     7      -         -
Curaçao                        6      1         2
Benin                          6      -         -
Greenland                      6      -         2
Laos                           6      -         -
Guyana                         5      1         -
Bahamas                        5      -         1
Fiji                           5      -         -
Mozambique                     5      -         -
Syria                          5      -         -
Cabo Verde                     4      1         -
Congo                          4      -         -
Eritrea                        4      -         -
Guinea                         4      -         -
Vatican City                   4      -         -
Eswatini                       4      -         -
Gambia                         3      1         -
Sudan                          3      1         -
Zimbabwe                       3      1         -
Nepal                          3      -         1
Angola                         3      -         -
Antigua and Barbuda            3      -         -
CAR                            3      -         -
Chad                           3      -         -
Liberia                        3      -         -
Mauritania                     3      -         -
Myanmar                        3      -         -
St. Barth                      3      -         -
Saint Lucia                    3      -         -
Sint Maarten                   3      -         -
Belize                         2      -         -
Bhutan                         2      -         -
British Virgin Islands         2      -         -
Guinea-Bissau                  2      -         -
Mali                           2      -         -
Nicaragua                      2      -         -
Saint Kitts and Nevis          2      -         -
Somalia                        2      -         -
Grenada                        1      -         -
Libya                          1      -         -
Montserrat                     1      -         -
Papua New Guinea               1      -         -
St. Vincent Grenadines         1      -         -
Timor-Leste                    1      -         -
Turks and Caicos               1      -         -
```

Time Series


```python
! wget https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv
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
print (confirmed.tail(4))
confirmed.plot()
plt.savefig('timeseries.png')
```

```text
            Confirmed
Date                 
2020-03-20     272164
2020-03-21     304519
2020-03-22     337089
2020-03-23     378547
```

![](timeseries.png)


```python
(confirmed.pct_change()*100.0).plot()
plt.title('Daily % Change')
plt.savefig('rate.png')
```

![](rate.png)


```python
avg_since_mar1 = confirmed[confirmed > '2020-03-01'].pct_change().mean()
print ('avg daily chg since march', np.round(np.float(avg_since_mar1 * 100.0),2), '%')
```

```text
avg daily chg since march 12.23 %
```

Files - [corona.csv](corona.csv), [corona-time.zip](corona-time.zip), [alpha3country.csv](alpha3country.csv), [util.py](util.py)

[Reference](https://www.worldometers.info/coronavirus/)

[Colors](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)