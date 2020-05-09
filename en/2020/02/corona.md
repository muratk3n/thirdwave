# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 100, 200, 1000, 2000, 10000, 100000, 800000, 1200000]
colors = ["lightsalmon","lightcoral", "tomato","red",\
	  "indianred","firebrick","maroon","dimgray"]
df, col_dict = util.retrieve_cor_data(bins,colors)
df = df.sort_values(by='Confirmed',ascending=False)
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
Total Confirmed 3834038.0

Updated: 2020-05-07 11:25:00.127330
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
16.88 %
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
United States             1263224  74809    213109   975306
Spain                      253682  25857    159359    68466
Italy                      214457  29684     93245    91528
United Kingdom             201101  30076         -        -
Russia                     177160   1625     23803   151732
France                     174191  25809     53972    94410
Germany                    168162   7275    139900    20987
Turkey                     131744   3584     78202    49958
Brazil                     126611   8588     51370    66653
Iran                       101650   6418     81587    13645
China                       82885   4633     77957      295
Canada                      63496   4232     28171    31093
Peru                        54817   1533     17527    35757
India                       53045   1787     15331    35927
Belgium                     50781   8339     12731    29711
Netherlands                 41319   5204         -        -
Saudi Arabia                31938    209      6783    24946
Switzerland                 30060   1805     25700     2555
Ecuador                     29420   1618      3433    24369
Mexico                      27634   2704     17781     7149
Portugal                    26182   1089      2076    23017
Pakistan                    24073    564      6464    17045
Sweden                      23918   2941      4074    16903
Chile                       23048    281     11189    11578
Ireland                     22248   1375     17110     3763
Singapore                   20939     20      1634    19285
Belarus                     19255    112      4388    14755
Qatar                       17972     12      2070    15890
Israel                      16310    239     10637     5434
United Arab Emirates        15738    157      3359    12222
Austria                     15684    608     13639     1437
Japan                       15253    556      4496    10201
Poland                      14740    733      4862     9145
Romania                     14107    868      5788     7451
Ukraine                     13691    340      2396    10955
Indonesia                   12438    895      2317     9226
Bangladesh                  11719    186      1403    10130
South Korea                 10810    256      9419     1135
Philippines                 10343    685      1618     8040
Denmark                     10083    506      7493     2084
Serbia                       9791    203      1971     7617
Colombia                     8959    397      2148     6414
Dominican Republic           8807    362      1960     6485
Norway                       7996    216        32     7748
Czech Republic               7979    263      4214     3502
South Africa                 7808    153      3153     4502
Panama                       7731    218       859     6654
Egypt                        7588    469      1815     5304
Australia                    6894     97      6040      757
Malaysia                     6428    107      4702     1619
Kuwait                       6289     42      2219     4028
Finland                      5573    252      3500     1821
Morocco                      5408    183      2017     3208
Argentina                    5208    273      1524     3411
Algeria                      4997    476      2197     2324
Kazakhstan                   4502     30      1408     3064
Moldova                      4476    143      1658     2675
Bahrain                      3934      8      1860     2066
Luxembourg                   3851     98      3452      301
Afghanistan                  3392    104       458     2830
Hungary                      3150    383       801     1966
Nigeria                      3145    103       534     2508
Ghana                        3091     18       303     2770
Thailand                     2992     55      2772      165
Oman                         2958     13       980     1965
Armenia                      2782     40      1135     1607
Greece                       2663    147      1374     1142
Iraq                         2480    102      1602      776
Uzbekistan                   2266     10      1577      679
Cameroon                     2265    108      1000     1157
Azerbaijan                   2127     28      1536      563
Croatia                      2119     85      1601      433
Bosnia and Herzegovina       1987     86       928      973
Bolivia                      1886     91       198     1597
Guinea                       1856     11       597     1248
Bulgaria                     1811     84       384     1343
Iceland                      1799     10      1750       39
Estonia                      1720     56       273     1391
Cuba                         1703     69      1001      633
North Macedonia              1539     88      1057      394
Ivory Coast                  1516     18       721      777
New Zealand                  1489     21      1332      136
Honduras                     1461     99       132     1230
Slovenia                     1448     99       246     1103
Slovakia                     1445     26       806      613
Lithuania                    1433     49       739      645
Senegal                      1433     12       493      928
Djibouti                     1124      3       755      366
Hong Kong                    1041      4       932      105
Tunisia                      1025     43       591      391
Latvia                        909     18       464      427
Kyrgyzstan                    895     12       637      246
Cyprus                        883     15       296      572
Somalia                       873     39        87      747
DRC                           863     36       103      724
Sudan                         852     49        80      723
Albania                       832     31       595      206
Guatemala                     798     21        86      691
Sri Lanka                     797      9       232      556
Niger                         770     38       561      171
Costa Rica                    761      6       428      327
Andorra                       751     46       521      184
Lebanon                       750     25       213      512
Mayotte                       739      9       352      378
Burkina Faso                  729     48       555      126
Diamond Princess              712     13       645       54
El Salvador                   695     15       245      435
Uruguay                       673     17       486      170
Mali                          631     32       261      338
Maldives                      617      2        20      595
Georgia                       615      9       275      331
San Marino                    608     41        97      470
Kenya                         582     26       190      366
Channel Islands               545     40       406       99
Malta                         484      5       407       72
Tanzania                      480     16       167      297
Jamaica                       478      9        57      412
Guinea-Bissau                 475      2        24      449
Jordan                        473      9       377       87
Paraguay                      440     10       142      288
Taiwan                        440      6       347       87
Equatorial Guinea             439      4        13      422
Gabon                         439      8        99      332
Réunion                       425      -       300        -
Venezuela                     379     10       176      193
Tajikistan                    379      8         -        -
Palestine                     374      2       174      198
Mauritius                     332     10       320        2
Isle of Man                   327     23       271       33
Montenegro                    324      8       265       51
Vietnam                       271      -       232        -
Rwanda                        268      -       130        -
Congo                         264     10        30      224
Sierra Leone                  225     14        54      157
Cabo Verde                    191      2        38      151
Faeroe Islands                187      -       185        -
Martinique                    182     14        83       85
Liberia                       178     20        75       83
Sao Tome and Principe         174      3         4      167
Chad                          170     17        43      110
Myanmar                       162      6        50      106
Ethiopia                      162      4        93       65
Madagascar                    158      -       101        -
Guadeloupe                    152     13       104       35
Zambia                        146      4       101       41
Gibraltar                     144      -       136        -
Brunei                        139      1       131        7
French Guiana                 138      1       112       25
Togo                          128      9        77       42
Eswatini                      123      2        12      109
Cambodia                      122      -       120        -
Bermuda                       118      7        59       52
Trinidad and Tobago           116      8       103        5
Haiti                         101     12        10       79
Aruba                         101      2        89       10
Uganda                        100      -        55        -
Nepal                          99      -        22        -
Benin                          96      2        50       44
Monaco                         95      4        82        9
CAR                            94      -        10        -
Guyana                         93     10        27       56
Bahamas                        92     11        26       55
Barbados                       82      7        47       28
Liechtenstein                  82      1        55       26
Mozambique                     81      -        21        -
Cayman Islands                 78      1        30       47
Sint Maarten                   76     14        44       18
Libya                          64      3        24       37
French Polynesia               60      -        55        -
South Sudan                    58      -         -        -
Syria                          45      3        27       15
Macao                          45      -        39        -
Malawi                         43      3         9       31
Mongolia                       41      -        13        -
Eritrea                        39      -        30        -
Saint Martin                   38      3        29        6
Angola                         36      2        11       23
Zimbabwe                       34      4         5       25
Yemen                          25      5         1       19
Antigua and Barbuda            25      3        16        6
Timor-Leste                    24      -        20        -
Botswana                       23      1         8       14
Grenada                        21      -        13        -
Laos                           19      -        10        -
Belize                         18      2        16        0
Fiji                           18      -        14        -
New Caledonia                  18      -        18        -
Saint Lucia                    18      -        15        -
St. Vincent Grenadines         17      -         9        -
Gambia                         17      1         9        7
Nicaragua                      16      5         7        4
Curaçao                        16      1        13        2
Dominica                       16      -        14        -
Namibia                        16      -         8        -
Burundi                        15      1         7        7
Saint Kitts and Nevis          15      -        12        -
Falkland Islands               13      -        13        -
Turks and Caicos               12      1         6        5
Vatican City                   12      -         2        -
Montserrat                     11      1         7        3
Greenland                      11      -        11        -
Seychelles                     11      -         8        -
Suriname                       10      1         9        0
MS Zaandam                      9      2         -        -
Comoros                         8      1         -        -
Mauritania                      8      1         6        1
Papua New Guinea                8      -         8        -
British Virgin Islands          7      1         3        3
Bhutan                          7      -         5        -
Caribbean Netherlands           6      -         -        -
St. Barth                       6      -         6        -
Western Sahara                  6      -         5        -
Anguilla                        3      -         3        -
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
2020-05-03  3506729.0
2020-05-04  3583055.0
2020-05-05  3662691.0
2020-05-06  3755341.0
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
2020-05-02       2.50
2020-05-03       2.32
2020-05-04       2.18
2020-05-05       2.22
2020-05-06       2.53
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

[Reference](https://www.worldometers.info/coronavirush/)

