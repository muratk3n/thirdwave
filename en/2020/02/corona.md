# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 50, 100, 200, 1000, 2000, 10000, 100000, 800000, 1200000]
colors = ["lightsalmon","salmon","lightcoral", "tomato","red",\
	  "indianred","firebrick","maroon","dimgray"]
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
Total Confirmed 3099990.0

Updated: 2020-04-28 20:09:19.436478
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
18.47 %
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
United States             1017155  57203    139927   820025
Spain                      232128  23822    123903    84403
Italy                      201505  27359     68941   105205
France                     165842  23293     45513    97036
Germany                    159137   6174    117400    35563
United Kingdom             157149  21092         -        -
Turkey                     114653   2992     38809    72852
Russia                      93558    867      8456    84235
Iran                        92584   5877     72439    14268
China                       82836   4633     77555      648
Brazil                      68188   4674     31142    32372
Canada                      49025   2766     18268    27991
Belgium                     47334   7331     10943    29060
Netherlands                 38416   4566         -        -
India                       29451    939      7137    21375
Switzerland                 29264   1699     22200     5365
Peru                        28699    782      8425    19492
Portugal                    24322    948      1389    21985
Ecuador                     23240    663      1557    21020
Saudi Arabia                20077    152      2784    17141
Ireland                     19648   1102      9233     9313
Sweden                      19621   2355      1005    16261
Israel                      15589    208      7375     8006
Mexico                      15529   1434      9086     5009
Austria                     15357    569     12580     2208
Singapore                   14951     14      1128    13809
Pakistan                    14514    312      3233    10969
Chile                       14365    207      7710     6448
Japan                       13614    385      1899    11330
Poland                      12218    596      2655     8967
Belarus                     12208     79      1993    10136
Qatar                       11921     10      1134    10777
Romania                     11616    663      3404     7549
United Arab Emirates        11380     89      2181     9110
South Korea                 10752    244      8854     1654
Indonesia                    9511    773      1254     7484
Ukraine                      9410    239       992     8179
Denmark                      8851    434      6121     2296
Serbia                       8497    168      1260     7069
Philippines                  7958    530       975     6453
Norway                       7619    206        32     7381
Czech Republic               7486    225      2942     4319
Australia                    6731     84      5626     1021
Bangladesh                   6462    155       139     6168
Dominican Republic           6416    286      1165     4965
Panama                       6021    167       455     5399
Malaysia                     5851    100      4032     1719
Colombia                     5597    253      1210     4134
Egypt                        5042    359      1304     3379
South Africa                 4793     90      1473     3230
Finland                      4740    199      2800     1741
Morocco                      4252    165       778     3309
Argentina                    4003    197      1140     2666
Luxembourg                   3741     89      3123      529
Algeria                      3649    437      1651     1561
Moldova                      3638    103       975     2560
Kuwait                       3440     23      1176     2241
Kazakhstan                   3019     25       754     2240
Thailand                     2938     54      2652      232
Bahrain                      2810      8      1246     1556
Hungary                      2649    291       516     1842
Greece                       2566    138       577     1851
Oman                         2131     10       364     1757
Croatia                      2047     63      1232      752
Uzbekistan                   1939      8       958      973
Iraq                         1928     90      1319      519
Armenia                      1867     30       866      971
Afghanistan                  1828     58       228     1542
Iceland                      1795     10      1624      161
Azerbaijan                   1717     22      1221      474
Cameroon                     1705     58       805      842
Estonia                      1660     50       240     1370
Bosnia and Herzegovina       1585     63       682      840
Ghana                        1550     11       155     1384
New Zealand                  1472     19      1214      239
Cuba                         1437     58       575      804
North Macedonia              1421     71       589      761
Slovenia                     1408     86       223     1099
Bulgaria                     1399     58       222     1119
Slovakia                     1384     20       423      941
Lithuania                    1344     44       536      764
Nigeria                      1337     40       255     1042
Ivory Coast                  1164     14       499      651
Guinea                       1163      7       246      910
Hong Kong                    1038      4       811      223
Djibouti                     1035      2       477      556
Bolivia                      1014     53        98      863
Tunisia                       967     39       279      649
Cyprus                        837     15       148      674
Latvia                        836     13       267      556
Senegal                       823      9       296      518
Albania                       750     30       431      289
Andorra                       743     40       385      318
Lebanon                       717     24       145      548
Diamond Princess              712     13       645       54
Kyrgyzstan                    708      8       416      284
Honduras                      702     64        79      559
Niger                         701     29       385      287
Costa Rica                    697      6       287      404
Burkina Faso                  635     42       469      124
Uruguay                       620     15       386      219
Sri Lanka                     611      7       134      470
San Marino                    538     41        64      433
Channel Islands               530     36       352      142
Guatemala                     530     15        49      466
Somalia                       528     28        19      481
Georgia                       511      6       156      349
DRC                           471     30        56      385
Mayotte                       460      4       235      221
Malta                         458      4       303      151
Jordan                        449      8       348       93
Taiwan                        429      6       307      116
Mali                          424     24       122      278
Réunion                       418      -       300        -
Kenya                         374     14       124      236
Jamaica                       364      7        29      328
El Salvador                   345      8        97      240
Palestine                     342      2        83      257
Mauritius                     334     10       303       21
Venezuela                     329     10       142      177
Montenegro                    321      7       199      115
Sudan                         318     25        31      262
Isle of Man                   308     20       248       40
Tanzania                      299     10        48      241
Vietnam                       270      -       225        -
Equatorial Guinea             258      1         9      248
Maldives                      245      -        17        -
Paraguay                      230      9        95      126
Gabon                         211      3        43      165
Congo                         207      8        19      180
Rwanda                        207      -        93        -
Faeroe Islands                187      -       181        -
Martinique                    175     14        77       84
Guadeloupe                    149     12        82       55
Myanmar                       149      5        16      128
Liberia                       141     16        45       80
Gibraltar                     141      -       131        -
Brunei                        138      1       124       13
Madagascar                    128      -        82        -
Ethiopia                      126      3        50       73
French Guiana                 124      1        91       32
Cambodia                      122      -       119        -
Trinidad and Tobago           116      8        59       49
Cabo Verde                    114      1         2      111
Bermuda                       110      6        44       60
Sierra Leone                  104      4        12       88
Aruba                         100      2        73       25
Togo                           99      6        62       31
Monaco                         95      4        42       49
Zambia                         95      3        42       50
Liechtenstein                  82      1        55       26
Bahamas                        80     11        22       47
Barbados                       80      6        39       35
Uganda                         79      -        52        -
Haiti                          76      6         8       62
Mozambique                     76      -        12        -
Sint Maarten                   75     13        33       29
Guyana                         74      8        15       51
Guinea-Bissau                  73      1        18       54
Eswatini                       71      1        10       60
Cayman Islands                 70      1        10       59
Benin                          64      1        33       30
Libya                          61      2        18       41
French Polynesia               58      -        49        -
Nepal                          54      -        16        -
CAR                            50      -        10        -
Chad                           46      -        15        -
Macao                          45      -        32        -
Syria                          43      3        19       21
Eritrea                        39      -        13        -
Saint Martin                   38      3        24       11
Mongolia                       38      -        10        -
Malawi                         36      3         4       29
Zimbabwe                       32      4         5       23
Angola                         27      2         6       19
Antigua and Barbuda            24      3        11       10
Timor-Leste                    24      -         6        -
Botswana                       22      1         -        -
Laos                           19      -         7        -
Belize                         18      2         6       10
Fiji                           18      -        12        -
Grenada                        18      -         7        -
New Caledonia                  18      -        17        -
Curaçao                        16      1        11        4
Dominica                       16      -        13        -
Namibia                        16      -         8        -
Saint Kitts and Nevis          15      -         4        -
Saint Lucia                    15      -        15        -
St. Vincent Grenadines         15      -         8        -
Nicaragua                      13      3         7        3
Falkland Islands               13      -        11        -
Turks and Caicos               12      1         5        6
Burundi                        11      1         4        6
Montserrat                     11      1         2        8
Greenland                      11      -        11        -
Seychelles                     11      -         6        -
Gambia                         10      1         8        1
Suriname                       10      1         7        2
Vatican City                   10      -         2        -
MS Zaandam                      9      2         -        -
Papua New Guinea                8      -         -        -
Sao Tome and Principe           8      -         4        -
Mauritania                      7      1         6        0
Bhutan                          7      -         5        -
British Virgin Islands          6      1         3        2
St. Barth                       6      -         6        -
South Sudan                     6      -         -        -
Western Sahara                  6      -         5        -
Caribbean Netherlands           5      -         -        -
Anguilla                        3      -         3        -
Saint Pierre Miquelon           1      -         -        -
Yemen                           1      -         1        -
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
2020-04-24    2811603
2020-04-25    2897624
2020-04-26    2972363
2020-04-27    3041764
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
2020-04-23       3.19
2020-04-24       3.84
2020-04-25       3.06
2020-04-26       2.58
2020-04-27       2.33
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

