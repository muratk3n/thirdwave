

```python
import pandas as pd, zipfile
with zipfile.ZipFile('gtd_0615dist.csv.zip', 'r') as z:
     df = pd.read_csv(z.open('gtd_0615dist.csv'),sep=';')
```

```python
import datetime
def f(x):
    try: return datetime.date(x['iyear'], x['imonth'], x['iday'])
    except: return 0    
df2 = df[ (df.nkill >= 2) & (df.success == 1) & df.attacktype1.isin([2,3,7]) ]
df2['cdate'] = df2.apply(f, axis=1)
df2 = df2[df2['cdate'] != 0]
#df2 = df2[df2.iyear > 2000]
```

```python
def dist(arg1, arg2, title):
   x1 = arg1.copy(); x2 = arg2.copy();
   x1['status'] = 0; x2['status'] = 1
   res = pd.concat([x1, x2])
   res = res.sort_index(by=['cdate','status'])
   res['diff'] = res['status'].diff()
   res['diff2'] = res['diff'].shift(-1)
   res['cdate2'] = res['cdate'].shift(-1)
   res = res[res['diff2'] == 1]
   res['duration'] = res.apply(lambda x: (x['cdate2']-x['cdate']).days,axis=1)
   res = res[res['duration'] > 0]
   res = res[['cdate','cdate2','duration']]
   return res

dfus = df2[['cdate']][ (df2['country'] == 217)  ]
dfeu = df2[['cdate']][ (df2['region'] == 8)] 
dfsoutham = df2[['cdate']][ (df2['region'] == 3)]
dfcanada = df2[['cdate']][ (df2['country'] == 38) ] 
dfchina = df2[['cdate']][ (df2['country'] == 44) ] 
dfrussia = df2[['cdate']][ (df2['country'] == 	 167) ] 
dfaustralia = df2[['cdate']][ (df2['region'] == 12) ] 
```


```python
reseu = dist(dfus, dfeu, 'eu')
ressa = dist(dfus, dfsoutham, 'sa',)
reschi = dist(dfus, dfchina, 'chi')
resrus = dist(dfus, dfrussia, 'rus')
rescan = dist(dfus, dfcanada, 'can')
resau = dist(dfus, dfaustralia, 'au')

import scipy.stats as stats
print 'Europe', reseu.duration.mean(), len(reseu), 'datapoints'
print 'South America', ressa.duration.mean(), len(ressa), 'datapoints', stats.mannwhitneyu(reseu.duration, ressa.duration)
print 'China', reschi.duration.mean(), len(reschi), 'datapoints', stats.mannwhitneyu(reseu.duration, reschi.duration)
print 'Canada', rescan.duration.mean(), len(rescan), 'datapoints', stats.mannwhitneyu(reseu.duration, rescan.duration)
print 'Russia', resrus.duration.mean(),  len(resrus), 'datapoints', stats.mannwhitneyu(reseu.duration, resrus.duration)
print 'Australia', resau.duration.mean(),  len(resau), 'datapoints', stats.mannwhitneyu(reseu.duration, resau.duration)
```

```text
Europe 5.8202247191 267 datapoints
South America 6.06467661692 201 datapoints (22055.0, 0.00040900033043877603)
China 87.5128205128 39 datapoints (1187.0, 1.447002828524365e-15)
Canada 73.25 12 datapoints (250.0, 2.4513300011194938e-07)
Russia 32.1194029851 134 datapoints (11824.5, 1.0223249256316842e-08)
Australia 103.142857143 28 datapoints (1442.0, 2.766824589804619e-08)
```
































































