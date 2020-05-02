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
Total Confirmed 3427406.0

Updated: 2020-05-02 18:15:33.576245
```

New cases in 4 days

```python
3427406-3099990
```

```text
Out[1]: 327416
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
18.03 %
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
United States             1134084  65888    161782   906414
Spain                      245567  25100    146233    74234
Italy                      207428  28236     78249   100943
United Kingdom             177454  27510         -        -
France                     167346  24594     50212    92540
Germany                    164271   6736    129000    28535
Russia                     124054   1222     15013   107819
Turkey                     122392   3258     53808    65326
Iran                        96448   6156     77350    12942
Brazil                      92630   6434     38039    48157
China                       82875   4633     77685      557
Canada                      55061   3391     22751    28919
Belgium                     49517   7765     12211    29541
Peru                        40459   1124     11129    28206
Netherlands                 40236   4987         -        -
India                       37336   1223     10007    26106
Switzerland                 29817   1754     23900     4163
Ecuador                     26336   1063      1913    23360
Saudi Arabia                25459    176      3765    21518
Portugal                    25190   1023      1671    22496
Sweden                      22082   2669      1005    18408
Ireland                     20833   1265     13386     6182
Mexico                      20739   1972     12377     6390
Pakistan                    18770    432      4753    13585
Singapore                   17548     16      1268    16264
Chile                       17008    234      9018     7756
Israel                      16152    227      9400     6525
Belarus                     15828     97      3117    12614
Austria                     15558    596     13180     1782
Qatar                       14872     12      1534    13326
Japan                       14305    455      2975    10875
Poland                      13375    664      3762     8949
United Arab Emirates        13038    111      2543    10384
Romania                     12732    755      4547     7430
Ukraine                     11411    279      1498     9634
Indonesia                   10843    831      1665     8347
South Korea                 10780    250      9123     1407
Denmark                      9407    475      6889     2043
Serbia                       9362    189      1426     7747
Philippines                  8928    603      1124     7201
Bangladesh                   8790    175       177     8438
Norway                       7783    210        32     7541
Czech Republic               7740    241      3378     4121
Dominican Republic           7288    313      1387     5588
Colombia                     7006    314      1551     5141
Australia                    6783     93      5789      901
Panama                       6720    192       622     5906
Malaysia                     6176    103      4326     1747
South Africa                 5951    116      2382     3453
Egypt                        5895    406      1460     4029
Finland                      5176    220      3000     1956
Morocco                      4687    172      1235     3280
Kuwait                       4619     33      1703     2883
Argentina                    4532    229      1320     2983
Algeria                      4295    459      1872     1964
Moldova                      4052    124      1334     2594
Luxembourg                   3802     92      3213      497
Kazakhstan                   3800     25       985     2790
Bahrain                      3273      8      1567     1698
Thailand                     2966     54      2732      180
Hungary                      2942    335       625     1982
Greece                       2612    140      1374     1098
Oman                         2483     12       750     1721
Afghanistan                  2469     72       331     2066
Armenia                      2273     33      1010     1230
Nigeria                      2170     68       351     1751
Ghana                        2169     18       229     1922
Iraq                         2153     94      1414      645
Uzbekistan                   2094      9      1271      814
Croatia                      2088     77      1463      548
Azerbaijan                   1894     25      1411      458
Bosnia and Herzegovina       1839     72       779      988
Cameroon                     1832     61       934      837
Iceland                      1798     10      1706       82
Estonia                      1699     53       256     1390
Bulgaria                     1594     72       287     1235
Cuba                         1537     64       714      759
Guinea                       1537      7       342     1188
North Macedonia              1506     82       852      572
New Zealand                  1485     20      1263      202
Slovenia                     1439     94       239     1106
Slovakia                     1407     24       608      775
Lithuania                    1406     46       632      728
Ivory Coast                  1333     15       597      721
Bolivia                      1229     66       134     1029
Senegal                      1115      9       368      738
Djibouti                     1112      2       686      424
Hong Kong                    1040      4       864      172
Tunisia                       998     41       316      641
Honduras                      899     75       112      712
Latvia                        871     16       348      507
Cyprus                        864     15       296      553
Albania                       789     31       519      239
Kyrgyzstan                    769      8       527      234
Andorra                       745     43       468      234
Lebanon                       733     25       197      511
Niger                         728     33       478      217
Costa Rica                    725      6       355      364
Diamond Princess              712     13       645       54
Sri Lanka                     690      7       172      511
Burkina Faso                  649     44       517       88
Uruguay                       648     17       435      196
Guatemala                     644     16        72      556
DRC                           604     32        75      497
Somalia                       601     28        31      542
Georgia                       582      8       207      367
San Marino                    580     41        83      456
Mayotte                       539      4       235      300
Channel Islands               538     41       406       91
Sudan                         533     36        46      451
Maldives                      514      1        17      496
Mali                          508     26       196      286
Tanzania                      480     16       167      297
Malta                         468      4       379       85
Jordan                        459      9       364       86
El Salvador                   446     10       138      298
Kenya                         435     22       152      261
Jamaica                       432      8        31      393
Taiwan                        432      6       324      102
Réunion                       422      -       300        -
Palestine                     353      2        76      275
Venezuela                     335     10       148      177
Paraguay                      333     10       115      208
Mauritius                     332     10       312       10
Montenegro                    322      7       240       75
Isle of Man                   320     22       271       27
Equatorial Guinea             315      1         9      305
Gabon                         276      3        67      206
Vietnam                       270      -       219        -
Guinea-Bissau                 257      1        19      237
Rwanda                        249      -       109        -
Congo                         229      9        25      195
Faeroe Islands                187      -       184        -
Martinique                    179     14        83       82
Sierra Leone                  155      8        21      126
Liberia                       152     18        45       89
Guadeloupe                    152     12        95       45
Myanmar                       151      6        37      108
Gibraltar                     144      -       131        -
Brunei                        138      1       126       11
Madagascar                    135      -        97        -
Ethiopia                      133      3        69       61
French Guiana                 128      1        98       29
Togo                          123      9        66       48
Cabo Verde                    122      1        18      103
Cambodia                      122      -       120        -
Zambia                        119      3        75       41
Trinidad and Tobago           116      8        83       25
Bermuda                       114      6        48       60
Eswatini                      108      1        12       95
Aruba                         100      2        81       17
Monaco                         95      4        73       18
Benin                          90      2        42       46
Haiti                          85      8        10       67
Uganda                         85      -        52        -
Bahamas                        82     11        24       47
Guyana                         82      9        22       51
Liechtenstein                  82      1        55       26
Barbados                       81      7        39       35
Mozambique                     79      -        18        -
Sint Maarten                   76     13        44       19
Cayman Islands                 74      1        10       63
Chad                           73      5        33       35
CAR                            72      -        10        -
Libya                          63      3        32       28
Nepal                          59      -        16        -
French Polynesia               58      -        51        -
Macao                          45      -        37        -
South Sudan                    45      -         -        -
Syria                          44      3        27       14
Eritrea                        39      -        26        -
Mongolia                       39      -        10        -
Saint Martin                   38      3        27        8
Malawi                         37      3         9       25
Zimbabwe                       34      4         5       25
Tajikistan                     32      -         -        -
Angola                         30      2        11       17
Antigua and Barbuda            25      3        15        7
Timor-Leste                    24      -        16        -
Botswana                       23      1         8       14
Grenada                        20      -        13        -
Laos                           19      -         9        -
Belize                         18      2        13        3
Fiji                           18      -        14        -
New Caledonia                  18      -        17        -
Saint Lucia                    17      -        15        -
Curaçao                        16      1        13        2
Sao Tome and Principe          16      1         4       11
Dominica                       16      -        13        -
Namibia                        16      -         8        -
St. Vincent Grenadines         16      -         8        -
Saint Kitts and Nevis          15      -         8        -
Nicaragua                      14      3         7        4
Falkland Islands               13      -        13        -
Gambia                         12      1         9        2
Turks and Caicos               12      1         5        6
Burundi                        11      1         4        6
Montserrat                     11      1         2        8
Greenland                      11      -        11        -
Vatican City                   11      -         2        -
Seychelles                     11      -         6        -
Suriname                       10      1         8        1
MS Zaandam                      9      2         -        -
Mauritania                      8      1         6        1
Papua New Guinea                8      -         -        -
Yemen                           7      2         1        4
Bhutan                          7      -         5        -
British Virgin Islands          6      1         3        2
Caribbean Netherlands           6      -         -        -
St. Barth                       6      -         6        -
Western Sahara                  6      -         5        -
Anguilla                        3      -         3        -
Comoros                         1      -         -        -
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
2020-04-28  3097190.0
2020-04-29  3172287.0
2020-04-30  3256853.0
2020-05-01  3343777.0
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
2020-04-27       2.32
2020-04-28       2.43
2020-04-29       2.42
2020-04-30       2.67
2020-05-01       2.67
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

