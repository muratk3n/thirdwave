# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 20, 50, 100, 200, 1000, 2000, 10000, 100000,200000]
colors = ["mistyrose","lightsalmon","salmon",\
          "lightcoral", "tomato","red",\
	  "indianred","firebrick","maroon"]
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
Total Confirmed 837021.0

Updated: 2020-03-31 20:55:28.026263
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
United States              176518   3431      6241   166846
Italy                      105792  12428     15729    77635
Spain                       94417   8269     19259    66889
China                       81518   3305     76052     2161
Germany                     68180    682     15824    51674
France                      52128   3523      7927    40678
Iran                        44605   2898     14656    27051
United Kingdom              25150   1789       135    23226
Switzerland                 16186    395      1823    13968
Turkey                      13531    214       243    13074
Belgium                     12775    705      1696    10374
Netherlands                 12595   1039       250    11306
Austria                     10109    128      1095     8886
South Korea                  9786    162      5408     4216
Canada                       8467     95      1162     7210
Portugal                     7443    160        43     7240
Israel                       4831     20       163     4648
Brazil                       4715    168       127     4420
Norway                       4605     39        13     4553
Australia                    4561     19       337     4205
Sweden                       4435    180        16     4239
Czech Republic               3257     31        45     3181
Ireland                      2910     54         5     2851
Denmark                      2860     90         1     2769
Malaysia                     2766     43       537     2186
Chile                        2738     12       156     2570
Russia                       2337     17       121     2199
Romania                      2245     80       220     1945
Ecuador                      2240     75        54     2111
Poland                       2215     32         7     2176
Luxembourg                   2178     23        80     2075
Philippines                  2084     88        49     1947
Japan                        1953     56       424     1473
Pakistan                     1914     26        76     1812
Thailand                     1651     10       342     1299
Saudi Arabia                 1563     10       165     1388
Indonesia                    1528    136        81     1311
Finland                      1418     17        10     1391
South Africa                 1353      3        31     1319
Greece                       1314     49        52     1213
India                        1251     32       102     1117
Iceland                      1135      2       198      935
Dominican Republic           1109     51         5     1053
Mexico                       1094     28        35     1031
Panama                       1075     27         9     1039
Peru                         1065     24        53      988
Argentina                     966     26       240      700
Singapore                     926      3       240      683
Serbia                        900     23        42      835
Croatia                       867      6        67      794
Slovenia                      802     15        10      777
Colombia                      798     14        15      769
Estonia                       745      4        26      715
Algeria                       716     44        46      626
Hong Kong                     714      4       128      582
Diamond Princess              712     10       603       99
Qatar                         693      1        51      641
United Arab Emirates          664      6        61      597
Egypt                         656     41       150      465
New Zealand                   647      1        74      572
Iraq                          630     46       152      432
Morocco                       602     36        24      542
Bahrain                       567      4       295      268
Ukraine                       549     13         8      528
Lithuania                     537      8         7      522
Armenia                       532      3        30      499
Hungary                       492     16        37      439
Lebanon                       463     12        37      414
Bosnia and Herzegovina        411     12        17      382
Bulgaria                      399      8        17      374
Latvia                        398      -         1        -
Andorra                       370      8        10      352
Slovakia                      363      -         3        -
Tunisia                       362     10         3      349
Moldova                       353      4        18      331
Kazakhstan                    340      2        22      316
Costa Rica                    330      2         4      324
North Macedonia               329      9        12      308
Taiwan                        322      5        39      278
Uruguay                       320      1        25      294
Azerbaijan                    298      5        26      267
Kuwait                        289      -        73        -
Jordan                        274      5        30      239
Cyprus                        262      8        23      231
Burkina Faso                  261     14        32      215
Réunion                       247      -         1        -
Albania                       243     15        52      176
San Marino                    230     25        13      192
Vietnam                       207      -        58        -
Cameroon                      193      6         5      182
Oman                          192      -        34        -
Cuba                          186      6         8      172
Senegal                       175      -        40        -
Afghanistan                   174      4         5      165
Faeroe Islands                169      -        74        -
Malta                         169      -         2        -
Ivory Coast                   168      1         6      161
Uzbekistan                    167      2         7      158
Ghana                         161      5        31      125
Belarus                       152      1        47      104
Mauritius                     143      4         -        -
Sri Lanka                     142      2        17      123
Honduras                      141      7         3      131
Channel Islands               141      3         -        -
Venezuela                     135      3        39       93
Nigeria                       135      2         8      125
Brunei                        129      1        45       83
Martinique                    119      2        27       90
Palestine                     117      1        18       98
Georgia                       110      -        21        -
Montenegro                    109      2         -        -
Cambodia                      109      -        23        -
Bolivia                       107      6         -        -
Kyrgyzstan                    107      -         3        -
Guadeloupe                    106      4        17       85
DRC                            98      8         2       88
Mayotte                        94      1        10       83
Trinidad and Tobago            85      3         1       81
Rwanda                         70      -         -        -
Gibraltar                      69      -        34        -
Liechtenstein                  68      -         -        -
Paraguay                       65      3         1       61
Isle of Man                    60      -         -        -
Kenya                          59      1         1       57
Aruba                          55      -         1        -
Monaco                         52      1         2       49
Bangladesh                     51      5        25       21
Madagascar                     46      -         -        -
French Guiana                  43      -         6        -
Macao                          41      -        10        -
Guatemala                      36      1        10       25
Jamaica                        36      1         2       33
French Polynesia               36      -         -        -
Zambia                         35      -         -        -
Togo                           34      1        10       23
Barbados                       34      -         -        -
Uganda                         33      -         -        -
El Salvador                    32      -         -        -
Djibouti                       30      -         -        -
Mali                           28      2         -        -
Niger                          27      3         -        -
Bermuda                        27      -        10        -
Ethiopia                       26      -         2        -
Guinea                         22      -         -        -
Tanzania                       19      1         1       17
Congo                          19      -         -        -
Maldives                       18      -        13        -
Gabon                          16      1         -        -
New Caledonia                  16      -         -        -
Myanmar                        15      1         -        -
Saint Martin                   15      1         2       12
Eritrea                        15      -         -        -
Haiti                          15      -         1        -
Bahamas                        14      -         1        -
Guyana                         12      2         -        -
Cayman Islands                 12      1         -        -
Dominica                       12      -         -        -
Equatorial Guinea              12      -         1        -
Mongolia                       12      -         2        -
Curaçao                        11      1         2        8
Namibia                        11      -         2        -
Syria                          10      2         -        -
Greenland                      10      -         2        -
Seychelles                     10      -         -        -
Benin                           9      -         1        -
Grenada                         9      -         -        -
Laos                            9      -         -        -
Saint Lucia                     9      -         1        -
Eswatini                        9      -         -        -
Zimbabwe                        8      1         -        -
Guinea-Bissau                   8      -         -        -
Libya                           8      -         -        -
Mozambique                      8      -         -        -
Saint Kitts and Nevis           8      -         -        -
Suriname                        8      -         -        -
Angola                          7      2         1        4
Sudan                           7      2         1        4
Antigua and Barbuda             7      -         -        -
Chad                            7      -         -        -
Cabo Verde                      6      1         -        -
Mauritania                      6      1         2        3
Vatican City                    6      -         -        -
St. Barth                       6      -         1        -
Sint Maarten                    6      -         -        -
Nepal                           5      -         1        -
Fiji                            5      -         -        -
Montserrat                      5      -         -        -
Somalia                         5      -         1        -
Turks and Caicos                5      -         -        -
Gambia                          4      1         -        -
Nicaragua                       4      1         -        -
Bhutan                          4      -         -        -
Belize                          3      -         -        -
Botswana                        3      -         -        -
British Virgin Islands          3      -         -        -
CAR                             3      -         -        -
Liberia                         3      -         -        -
MS Zaandam                      2      -         -        -
Anguilla                        2      -         -        -
Burundi                         2      -         -        -
Papua New Guinea                1      -         -        -
St. Vincent Grenadines          1      -         1        -
Sierra Leone                    1      -         -        -
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
2020-03-28   660706.0
2020-03-29   720117.0
2020-03-30   782365.0
2020-03-31   857487.0
```

![](timeseries.png)


```python
chg = confirmed.pct_change()*100.0
chg.plot()
print (chg.tail(5))
plt.title('Daily % Change')
plt.savefig('rate.png')
```

```text
            Confirmed
Date                 
2020-03-27  12.028150
2020-03-28  11.362889
2020-03-29   8.992048
2020-03-30   8.644151
2020-03-31   9.601912
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

