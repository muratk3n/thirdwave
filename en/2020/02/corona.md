# The Coronavirus Map

```python
import util, pandas as pd

bins = [0, 100, 200, 1000, 2000, 10000, 100000, 800000, 1200000]
colors = ["lightsalmon","lightcoral", "tomato","red",\
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
Total Confirmed 7910395.0

Updated: 2020-06-14 17:41:32.915791
```

Symptomatic Death Rate

```python
recov = df['Recovered'].sum() 
death = df['Deaths'].sum()
print ( np.round(  death / (death + recov) * 100.0, 2) , '%')
```

```text
10.09 %
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
United States             2143648 117555    854106  1171987
Brazil                     851321  42802    437512   371007
Russia                     528964   6948    280050   241966
India                      324482   9247    164803   150432
United Kingdom             294375  41662         -        -
Spain                      290685  27136         -        -
Italy                      236651  34301    174865    27485
Peru                       225132   6498    111724   106910
Germany                    187489   8867    172200     6422
Iran                       187427   8837    148674    29916
Turkey                     176677   4792    150087    21798
Chile                      167355   3101    137296    26958
France                     156813  29398     72808    54607
Mexico                     142690  16872    104975    20843
Pakistan                   139230   2632     51735    84863
Saudi Arabia               127541    972     84720    41849
Canada                      98410   8107     59354    30949
Bangladesh                  87520   1171     18730    67619
China                       83132   4634     78369      129
Qatar                       79602     73     56898    22631
South Africa                65736   1423     36850    27463
Belgium                     60029   9655     16589    33785
Belarus                     53973    308     30103    23562
Sweden                      51614   4874         -        -
Netherlands                 48783   6059         -        -
Colombia                    48746   1592     19426    27728
Ecuador                     46356   3874     22865    19617
Egypt                       42980   1484     11529    29967
United Arab Emirates        42294    289     27462    14543
Singapore                   40604     26     28808    11770
Indonesia                   38277   2134     14531    21612
Portugal                    36690   1517     22669    12504
Kuwait                      35920    296     26759     8865
Ukraine                     31154    889     14082    16183
Switzerland                 31117   1938     28800      379
Argentina                   30295    819      9564    19912
Poland                      29392   1247     14226    13919
Philippines                 25930   1088      5954    18888
Ireland                     25295   1705     22698      892
Afghanistan                 24766    471      4725    19570
Oman                        23481    104      8454    14923
Dominican Republic          22962    592     13320     9050
Romania                     21999   1410     15719     4870
Iraq                        20209    607      8121    11481
Panama                      20059    429     13759     5871
Israel                      19008    300     15360     3348
Bahrain                     18227     41     12818     5368
Bolivia                     17842    585      2768    14489
Japan                       17382    924     15580      878
Austria                     17109    677     16059      373
Armenia                     16667    269      6214    10184
Nigeria                     15682    407      5101    10174
Kazakhstan                  14496     73      9114     5309
Serbia                      12310    254     11511      545
Denmark                     12193    597     11068      528
South Korea                 12085    277     10718     1090
Moldova                     11740    406      6623     4711
Ghana                       11422     51      4156     7215
Algeria                     10810    760      7420     2630
Czech Republic               9991    328      7219     2444
Azerbaijan                   9570    115      5309     4146
Guatemala                    9491    367      1804     7320
Morocco                      8734    212      7725      797
Cameroon                     8681    212      4836     3633
Norway                       8629    242      8138      249
Honduras                     8455    310       894     7251
Malaysia                     8453    121      7346      986
Australia                    7320    102      6838      380
Finland                      7104    326      6200      578
Sudan                        7007    447      2556     4004
Nepal                        5760     19       974     4767
Senegal                      5090     60      3344     1686
Uzbekistan                   5051     19      3910     1122
Tajikistan                   4971     50      3288     1633
Ivory Coast                  4848     45      2397     2406
DRC                          4778    107       600     4071
Guinea                       4484     25      3213     1246
Djibouti                     4449     41      2823     1585
Haiti                        4165     70        24     4071
Hungary                      4069    562      2482     1025
Luxembourg                   4063    110      3922       31
North Macedonia              4057    188      1710     2159
El Salvador                  3720     72      1837     1811
Kenya                        3594    100      1221     2273
Gabon                        3463     23      1024     2416
Ethiopia                     3345     57       545     2743
Bulgaria                     3266    172      1723     1371
Thailand                     3135     58      2987       90
Greece                       3112    183      1374     1555
Venezuela                    2904     24       487     2393
Bosnia and Herzegovina       2893    163      2119      611
Somalia                      2579     87       559     1933
Kyrgyzstan                   2285     27      1791      467
Mayotte                      2282     28      1790      464
Croatia                      2252    107      2134       11
Cuba                         2248     84      1948      216
CAR                          2057      7       363     1687
Maldives                     2013      8      1217      788
Estonia                      1973     69      1705      199
Sri Lanka                    1889     11      1287      591
Iceland                      1810     10      1796        4
Mali                         1776    104      1058      614
Lithuania                    1768     75      1427      266
South Sudan                  1693     27        49     1617
Mauritania                   1682     83       311     1288
Costa Rica                   1662     12       743      907
Slovakia                     1548     28      1410      110
Albania                      1521     36      1044      441
New Zealand                  1504     22      1482        0
Slovenia                     1495    109      1359       27
Nicaragua                    1464     55       953      456
Guinea-Bissau                1460     15       153     1292
Lebanon                      1446     32       868      546
Zambia                       1357     10      1114      233
Equatorial Guinea            1306     12       200     1094
Madagascar                   1272     10       367      895
Paraguay                     1261     11       647      603
Sierra Leone                 1169     51       680      438
French Guiana                1161      2       520      639
Hong Kong                    1110      4      1067       39
Latvia                       1097     28       845      224
Tunisia                      1096     49       998       49
Cyprus                        980     18       807      155
Niger                         980     66       881       33
Jordan                        953      9       678      266
Burkina Faso                  894     53       799       42
Georgia                       864     14       703      147
Andorra                       853     51       781       21
Chad                          848     72       718       58
Uruguay                       847     23       784       40
Cabo Verde                    750      6       301      443
Congo                         728     24       221      483
Diamond Princess              712     13       651       48
Yemen                         705    160        39      506
Uganda                        696      -       240        -
San Marino                    694     42       520      132
Sao Tome and Principe         659     12       176      471
Malta                         649      9       603       37
Jamaica                       615     10       420      185
Mozambique                    583      3       151      429
Channel Islands               565     48       512        5
Rwanda                        541      2       332      207
Togo                          530     13       291      226
Malawi                        529      5        66      458
Tanzania                      509     21       183      305
Palestine                     489      3       415       71
Réunion                       489      1       460       28
Eswatini                      486      3       247      236
Liberia                       446     32       214      200
Taiwan                        443      7       431        5
Libya                         418      8        62      348
Benin                         412      6       222      184
Zimbabwe                      356      4        54      298
Mauritius                     337     10       325        2
Isle of Man                   336     24       312        0
Vietnam                       334      -       323        -
Montenegro                    324      9       315        0
Myanmar                       261      6       167       88
Martinique                    202     14        98       90
Mongolia                      197      -        98        -
Suriname                      196      3         9      184
Faeroe Islands                187      -       187        -
Cayman Islands                187      1       115       71
Syria                         177      6        74       97
Comoros                       176      2       114       60
Gibraltar                     176      -       173        -
Guadeloupe                    171     14       157        0
Guyana                        159     12        95       52
Bermuda                       142      9       127        6
Brunei                        141      2       138        1
Angola                        138      6        61       71
Cambodia                      128      -       125        -
Trinidad and Tobago           117      8       109        0
Bahamas                       103     11        68       24
Aruba                         101      3        98        0
Monaco                         99      4        93        2
Barbados                       96      7        83        6
Burundi                        85      1        45       39
Liechtenstein                  82      1        55       26
Sint Maarten                   77     15        61        1
Bhutan                         66      -        21        -
Eritrea                        65      -        39        -
Botswana                       60      1        24       35
French Polynesia               60      -        60        -
Macao                          45      -        45        -
Saint Martin                   42      3        36        3
Namibia                        32      -        17        -
Gambia                         28      1        24        3
St. Vincent Grenadines         27      -        25        -
Antigua and Barbuda            26      3        20        3
Timor-Leste                    24      -        24        -
Grenada                        23      -        22        -
Curaçao                        22      1        15        6
New Caledonia                  21      -        20        -
Belize                         20      2        16        2
Laos                           19      -        19        -
Saint Lucia                    19      -        18        -
Dominica                       18      -        16        -
Fiji                           18      -        18        -
Saint Kitts and Nevis          15      -        15        -
Falkland Islands               13      -        13        -
Greenland                      13      -        13        -
Vatican City                   12      -        12        -
Turks and Caicos               12      1        11        0
Montserrat                     11      1        10        0
Seychelles                     11      -        11        -
MS Zaandam                      9      2         -        -
Western Sahara                  9      1         8        0
British Virgin Islands          8      1         7        0
Papua New Guinea                8      -         8        -
Caribbean Netherlands           7      -         7        -
St. Barth                       6      -         6        -
Lesotho                         4      -         2        -
Anguilla                        3      -         3        -
Saint Pierre Miquelon           1      -         1        -
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
2020-06-10    7376333
2020-06-11    7514724
2020-06-12    7632802
2020-06-13    7766952
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
2020-06-09       1.73
2020-06-10       1.85
2020-06-11       1.88
2020-06-12       1.57
2020-06-13       1.76
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

