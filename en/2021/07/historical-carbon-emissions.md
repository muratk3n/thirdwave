# Historical Carbon Emissions

Summary: US is the worst polluter, followed by China, USSR, UK.. These
countries are responsible for global warming.

2014 has China with double carbon emissions of US. 

Units are thousans of metric tons. [Data](https://github.com/datasets/co2-fossil-by-nation).

### Annual Emissions, Every Country

```python
import pandas as pd
url = "https://raw.githubusercontent.com/datasets/co2-fossil-by-nation/master/data/fossil-fuel-co2-emissions-by-nation.csv"
df = pd.read_csv(url)
df.loc[df.Country == 'CHINA (MAINLAND)', 'Country'] = 'China'
g = df.groupby('Year')['Total'].sum()
g.plot()
plt.savefig('ghg1.png')
```

![](ghg1.png)

### Top Polluters, All Time, 1751-2014

```python
g = df.groupby('Country')['Total'].sum()
g = g.sort_values(ascending=False)
print (g.head(30))
```

```text
Country
UNITED STATES OF AMERICA             102510260
China                                 47649834
USSR                                  30790355
UNITED KINGDOM                        20500813
JAPAN                                 14585037
GERMANY                               12764185
INDIA                                 11385351
RUSSIAN FEDERATION                    10466421
FRANCE (INCLUDING MONACO)              9697149
CANADA                                 8038299
FEDERAL REPUBLIC OF GERMANY            7492600
POLAND                                 6960097
ITALY (INCLUDING SAN MARINO)           6032718
SOUTH AFRICA                           5030416
MEXICO                                 4768665
AUSTRALIA                              4252724
ISLAMIC REPUBLIC OF IRAN               4028153
REPUBLIC OF KOREA                      3824538
SPAIN                                  3529437
BRAZIL                                 3513002
FORMER GERMAN DEMOCRATIC REPUBLIC      3323467
SAUDI ARABIA                           3266162
BELGIUM                                3184611
CZECHOSLOVAKIA                         3068081
INDONESIA                              2999862
NETHERLANDS                            2966741
UKRAINE                                2200321
ROMANIA                                2188014
TURKEY                                 2184948
ARGENTINA                              2013085
Name: Total, dtype: int64
```

```python
int(102510260 / 2999862)
```

```text
Out[1]: 34
```

### Top Polluters 2014

```python
df1 = df[df['Year'] == 2014]
df1 = df1.sort_values(by='Total',ascending=False)
df1 = df1.set_index('Country').head(10)['Total']
df1.plot.barh(fontsize=8)
plt.savefig('ghg2.png')
print (df1)
```

```text
Country
China                       2806634
UNITED STATES OF AMERICA    1432855
INDIA                        610411
RUSSIAN FEDERATION           465052
JAPAN                        331074
GERMANY                      196314
ISLAMIC REPUBLIC OF IRAN     177115
SAUDI ARABIA                 163907
REPUBLIC OF KOREA            160119
CANADA                       146494
Name: Total, dtype: int64
```

![](ghg2.png)



