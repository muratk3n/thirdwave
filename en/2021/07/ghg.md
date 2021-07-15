
Thousans of metric tons


```python
url = "https://raw.githubusercontent.com/datasets/co2-fossil-by-nation/master/data/fossil-fuel-co2-emissions-by-nation.csv"

import pandas as pd

df = pd.read_csv(url)
df.loc[df.Country == 'CHINA (MAINLAND)', 'Country'] = 'China'
```

```python
g = df.groupby('Year')['Total'].sum()
print (g)
g.plot()
plt.savefig('ghg1.png')
```

```text
Year
1751       2552
1752       2553
1753       2553
1754       2554
1755       2555
         ...   
2010    8701391
2011    9042599
2012    9209392
2013    9234807
2014    9306200
Name: Total, Length: 264, dtype: int64
```


```python
g = df.groupby('Country')['Total'].sum()
g = g.sort_values(ascending=False)
print (g)
```

```text
Country
UNITED STATES OF AMERICA    102510260
China                        47649834
USSR                         30790355
UNITED KINGDOM               20500813
JAPAN                        14585037
                              ...    
NIUE                               64
TUVALU                             60
PUERTO RICO                        57
LEEWARD ISLANDS                    49
ANTARCTIC FISHERIES                42
Name: Total, Length: 256, dtype: int64
```


```python
df1 = df[df['Year'] == 2014]
df1 = df1.sort_values(by='Total',ascending=False)
df1 = df1.set_index('Country').head(10)['Total']
print (df1)
df1.plot.barh(fontsize=8)
plt.savefig('ghg2.png')
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


