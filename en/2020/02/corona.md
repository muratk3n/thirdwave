# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 20, 50, 100, 200, 1000, 2000, 100000]
colors = ["mistyrose","lightsalmon","salmon", "lightcoral",\
          "tomato","red","firebrick"]	      
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
        if ('str' in str(type(c))): ax.add_geometries(n.geometry, ccrs.PlateCarree(), facecolor=col_dict[n.attributes['ADM0_A3']])
plt.savefig('corworld.png')
```

![](corworld.png)

```python
import datetime
print ('Total Confirmed', df['Confirmed'].str.replace(",","").astype(np.float).sum() )
print ('\nUpdated:',datetime.datetime.now())
```

```text
Total Confirmed 220313.0

Updated: 2020-03-19 12:48:56.721072
```

Death Rate

```python
recov = df['Recovered'].str.replace(",","").astype(np.float).sum() 
death = df['Deaths'].str.replace(",","").astype(np.float).sum()
print ( 'Death Rate =', np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
Death Rate = 9.48 %
```

```python
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10000)
pd.set_option('precision', 2)
pd.set_option('display.float_format', lambda x: '%.3f' % x) 
print (df.set_index('Country').fillna('-'))
```

```text
                       Confirmed Deaths Recovered
Country                                          
China                     80,928  3,245    70,420
Italy                     35,713  2,978     4,025
Iran                      17,361  1,135     5,710
Spain                     14,769    638     1,081
Germany                   12,343     28       105
United States              9,464    155       108
France                     9,134    264       602
South Korea                8,565     91     1,947
Switzerland                3,115     33        15
United Kingdom             2,626    104        65
Netherlands                2,051     58         2
Austria                    1,843      5         9
Norway                     1,599      6         1
Belgium                    1,486     14        31
Sweden                     1,301     10        15
Denmark                    1,132      4         1
Japan                        923     32       191
Malaysia                     900      2        75
Canada                       727      9        12
Diamond Princess             712      7       527
Australia                    687      6        43
Portugal                     642      2         4
Czech Republic               572      -         3
Brazil                       529      4         2
Israel                       529      -        13
Qatar                        452      -         4
Greece                       418      5        14
Ireland                      366      2         5
Finland                      359      -        10
Luxembourg                   335      4         -
Singapore                    313      -       117
Indonesia                    311     25        11
Pakistan                     307      2        13
Poland                       305      5        13
Slovenia                     286      1         -
Thailand                     272      1        42
Romania                      260      -        19
Estonia                      258      -         1
Bahrain                      256      1        95
Iceland                      250      -         5
Saudi Arabia                 238      -         6
Chile                        238      -         -
Egypt                        210      6        28
Philippines                  202     17         7
Hong Kong                    193      4        95
Turkey                       191      2         -
India                        174      3        15
Ecuador                      168      3         1
Iraq                         164     12        43
Kuwait                       148      -        18
Russia                       147      1         8
Peru                         145      -         1
San Marino                   140     14         4
Lebanon                      139      4         4
Mexico                       118      1         4
South Africa                 116      -         -
Armenia                      115      -         1
United Arab Emirates         113      -        26
Slovakia                     111      -         -
Panama                       109      1         -
Taiwan                       108      1        26
Colombia                     102      -         1
Croatia                       99      -         5
Argentina                     97      3         3
Serbia                        97      -         1
Bulgaria                      94      3         -
Latvia                        86      -         1
Algeria                       82      7        32
Uruguay                       79      -         -
Vietnam                       76      -        16
Hungary                       73      1         2
Faeroe Islands                72      -         1
Costa Rica                    69      1         -
Brunei                        68      -         -
Albania                       59      2         -
Cyprus                        58      -         -
Jordan                        56      -         1
Morocco                       54      2         1
Andorra                       53      -         1
Sri Lanka                     53      -         3
Belarus                       51      -         5
Malta                         48      -         2
Kazakhstan                    44      -         -
Palestine                     44      -         -
North Macedonia               43      -         1
Georgia                       40      -         1
Oman                          39      -        13
Bosnia and Herzegovina        39      -         2
Cambodia                      37      -         1
Moldova                       36      1         1
Senegal                       36      -         2
Venezuela                     36      -         -
Dominican Republic            34      2         -
Azerbaijan                    34      1         7
Lithuania                     34      -         1
Guadeloupe                    33      -         -
Tunisia                       29      -         1
New Zealand                   28      -         -
Liechtenstein                 28      -         -
Burkina Faso                  27      1         -
Martinique                    23      1         -
Uzbekistan                    23      -         -
Afghanistan                   22      -         1
Bangladesh                    17      1         3
Macao                         17      -        10
Ukraine                       16      2         -
Jamaica                       15      1         2
French Guiana                 15      -         -
DRC                           14      -         -
Réunion                       14      -         -
Cameroon                      13      -         -
Maldives                      13      -         -
Bolivia                       12      -         -
Honduras                      12      -         -
Cuba                          11      1         -
Paraguay                      11      -         -
Rwanda                        11      -         -
Monaco                         9      -         -
Ivory Coast                    9      -         1
Ghana                          9      -         -
Trinidad and Tobago            9      -         -
Guatemala                      8      1         -
Nigeria                        8      -         1
Gibraltar                      8      -         2
Guam                           8      -         -
Montenegro                     8      -         -
Channel Islands                7      -         -
Kenya                          7      -         -
Ethiopia                       6      -         -
French Polynesia               6      -         -
Mongolia                       6      -         -
Puerto Rico                    6      -         -
Seychelles                     6      -         -
Guyana                         4      1         -
Aruba                          4      -         -
Equatorial Guinea              4      -         -
Curaçao                        3      1         -
Gabon                          3      -         -
Kyrgyzstan                     3      -         -
Mauritius                      3      -         -
Mayotte                        3      -         -
St. Barth                      3      -         -
Saint Martin                   3      -         -
Tanzania                       3      -         -
Sudan                          2      1         -
Barbados                       2      -         -
Benin                          2      -         -
Bermuda                        2      -         -
Greenland                      2      -         -
Liberia                        2      -         -
Mauritania                     2      -         -
Namibia                        2      -         -
New Caledonia                  2      -         -
Saint Lucia                    2      -         -
U.S. Virgin Islands            2      -         -
Zambia                         2      -         -
Cayman Islands                 1      1         -
Nepal                          1      -         1
Antigua and Barbuda            1      -         -
Bahamas                        1      -         -
Bhutan                         1      -         -
CAR                            1      -         -
Congo                          1      -         -
Djibouti                       1      -         -
El Salvador                    1      -         -
Fiji                           1      -         -
Gambia                         1      -         -
Guinea                         1      -         -
Vatican City                   1      -         -
Montserrat                     1      -         -
Nicaragua                      1      -         -
St. Vincent Grenadines         1      -         -
Sint Maarten                   1      -         -
Somalia                        1      -         -
Suriname                       1      -         -
Eswatini                       1      -         -
Togo                           1      -         -
```

[corona.csv](corona.csv), [alpha3country.csv](alpha3country.csv), [util.py](util.py)

[Data](https://www.worldometers.info/coronavirus/)

