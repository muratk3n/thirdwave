# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 50, 100, 200, 1000, 2000, 10000, 100000, 400000, 800000]
colors = ["lightsalmon","salmon","lightcoral", "tomato","red",\
	  "indianred","firebrick","maroon","darkblue"]
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
Total Confirmed 1733821.0

Updated: 2020-04-11 19:23:45.099031
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
21.33 %
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
United States              507412  19816     28224   459372
Spain                      161852  16353     59109    86390
Italy                      152271  19468     32534   100269
France                     124869  13197     24932    86740
Germany                    122855   2736     53913    66206
China                       81953   3339     77525     1089
United Kingdom              78991   9875       344    68772
Iran                        70029   4357     41947    23725
Turkey                      47029   1006      2423    43600
Belgium                     28018   3346      5986    18686
Switzerland                 24900   1015     11100    12785
Netherlands                 24413   2643       250    21520
Canada                      22559    569      6013    15977
Brazil                      20022   1075       173    18774
Portugal                    15987    470       266    15251
Austria                     13795    337      6604     6854
Russia                      13584    106      1045    12433
Israel                      10525     96      1258     9171
South Korea                 10480    211      7243     3026
Sweden                      10151    887       381     8883
Ireland                      8089    287        25     7777
India                        8063    249       774     7040
Ecuador                      7161    297       368     6496
Chile                        6927     73      1864     4990
Norway                       6360    114        32     6214
Poland                       6356    208       375     5773
Australia                    6303     56      3265     2982
Japan                        6005     99       762     5144
Denmark                      5996    260      1955     3781
Romania                      5990    282       758     4950
Peru                         5897    169      1569     4159
Czech Republic               5831    129       411     5291
Pakistan                     4970     77       762     4131
Malaysia                     4530     73      1995     2462
Philippines                  4428    247       157     4024
Saudi Arabia                 4033     52       720     3261
Mexico                       3844    233       633     2978
Indonesia                    3842    327       286     3229
United Arab Emirates         3736     20       588     3128
Serbia                       3380     74       118     3188
Luxembourg                   3223     54       500     2669
Panama                       2974     74        17     2883
Finland                      2905     49       300     2556
Qatar                        2728      6       247     2475
Dominican Republic           2620    126        98     2396
Thailand                     2518     35      1135     1348
Ukraine                      2511     73        79     2359
Colombia                     2473     80       197     2196
Singapore                    2299      8       528     1763
Belarus                      2226     23       172     2031
Greece                       2081     93       269     1719
South Africa                 2003     24       410     1569
Argentina                    1975     83       440     1452
Algeria                      1825    275       460     1090
Egypt                        1794    135       384     1275
Iceland                      1689      7       841      841
Moldova                      1560     30        75     1455
Croatia                      1534     21       323     1190
Morocco                      1527    110       141     1276
Iraq                         1318     72       601      645
New Zealand                  1312      4       422      886
Hungary                      1310     85       115     1110
Estonia                      1304     24        93     1187
Slovenia                     1188     50       148      990
Kuwait                       1154      1       133     1020
Azerbaijan                   1058     11       200      847
Lithuania                    1026     23        54      949
Bahrain                      1016      6       551      459
Hong Kong                    1001      4       336      661
Armenia                       977     13       173      791
Bosnia and Herzegovina        935     37       139      759
Kazakhstan                    859     10        81      768
Cameroon                      820     12        98      710
North Macedonia               760     34        41      685
Uzbekistan                    729      3        42      684
Slovakia                      728      2        23      703
Diamond Princess              712     11       619       82
Tunisia                       671     25        43      603
Bulgaria                      661     28        62      571
Latvia                        630      3        16      611
Cuba                          620     16        77      527
Lebanon                       619     20        77      522
Cyprus                        616     10        58      548
Andorra                       601     26        71      504
Costa Rica                    558      3        42      513
Afghanistan                   555     18        32      505
Oman                          546      3       109      434
Uruguay                       494      7       214      273
Bangladesh                    482     30        36      416
Ivory Coast                   480      3        54      423
Burkina Faso                  448     26       149      273
Niger                         438     11        41      386
Albania                       433     23       197      213
Ghana                         408      8         4      396
Channel Islands               398      9        40      349
Honduras                      392     24         7      361
Réunion                       388      -        40        -
Taiwan                        385      6        99      280
Jordan                        372      7       170      195
Malta                         370      3        16      351
San Marino                    356     35        53      268
Kyrgyzstan                    339      5        44      290
Mauritius                     319      9        28      282
Nigeria                       305      7        58      240
Senegal                       278      2       152      124
Bolivia                       275     20         2      253
Palestine                     268      2        46      220
Montenegro                    263      2         5      256
Vietnam                       258      -       144        -
Georgia                       242      3        56      183
DRC                           223     20        16      187
Guinea                        212      -        15        -
Isle of Man                   204      1       112       91
Sri Lanka                     198      7        54      137
Mayotte                       196      3        59      134
Kenya                         191      7        24      160
Djibouti                      187      2        36      149
Faeroe Islands                184      -       145        -
Venezuela                     175      9        84       82
Martinique                    155      6        50       99
Guadeloupe                    143      8        67       68
Guatemala                     137      3        19      115
Brunei                        136      1       104       31
Paraguay                      133      6        18      109
Gibraltar                     127      -        69        -
Cambodia                      120      -        75        -
El Salvador                   118      6        19       93
Rwanda                        118      -        18        -
Trinidad and Tobago           109      8         3       98
Madagascar                    102      -        11        -
Monaco                         90      1         5       84
Mali                           87      7        22       58
Aruba                          86      -        27        -
French Guiana                  83      -        43        -
Liechtenstein                  79      1        55       23
Togo                           76      3        25       48
Ethiopia                       69      3        10       56
Barbados                       67      4        11       52
Jamaica                        65      4        13       48
Congo                          60      5         5       50
Uganda                         53      -         3        -
French Polynesia               51      -         -        -
Sint Maarten                   50      8         3       39
Bermuda                        48      4        25       19
Cayman Islands                 45      1         6       38
Macao                          45      -        10        -
Gabon                          44      1         1       42
Bahamas                        42      8         5       29
Guyana                         40      6         8       26
Zambia                         40      2        28       10
Guinea-Bissau                  38      -         -        -
Liberia                        37      5         3       29
Benin                          35      1         5       29
Eritrea                        34      -         -        -
Tanzania                       32      3         5       24
Saint Martin                   32      2        11       19
Myanmar                        31      3         2       26
Haiti                          31      2         -        -
Syria                          25      2         4       19
Libya                          24      1         8       15
Antigua and Barbuda            21      2         -        -
Somalia                        21      1         1       19
Mozambique                     20      -         2        -
Angola                         19      2         2       15
Sudan                          19      2         2       15
Maldives                       19      -        13        -
Equatorial Guinea              18      -         3        -
Laos                           18      -         -        -
New Caledonia                  18      -         1        -
Dominica                       16      -         5        -
Fiji                           16      -         -        -
Mongolia                       16      -         4        -
Namibia                        16      -         3        -
Saint Lucia                    15      -         1        -
Curaçao                        14      1         7        6
Grenada                        14      -         -        -
Zimbabwe                       13      3         -        -
Botswana                       13      1         -        -
Malawi                         12      2         -        -
Saint Kitts and Nevis          12      -         -        -
St. Vincent Grenadines         12      -         1        -
Eswatini                       12      -         7        -
Chad                           11      -         2        -
Greenland                      11      -        11        -
Seychelles                     11      -         -        -
Belize                         10      2         -        -
Suriname                       10      1         4        5
MS Zaandam                      9      2         -        -
Nepal                           9      -         1        -
Montserrat                      9      -         -        -
Cabo Verde                      8      1         1        6
Nicaragua                       8      1         -        -
Turks and Caicos                8      1         -        -
CAR                             8      -         -        -
Vatican City                    8      -         2        -
Sierra Leone                    8      -         -        -
Mauritania                      7      1         2        4
St. Barth                       6      -         1        -
Bhutan                          5      -         2        -
Falkland Islands                5      -         1        -
Gambia                          4      1         2        1
Sao Tome and Principe           4      -         -        -
South Sudan                     4      -         -        -
Western Sahara                  4      -         -        -
Anguilla                        3      -         -        -
British Virgin Islands          3      -         2        -
Burundi                         3      -         -        -
Caribbean Netherlands           2      -         -        -
Papua New Guinea                2      -         -        -
Timor-Leste                     2      -         1        -
Saint Pierre Miquelon           1      -         -        -
Yemen                           1      -         -        -
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
confirmed = df.groupby('Date').sum() / 1e6
print (confirmed.tail(4))
confirmed.plot()
plt.savefig('timeseries.png')
```

```text
            Confirmed
Date                 
2020-04-07       1.43
2020-04-08       1.51
2020-04-09       1.60
2020-04-10       1.69
```

![](timeseries.png)


```python
pd.set_option('display.float_format', lambda x: '%.2f' % x) 
chg = confirmed.pct_change()*100.0
chg.plot()
print (chg.tail(5))
plt.title('Daily % Change')
plt.savefig('rate.png')
```

```text
            Confirmed
Date                 
2020-04-06       5.74
2020-04-07       6.02
2020-04-08       5.96
2020-04-09       5.58
2020-04-10       6.04
```

![](rate.png)


County Level Data (NYT)

```python
! wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
! zip $HOME/Downloads/corona-county.zip us-counties.csv
! rm us-counties.csv
```

Files - [corona.csv](corona.csv), [corona-time.zip](corona-time.zip), [alpha3country.csv](alpha3country.csv), [util.py](util.py)

[Colors](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)

[Reference](https://www.worldometers.info/coronavirus/)

