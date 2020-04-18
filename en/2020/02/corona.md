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
Total Confirmed 2258516.0

Updated: 2020-04-18 10:53:39.847421
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
21.17 %
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
United States              710272  37175     63510   609587
Spain                      190839  20002     74797    96040
Italy                      172434  22745     42727   106962
France                     147969  18681     34420    94868
Germany                    141397   4352     83114    53931
United Kingdom             108692  14576         -        -
China                       82719   4632     77029     1058
Iran                        79494   4958     54064    20472
Turkey                      78546   1769      8631    68146
Russia                      36793    313      3057    33423
Belgium                     36138   5163      7961    23014
Brazil                      34221   2171     14026    18024
Canada                      31927   1310     10543    20074
Netherlands                 30449   3459       250    26740
Switzerland                 27078   1327     16400     9351
Portugal                    19022    657       519    17846
Austria                     14595    431      9704     4460
India                       14425    488      2045    11892
Ireland                     13980    530        77    13373
Peru                        13489    300      6541     6648
Sweden                      13216   1400       550    11266
Israel                      13107    158      3247     9702
South Korea                 10653    232      7937     2484
Japan                        9787    190       935     8662
Chile                        9252    116      3621     5515
Ecuador                      8450    421       838     7191
Poland                       8379    332       981     7066
Romania                      8067    411      1508     6148
Pakistan                     7481    143      1832     5506
Saudi Arabia                 7142     87      1049     6006
Denmark                      7073    336      3389     3348
Norway                       6992    162        32     6798
Mexico                       6875    546      2125     4204
Australia                    6560     69      4132     2359
Czech Republic               6553    176      1183     5194
United Arab Emirates         6302     37      1188     5077
Singapore                    5992     11       708     5273
Indonesia                    5923    520       607     4796
Philippines                  5878    387       487     5004
Serbia                       5690    110       534     5046
Malaysia                     5251     86      2967     2198
Ukraine                      5106    133       275     4698
Belarus                      4779     42       342     4395
Qatar                        4663      7       464     4192
Panama                       4210    116       122     3972
Dominican Republic           4126    200       268     3658
Finland                      3489     82      1700     1707
Luxembourg                   3480     72       579     2829
Colombia                     3439    153       634     2652
Egypt                        2844    205       646     1993
South Africa                 2783     50       903     1830
Argentina                    2758    129       666     1963
Thailand                     2733     47      1787      899
Morocco                      2564    135       281     2148
Algeria                      2418    364       846     1208
Moldova                      2264     56       276     1932
Greece                       2224    108       269     1847
Bangladesh                   1838     75        58     1705
Hungary                      1834    172       231     1431
Croatia                      1814     36       600     1178
Iceland                      1754      9      1224      521
Bahrain                      1740      7       725     1008
Kuwait                       1658      5       258     1395
Kazakhstan                   1591     17       347     1227
Iraq                         1482     81       906      495
Estonia                      1459     38       145     1276
Uzbekistan                   1450      4       156     1290
New Zealand                  1422     11       867      544
Azerbaijan                   1340     15       528      797
Slovenia                     1304     66       174     1064
Armenia                      1248     20       523      705
Lithuania                    1239     33       228      978
Bosnia and Herzegovina       1214     46       320      848
Oman                         1180      6       176      998
North Macedonia              1117     49       139      929
Slovakia                     1049      9       175      865
Hong Kong                    1022      4       533      485
Cameroon                     1017     22       177      818
Afghanistan                   933     30       112      791
Cuba                          923     31       192      700
Bulgaria                      865     41       153      671
Tunisia                       864     37        43      784
Cyprus                        750     12        77      661
Djibouti                      732      2        76      654
Diamond Princess              712     13       644       55
Latvia                        712      5        88      619
Andorra                       696     35       191      470
Ivory Coast                   688      6       193      489
Lebanon                       668     21        94      553
Costa Rica                    649      4        88      557
Ghana                         641      8        83      550
Niger                         627     18       110      499
Burkina Faso                  557     35       294      228
Albania                       539     26       283      230
Uruguay                       508      9       294      205
Kyrgyzstan                    506      5       130      371
Bolivia                       493     31        31      431
Nigeria                       493     17       159      317
Guinea                        477      3        59      415
Channel Islands               470     20        73      377
Honduras                      457     46        10      401
San Marino                    435     39        57      339
Malta                         422      3        91      328
Jordan                        407      7       265      135
Palestine                     402      2        69      331
Réunion                       402      -       237        -
Taiwan                        398      6       178      214
Georgia                       385      3        84      298
Senegal                       342      2       198      142
Mauritius                     324      9       108      207
Montenegro                    305      5        55      245
Isle of Man                   291      4       169      118
DRC                           287     23        25      239
Vietnam                       268      -       201        -
Kenya                         246     11        53      182
Mayotte                       245      4       117      124
Sri Lanka                     244      7        77      160
Guatemala                     235      7        21      207
Venezuela                     227      9       113      105
Paraguay                      202      8        35      159
El Salvador                   190      7        43      140
Faeroe Islands                184      -       173        -
Mali                          171     13        34      124
Jamaica                       163      5        25      133
Martinique                    158      8        73       77
Tanzania                      147      5        11      131
Guadeloupe                    145      8        67       70
Congo                         143      6        11      126
Rwanda                        143      -        65        -
Brunei                        136      1       112       23
Gibraltar                     132      -       105        -
Cambodia                      122      -       103        -
Madagascar                    117      -        33        -
Somalia                       116      6         2      108
Trinidad and Tobago           114      8        20       86
Gabon                         108      1         7      100
Ethiopia                       96      3        15       78
Aruba                          96      2        43       51
French Guiana                  96      -        61        -
Myanmar                        94      5         5       84
Monaco                         94      3        20       71
Bermuda                        83      5        35       43
Togo                           83      5        48       30
Liechtenstein                  79      1        55       23
Equatorial Guinea              79      -         4        -
Liberia                        76      7         7       62
Barbados                       75      5        15       55
Sudan                          66     10         6       50
Guyana                         63      6         9       48
Cayman Islands                 61      1         7       53
Sint Maarten                   57      9        12       36
Cabo Verde                     56      1         1       54
French Polynesia               55      -         2        -
Uganda                         55      -        20        -
Bahamas                        54      9         9       36
Zambia                         52      2        30       20
Libya                          49      1        11       37
Macao                          45      -        16        -
Haiti                          43      3         -        -
Guinea-Bissau                  43      -         -        -
Syria                          38      2         5       31
Saint Martin                   35      2        13       20
Benin                          35      1        18       16
Eritrea                        35      -         -        -
Mozambique                     34      -         2        -
Mongolia                       31      -         5        -
Nepal                          30      -         2        -
Maldives                       29      -        16        -
Chad                           27      -         5        -
Sierra Leone                   26      -         -        -
Zimbabwe                       24      3         2       19
Antigua and Barbuda            23      3         3       17
Angola                         19      2         5       12
Eswatini                       19      1         8       10
Laos                           19      -         2        -
Belize                         18      2         -        -
New Caledonia                  18      -        14        -
Timor-Leste                    18      -         1        -
Malawi                         17      2         3       12
Fiji                           17      -         -        -
Dominica                       16      -         8        -
Namibia                        16      -         4        -
Botswana                       15      1         -        -
Saint Lucia                    15      -        11        -
Curaçao                        14      1        10        3
Grenada                        14      -         6        -
Saint Kitts and Nevis          14      -         -        -
CAR                            12      -         4        -
St. Vincent Grenadines         12      -         1        -
Turks and Caicos               11      1         -        -
Falkland Islands               11      -         3        -
Greenland                      11      -        11        -
Montserrat                     11      -         1        -
Seychelles                     11      -         5        -
Suriname                       10      1         6        3
MS Zaandam                      9      2         -        -
Gambia                          9      1         2        6
Nicaragua                       9      1         6        2
Vatican City                    8      -         2        -
Mauritania                      7      1         2        4
Papua New Guinea                7      -         -        -
St. Barth                       6      -         5        -
Western Sahara                  6      -         -        -
Burundi                         5      1         -        -
Bhutan                          5      -         2        -
British Virgin Islands          4      -         2        -
Sao Tome and Principe           4      -         -        -
South Sudan                     4      -         -        -
Anguilla                        3      -         1        -
Caribbean Netherlands           3      -         -        -
Saint Pierre Miquelon           1      -         -        -
Yemen                           1      -         -        -
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
2020-04-14    1976191
2020-04-15    2056054
2020-04-16    2152646
2020-04-17    2240190
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
2020-04-13       3.82
2020-04-14       3.75
2020-04-15       4.04
2020-04-16       4.70
2020-04-17       4.07
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

