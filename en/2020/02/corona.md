# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 100, 200, 1000, 2000, 10000, 100000, 1000000, 2000000, 4000000]
colors = ["lightsalmon","lightcoral", "tomato","red",\
	  "indianred","firebrick","maroon","dimgray", "black"]
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
Total Confirmed 9549392.0

Updated: 2020-06-25 09:41:46.705229
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
5.21 %
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
United States             2462708 124282   1040608  1297818
Brazil                    1192474  53874    649908   488692
Russia                     606881   8513    368822   229546
India                      473719  14907    271723   187089
United Kingdom             306862  43081         -        -
Spain                      294166  28327         -        -
Peru                       264689   8586    151589   104514
Chile                      254416   4731    215093    34592
Italy                      239410  34644    186111    18655
Iran                       212501   9996    172096    30409
Mexico                     196847  24324    149318    23205
Germany                    193254   9003    176300     7951
Pakistan                   192970   3903     81307   107760
Turkey                     191657   5025    164234    22398
Saudi Arabia               167267   1387    112797    53083
France                     161348  29731     75127    56490
Bangladesh                 122660   1582     49666    71412
South Africa               111796   2205     56874    52717
Canada                     102242   8484     65091    28667
Qatar                       90778    104     73083    17591
China                       83449   4634     78443      372
Colombia                    77113   2491     31671    42951
Sweden                      62324   5209         -        -
Belgium                     60898   9722     16771    34405
Belarus                     59945    362     40136    19447
Egypt                       59561   2450     15935    41176
Ecuador                     51643   4274     24991    22378
Argentina                   49851   1116     13816    34919
Netherlands                 49804   6097         -        -
Indonesia                   49009   2573     19658    26778
United Arab Emirates        46133    307     34405    11421
Singapore                   42623     26     36299     6298
Kuwait                      41879    337     32809     8733
Portugal                    40104   1543     26083    12478
Ukraine                     40008   1067     17758    21183
Iraq                        36702   1330     16814    18558
Oman                        33536    142     17972    15422
Poland                      32821   1396     18134    13291
Philippines                 32295   1204      8656    22435
Switzerland                 31376   1958     29000      418
Afghanistan                 30175    675     10174    19326
Dominican Republic          28631    691     16006    11934
Panama                      28030    547     14794    12689
Bolivia                     27487    876      6795    19816
Ireland                     25396   1726     23364      306
Romania                     24826   1555     17391     5880
Bahrain                     23570     69     17977     5524
Israel                      22044    308     15940     5796
Nigeria                     22020    542      7613    13865
Armenia                     21717    386     10797    10534
Kazakhstan                  19285    136     11882     7267
Japan                       18024    963     16263      798
Austria                     17449    693     16282      474
Moldova                     15078    495      8400     6183
Ghana                       15013     95     11078     3840
9,534,437                   14955   1217   3869514 -3855776
Guatemala                   14819    601      2930    11288
Honduras                    14571    417      1546    12608
Azerbaijan                  14305    174      7768     6363
Serbia                      13235    263     12111      861
Denmark                     12615    603     11422      590
Cameroon                    12592    313     10100     2179
South Korea                 12563    282     10974     1307
Algeria                     12248    869      8792     2587
Morocco                     10907    216      8468     2223
Czech Republic              10777    343      7588     2846
Nepal                       10728     24      2338     8366
Sudan                        8889    548      3699     4642
Norway                       8788    249      8138      401
Malaysia                     8596    121      8231      244
Ivory Coast                  8164     58      3419     4687
Australia                    7558    104      6931      523
Finland                      7167    327      6600      240
Uzbekistan                   6990     19      4685     2286
DRC                          6213    142       870     5201
Senegal                      6129     93      4072     1964
Tajikistan                   5630     52      4194     1384
North Macedonia              5445    259      2091     3095
Haiti                        5429     92       512     4825
Kenya                        5206    130      1823     3253
Guinea                       5174     29      3861     1284
El Salvador                  5150    119      2950     2081
Ethiopia                     5034     78      1486     3470
Gabon                        4956     39      2177     2740
Djibouti                     4630     52      4182      396
Venezuela                    4366     38      1327     3001
Bulgaria                     4242    209      2263     1770
Luxembourg                   4140    110      3965       65
Hungary                      4123    577      2640      906
Kyrgyzstan                   3954     43      2112     1799
Bosnia and Herzegovina       3676    173      2297     1206
Mauritania                   3519    116      1074     2329
Greece                       3310    190      1374     1746
Thailand                     3158     58      3038       62
CAR                          3099     38       572     2489
Somalia                      2835     90       829     1916
French Guiana                2827      9      1056     1762
Costa Rica                   2515     12      1210     1293
Mayotte                      2467     32      2218      217
Croatia                      2388    107      2145      136
Cuba                         2319     85      2130      104
Maldives                     2261      8      1839      414
Nicaragua                    2170     74      1238      858
Albania                      2114     47      1217      850
Mali                         2005    112      1354      539
Sri Lanka                    2001     11      1562      428
Estonia                      1983     69      1783      131
South Sudan                  1942     36       224     1682
Iceland                      1824     10      1806        8
Lithuania                    1804     78      1484      242
Madagascar                   1787     16       779      992
Equatorial Guinea            1664     32       515     1117
Lebanon                      1644     33      1103      508
Slovakia                     1607     28      1448      131
Guinea-Bissau                1556     19       191     1346
Slovenia                     1541    109      1376       56
Paraguay                     1528     13       944      571
New Zealand                  1519     22      1484       13
Zambia                       1489     18      1223      248
Sierra Leone                 1354     55       869      430
Palestine                    1328      3       442      883
Hong Kong                    1180      6      1086       88
Tunisia                      1160     50      1023       87
Latvia                       1111     30       903      178
Congo                        1087     37       456      594
Jordan                       1071      9       782      280
Niger                        1051     67       913       71
Yemen                        1015    274       379      362
Cabo Verde                    999      8       479      512
Cyprus                        991     19       824      148
Malawi                        941     11       259      671
Burkina Faso                  919     53       825       41
Georgia                       917     14       776      127
Uruguay                       902     26       815       61
Benin                         902     13       277      612
Chad                          860     74       770       16
Andorra                       855     52       797        6
Rwanda                        830      2       376      452
Uganda                        805      -       717        -
Mozambique                    762      5       220      537
Diamond Princess              712     13       651       48
Sao Tome and Principe         710     13       211      486
San Marino                    698     42       647        9
Eswatini                      690      7       331      352
Jamaica                       678     10       521      147
Libya                         670     18       138      514
Malta                         665      9       624       32
Liberia                       662     34       270      358
Togo                          583     14       392      177
Channel Islands               571     47       512       12
Zimbabwe                      530      6       123      401
Tanzania                      509     21       183      305
Réunion                       508      1       460       47
Taiwan                        446      7       435        4
Montenegro                    389      9       315       65
Suriname                      357     10       154      193
Vietnam                       352      -       329        -
Mauritius                     341     10       326        5
Isle of Man                   336     24       312        0
Myanmar                       293      6       208       79
Comoros                       265      7       159       99
Martinique                    236     14        98      124
Syria                         231      7        94      130
Mongolia                      216      -       169        -
Guyana                        209     12       107       90
Angola                        197     10        77      110
Cayman Islands                196      1       169       26
Faeroe Islands                187      -       187        -
Gibraltar                     176      -       176        -
Guadeloupe                    174     14       157        3
Bermuda                       146      9       132        5
Burundi                       144      1        93       50
Eritrea                       144      -        39        -
Brunei                        141      3       138        0
Cambodia                      130      -       127        -
Trinidad and Tobago           123      8       109        6
Bahamas                       104     11        83       10
Monaco                        102      4        95        3
Aruba                         101      3        98        0
Barbados                       97      7        85        5
Botswana                       92      1        25       66
Liechtenstein                  82      1        81        0
Sint Maarten                   77     15        62        0
Namibia                        76      -        21        -
Bhutan                         70      -        34        -
Antigua and Barbuda            65      3        22       40
French Polynesia               60      -        60        -
Macao                          45      -        45        -
Saint Martin                   42      3        36        3
Gambia                         42      2        26       14
St. Vincent Grenadines         29      -        27        -
Timor-Leste                    24      -        24        -
Curaçao                        23      1        19        3
Grenada                        23      -        23        -
Belize                         23      2        17        4
New Caledonia                  21      -        21        -
Laos                           19      -        19        -
Saint Lucia                    19      -        19        -
Dominica                       18      -        18        -
Fiji                           18      -        18        -
Lesotho                        17      -         2        -
Turks and Caicos               15      1        11        3
Saint Kitts and Nevis          15      -        15        -
Falkland Islands               13      -        13        -
Greenland                      13      -        13        -
Vatican City                   12      -        12        -
Seychelles                     11      -        11        -
Montserrat                     11      1        10        0
Papua New Guinea               10      -         8        -
Western Sahara                 10      1         8        1
MS Zaandam                      9      2         -        -
British Virgin Islands          8      1         7        0
Caribbean Netherlands           7      -         7        -
St. Barth                       6      -         6        -
Anguilla                        3      -         3        -
Saint Pierre Miquelon           1      -         1        -
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
2020-06-20    8829186
2020-06-21    8960607
2020-06-22    9098643
2020-06-23    9263466
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
2020-06-19       2.14
2020-06-20       1.83
2020-06-21       1.49
2020-06-22       1.54
2020-06-23       1.81
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

