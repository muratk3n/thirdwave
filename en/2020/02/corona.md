# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 50, 100, 200, 1000, 2000, 10000, 100000,200000, 400000]
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
Total Confirmed 946875.0

Updated: 2020-04-02 12:58:56.913111
```

Sympotatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( 'Symp. Death Rate =', np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
Symp. Death Rate = 19.37 %
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
United States              215344   5112      8878   201354
Italy                      110574  13155     16847    80572
Spain                      110238  10003     26743    73492
China                       81589   3318     76408     1863
Germany                     77981    931     19175    57875
France                      56989   4032     10935    42022
Iran                        47593   3036     15473    29084
United Kingdom              29474   2352       135    26987
Switzerland                 17781    488      2967    14326
Turkey                      15679    277       333    15069
Belgium                     15348   1011      2495    11842
Netherlands                 13614   1173       250    12191
Austria                     10842    158      1749     8935
South Korea                  9976    169      5828     3979
Canada                       9731    129      1736     7866
Portugal                     8251    187        43     8021
Brazil                       6931    244       127     6560
Israel                       6211     31       289     5891
Australia                    5137     25       345     4767
Sweden                       4947    239       103     4605
Norway                       4898     45        13     4840
Czech Republic               3604     40        61     3503
Russia                       3548     30       235     3283
Ireland                      3447     85         5     3357
Denmark                      3355    104       894     2357
Malaysia                     3116     50       767     2299
Chile                        3031     16       234     2781
Ecuador                      2758     98        58     2602
Philippines                  2633    107        51     2475
Poland                       2633     45        56     2532
Romania                      2460     94       252     2114
Japan                        2384     57       472     1855
Luxembourg                   2319     29        80     2210
Pakistan                     2291     31       107     2153
India                        2032     58       148     1826
Thailand                     1875     15       505     1355
Indonesia                    1790    170       112     1508
Saudi Arabia                 1720     16       264     1440
Finland                      1518     17       300     1201
Greece                       1415     51        52     1312
South Africa                 1380      5        50     1325
Mexico                       1378     37        35     1306
Peru                         1323     47       394      882
Panama                       1317     32         9     1276
Dominican Republic           1284     57         9     1218
Iceland                      1220      2       236      982
Argentina                    1133     33       248      852
Colombia                     1065     17        39     1009
Serbia                       1060     28        42      990
Singapore                    1000      4       245      751
Croatia                       963      6        73      884
Slovenia                      897     16        10      871
Estonia                       858     11        45      802
Algeria                       847     58        61      728
Qatar                         835      2        71      762
United Arab Emirates          814      8        61      745
Ukraine                       804     20        13      771
Hong Kong                     802      4       154      644
New Zealand                   797      1        92      704
Egypt                         779     52       179      548
Iraq                          728     52       182      494
Diamond Princess              712     11       619       82
Morocco                       676     39        29      608
Armenia                       663      4        33      626
Lithuania                     649      8         7      634
Hungary                       585     21        42      522
Bahrain                       569      4       337      228
Bosnia and Herzegovina        512     15        20      477
Lebanon                       494     16        43      435
Latvia                        458      -         1        -
Bulgaria                      449     10        25      414
Tunisia                       423     12         5      406
Moldova                       423      5        23      395
Kazakhstan                    402      3        27      372
Azerbaijan                    400      5        26      369
Slovakia                      400      1         3      396
Andorra                       390     14        10      366
Costa Rica                    375      2         4      369
North Macedonia               354     11        17      326
Uruguay                       350      2        62      286
Kuwait                        342      -        81        -
Taiwan                        339      5        50      284
Cyprus                        320      9        28      283
Burkina Faso                  282     16        46      220
Réunion                       281      -        40        -
Jordan                        278      5        36      237
Albania                       277     16        67      194
Cameroon                      255      6        10      239
Afghanistan                   239      4         5      230
San Marino                    236     28        13      195
Oman                          231      1        57      173
Vietnam                       222      -        75        -
Honduras                      219     14         3      202
Cuba                          212      6        12      194
Ghana                         195      5        31      159
Uzbekistan                    190      2        12      176
Ivory Coast                   190      1         9      180
Senegal                       190      1        45      144
Malta                         188      -         2        -
Faeroe Islands                177      -        81        -
Nigeria                       174      2         9      163
Channel Islands               172      3         -        -
Belarus                       163      2        53      108
Mauritius                     161      7         -        -
Palestine                     155      1        18      136
Sri Lanka                     148      3        21      124
Venezuela                     144      3        43       98
Montenegro                    140      2         -        -
Martinique                    135      3        27      105
Brunei                        133      1        56       76
Georgia                       130      -        26        -
Guadeloupe                    125      6        24       95
DRC                           123     11         3      109
Bolivia                       123      7         1      115
Mayotte                       116      1        10      105
Kyrgyzstan                    116      -         5        -
Cambodia                      110      -        34        -
Trinidad and Tobago            90      5         1       84
Rwanda                         82      -         -        -
Kenya                          81      1         3       77
Gibraltar                      81      -        34        -
Paraguay                       77      3         2       72
Isle of Man                    75      1         -        -
Niger                          74      5         -        -
Liechtenstein                  72      -         -        -
Madagascar                     57      -         -        -
Bangladesh                     56      6        25       25
Monaco                         55      1         2       52
Aruba                          55      -         1        -
French Guiana                  51      -        15        -
Guatemala                      46      1        12       33
Barbados                       45      -         -        -
Jamaica                        44      3         2       39
Uganda                         44      -         -        -
El Salvador                    41      2         -        -
Macao                          41      -        10        -
French Polynesia               37      -         -        -
Togo                           36      2        10       24
Zambia                         36      -         -        -
Djibouti                       33      -         -        -
Bermuda                        32      -        10        -
Mali                           31      3         -        -
Guinea                         30      -         -        -
Ethiopia                       29      -         2        -
Congo                          22      2         -        -
Cayman Islands                 22      1         -        -
Saint Martin                   22      1         2       19
Bahamas                        21      1         1       19
Tanzania                       20      1         1       18
Guyana                         19      4         -        -
Maldives                       19      -        13        -
Gabon                          18      1         -        -
Eritrea                        18      -         -        -
New Caledonia                  18      -         1        -
Myanmar                        16      1         -        -
Sint Maarten                   16      1         6        9
Haiti                          16      -         1        -
Equatorial Guinea              15      -         1        -
Mongolia                       14      -         2        -
Namibia                        14      -         2        -
Benin                          13      -         1        -
Saint Lucia                    13      -         1        -
Dominica                       12      -         -        -
Curaçao                        11      1         3        7
Syria                          10      2         -        -
Greenland                      10      -         2        -
Grenada                        10      -         -        -
Laos                           10      -         -        -
Libya                          10      -         -        -
Mozambique                     10      -         -        -
Seychelles                     10      -         -        -
Suriname                       10      -         -        -
MS Zaandam                      9      2         -        -
Guinea-Bissau                   9      -         -        -
Eswatini                        9      -         -        -
Angola                          8      2         1        5
Zimbabwe                        8      1         -        -
Saint Kitts and Nevis           8      -         -        -
Sudan                           7      2         2        3
Antigua and Barbuda             7      -         -        -
Chad                            7      -         -        -
Fiji                            7      -         -        -
Cabo Verde                      6      1         -        -
Mauritania                      6      1         2        3
Vatican City                    6      -         -        -
Liberia                         6      -         -        -
St. Barth                       6      -         1        -
Turks and Caicos                6      -         -        -
Nicaragua                       5      1         -        -
Nepal                           5      -         1        -
Bhutan                          5      -         1        -
Montserrat                      5      -         -        -
Somalia                         5      -         1        -
Botswana                        4      1         -        -
Gambia                          4      1         2        1
Belize                          3      -         -        -
British Virgin Islands          3      -         -        -
CAR                             3      -         -        -
Anguilla                        2      -         -        -
Burundi                         2      -         -        -
Caribbean Netherlands           2      -         -        -
St. Vincent Grenadines          2      -         1        -
Sierra Leone                    2      -         -        -
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
2020-03-29     720117
2020-03-30     782365
2020-03-31     857487
2020-04-01     932605
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
2020-03-28      11.36
2020-03-29       8.99
2020-03-30       8.64
2020-03-31       9.60
2020-04-01       8.76
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

