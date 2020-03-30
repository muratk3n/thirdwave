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
3        c = col_dict[n.attributes['ADM0_A3']]
        if 'nan' not in str(c): 
            ax.add_geometries(n.geometry, ccrs.PlateCarree(), facecolor=col_dict[n.attributes['ADM0_A3']])
plt.savefig('corworld.png')
```

![](corworld.png)

```python
import datetime
print ('Total Confirmed', df['Confirmed'].sum() )
print ('\nUpdated:',datetime.datetime.now())
```

```text
Total Confirmed 723823.0

Updated: 2020-03-30 12:02:40.068534
```

```python
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10000)
pd.set_option('precision', 2)
pd.set_option('display.float_format', lambda x: '%.0f' % x) 
print (df.set_index('Country').fillna('-'))
```

```text
                        Confirmed Deaths Recovered NewCases
Country                                                    
United States              142735   2489      4562   135684
Italy                       97689  10779     13030    73880
China                       81470   3304     75700     2466
Spain                       80110   6803     14709    58598
Germany                     62435    541      9211    52683
France                      40174   2606      7202    30366
Iran                        38309   2640     12391    23278
United Kingdom              19522   1228       135    18159
Switzerland                 14829    300      1595    12934
Netherlands                 10866    771       250     9845
Belgium                     10836    431      1359     9046
South Korea                  9661    158      5228     4275
Turkey                       9217    131       105     8981
Austria                      8958     86       479     8393
Canada                       6320     65       573     5682
Portugal                     5962    119        43     5800
Israel                       4347     15       134     4198
Norway                       4305     26         7     4272
Brazil                       4256    136         6     4114
Australia                    4163     18       244     3901
Sweden                       3700    110        16     3574
Czech Republic               2837     17        11     2809
Ireland                      2615     46         5     2564
Malaysia                     2470     35       388     2047
Denmark                      2395     72         1     2322
Chile                        2139      7        75     2057
Luxembourg                   1950     21        40     1889
Ecuador                      1924     58         3     1863
Poland                       1905     26         7     1872
Japan                        1866     54       424     1388
Romania                      1815     43       206     1566
Pakistan                     1625     18        29     1578
Russia                       1534      8        64     1462
Thailand                     1524      7       229     1288
Philippines                  1418     71        42     1305
Saudi Arabia                 1299      8        66     1225
Indonesia                    1285    114        64     1107
South Africa                 1280      2        31     1247
Finland                      1240     11        10     1219
Greece                       1156     39        52     1065
India                        1071     29       100      942
Iceland                      1020      2       135      883
Mexico                        993     20        35      938
Panama                        989     24         4      961
Dominican Republic            859     39         3      817
Peru                          852     18        16      818
Singapore                     844      3       212      629
Argentina                     820     20        91      709
Serbia                        741     13        42      686
Slovenia                      730     11        10      709
Estonia                       715      3        20      692
Croatia                       713      6        55      652
Diamond Princess              712     10       603       99
Colombia                      702     10        10      682
Hong Kong                     642      4       118      520
Qatar                         634      1        48      585
Egypt                         609     40       132      437
New Zealand                   589      1        63      525
United Arab Emirates          570      3        58      509
Iraq                          547     42       143      362
Morocco                       516     27        13      476
Bahrain                       515      4       279      232
Algeria                       511     31        31      449
Lithuania                     484      7         1      476
Ukraine                       475     10         6      459
Hungary                       447     15        34      398
Lebanon                       438     10        30      398
Armenia                       424      3        30      391
Latvia                        376      -         1        -
Bulgaria                      354      8        15      331
Bosnia and Herzegovina        340      6         8      326
Andorra                       334      6         6      322
Costa Rica                    314      2         3      309
Slovakia                      314      -         2        -
Tunisia                       312      8         2      302
Uruguay                       304      1         -        -
Taiwan                        298      3        39      256
Kazakhstan                    293      1        20      272
Moldova                       263      2        13      248
North Macedonia               259      6         3      250
Jordan                        259      3        18      238
Kuwait                        255      -        67        -
San Marino                    224     22         6      196
Burkina Faso                  222     12        23      187
Cyprus                        214      6        15      193
Albania                       212     10        33      169
Azerbaijan                    209      4        15      190
Vietnam                       194      -        52        -
Réunion                       183      -         1        -
Oman                          167      -        23        -
Ivory Coast                   165      1         4      160
Faeroe Islands                159      -        70        -
Ghana                         152      5         2      145
Malta                         151      -         2        -
Uzbekistan                    144      2         7      135
Senegal                       142      -        27        -
Cameroon                      139      6         5      128
Cuba                          139      3         4      132
Honduras                      139      3         3      133
Brunei                        126      1        34       91
Afghanistan                   120      4         2      114
Sri Lanka                     120      1        11      108
Venezuela                     119      3        39       77
Nigeria                       111      1         3      107
Mauritius                     110      3         -        -
Palestine                     109      1        18       90
Channel Islands               108      2         -        -
Guadeloupe                    106      4        17       85
Cambodia                      103      -        21        -
Georgia                        98      -        18        -
Bolivia                        96      1         -        -
Belarus                        94      -        32        -
Martinique                     93      1         -        -
Montenegro                     91      1         -        -
Kyrgyzstan                     84      -         -        -
DRC                            81      8         2       71
Trinidad and Tobago            78      3         1       74
Rwanda                         70      -         -        -
Gibraltar                      65      -        14        -
Paraguay                       64      3         1       60
Mayotte                        63      -         -        -
Liechtenstein                  56      -         -        -
Aruba                          50      -         1        -
Bangladesh                     49      5        19       25
Monaco                         46      1         1       44
French Guiana                  43      -         6        -
Kenya                          42      1         1       40
Isle of Man                    42      -         -        -
Madagascar                     39      -         -        -
Macao                          37      -        10        -
Guatemala                      34      1        10       23
Barbados                       33      -         -        -
Uganda                         33      -         -        -
Jamaica                        32      1         2       29
Togo                           30      1         1       28
El Salvador                    30      -         -        -
French Polynesia               30      -         -        -
Zambia                         29      -         -        -
Bermuda                        22      -         2        -
Ethiopia                       21      -         1        -
Congo                          19      -         -        -
Mali                           18      1         -        -
Niger                          18      1         -        -
Djibouti                       18      -         -        -
Maldives                       17      -        13        -
Guinea                         16      -         -        -
Haiti                          15      -         1        -
New Caledonia                  15      -         -        -
Bahamas                        14      -         1        -
Tanzania                       14      -         1        -
Cayman Islands                 12      1         -        -
Equatorial Guinea              12      -         -        -
Eritrea                        12      -         -        -
Mongolia                       12      -         2        -
Dominica                       11      -         -        -
Namibia                        11      -         2        -
Saint Martin                   11      -         -        -
Greenland                      10      -         2        -
Myanmar                        10      -         -        -
Syria                           9      1         -        -
Grenada                         9      -         -        -
Saint Lucia                     9      -         1        -
Eswatini                        9      -         -        -
Curaçao                         8      1         2        5
Guyana                          8      1         -        -
Laos                            8      -         -        -
Libya                           8      -         -        -
Mozambique                      8      -         -        -
Seychelles                      8      -         -        -
Suriname                        8      -         -        -
Angola                          7      2         -        -
Gabon                           7      1         -        -
Zimbabwe                        7      1         -        -
Antigua and Barbuda             7      -         -        -
Cabo Verde                      6      1         -        -
Sudan                           6      1         -        -
Benin                           6      -         -        -
Vatican City                    6      -         -        -
Sint Maarten                    6      -         -        -
Nepal                           5      -         1        -
Fiji                            5      -         -        -
Mauritania                      5      -         2        -
Montserrat                      5      -         -        -
St. Barth                       5      -         -        -
Gambia                          4      1         -        -
Nicaragua                       4      1         -        -
Bhutan                          4      -         -        -
Turks and Caicos                4      -         -        -
CAR                             3      -         -        -
Chad                            3      -         -        -
Liberia                         3      -         -        -
Somalia                         3      -         -        -
MS Zaandam                      2      -         -        -
Anguilla                        2      -         -        -
Belize                          2      -         -        -
British Virgin Islands          2      -         -        -
Guinea-Bissau                   2      -         -        -
Saint Kitts and Nevis           2      -         -        -
Papua New Guinea                1      -         -        -
St. Vincent Grenadines          1      -         1        -
Timor-Leste                     1      -         -        -
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
2020-03-23     378235
2020-03-24     418045
2020-03-25     467653
2020-03-26     529591
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
avg daily chg since march 12.21 %
```

County Level Data (NYT)

```python
! wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
! zip $HOME/Downloads/corona-county.zip us-counties.csv
! rm us-counties.csv
```


Files - [corona.csv](corona.csv), [corona-time.zip](corona-time.zip), [alpha3country.csv](alpha3country.csv), [util.py](util.py)

[Colors](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)

[Reference](https://www.worldometers.info/coronavirus/)

