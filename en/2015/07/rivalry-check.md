# Rivalry Check

Why would this rivalry exist? More importantly, for the data
investigation, how would this rivalry leave its mark in data so it can
be caught?

Let's look at the evolutionary landscape: we are transitioning to a
supersymbolic economy in which the most precious resource is
talent. US wants talent, does not want to lose it to EU. Talent wants
nice cities, safe environment, nice parks. That means if US suffers a
terror attack of any kind, it would have a bad image for talent. Then,
the theory goes US' shadowy pukes would instigate an attack in Europe
in short time, in response, to balance their image.

My plan was I would get terror attack data, look at US-EU pairing
first, for each US attack, calculate the difference in days to the
closest EU attack. These collection of numbers are "waiting times" for
this supposed tit-for-tat scenario. Then I calculate the same numbers
for US-South America, US-China so forth. Now we have bunch of numbers
for each pairing representing their distributions. We then check if
US-EU numbers are smaller than all the rest of the regional waiting
times, and if that smallness is statistically significant. [geek] The
statistical test to use for this is two sample Wilcoxon test, as the
waiting time data is distributed non-normally -exponentially- [/geek].

First I wanted to use GDELT data in this analysis, Google provides
access to it, but  it turns out GDELT has a lot of repeats, i.e. for
Charleston attack people mourning about it, commenting etc. would
appear as data points with an incorrect status code indicating an
actual attack. The GDELT option would need a lot of dedup code. So I
looked for other data sources, and found [GTD](http://www.start.umd.edu/gtd/)
available in Excel format covering attacks between 1970-2014.
I converted it into CSV and [zipped it](https://drive.google.com/uc?export=view&id=1YnXq12oxw6ijwq3hcrfxcqND96Jyoe2d),
code at the bottom.

[geek]Me not like binary formats like Excel, oddly it turns out zipped
up CSV is smaller than xlsx, and processed by Python Pandas at the
same speed [/geek].

The analysis showed, at first, looking at all data, US-EU attack
delays are smaller than all the rest, and the difference was
significant.

The wait times were smaller than even for US-South America pairing
where one would expect drug related crimes would be common. But the
moment we change date filter to look at data after 1980, things
change. Then US-EU and US-SA are not statistically different from
eachother (but still smaller from other regions, China, Russia,
Australia, Canada). 70s must have been a bad time in Europe. Also,
removing UK from Europe list, even for the entire time periods, again
causes a US-SA tie, possibly due to all these IRA attacks there. But
since UK is part of Europe (heh heh) I kept its data in the US-EU
calc.

In conclusion though, using the assumptions above, the hypothesis is
disproved.

Other methods to use here: time-series analysis to identify dependence
between time-lagged EU vs US attack data. I cannot get into that at
the moment, as I have no time.


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

