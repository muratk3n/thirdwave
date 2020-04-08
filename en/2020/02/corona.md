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
Total Confirmed 1491685.0

Updated: 2020-04-08 21:24:25.211737
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( 'Symp. Death Rate =', np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
Symp. Death Rate = 21.51 %
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
United States              418410  14240     22184   381986
Spain                      146690  14673     48021    83996
Italy                      139422  17669     26491    95262
France                     112950  10869     21254    80827
Germany                    110698   2192     36081    72425
China                       81802   3333     77279     1190
Iran                        64586   3993     29812    30781
United Kingdom              60733   7097       135    53501
Turkey                      38226    812      1846    35568
Belgium                     23403   2240      4681    16482
Switzerland                 23248    895      9800    12553
Netherlands                 20549   2248       250    18051
Canada                      19179    427      4474    14278
Brazil                      14347    719       127    13501
Portugal                    13141    380       196    12565
Austria                     12930    273      4512     8145
South Korea                 10384    200      6776     3408
Israel                       9404     72       801     8531
Russia                       8672     63       580     8029
Sweden                       8419    687       205     7527
Norway                       6086    101        32     5953
Ireland                      6074    235        25     5814
Australia                    6013     50      2813     3150
India                        5749    178       506     5065
Chile                        5546     48      1115     4383
Denmark                      5402    218      1621     3563
Czech Republic               5221     99       233     4889
Poland                       5205    159       222     4824
Romania                      4761    215       528     4018
Japan                        4257     93       622     3542
Pakistan                     4196     60       467     3669
Malaysia                     4119     65      1487     2567
Ecuador                      3995    220       140     3635
Philippines                  3870    182        96     3592
Saudi Arabia                 3122     41       631     2450
Luxembourg                   3034     46       500     2488
Indonesia                    2956    240       222     2494
Peru                         2954    107      1301     1546
Mexico                       2785    141       633     2011
Serbia                       2666     65       118     2483
United Arab Emirates         2659     12       239     2408
Finland                      2487     40       300     2147
Thailand                     2369     30       888     1451
Panama                       2249     59        16     2174
Qatar                        2210      6       178     2026
Dominican Republic           2111    108        50     1953
Greece                       1884     83       269     1532
Colombia                     1780     50       100     1630
South Africa                 1749     13        95     1641
Argentina                    1715     63       338     1314
Ukraine                      1668     52        35     1581
Singapore                    1623      6       406     1211
Iceland                      1616      6       633      977
Algeria                      1572    205       237     1130
Egypt                        1560    103       305     1152
Croatia                      1343     19       179     1145
Morocco                      1275     93        97     1085
New Zealand                  1210      1       282      927
Iraq                         1202     69       452      681
Estonia                      1185     24        72     1089
Moldova                      1174     27        40     1107
Slovenia                     1091     40       120      931
Belarus                      1066     13        77      976
Hong Kong                     961      4       264      693
Lithuania                     912     15         8      889
Hungary                       895     58        94      743
Armenia                       881      9       114      758
Kuwait                        855      1       111      743
Bahrain                       823      5       477      341
Azerbaijan                    822      8        63      751
Bosnia and Herzegovina        803     34        79      690
Kazakhstan                    718      7        54      657
Diamond Princess              712     11       619       82
Cameroon                      685      9        60      616
Slovakia                      682      2        16      664
Tunisia                       623     23        25      575
North Macedonia               617     29        35      553
Bulgaria                      593     24        42      527
Latvia                        577      2        16      559
Lebanon                       575     19        62      494
Andorra                       564     23        52      489
Uzbekistan                    545      3        30      512
Cyprus                        526      9        52      465
Costa Rica                    483      2        24      457
Cuba                          457     12        27      418
Afghanistan                   444     14        29      401
Uruguay                       424      7       150      267
Oman                          419      2        72      345
Albania                       400     22       154      224
Burkina Faso                  384     19       127      238
Taiwan                        379      5        67      307
Jordan                        358      6       150      202
Réunion                       358      -        40        -
Channel Islands               351      8        38      305
Ivory Coast                   349      3        41      305
Ghana                         313      6        34      273
Honduras                      312     22         6      284
Malta                         299      1         5      293
San Marino                    279     34        40      205
Niger                         278     11        26      241
Mauritius                     273      7        19      247
Kyrgyzstan                    270      4        33      233
Palestine                     263      1        44      218
Nigeria                       254      6        44      204
Vietnam                       251      -       126        -
Montenegro                    248      2         4      242
Senegal                       244      2       113      129
Bangladesh                    218     20        33      165
Bolivia                       210     15         2      193
Georgia                       208      3        50      155
Sri Lanka                     189      7        44      138
Faeroe Islands                184      -       131        -
DRC                           180     18         9      153
Kenya                         179      6         9      164
Mayotte                       171      2        22      147
Venezuela                     166      7        65       94
Isle of Man                   158      1        82       75
Martinique                    152      4        50       98
Guinea                        144      -         5        -
Guadeloupe                    139      7        31      101
Brunei                        135      1        91       43
Djibouti                      135      -        25        -
Gibraltar                     120      -        60        -
Paraguay                      119      5        15       99
Cambodia                      117      -        63        -
Rwanda                        110      -         7        -
Trinidad and Tobago           107      8         1       98
El Salvador                    93      5         9       79
Madagascar                     93      -        11        -
Guatemala                      87      3        17       67
Monaco                         81      1         4       76
Liechtenstein                  78      1        55       22
French Guiana                  77      -        34        -
Aruba                          74      -        14        -
Togo                           70      3        23       44
Barbados                       63      3         6       54
Jamaica                        63      3        10       50
Mali                           59      7        16       36
Ethiopia                       55      2         4       49
Uganda                         52      -         -        -
French Polynesia               47      -         -        -
Congo                          45      5         2       38
Cayman Islands                 45      1         6       38
Macao                          45      -        10        -
Sint Maarten                   40      6         1       33
Bermuda                        39      2        17       20
Zambia                         39      1         7       31
Bahamas                        36      6         5       25
Guyana                         33      5         8       20
Guinea-Bissau                  33      -         -        -
Saint Martin                   32      2         7       23
Liberia                        31      4         3       24
Eritrea                        31      -         -        -
Gabon                          30      1         1       28
Haiti                          27      1         -        -
Benin                          26      1         5       20
Tanzania                       25      1         5       19
Myanmar                        22      3         -        -
Libya                          21      1         2       18
Antigua and Barbuda            19      2         -        -
Syria                          19      2         3       14
Maldives                       19      -        13        -
New Caledonia                  18      -         1        -
Angola                         17      2         2       13
Mozambique                     17      -         1        -
Equatorial Guinea              16      -         3        -
Mongolia                       16      -         4        -
Namibia                        16      -         3        -
Dominica                       15      -         1        -
Fiji                           15      -         -        -
Laos                           15      -         -        -
Sudan                          14      2         2       10
Saint Lucia                    14      -         1        -
Curaçao                        13      1         7        5
Somalia                        12      1         1       10
Grenada                        12      -         -        -
Eswatini                       12      -         7        -
Zimbabwe                       11      2         -        -
Greenland                      11      -        11        -
Saint Kitts and Nevis          11      -         -        -
Seychelles                     11      -         -        -
Suriname                       10      1         3        6
Chad                           10      -         2        -
MS Zaandam                      9      2         -        -
Nepal                           9      -         1        -
Montserrat                      9      -         -        -
Belize                          8      1         -        -
Malawi                          8      1         -        -
Turks and Caicos                8      1         -        -
CAR                             8      -         -        -
St. Vincent Grenadines          8      -         1        -
Cabo Verde                      7      1         1        5
Vatican City                    7      -         -        -
Sierra Leone                    7      -         -        -
Botswana                        6      1         -        -
Mauritania                      6      1         2        3
Nicaragua                       6      1         -        -
St. Barth                       6      -         1        -
Bhutan                          5      -         2        -
Gambia                          4      1         2        1
Sao Tome and Principe           4      -         -        -
Western Sahara                  4      -         -        -
Anguilla                        3      -         -        -
British Virgin Islands          3      -         -        -
Burundi                         3      -         -        -
Caribbean Netherlands           2      -         -        -
Falkland Islands                2      -         -        -
Papua New Guinea                2      -         -        -
South Sudan                     2      -         -        -
Saint Pierre Miquelon           1      -         -        -
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
2020-04-04    1197405
2020-04-05    1272115
2020-04-06    1345101
2020-04-07    1426096
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
2020-04-03       8.15
2020-04-04       9.26
2020-04-05       6.24
2020-04-06       5.74
2020-04-07       6.02
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

