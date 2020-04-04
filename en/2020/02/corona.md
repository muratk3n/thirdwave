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
Total Confirmed 1117942.0

Updated: 2020-04-04 09:05:11.464534
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( 'Symp. Death Rate =', np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
Symp. Death Rate = 20.53 %
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
United States              277475   7402     12283   257790
Italy                      119827  14681     19758    85388
Spain                      119199  11198     30513    77488
Germany                     91159   1275     24575    65309
France                      82165   6507     14008    61650
China                       81639   3326     76755     1558
Iran                        53183   3294     17935    31954
United Kingdom              38168   3605       135    34428
Turkey                      20921    425       484    20012
Switzerland                 19606    591      4846    14169
Belgium                     16770   1143      2872    12755
Netherlands                 15723   1487       250    13986
Canada                      12549    208      2322    10019
Austria                     11525    168      2022     9335
South Korea                 10156    177      6325     3654
Portugal                     9886    246        68     9572
Brazil                       9216    365       127     8724
Israel                       7428     40       403     6985
Sweden                       6131    358       205     5568
Australia                    5454     30       585     4839
Norway                       5370     59        32     5279
Ireland                      4273    120        25     4128
Czech Republic               4190     53        72     4065
Russia                       4149     34       281     3834
Denmark                      3757    139      1193     2425
Chile                        3737     22       427     3288
Poland                       3383     71        56     3256
Ecuador                      3368    145        65     3158
Malaysia                     3333     53       827     2453
Romania                      3183    133       283     2767
India                        3082     86       229     2767
Philippines                  3018    136        52     2830
Japan                        2935     69       514     2352
Pakistan                     2708     40       130     2538
Luxembourg                   2612     31       500     2081
Thailand                     2067     20       612     1435
Saudi Arabia                 2039     25       351     1663
Indonesia                    1986    181       134     1671
Mexico                       1688     60       633      995
Panama                       1673     41        10     1622
Finland                      1615     20       300     1295
Greece                       1613     63        78     1472
Peru                         1595     61       537      997
South Africa                 1505      9        95     1401
Dominican Republic           1488     68        16     1404
Serbia                       1476     39        54     1383
Iceland                      1364      4       309     1051
Argentina                    1353     42       266     1045
Colombia                     1267     25        55     1187
United Arab Emirates         1264      9       108     1147
Algeria                      1171    105        62     1004
Singapore                    1114      6       282      826
Croatia                      1079      8        92      979
Qatar                        1075      3        93      979
Ukraine                      1072     27        22     1023
Egypt                         985     66       216      703
Estonia                       961     12        48      901
New Zealand                   950      1       127      822
Slovenia                      934     20        70      844
Hong Kong                     845      4       173      668
Iraq                          820     54       226      540
Morocco                       791     48        57      686
Lithuania                     771      9         7      755
Armenia                       736      7        43      686
Diamond Princess              712     11       619       82
Hungary                       678     32        58      588
Bahrain                       672      4       382      286
Moldova                       591      8        26      557
Bosnia and Herzegovina        579     17        27      535
Cameroon                      509      8        17      484
Lebanon                       508     17        50      441
Kazakhstan                    500      4        35      461
Bulgaria                      498     14        34      450
Tunisia                       495     18         5      472
Latvia                        493      1         1      491
Slovakia                      450      1        10      439
Azerbaijan                    443      5        32      406
Andorra                       439     16        16      407
North Macedonia               430     12        20      398
Kuwait                        417      1        82      334
Costa Rica                    416      2        11      403
Cyprus                        396     11        28      357
Uruguay                       386      4        86      296
Belarus                       351      4        53      294
Taiwan                        348      5        50      293
Réunion                       321      -        40        -
Jordan                        310      5        58      247
Albania                       304     17        89      198
Burkina Faso                  302     16        50      236
Afghanistan                   299      6        10      283
Cuba                          269      6        15      248
Honduras                      264     15         3      246
Oman                          252      1        57      194
San Marino                    251     32        26      193
Vietnam                       239      -        90        -
Channel Islands               232      4        13      215
Uzbekistan                    227      2        25      200
Ivory Coast                   218      1        19      198
Nigeria                       210      4        25      181
Senegal                       207      1        66      140
Ghana                         205      5        31      169
Malta                         202      -         2        -
Palestine                     194      1        21      172
Mauritius                     186      7         -        -
Faeroe Islands                179      -        91        -
Montenegro                    174      2         1      171
Sri Lanka                     159      5        24      130
Georgia                       155      -        28        -
Venezuela                     153      7        52       94
DRC                           148     16         3      129
Kyrgyzstan                    144      1         6      137
Martinique                    143      3        27      113
Bolivia                       139     10         1      128
Brunei                        134      1        65       68
Guadeloupe                    130      7        24       99
Mayotte                       128      2        10      116
Kenya                         122      4         4      114
Niger                         120      5         -        -
Isle of Man                   114      1         -        -
Cambodia                      114      -        50        -
Trinidad and Tobago           100      6         1       93
Paraguay                       96      3        12       81
Gibraltar                      95      -        46        -
Rwanda                         89      -         -        -
Liechtenstein                  75      -         -        -
Guinea                         73      -         2        -
Madagascar                     70      -         -        -
Monaco                         64      1         3       60
Aruba                          62      -         1        -
Bangladesh                     61      6        26       29
French Guiana                  57      -        22        -
El Salvador                    56      3         -        -
Jamaica                        53      3         7       43
Barbados                       51      -         -        -
Guatemala                      50      1        12       37
Djibouti                       49      -         8        -
Uganda                         48      -         -        -
Macao                          42      -        10        -
Togo                           40      3        17       20
Mali                           39      3         -        -
Zambia                         39      1         2       36
French Polynesia               39      -         -        -
Bermuda                        35      -        14        -
Ethiopia                       35      -         3        -
Cayman Islands                 29      1         1       27
Bahamas                        24      3         -        -
Guyana                         23      4         -        -
Sint Maarten                   23      4         6       13
Congo                          22      2         2       18
Saint Martin                   22      1         2       19
Eritrea                        22      -         -        -
Gabon                          21      1         1       19
Myanmar                        20      1         -        -
Tanzania                       20      1         3       16
Maldives                       19      -        13        -
Haiti                          18      -         1        -
New Caledonia                  18      -         1        -
Libya                          17      1         -        -
Syria                          16      2         -        -
Benin                          16      -         2        -
Equatorial Guinea              16      -         1        -
Antigua and Barbuda            15      -         -        -
Guinea-Bissau                  15      -         -        -
Dominica                       14      -         -        -
Mongolia                       14      -         2        -
Namibia                        14      -         3        -
Saint Lucia                    13      -         1        -
Fiji                           12      -         -        -
Grenada                        12      -         -        -
Curaçao                        11      1         3        7
Sudan                          10      2         2        6
Suriname                       10      1         -        -
Greenland                      10      -         3        -
Laos                           10      -         -        -
Mozambique                     10      -         -        -
Seychelles                     10      -         -        -
MS Zaandam                      9      2         -        -
Zimbabwe                        9      1         -        -
Saint Kitts and Nevis           9      -         -        -
Eswatini                        9      -         -        -
Angola                          8      2         1        5
CAR                             8      -         -        -
Chad                            8      -         -        -
Vatican City                    7      -         -        -
Liberia                         7      -         -        -
St. Vincent Grenadines          7      -         1        -
Somalia                         7      -         1        -
Cabo Verde                      6      1         -        -
Mauritania                      6      1         2        3
Nepal                           6      -         1        -
Montserrat                      6      -         -        -
St. Barth                       6      -         1        -
Nicaragua                       5      1         -        -
Bhutan                          5      -         2        -
Turks and Caicos                5      -         -        -
Botswana                        4      1         -        -
Gambia                          4      1         2        1
Belize                          4      -         -        -
Anguilla                        3      -         -        -
British Virgin Islands          3      -         -        -
Burundi                         3      -         -        -
Malawi                          3      -         -        -
Caribbean Netherlands           2      -         -        -
Sierra Leone                    2      -         -        -
Falkland Islands                1      -         -        -
Papua New Guinea                1      -         -        -
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
2020-03-31   857487.0
2020-04-01   932605.0
2020-04-02  1013157.0
2020-04-03  1095917.0
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
2020-03-30       8.64
2020-03-31       9.60
2020-04-01       8.76
2020-04-02       8.64
2020-04-03       8.17
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

