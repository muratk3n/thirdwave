# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 50, 100, 200, 1000, 2000, 10000, 100000, 800000, 1200000]
colors = ["lightsalmon","salmon","lightcoral", "tomato","red",\
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
Total Confirmed 3427406.0

Updated: 2020-05-04 21:56:16.995628
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
                                  Confirmed  Deaths  Recovered  NewCases
Country                                                                 
United States                       1158040   67682     180152    910206
Spain                                217466   25264     118902     73300
Italy                                210717   28884      81654    100179
United Kingdom                       186599   28446          0    158153
France                               167272   24864      49973     92435
Germany                              165664    6866     130600     28198
Russia                               134687    1280      16639    116768
Turkey                               126045    3397      63151     59497
Brazil                               101826    7051      42991     51784
Iran                                  97424    6203      78422     12799
China                                 68128    4512      63616         0
Belgium                               49906    7844      12309     29753
Peru                                  45928    1286      13550     31092
India                                 42505    1391      11775     29339
Netherlands                           40571    5056          0     35515
Canada                                31873    2206          1     29666
Switzerland                           29905    1762      24500      3643
Ecuador                               29538    1564       3300     24674
Saudi Arabia                          27011     184       4134     22693
Portugal                              25282    1043       1689     22550
Mexico                                23471    2154      13447      7870
Sweden                                22317    2679       1005     18633
Ireland                               21506    1303      13386      6817
Pakistan                              20084     457       5114     14513
Chile                                 19663     260      10041      9362
Canada                                18574    1326        159     17089
Singapore                             18205      18       1408     16779
Belarus                               16705      99       3196     13410
Israel                                16208     232       9749      6227
Austria                               15597     598      13228      1771
Qatar                                 15551      12       1664     13875
Japan                                 14877     487       3981     10409
United Arab Emirates                  14163     126       2763     11274
Poland                                13693     678       3945      9070
Romania                               13163     790       4869      7504
Ukraine                               11913     288       1548     10077
Indonesia                             11192     845       1876      8471
Korea, South                          10801     252       9217      1332
Denmark                                9523     484       6987      2052
Serbia                                 9464     193       1551      7720
Bangladesh                             9455     177       1063      8215
Philippines                            9223     607       1214      7402
Dominican Republic                     7954     333       1606      6015
Norway                                 7847     211         32      7604
Czechia                                7781     248       3587      3946
Colombia                               7668     340       1722      5606
Panama                                 7090     197        641      6252
South Africa                           6783     131       2549      4103
Egypt                                  6465     429       1562      4474
Malaysia                               6298     105       4413      1780
Canada                                 5766      95        874      4797
Finland                                5254     230       3000      2024
Kuwait                                 4983      38       1776      3169
Morocco                                4903     174       1438      3291
Argentina                              4783     246       1354      3183
Algeria                                4474     463       1936      2075
Moldova                                4121     125       1382      2614
Kazakhstan                             3920      27       1084      2809
Luxembourg                             3824      96       3379       349
Bahrain                                3383       8       1718      1657
Australia                              3033      42       2328       663
Hungary                                2998     340        629      2029
Thailand                               2969      54       2739       176
Afghanistan                            2704      85        345      2274
Greece                                 2626     144       1374      1108
Oman                                   2568      12        750      1806
Nigeria                                2558      87        400      2071
Armenia                                2386      35       1035      1316
Iraq                                   2296      97       1490       709
Canada                                 2171     114        794      1263
Ghana                                  2169      18        229      1922
Uzbekistan                             2149      10       1319       820
Croatia                                2096      79       1489       528
Cameroon                               2077      64        953      1060
Azerbaijan                             1932      25       1441       466
Bosnia and Herzegovina                 1857      77        825       955
Iceland                                1799      10       1717        72
Estonia                                1700      55        259      1386
Cuba                                   1649      67        827       755
Bulgaria                               1618      73        308      1237
Bolivia                                1594      76        166      1352
China                                  1588       8       1569        11
Guinea                                 1586       7        405      1174
North Macedonia                        1511      84        945       482
New Zealand                            1487      20       1276       191
Slovenia                               1439      96        241      1102
Lithuania                              1410      46        635       729
Slovakia                               1408      24        619       765
Australia                              1406      18       1300        88
Cote d'Ivoire                          1398      17        653       728
China                                  1276      22       1254         0
China                                  1268       1       1265         2
Senegal                                1182       9        372       801
Djibouti                               1112       2        686       424
Honduras                               1055      82        118       855
China                                  1039       4        879       156
Australia                              1038       6        980        52
China                                  1019       4       1015         0
Tunisia                                1013      42        328       643
China                                   991       6        985         0
Canada                                  971      37        239       695
China                                   944      13        657       274
China                                   937       1        936         0
Latvia                                  879      16        348       515
Cyprus                                  872      15        296       561
Kosovo                                  851      22        381       448
Kyrgyzstan                              795      10        564       221
Albania                                 795      31        531       233
China                                   788       7        773         8
Niger                                   750      36        518       196
Andorra                                 748      45        493       210
Costa Rica                              739       6        386       347
Lebanon                                 737      25        200       512
Somalia                                 722      32         44       646
Sri Lanka                               718       7        184       527
Diamond Princess                        712      13        645        54
Guatemala                               703      17         72       614
Congo (Kinshasa)                        674      33         75       566
Burkina Faso                            662      45        540        77
China                                   655       7        615        33
Uruguay                                 655      17        442       196
China                                   653       0        650         3
France                                  650       6        235       409
China                                   593       9        553        31
Sudan                                   592      41         52       499
Georgia                                 589       9        223       357
San Marino                              582      41         86       455
China                                   579       6        573         0
Mali                                    563      27        213       323
China                                   561       3        558         0
Australia                               551       9        523        19
United Kingdom                          544      41        406        97
Maldives                                527       1         18       508
El Salvador                             490      11        154       325
Tanzania                                480      16        167       297
Malta                                   477       4        392        81
Jamaica                                 469       9         38       422
Kenya                                   465      24        167       274
Jordan                                  461       9        367        85
Australia                               438       4        427         7
Taiwan*                                 436       6        332        98
Canada                                  433       7      12521    -12095
France                                  423       0        300       123
Paraguay                                396      10        126       260
Venezuela                               357      10        158       189
China                                   356       1        353         2
West Bank and Gaza                      353       2         77       274
Gabon                                   335       5         85       245
Mauritius                               332      10        315         7
China                                   328       6        318         4
Montenegro                              322       8        249        65
United Kingdom                          321      22        271        28
Equatorial Guinea                       315       1          9       305
Canada                                  306      21      24921    -24636
China                                   306       3        263        40
Canada                                  282       6        556      -280
Vietnam                                 271       0        219        52
Canada                                  259       3        398      -142
Rwanda                                  259       0        124       135
Guinea-Bissau                           257       1         19       237
China                                   254       2        252         0
Congo (Brazzaville)                     229       9         25       195
Australia                               221      13        164        44
China                                   201       1        156        44
China                                   198       0        180        18
China                                   190       3        186         1
Denmark                                 187       0        185         2
China                                   185       2        181         2
France                                  179      14         83        82
China                                   168       6        162         0
Sierra Leone                            166       8         29       129
Cabo Verde                              165       2         33       130
Liberia                                 158      18         58        82
Burma                                   155       6         43       106
France                                  152      12         95        45
Madagascar                              149       0         98        51
China                                   147       2        145         0
China                                   146       2        144         0
United Kingdom                          144       0        132        12
China                                   139       2        137         0
Brunei                                  138       1        128         9
Ethiopia                                135       3         75        57
Tajikistan                              128       2          0       126
France                                  128       1         98        29
Togo                                    124       9         67        48
Zambia                                  124       3         78        43
Cambodia                                122       0        120         2
Canada                                  118       0        477      -359
Chad                                    117      10         39        68
Trinidad and Tobago                     116       8         93        15
United Kingdom                          115       7         51        57
China                                   112       1        103         8
Eswatini                                112       1         12        99
Australia                               106       3        103         0
Netherlands                             100       2         81        17
Monaco                                   95       4         78        13
Benin                                    90       2         42        46
Uganda                                   89       0         52        37
Haiti                                    88       9         10        69
Bahamas                                  83      11         24        48
Barbados                                 82       7         44        31
Liechtenstein                            82       1         55        26
Guyana                                   82       9         22        51
Mozambique                               80       0         19        61
Netherlands                              76      13         44        19
China                                    76       3         73         0
China                                    75       0         75         0
Nepal                                    75       0         16        59
United Kingdom                           74       1         10        63
Central African Republic                 72       0         10        62
Libya                                    63       3         22        38
France                                   58       0         51         7
South Sudan                              46       0          0        46
China                                    45       0         39         6
Syria                                    44       3         27        14
Mongolia                                 39       0         10        29
Malawi                                   39       3          9        27
Eritrea                                  39       0         26        13
France                                   38       3         27         8
Angola                                   35       2         11        22
Zimbabwe                                 34       4          5        25
Australia                                29       0         24         5
Canada                                   27       0         80       -53
Antigua and Barbuda                      25       3         15         7
Timor-Leste                              24       0         16         8
Botswana                                 23       1          8        14
Grenada                                  21       0         13         8
Laos                                     19       0          9        10
China                                    18       0         18         0
Belize                                   18       2         13         3
Fiji                                     18       0         14         4
Saint Lucia                              18       0         15         3
France                                   18       0         17         1
Gambia                                   17       1          9         7
Namibia                                  16       0          8         8
Netherlands                              16       1         13         2
Sao Tome and Principe                    16       1          4        11
Saint Vincent and the Grenadines         16       0          8         8
Dominica                                 16       0         13         3
Burundi                                  15       1          7         7
Nicaragua                                15       5          7         3
Saint Kitts and Nevis                    15       0          8         7
United Kingdom                           13       0         13         0
Canada                                   13       0        636      -623
United Kingdom                           12       1          5         6
Denmark                                  11       0         11         0
United Kingdom                           11       1          7         3
Holy See                                 11       0          2         9
Seychelles                               11       0          6         5
Canada                                   11       0        120      -109
Yemen                                    10       2          1         7
Suriname                                 10       1          9         0
MS Zaandam                                9       2          0         7
Mauritania                                8       1          6         1
Papua New Guinea                          8       0          0         8
Bhutan                                    7       0          5         2
Netherlands                               6       0          0         6
Western Sahara                            6       0          5         1
France                                    6       0          6         0
United Kingdom                            6       1          3         2
Canada                                    5       0        318      -313
Comoros                                   3       0          0         3
United Kingdom                            3       0          3         0
Canada                                    1       1        715      -715
China                                     1       0          1         0
France                                    1       0          0         1
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

