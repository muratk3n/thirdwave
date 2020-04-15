# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 50, 100, 200, 1000, 2000, 10000, 100000, 800000, 1200000]
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
Total Confirmed 2013998.0

Updated: 2020-04-15 13:16:56.100571
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
20.61 %
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
United States              614246  26064     38820   549362
Spain                      177633  18579     70853    88201
Italy                      162488  21067     37130   104291
France                     143303  15729     28805    98769
Germany                    132210   3495     72600    56115
United Kingdom              93873  12107         -        -
China                       82295   3342     77816     1137
Iran                        76389   4777     49933    21679
Turkey                      65111   1403      4799    58909
Belgium                     33573   4440      7107    22026
Netherlands                 27419   2945       250    24224
Canada                      27063    903      8235    17925
Switzerland                 26023   1190     14700    10133
Brazil                      25684   1552     14026    10106
Russia                      24490    198      1986    22306
Portugal                    17448    567       347    16534
Austria                     14280    393      8098     5789
Israel                      12200    126      2309     9765
India                       11555    396      1362     9797
Ireland                     11479    406        77    10996
Sweden                      11445   1033       381    10031
South Korea                 10591    225      7616     2750
Peru                        10303    230      2869     7204
Japan                        8100    146       853     7101
Chile                        7917     92      2646     5179
Ecuador                      7603    369       696     6538
Poland                       7408    268       668     6472
Romania                      7216    362      1217     5637
Norway                       6686    142        32     6512
Denmark                      6681    299      2515     3867
Australia                    6447     63      3686     2698
Czech Republic               6151    163       676     5312
Pakistan                     5988    107      1446     4435
Philippines                  5453    349       353     4751
Mexico                       5399    406      2125     2868
Saudi Arabia                 5369     73       889     4407
Indonesia                    5136    469       446     4221
Malaysia                     5072     83      2647     2342
United Arab Emirates         4933     28       933     3972
Serbia                       4465     94       400     3971
Ukraine                      3764    108       143     3513
Panama                       3574     95        72     3407
Qatar                        3428      7       373     3048
Luxembourg                   3307     67       500     2740
Dominican Republic           3286    183       162     2941
Belarus                      3281     33       203     3045
Singapore                    3252     10       611     2631
Finland                      3237     64       300     2873
Colombia                     2979    127       354     2498
Thailand                     2643     43      1497     1103
Argentina                    2443    105       559     1779
South Africa                 2415     27       410     1978
Egypt                        2350    178       589     1583
Greece                       2170    101       269     1800
Algeria                      2070    326       691     1053
Morocco                      1988    127       218     1643
Moldova                      1934     41       171     1722
Iceland                      1720      8       989      723
Croatia                      1704     31       415     1258
Hungary                      1579    134       192     1253
Bahrain                      1528      7       648      873
Kuwait                       1405      3       206     1196
Iraq                         1400     78       766      556
Estonia                      1400     35       117     1248
New Zealand                  1386      9       728      649
Kazakhstan                   1275     15       220     1040
Slovenia                     1248     61       165     1022
Bangladesh                   1231     50        49     1132
Uzbekistan                   1214      4        99     1111
Azerbaijan                   1197     13       351      833
Armenia                      1111     17       297      797
Lithuania                    1091     29       138      924
Bosnia and Herzegovina       1083     40       236      807
Hong Kong                    1017      4       459      554
Oman                          910      4       131      775
North Macedonia               908     44        86      778
Slovakia                      863      2       113      748
Cameroon                      848     14       130      704
Afghanistan                   784     25        43      716
Cuba                          766     21       132      613
Tunisia                       747     34        43      670
Bulgaria                      735     36       105      594
Diamond Princess              712     12       639       61
Cyprus                        695     12        65      618
Latvia                        666      5        16      645
Andorra                       659     31       128      500
Lebanon                       658     21        81      556
Ivory Coast                   638      6       114      518
Ghana                         636      8        17      611
Costa Rica                    618      3        66      549
Niger                         570     14        90      466
Burkina Faso                  528     30       177      321
Albania                       494     25       251      218
Uruguay                       492      8       260      224
Kyrgyzstan                    449      5        78      366
Channel Islands               440     13        48      379
Honduras                      419     31         9      379
Bolivia                       397     28         7      362
Jordan                        397      7       235      155
Taiwan                        395      6       137      252
Malta                         393      3        44      346
Réunion                       391      -        40        -
Nigeria                       373     11        99      263
San Marino                    372     36        53      283
Djibouti                      363      2        53      308
Guinea                        363      -        31        -
Mauritius                     324      9        51      264
Palestine                     308      2        62      244
Georgia                       306      3        69      234
Senegal                       299      2       183      114
Montenegro                    288      4        46      238
Vietnam                       267      -       171        -
Isle of Man                   254      2       141      111
DRC                           241     20        20      201
Sri Lanka                     233      7        63      163
Mayotte                       217      3        69      145
Kenya                         216      9        41      166
Venezuela                     197      9       111       77
Faeroe Islands                184      -       166        -
Guatemala                     180      5        19      156
Paraguay                      161      8        23      130
El Salvador                   159      6        30      123
Martinique                    158      8        73       77
Guadeloupe                    145      8        67       70
Mali                          144     13        34       97
Brunei                        136      1       107       28
Rwanda                        134      -        49        -
Gibraltar                     129      -        93        -
Cambodia                      122      -        96        -
Trinidad and Tobago           113      8        17       88
Madagascar                    108      -        23        -
Jamaica                       105      5        21       79
Monaco                         93      1         6       86
Aruba                          92      -        32        -
French Guiana                  86      -        51        -
Ethiopia                       85      3        15       67
Gabon                          80      1         4       75
Liechtenstein                  79      1        55       23
Togo                           77      3        32       42
Congo                          74      5        10       59
Myanmar                        74      4         2       68
Barbados                       73      5        15       53
Somalia                        60      2         2       56
Liberia                        59      6         4       49
Tanzania                       59      3         7       49
Bermuda                        57      5        30       22
French Polynesia               55      -         -        -
Uganda                         55      -         8        -
Cayman Islands                 54      1         6       47
Sint Maarten                   52      9         5       38
Bahamas                        49      8         6       35
Guyana                         47      6         8       33
Zambia                         45      2        30       13
Macao                          45      -        10        -
Guinea-Bissau                  43      -         -        -
Equatorial Guinea              41      -         4        -
Haiti                          40      3         -        -
Benin                          35      1        18       16
Libya                          35      1         9       25
Eritrea                        35      -         -        -
Sudan                          32      5         4       23
Saint Martin                   32      2        11       19
Mongolia                       30      -         5        -
Syria                          29      2         5       22
Mozambique                     28      -         2        -
Antigua and Barbuda            23      2         3       18
Chad                           23      -         2        -
Maldives                       21      -        16        -
Angola                         19      2         5       12
Laos                           19      -         1        -
Zimbabwe                       18      3         1       14
Belize                         18      2         -        -
New Caledonia                  18      -         1        -
Malawi                         16      2         -        -
Nepal                          16      -         1        -
Dominica                       16      -         8        -
Fiji                           16      -         -        -
Namibia                        16      -         3        -
Saint Lucia                    15      -        11        -
Eswatini                       15      -         8        -
Curaçao                        14      1        10        3
Grenada                        14      -         -        -
Saint Kitts and Nevis          14      -         -        -
Botswana                       13      1         -        -
St. Vincent Grenadines         12      -         1        -
Cabo Verde                     11      1         1        9
CAR                            11      -         4        -
Falkland Islands               11      -         1        -
Greenland                      11      -        11        -
Montserrat                     11      -         1        -
Seychelles                     11      -         -        -
Sierra Leone                   11      -         -        -
Suriname                       10      1         6        3
Turks and Caicos               10      1         -        -
MS Zaandam                      9      2         -        -
Gambia                          9      1         2        6
Nicaragua                       9      1         4        4
Vatican City                    8      -         2        -
Timor-Leste                     8      -         1        -
Mauritania                      7      1         2        4
St. Barth                       6      -         4        -
Western Sahara                  6      -         -        -
Burundi                         5      1         -        -
Bhutan                          5      -         2        -
Sao Tome and Principe           4      -         -        -
South Sudan                     4      -         -        -
Anguilla                        3      -         1        -
British Virgin Islands          3      -         2        -
Caribbean Netherlands           3      -         -        -
Papua New Guinea                2      -         -        -
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
2020-04-11    1771514
2020-04-12    1846679
2020-04-13    1917319
2020-04-14    1976191
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
2020-04-10       6.04
2020-04-11       4.72
2020-04-12       4.24
2020-04-13       3.83
2020-04-14       3.07
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

