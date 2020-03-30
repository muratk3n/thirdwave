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
Total Confirmed 723823.0

Updated: 2020-03-30 11:03:56.562162
```

Death Rate

```python
recov = df['Recovered'].str.replace(",","").astype(np.float).sum() 
death = df['Deaths'].str.replace(",","").astype(np.float).sum()
print ( 'Death Rate =', np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
Death Rate = 18.3 %
```

```python
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10000)
pd.set_option('precision', 2)
pd.set_option('display.float_format', lambda x: '%.3f' % x) 
print (df.set_index('Country').fillna('-'))
```

```text
                       Confirmed  Deaths Recovered
Country                                           
United States            142,735   2,489     4,562
Italy                     97,689  10,779    13,030
China                     81,470   3,304    75,700
Spain                     80,110   6,803    14,709
Germany                   62,435     541     9,211
France                    40,174   2,606     7,202
Iran                      38,309   2,640    12,391
United Kingdom            19,522   1,228       135
Switzerland               14,829     300     1,595
Netherlands               10,866     771       250
Belgium                   10,836     431     1,359
South Korea                9,661     158     5,228
Turkey                     9,217     131       105
Austria                    8,958      86       479
Canada                     6,320      65       573
Portugal                   5,962     119        43
Israel                     4,347      15       134
Norway                     4,305      26         7
Brazil                     4,256     136         6
Australia                  4,163      18       244
Sweden                     3,700     110        16
Czech Republic             2,837      17        11
Ireland                    2,615      46         5
Malaysia                   2,470      35       388
Denmark                    2,395      72         1
Chile                      2,139       7        75
Luxembourg                 1,950      21        40
Ecuador                    1,924      58         3
Poland                     1,905      26         7
Japan                      1,866      54       424
Romania                    1,815      43       206
Pakistan                   1,625      18        29
Russia                     1,534       8        64
Thailand                   1,524       7       229
Philippines                1,418      71        42
Saudi Arabia               1,299       8        66
Indonesia                  1,285     114        64
South Africa               1,280       2        31
Finland                    1,240      11        10
Greece                     1,156      39        52
India                      1,071      29       100
Iceland                    1,020       2       135
Mexico                       993      20        35
Panama                       989      24         4
Dominican Republic           859      39         3
Peru                         852      18        16
Singapore                    844       3       212
Argentina                    820      20        91
Serbia                       741      13        42
Slovenia                     730      11        10
Estonia                      715       3        20
Croatia                      713       6        55
Diamond Princess             712      10       603
Colombia                     702      10        10
Hong Kong                    642       4       118
Qatar                        634       1        48
Egypt                        609      40       132
New Zealand                  589       1        63
United Arab Emirates         570       3        58
Iraq                         547      42       143
Morocco                      516      27        13
Bahrain                      515       4       279
Algeria                      511      31        31
Lithuania                    484       7         1
Ukraine                      475      10         6
Hungary                      447      15        34
Lebanon                      438      10        30
Armenia                      424       3        30
Latvia                       376       -         1
Bulgaria                     354       8        15
Bosnia and Herzegovina       340       6         8
Andorra                      334       6         6
Costa Rica                   314       2         3
Slovakia                     314       -         2
Tunisia                      312       8         2
Uruguay                      304       1         -
Taiwan                       298       3        39
Kazakhstan                   293       1        20
Moldova                      263       2        13
North Macedonia              259       6         3
Jordan                       259       3        18
Kuwait                       255       -        67
San Marino                   224      22         6
Burkina Faso                 222      12        23
Cyprus                       214       6        15
Albania                      212      10        33
Azerbaijan                   209       4        15
Vietnam                      194       -        52
Réunion                      183       -         1
Oman                         167       -        23
Ivory Coast                  165       1         4
Faeroe Islands               159       -        70
Ghana                        152       5         2
Malta                        151       -         2
Uzbekistan                   144       2         7
Senegal                      142       -        27
Cameroon                     139       6         5
Cuba                         139       3         4
Honduras                     139       3         3
Brunei                       126       1        34
Afghanistan                  120       4         2
Sri Lanka                    120       1        11
Venezuela                    119       3        39
Nigeria                      111       1         3
Mauritius                    110       3         -
Palestine                    109       1        18
Channel Islands              108       2         -
Guadeloupe                   106       4        17
Cambodia                     103       -        21
Georgia                       98       -        18
Bolivia                       96       1         -
Belarus                       94       -        32
Martinique                    93       1         -
Montenegro                    91       1         -
Kyrgyzstan                    84       -         -
DRC                           81       8         2
Trinidad and Tobago           78       3         1
Rwanda                        70       -         -
Gibraltar                     65       -        14
Paraguay                      64       3         1
Mayotte                       63       -         -
Liechtenstein                 56       -         -
Aruba                         50       -         1
Bangladesh                    49       5        19
Monaco                        46       1         1
French Guiana                 43       -         6
Kenya                         42       1         1
Isle of Man                   42       -         -
Madagascar                    39       -         -
Macao                         37       -        10
Guatemala                     34       1        10
Barbados                      33       -         -
Uganda                        33       -         -
Jamaica                       32       1         2
Togo                          30       1         1
El Salvador                   30       -         -
French Polynesia              30       -         -
Zambia                        29       -         -
Bermuda                       22       -         2
Ethiopia                      21       -         1
Congo                         19       -         -
Mali                          18       1         -
Niger                         18       1         -
Djibouti                      18       -         -
Maldives                      17       -        13
Guinea                        16       -         -
Haiti                         15       -         1
New Caledonia                 15       -         -
Bahamas                       14       -         1
Tanzania                      14       -         1
Cayman Islands                12       1         -
Equatorial Guinea             12       -         -
Eritrea                       12       -         -
Mongolia                      12       -         2
Dominica                      11       -         -
Namibia                       11       -         2
Saint Martin                  11       -         -
Greenland                     10       -         2
Myanmar                       10       -         -
Syria                          9       1         -
Grenada                        9       -         -
Saint Lucia                    9       -         1
Eswatini                       9       -         -
Curaçao                        8       1         2
Guyana                         8       1         -
Laos                           8       -         -
Libya                          8       -         -
Mozambique                     8       -         -
Seychelles                     8       -         -
Suriname                       8       -         -
Angola                         7       2         -
Gabon                          7       1         -
Zimbabwe                       7       1         -
Antigua and Barbuda            7       -         -
Cabo Verde                     6       1         -
Sudan                          6       1         -
Benin                          6       -         -
Vatican City                   6       -         -
Sint Maarten                   6       -         -
Nepal                          5       -         1
Fiji                           5       -         -
Mauritania                     5       -         2
Montserrat                     5       -         -
St. Barth                      5       -         -
Gambia                         4       1         -
Nicaragua                      4       1         -
Bhutan                         4       -         -
Turks and Caicos               4       -         -
CAR                            3       -         -
Chad                           3       -         -
Liberia                        3       -         -
Somalia                        3       -         -
MS Zaandam                     2       -         -
Anguilla                       2       -         -
Belize                         2       -         -
British Virgin Islands         2       -         -
Guinea-Bissau                  2       -         -
Saint Kitts and Nevis          2       -         -
Papua New Guinea               1       -         -
St. Vincent Grenadines         1       -         1
Timor-Leste                    1       -         -
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

County Level Data (NYT)

```python
! wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
! zip $HOME/Downloads/corona-county.zip us-counties.csv
! rm us-counties.csv
```


Files - [corona.csv](corona.csv), [corona-time.zip](corona-time.zip), [alpha3country.csv](alpha3country.csv), [util.py](util.py)

[Colors](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)

[Reference](https://www.worldometers.info/coronavirus/)

