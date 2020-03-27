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
Total Confirmed 549136.0

Updated: 2020-03-27 14:13:29.705739
```

Death Rate

```python
recov = df['Recovered'].str.replace(",","").astype(np.float).sum() 
death = df['Deaths'].str.replace(",","").astype(np.float).sum()
print ( 'Death Rate =', np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
Death Rate = 16.2 %
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
United States             85,749  1,304     1,868
China                     81,340  3,292    74,588
Italy                     80,589  8,215    10,361
Spain                     64,059  4,858     9,357
Germany                   47,278    281     5,673
Iran                      32,332  2,378    11,133
France                    29,155  1,696     4,948
Switzerland               11,951    197       897
United Kingdom            11,658    578       135
South Korea                9,332    139     4,528
Netherlands                7,431    434         3
Belgium                    7,284    289       858
Austria                    7,196     58       225
Canada                     4,043     39       228
Turkey                     3,629     75        26
Portugal                   3,544     60        43
Norway                     3,441     15         6
Australia                  3,180     13       170
Israel                     3,035     10        79
Brazil                     2,988     77         6
Sweden                     2,858     77        16
Malaysia                   2,161     26       259
Czech Republic             2,062      9        10
Denmark                    2,010     41         1
Ireland                    1,819     19         5
Luxembourg                 1,453      9         6
Ecuador                    1,403     34         3
Japan                      1,387     47       359
Chile                      1,306      4        22
Romania                    1,292     24       115
Pakistan                   1,252      9        23
Poland                     1,244     16         7
Thailand                   1,136      5        97
Indonesia                  1,046     87        46
Finland                    1,038      5        10
Russia                     1,036      3        45
Saudi Arabia               1,012      3        33
South Africa                 927      2        12
Greece                       892     27        42
Philippines                  803     54        31
Iceland                      802      2        82
India                        775     20        71
Diamond Princess             712     10       597
Singapore                    683      2       172
Panama                       674      9         2
Slovenia                     632      6        10
Argentina                    589     12        72
Mexico                       585      8         4
Peru                         580      9        14
Estonia                      575      1        11
Croatia                      551      3        37
Qatar                        549      -        43
Hong Kong                    518      4       111
Egypt                        495     24       102
Colombia                     491      6         8
Dominican Republic           488     10         3
Bahrain                      466      4       210
Serbia                       457      7        15
Lebanon                      391      7        23
Iraq                         382     36       105
New Zealand                  368      -        37
Algeria                      367     25        29
Lithuania                    345      5         1
United Arab Emirates         333      2        52
Armenia                      329      1        18
Hungary                      300     10        34
Latvia                       280      -         1
Bulgaria                     276      3         8
Morocco                      275     11         8
Slovakia                     269      -         2
Taiwan                       267      2        30
Uruguay                      238      -         -
Costa Rica                   231      2         2
Bosnia and Herzegovina       230      3         5
Tunisia                      227      6         2
Ukraine                      226      5         4
Kuwait                       225      -        57
Andorra                      224      3         1
Jordan                       212      -         2
San Marino                   208     21         4
North Macedonia              201      3         3
Albania                      186      8        17
Moldova                      177      2         2
Vietnam                      153      -        20
Burkina Faso                 152      7        10
Cyprus                       146      3         4
Faeroe Islands               144      -        54
Ghana                        136      4         1
Réunion                      135      -         1
Malta                        134      -         2
Oman                         131      -        23
Kazakhstan                   125      1         2
Azerbaijan                   122      3        15
Senegal                      119      -        11
Brunei                       115      -        11
Venezuela                    107      1        15
Sri Lanka                    106      -         7
Cambodia                      98      -        11
Ivory Coast                   96      -         3
Afghanistan                   94      4         2
Belarus                       94      -        29
Palestine                     91      1        17
Cameroon                      88      2         2
Uzbekistan                    83      1         5
Mauritius                     81      2         -
Martinique                    81      1         -
Georgia                       81      -        13
Guadeloupe                    73      1         -
Montenegro                    70      1         -
Cuba                          67      2         1
Honduras                      67      1         -
Channel Islands               66      1         -
Nigeria                       65      1         3
Trinidad and Tobago           65      1         -
Bolivia                       61      -         -
Kyrgyzstan                    58      -         -
Liechtenstein                 56      -         -
Paraguay                      52      3         1
DRC                           51      3         2
Mayotte                       50      -         -
Rwanda                        50      -         -
Bangladesh                    48      5        11
Gibraltar                     35      -        13
Macao                         33      -        10
Monaco                        33      -         1
Kenya                         31      1         1
French Polynesia              30      -         -
Isle of Man                   29      -         -
Aruba                         28      -         1
French Guiana                 28      -         6
Jamaica                       26      1         2
Guatemala                     25      1         4
Togo                          25      -         1
Barbados                      24      -         -
Madagascar                    23      -         -
Uganda                        18      -         -
Ethiopia                      16      -         -
Zambia                        16      -         -
Bermuda                       15      -         2
New Caledonia                 15      -         -
Maldives                      14      -         9
El Salvador                   13      -         -
Tanzania                      13      -         -
Equatorial Guinea             12      -         -
Djibouti                      11      -         -
Dominica                      11      -         -
Mongolia                      11      -         -
Saint Martin                  11      -         -
Niger                         10      1         -
Bahamas                        9      -         1
Greenland                      9      -         2
Cayman Islands                 8      1         -
Guinea                         8      -         -
Haiti                          8      -         -
Namibia                        8      -         2
Suriname                       8      -         -
Curaçao                        7      1         2
Gabon                          7      1         -
Antigua and Barbuda            7      -         -
Grenada                        7      -         -
Mozambique                     7      -         -
Seychelles                     7      -         -
Benin                          6      -         -
Eritrea                        6      -         -
Laos                           6      -         -
Eswatini                       6      -         -
Cabo Verde                     5      1         -
Guyana                         5      1         -
Zimbabwe                       5      1         -
Fiji                           5      -         -
Montserrat                     5      -         -
Myanmar                        5      -         -
Syria                          5      -         -
Angola                         4      -         -
Congo                          4      -         -
Vatican City                   4      -         -
Mali                           4      -         -
Gambia                         3      1         -
Sudan                          3      1         -
Nepal                          3      -         1
Bhutan                         3      -         -
CAR                            3      -         -
Chad                           3      -         -
Liberia                        3      -         -
Mauritania                     3      -         -
St. Barth                      3      -         -
Saint Lucia                    3      -         1
Sint Maarten                   3      -         -
Somalia                        3      -         -
Nicaragua                      2      1         -
Anguilla                       2      -         -
Belize                         2      -         -
British Virgin Islands         2      -         -
Guinea-Bissau                  2      -         -
Saint Kitts and Nevis          2      -         -
Turks and Caicos               2      -         -
Libya                          1      -         -
Papua New Guinea               1      -         -
St. Vincent Grenadines         1      -         -
Timor-Leste                    1      -         -
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
2020-03-23     378235
2020-03-24     418045
2020-03-25     467653
2020-03-26     529591
```

![](timeseries.png)


```python
(confirmed.pct_change()*100.0).plot()
plt.title('Daily % Change')
plt.savefig('rate.png')
```

![](rate.png)


```python
avg_since_mar1 = confirmed[confirmed > '2020-03-01'].pct_change().mean()
print ('avg daily chg since march', np.round(np.float(avg_since_mar1 * 100.0),2), '%')
```

```text
avg daily chg since march 12.21 %
```

Files - [corona.csv](corona.csv), [corona-time.zip](corona-time.zip), [alpha3country.csv](alpha3country.csv), [util.py](util.py)

[Reference](https://www.worldometers.info/coronavirus/)

[Colors](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)