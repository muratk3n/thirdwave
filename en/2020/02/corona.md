# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 50, 100, 200, 1000, 2000, 10000, 100000, 800000, 1200000]
colors = ["lightsalmon","salmon","lightcoral", "tomato","red",\
	  "indianred","firebrick","maroon","midnightblue"]
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
Total Confirmed 2557503.0

Updated: 2020-04-22 07:16:53.137240
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
20.38 %
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
United States              819164  45340     82973   690851
Spain                      204178  21282     82514   100382
Italy                      183957  24648     51600   107709
France                     158050  20796     39181    98073
Germany                    148453   5086     99400    43967
United Kingdom             129044  17337         -        -
Turkey                      95591   2259     14918    78414
Iran                        84802   5297     60965    18540
China                       82788   4632     77151     1005
Russia                      52763    456      3873    48434
Brazil                      43368   2761     24325    16282
Belgium                     40956   5998      9002    25956
Canada                      38422   1834     13188    23400
Netherlands                 34134   3916         -        -
Switzerland                 28063   1478     19400     7185
Portugal                    21379    762       917    19700
India                       20080    645      3975    15460
Peru                        17837    484      6982    10371
Ireland                     16040    730      9233     6077
Sweden                      15322   1765       550    13007
Austria                     14873    491     10971     3411
Israel                      13942    184      4507     9251
Saudi Arabia                11631    109      1640     9882
Japan                       11512    281      1356     9875
Chile                       10832    147      4969     5716
South Korea                 10694    238      8277     2179
Ecuador                     10398    520      1207     8671
Poland                       9856    401      1297     8158
Pakistan                     9565    201      2073     7291
Mexico                       9501    857      2627     6017
Romania                      9242    498      2153     6591
Singapore                    9125     11       839     8275
United Arab Emirates         7755     46      1443     6266
Denmark                      7695    370      4700     2625
Norway                       7241    182        32     7027
Indonesia                    7135    616       842     5677
Czech Republic               7033    201      1753     5079
Serbia                       6890    130       977     5783
Belarus                      6723     55       577     6091
Australia                    6647     74      4912     1661
Philippines                  6599    437       654     5508
Qatar                        6533      9       614     5910
Ukraine                      6125    161       367     5597
Malaysia                     5482     92      3349     2041
Dominican Republic           5044    245       463     4336
Panama                       4821    141       231     4449
Colombia                     4149    196       804     3149
Finland                      4014    141      2000     1873
Luxembourg                   3618     78       670     2870
Egypt                        3490    264       870     2356
South Africa                 3465     58      1055     2352
Bangladesh                   3382    110        87     3185
Morocco                      3209    145       393     2671
Argentina                    3144    151       840     2153
Algeria                      2811    392      1152     1267
Thailand                     2811     48      2108      655
Moldova                      2614     72       505     2037
Greece                       2401    121       577     1703
Hungary                      2098    213       287     1598
Kuwait                       2080     11       412     1657
Kazakhstan                   2025     19       489     1517
Bahrain                      1973      7       784     1182
Croatia                      1908     48       801     1059
Iceland                      1778     10      1417      351
Uzbekistan                   1678      6       357     1315
Iraq                         1602     83      1096      423
Estonia                      1552     43       169     1340
Oman                         1508      8       238     1262
Azerbaijan                   1480     20       865      595
New Zealand                  1451     14      1036      401
Armenia                      1401     24       609      768
Lithuania                    1350     38       298     1014
Slovenia                     1344     77       197     1070
Bosnia and Herzegovina       1342     51       437      854
North Macedonia              1231     55       224      952
Slovakia                     1199     14       258      927
Cameroon                     1163     43       329      791
Cuba                         1137     38       309      790
Afghanistan                  1092     36       150      906
Ghana                        1042      9        99      934
Hong Kong                    1030      4       650      376
Bulgaria                      975     45       170      760
Djibouti                      945      2       112      831
Ivory Coast                   916     13       303      600
Tunisia                       901     38       170      693
Cyprus                        784     12        98      674
Nigeria                       782     25       197      560
Latvia                        748      9       133      606
Andorra                       717     37       282      398
Diamond Princess              712     13       644       55
Guinea                        688      6       127      555
Lebanon                       677     21       108      548
Costa Rica                    669      6       150      513
Niger                         657     20       127      510
Bolivia                       609     37        44      528
Albania                       609     26       345      238
Burkina Faso                  600     38       362      200
Kyrgyzstan                    590      7       216      367
Uruguay                       543     12       324      207
Honduras                      510     46        30      434
Channel Islands               496     24       256      216
San Marino                    476     40        62      374
Palestine                     466      4        71      391
Malta                         443      3       150      290
Jordan                        428      7       297      124
Taiwan                        425      6       217      202
Senegal                       412      5       242      165
Réunion                       410      -       238        -
Georgia                       408      4        97      307
DRC                           350     25        35      290
Mauritius                     328      9       243       76
Guatemala                     316      8        24      284
Montenegro                    313      5       101      207
Mayotte                       311      4       117      190
Sri Lanka                     310      7       102      201
Isle of Man                   307      9       209       89
Kenya                         296     14        74      208
Venezuela                     288     10       122      156
Somalia                       286      8         4      274
Vietnam                       268      -       216        -
Mali                          258     14        57      187
Tanzania                      254     10        11      233
Jamaica                       233      6        27      200
El Salvador                   225      7        48      170
Paraguay                      213      9        62      142
Faeroe Islands                185      -       178        -
Congo                         165      6        16      143
Martinique                    164     14        73       77
Gabon                         156      1        16      139
Rwanda                        150      -        84        -
Guadeloupe                    148     12        73       63
Sudan                         140     13         8      119
Brunei                        138      1       116       21
Gibraltar                     132      -       120        -
Cambodia                      122      -       110        -
Myanmar                       121      5         7      109
Madagascar                    121      -        44        -
Trinidad and Tobago           115      8        28       79
Ethiopia                      114      3        16       95
Liberia                       101      8         7       86
Bermuda                        98      5        39       54
Aruba                          97      2        51       44
French Guiana                  97      1        83       13
Monaco                         94      3        26       65
Togo                           86      6        56       24
Maldives                       86      -        16        -
Equatorial Guinea              83      -         7        -
Liechtenstein                  81      1        55       25
Barbados                       75      5        25       45
Zambia                         70      3        35       32
Sint Maarten                   68     10        12       46
Cabo Verde                     68      1         1       66
Guyana                         66      7         9       50
Cayman Islands                 66      1         7       58
Bahamas                        65      9        12       44
Uganda                         61      -        38        -
Libya                          59      1        15       43
Haiti                          58      4         2       52
French Polynesia               57      -        35        -
Benin                          54      1        27       26
Guinea-Bissau                  50      -         3        -
Sierra Leone                   50      -         6        -
Macao                          45      -        24        -
Syria                          42      3         6       33
Nepal                          42      -         5        -
Eritrea                        39      -         6        -
Mozambique                     39      -         8        -
Saint Martin                   38      2        19       17
Mongolia                       35      -         8        -
Chad                           33      -         8        -
Eswatini                       31      1         8       22
Zimbabwe                       28      3         2       23
Antigua and Barbuda            24      3         7       14
Angola                         24      2         6       16
Timor-Leste                    23      -         1        -
Botswana                       20      1         -        -
Laos                           19      -         2        -
Belize                         18      2         2       14
Malawi                         18      2         3       13
Fiji                           18      -         8        -
New Caledonia                  18      -        17        -
Dominica                       16      -         9        -
Namibia                        16      -         6        -
Saint Kitts and Nevis          15      -         -        -
Saint Lucia                    15      -        13        -
Curaçao                        14      1        11        2
CAR                            14      -        10        -
Grenada                        14      -         6        -
St. Vincent Grenadines         13      -         3        -
Turks and Caicos               11      1         -        -
Falkland Islands               11      -         3        -
Greenland                      11      -        11        -
Montserrat                     11      -         2        -
Seychelles                     11      -         5        -
Nicaragua                      10      2         7        1
Gambia                         10      1         2        7
Suriname                       10      1         6        3
MS Zaandam                      9      2         -        -
Vatican City                    9      -         2        -
Mauritania                      7      1         6        0
Papua New Guinea                7      -         -        -
Bhutan                          6      -         2        -
St. Barth                       6      -         6        -
Western Sahara                  6      -         -        -
British Virgin Islands          5      1         3        1
Burundi                         5      1         4        0
Caribbean Netherlands           5      -         -        -
Sao Tome and Principe           4      -         -        -
South Sudan                     4      -         -        -
Anguilla                        3      -         1        -
Saint Pierre Miquelon           1      -         -        -
```

Time Series


```python
! wget https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv
! zip /tmp/corona-time.zip time-series-19-covid-combined.csv
! rm time-series-19-covid-combined.csv
```

```python
import pandas as pd, zipfile

with zipfile.ZipFile('/tmp/corona-time.zip', 'r') as z:
    df =  pd.read_csv(z.open('time-series-19-covid-combined.csv'),parse_dates=['Date'])
df = df[['Date','Confirmed']]
df = df.set_index('Date')
confirmed = df.groupby('Date').sum()
print (confirmed.tail(4))
confirmed.plot() # in millions
plt.savefig('timeseries.png')
```

```text
            Confirmed
Date                 
2020-04-20  2472258.0
2020-04-21  2549122.0
2020-04-22  2624089.0
2020-04-23  2708884.0
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
2020-04-19       3.60
2020-04-20       2.96
2020-04-21       3.11
2020-04-22       2.94
2020-04-23       3.23
```

![](rate.png)

County Level Data (NYT)

```python
! wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
! zip /tmp/corona-county.zip us-counties.csv
! rm us-counties.csv
```

Files - [corona.csv](corona.csv), [alpha3country.csv](alpha3country.csv), [util.py](util.py)

[Colors](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)

[Reference](https://www.worldometers.info/coronavirus/)

