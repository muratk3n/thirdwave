
https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_outbreak

```python
import pandas as pd, csv

df1 = pd.read_csv('corona.csv',sep='\t')
d1 = df1[['Country','Confirmed']].set_index('Country').to_dict()
df2 = pd.read_csv('alpha3country.csv',sep=',', skipinitialspace=True)
d2 = df2[['Country','Alpha-3 code']].set_index('Country').to_dict()

res = []
for c in d1['Confirmed'].keys():
    code = d2['Alpha-3 code'].get(c.strip())
    val = float(d1['Confirmed'][c].replace(",",""))
    if code: res.append([val, code])
    
df = pd.DataFrame(res)

bins = [0, 50, 100, 200, 500, 2000, 5000, 10000]
colors = ["mistyrose","lightsalmon","salmon","lightcoral","tomato","red","firebrick"]
df['colors'] = pd.cut(np.array(df[0]), bins=bins, labels=colors)
col_dict = df.set_index(1)['colors'].to_dict()
col_dict
```

```text
Out[1]: 
{'ARE': 'mistyrose',
 'AUS': 'mistyrose',
 'BEL': 'mistyrose',
 'CAN': 'mistyrose',
 'CHN': nan,
 'DEU': 'mistyrose',
 'EGY': 'mistyrose',
 'ESP': 'mistyrose',
 'FIN': 'mistyrose',
 'FRA': 'mistyrose',
 'GBR': 'mistyrose',
 'HKG': 'lightsalmon',
 'IND': 'mistyrose',
 'ISR': 'mistyrose',
 'ITA': 'lightsalmon',
 'JPN': 'salmon',
 'KHM': 'mistyrose',
 'KOR': 'lightcoral',
 'LBN': 'mistyrose',
 'LKA': 'mistyrose',
 'MYS': 'mistyrose',
 'NPL': 'mistyrose',
 'PHL': 'mistyrose',
 'RUS': 'mistyrose',
 'SGP': 'lightsalmon',
 'SWE': 'mistyrose',
 'THA': 'mistyrose',
 'TWN': 'mistyrose',
 'USA': 'mistyrose',
 'VNM': 'mistyrose'}
```






















