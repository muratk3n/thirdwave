# The Coronavirus Map

```python
import util
df, col_dict = util.retrieve_cor_data()
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
        if ('str' in str(type(c))): ax.add_geometries(n.geometry, ccrs.PlateCarree(), facecolor=col_dict[n.attributes['ADM0_A3']])
plt.savefig('corworld.png')
```

![](corworld.png)

```python
import datetime
print ('Total Confirmed', df[0].sum())
print ('\nUpdated:',datetime.datetime.now())
```

```text
Total Confirmed 217909.0

Updated: 2020-03-19 09:12:36.591380
```

Death Rate

```python
8970 / (8970+85745) * 100.0
```

```text
Out[1]: 9.47051681359869
```

```python
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10000)
pd.set_option('precision', 2)
pd.set_option('display.float_format', lambda x: '%.3f' % x) 
print (df1.set_index('Country').fillna('-'))
```

```text
                                 Confirmed Deaths Recovered
Country                                                    
China                               80,849  3,199    66,931
Italy                               21,157  1,441     1,966
Iran                                13,938    724     4,590
South Korea                          8,162     75       834
Spain                                7,753    291       517
Germany                              5,426     11        46
France                               4,499     91        12
United States                        3,083     60        56
Switzerland                          2,217     14         4
Norway                               1,206      3         1
United Kingdom                       1,140     21        18
Netherlands                          1,135     20         2
Sweden                               1,024      2         1
Belgium                                886      4         1
Denmark                                864      2         1
Austria                                860      1         6
Japan                                  814     24       144
Diamond Princess                       696      7       456
Malaysia                               428      -        42
Qatar                                  337      -         4
Australia                              300      5        27
Canada                                 255      1        11
Portugal                               245      -         2
Finland                                244      -        10
Czechia                                231      -         -
Greece                                 228      4         8
Singapore                              226      -       105
Slovenia                               219      1         -
Bahrain                                214      -        60
Israel                                 200      -         4
Iceland                                161      -         -
Hong Kong                              145      4        81
Philippines                            140     11         2
Romania                                139      -         9
Estonia                                135      -         1
Ireland                                129      2         1
Brazil                                 121      -         1
Poland                                 119      3        13
Indonesia                              117      5         8
Thailand                               114      1        35
Kuwait                                 112      -         9
Iraq                                   111     10        26
Egypt                                  110      2        27
India                                  108      2        10
Saudi Arabia                           103      -         2
San Marino                             101      5         4
Lebanon                                 99      3         1
United Arab Emirates                    86      -        20
Russia                                  63      -         8
Chile                                   61      -         -
Luxembourg                              59      1         -
Taiwan                                  59      1        20
Vietnam                                 56      -        16
Slovakia                                54      -         -
Pakistan                                53      -         2
Bulgaria                                51      2         -
South Africa                            51      -         -
Brunei                                  50      -         -
Croatia                                 49      -         2
Algeria                                 48      4        10
Serbia                                  46      -         1
Argentina                               45      2         -
Panama                                  43      1         -
Peru                                    43      -         -
Albania                                 42      1         -
Mexico                                  41      -         4
Palestine                               38      -         -
Colombia                                34      -         -
Georgia                                 33      -         1
Hungary                                 32      1         1
Latvia                                  30      -         1
Ecuador                                 28      2         -
Morocco                                 28      1         1
Belarus                                 27      -         3
Costa Rica                              27      -         -
Cyprus                                  26      -         -
Senegal                                 24      -         2
Azerbaijan                              23      1         6
Armenia                                 23      -         -
Moldova                                 23      -         -
Oman                                    22      -         9
Bosnia and Herzegovina                  21      -         -
Malta                                   21      -         2
North Macedonia                         19      -         1
Tunisia                                 18      -         -
Afghanistan                             16      -         1
Maldives                                13      -         -
Lithuania                               12      -         1
Dominican Republic                      11      -         -
Sri Lanka                               11      -         1
Faeroe Islands                          11      -         -
Macao                                   10      -        10
Bolivia                                 10      -         -
Martinique                              10      -         -
Venezuela                               10      -         -
New Zealand                              8      -         -
Jamaica                                  8      -         -
Kazakhstan                               8      -         -
Cambodia                                 7      -         1
Jordan                                   7      -         1
French Guiana                            7      -         -
Liechtenstein                            7      -         -
Paraguay                                 7      -         -
Réunion                                  7      -         -
Ghana                                    6      -         -
Turkey                                   6      -         -
Uruguay                                  6      -         -
Bangladesh                               5      -         2
Guyana                                   4      1         -
Ivory Coast                              4      -         -
Cuba                                     4      -         -
Puerto Rico                              4      -         -
Ukraine                                  3      1         -
Burkina Faso                             3      -         -
Channel Islands                          3      -         -
French Polynesia                         3      -         -
Guadeloupe                               3      -         -
Guam                                     3      -         -
Honduras                                 3      -         -
Kenya                                    3      -         -
Monaco                                   2      -         -
Nigeria                                  2      -         1
Aruba                                    2      -         -
Cameroon                                 2      -         -
Curaçao                                  2      -         -
DRC                                      2      -         -
Namibia                                  2      -         -
Saint Lucia                              2      -         -
Saint Martin                             2      -         -
Seychelles                               2      -         -
Trinidad and Tobago                      2      -         -
Sudan                                    1      1         -
Andorra                                  1      -         -
Nepal                                    1      -         1
Antigua and Barbuda                      1      -         -
Bhutan                                   1      -         -
Cayman Islands                           1      -         -
CAR                                      1      -         -
Congo                                    1      -         -
Equatorial Guinea                        1      -         -
Ethiopia                                 1      -         -
Gabon                                    1      -         -
Gibraltar                                1      -         1
Guatemala                                1      -         -
Guinea                                   1      -         -
Vatican City                             1      -         -
Mauritania                               1      -         -
Mayotte                                  1      -         -
Mongolia                                 1      -         -
Rwanda                                   1      -         -
St. Barth                                1      -         -
Saint Vincent and the Grenadines         1      -         -
Suriname                                 1      -         -
Eswatini                                 1      -         -
Togo                                     1      -         -
Virgin Islands                           1      -         -
Uzbekistan                               1      -         -
```


[corona.csv](corona.csv), [alpha3country.csv](alpha3country.csv), [util.py](util.py)

[Data](https://www.worldometers.info/coronavirus/)

