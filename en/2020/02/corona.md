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
Total Confirmed 2921571.0

Updated: 2020-04-26 09:01:29.697937
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
19.55 %
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
United States              960896  54265    118162   788469
Spain                      223759  22902     95708   105149
Italy                      195351  26384     63120   105847
France                     161488  22614     44594    94280
Germany                    156513   5877    109800    40836
United Kingdom             148377  20319         -        -
Turkey                     107773   2706     25582    79485
Iran                        89328   5650     68193    15485
China                       82827   4632     77394      801
Russia                      74588    681      6250    67657
Brazil                      59324   4057     29160    26107
Canada                      45354   2465     16425    26464
Belgium                     45325   6917     10417    27991
Netherlands                 37190   4409         -        -
Switzerland                 28894   1599     21300     5995
India                       26496    825      5939    19732
Peru                        25331    700      7797    16834
Portugal                    23392    880      1277    21235
Ecuador                     22719    576      1366    20777
Ireland                     18561   1063      9233     8265
Sweden                      18177   2192      1005    14980
Saudi Arabia                16299    136      2215    13948
Israel                      15298    199      6435     8664
Austria                     15148    536     12103     2509
Mexico                      13842   1305      7149     5388
Japan                       13231    360      1656    11215
Chile                       12858    181      6746     5931
Pakistan                    12723    269      2866     9588
Singapore                   12693     12      1002    11679
Poland                      11273    524      2126     8623
South Korea                 10728    242      8717     1769
Romania                     10635    601      2890     7144
United Arab Emirates         9813     71      1887     7855
Belarus                      9590     67      1573     7950
Qatar                        9358     10       929     8419
Indonesia                    8607    720      1042     6845
Denmark                      8445    418      5669     2358
Ukraine                      8125    201       782     7142
Serbia                       7779    151      1152     6476
Norway                       7499    201        32     7266
Czech Republic               7352    218      2453     4681
Philippines                  7294    494       792     6008
Australia                    6710     83      5523     1104
Dominican Republic           5926    273       822     4831
Malaysia                     5742     98      3762     1882
Panama                       5538    159       338     5041
Colombia                     5142    233      1067     3842
Bangladesh                   4998    140       113     4745
Finland                      4475    186      2500     1789
South Africa                 4361     86      1473     2802
Egypt                        4319    307      1114     2898
Morocco                      3897    159       537     3201
Argentina                    3780    185      1030     2565
Luxembourg                   3711     85      3088      538
Moldova                      3304     94       825     2385
Algeria                      3256    419      1479     1358
Thailand                     2907     51      2547      309
Kuwait                       2892     19       656     2217
Kazakhstan                   2601     25       646     1930
Bahrain                      2588      8      1160     1420
Greece                       2506    130       577     1799
Hungary                      2500    272       485     1743
Croatia                      2016     54      1034      928
Oman                         1905     10       329     1566
Uzbekistan                   1865      8       707     1150
Iceland                      1790     10      1570      210
Iraq                         1763     86      1224      453
Armenia                      1677     28       803      846
Estonia                      1635     46       228     1361
Azerbaijan                   1617     21      1080      516
Cameroon                     1518     53       697      768
Bosnia and Herzegovina       1486     57       592      837
New Zealand                  1470     18      1142      310
Afghanistan                  1463     47       188     1228
Lithuania                    1438     41       467      930
Slovenia                     1388     81       219     1088
Slovakia                     1373     17       386      970
North Macedonia              1367     59       374      934
Cuba                         1337     51       437      849
Bulgaria                     1290     55       205     1030
Ghana                        1279     10       134     1135
Nigeria                      1182     35       222      925
Ivory Coast                  1077     14       419      644
Hong Kong                    1038      4       753      281
Djibouti                     1008      2       373      633
Guinea                        996      7       208      781
Tunisia                       939     38       207      694
Bolivia                       866     46        54      766
Cyprus                        810     14       148      648
Latvia                        804     12       267      525
Andorra                       738     40       344      354
Albania                       712     27       403      282
Diamond Princess              712     13       645       54
Lebanon                       704     24       143      537
Costa Rica                    693      6       242      445
Niger                         684     27       325      332
Kyrgyzstan                    682      8       370      304
Burkina Faso                  629     41       442      146
Honduras                      627     59        65      503
Senegal                       614      7       276      331
Uruguay                       596     14       370      212
Channel Islands               525     35       332      158
San Marino                    513     40        64      409
Guatemala                     473     13        45      415
Sri Lanka                     460      7       118      335
Georgia                       456      5       139      312
Malta                         448      4       249      195
Jordan                        444      7       332      105
Taiwan                        429      6       275      148
Réunion                       417      -       300        -
DRC                           416     28        49      339
Somalia                       390     18         8      364
Mayotte                       380      4       144      232
Mali                          370     21        91      258
Kenya                         343     14        98      231
Palestine                     342      2        92      248
Mauritius                     331      9       295       27
Venezuela                     323     10       132      181
Montenegro                    320      6       153      161
Isle of Man                   308     18       243       47
Jamaica                       305      7        28      270
Tanzania                      299     10        48      241
El Salvador                   298      8        83      207
Vietnam                       270      -       225        -
Equatorial Guinea             258      1         7      250
Paraguay                      228      9        85      134
Sudan                         213     17        19      177
Congo                         200      6        19      175
Faeroe Islands                187      -       178        -
Rwanda                        183      -        88        -
Maldives                      177      -        17        -
Gabon                         176      3        30      143
Martinique                    175     14        77       84
Guadeloupe                    149     12        82       55
Myanmar                       146      5        10      131
Brunei                        138      1       121       16
Gibraltar                     136      -       131        -
Madagascar                    123      -        62        -
Ethiopia                      122      3        29       90
Cambodia                      122      -       117        -
Liberia                       120     11        25       84
Trinidad and Tobago           115      8        53       54
French Guiana                 111      1        87       23
Bermuda                       109      5        39       65
Aruba                         100      2        69       29
Togo                           96      6        62       28
Monaco                         94      4        42       48
Cabo Verde                     90      1         1       88
Zambia                         84      3        37       44
Sierra Leone                   82      2        10       70
Liechtenstein                  81      1        55       25
Barbados                       79      6        31       42
Bahamas                        78     11        15       52
Uganda                         75      -        46        -
Sint Maarten                   73     12        22       39
Guyana                         73      7        12       54
Haiti                          72      6         6       60
Cayman Islands                 70      1         8       61
Mozambique                     70      -        12        -
Libya                          61      2        18       41
French Polynesia               57      -        41        -
Eswatini                       56      1        10       45
Benin                          54      1        27       26
Guinea-Bissau                  52      -         3        -
Nepal                          49      -        12        -
Chad                           46      -        15        -
Macao                          45      -        28        -
Syria                          42      3        11       28
Eritrea                        39      -        13        -
Saint Martin                   38      3        24       11
Mongolia                       38      -         9        -
Malawi                         33      3         4       26
Zimbabwe                       31      4         2       25
Angola                         25      2         6       17
Antigua and Barbuda            24      3        11       10
Timor-Leste                    24      -         2        -
Botswana                       22      1         -        -
Laos                           19      -         7        -
Belize                         18      2         5       11
Fiji                           18      -        10        -
Grenada                        18      -         7        -
New Caledonia                  18      -        17        -
Curaçao                        16      1        11        4
CAR                            16      -        10        -
Dominica                       16      -        13        -
Namibia                        16      -         7        -
Saint Kitts and Nevis          15      -         2        -
Saint Lucia                    15      -        15        -
St. Vincent Grenadines         14      -         5        -
Falkland Islands               13      -        11        -
Nicaragua                      12      3         7        2
Burundi                        11      1         4        6
Montserrat                     11      1         2        8
Turks and Caicos               11      1         4        6
Greenland                      11      -        11        -
Seychelles                     11      -         6        -
Gambia                         10      1         8        1
Suriname                       10      1         7        2
MS Zaandam                      9      2         -        -
Vatican City                    9      -         2        -
Papua New Guinea                8      -         -        -
Mauritania                      7      1         6        0
Bhutan                          7      -         3        -
British Virgin Islands          6      1         3        2
St. Barth                       6      -         6        -
Western Sahara                  6      -         5        -
Caribbean Netherlands           5      -         -        -
South Sudan                     5      -         -        -
Sao Tome and Principe           4      -         -        -
Anguilla                        3      -         1        -
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
2020-04-21    2548091
2020-04-22    2623049
2020-04-23    2707728
2020-04-24    2809977
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
2020-04-20       2.97
2020-04-21       3.11
2020-04-22       2.94
2020-04-23       3.23
2020-04-24       3.78
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

