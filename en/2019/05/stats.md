# Calculations, Data

## Trump

<a name="prez"></a>

Latest net-aproval = -11.8 % (approval 42 % minus 53.8 % disproval)

```python
from io import StringIO
import statsmodels.formula.api as smf
import pandas as pd

s="""year,gdp_growth,net_approval,two_terms,incumbent_vote
2012,1.3,-0.8,0,52
2008,1.3,-37,1,46.3
2004,2.6,-0.5,0,51.2
2000,8,19.5,1,50.3
1996,7.1,15.5,0,54.7
1992,4.3,-18,1,46.5
1988,5.2,10,1,53.9
1984,7.1,20,0,59.2
1980,-7.9,-21.7,0,44.7
1976,3,5,1,48.9
1972,9.8,26,0,61.8
1968,7,-5,1,49.6
1964,4.7,60.3,0,61.3
1960,-1.9,37,1,49.9
1956,3.2,53.5,0,57.8
1952,0.4,-27,1,44.5
1948,7.5,-6,1,52.4
"""
df = pd.read_csv(StringIO(s))
regr = 'incumbent_vote ~ gdp_growth + net_approval + two_terms'
results = smf.ols(regr, data=df).fit()

conf = results.conf_int()
net_approv = -11.8

gdg_growth = 2.0
pred = [1., gdg_growth, net_approv, 0]
print (np.dot(pred, conf), np.dot(pred, results.params))

gdg_growth = 1.0
pred = [1., gdg_growth, net_approv, 0]
print (np.dot(pred, conf), np.dot(pred, results.params))

gdg_growth = 0.0
pred = [1., gdg_growth, net_approv, 0]
print (np.dot(pred, conf), np.dot(pred, results.params))
```

```text
[49.6962248  53.16687853] 51.431551669024834
[49.37184684 52.33149113] 50.85166898486028
[49.04746888 51.49610372] 50.27178630069573
```

## Unemp

```python
import pandas as pd, datetime
from pandas_datareader import data

start=datetime.datetime(1950, 1, 1)
end=datetime.datetime(2019, 6, 1)
cols = ['ECIWAG','LNS12300060','UNRATE']
df3 = data.DataReader(cols, 'fred', start, end)
df3 = df3.dropna()
df3['ECIWAG2'] = df3.shift(4).ECIWAG
df3['wagegrowth'] = (df3.ECIWAG-df3.ECIWAG2) / df3.ECIWAG2 * 100.
df3['unemp_real'] = 100. - df3.LNS12300060
```

```python
print (df3.wagegrowth.tail(1))
print (df3.unemp_real.tail(1))
```

```text
DATE
2019-01-01    2.954545
Freq: 3MS, Name: wagegrowth, dtype: float64
DATE
2019-01-01    20.1
Freq: 3MS, Name: unemp_real, dtype: float64
```

```python
df3.unemp_real.plot()
#plt.ylim(0,30)
plt.savefig('unemploy.png')
```
![]('unemploy.png')


```python
import pandas as pd, datetime
from pandas_datareader import data

start=datetime.datetime(1950, 1, 1)
end=datetime.datetime(2019, 6, 1)
cols = ['PRS85006173']
df4 = data.DataReader(cols, 'fred', start, end)
df4.columns = ['labor_share_of_income']
print (df4.labor_share_of_income.max())
df4.ix[:,'labor_share_of_income'] = df4.labor_share_of_income / df4.labor_share_of_income.max()
print (df4.tail(4))
```

```text
117.495
            labor_share_of_income
DATE                             
2018-04-01               0.847032
2018-07-01               0.847508
2018-10-01               0.843364
2019-01-01               0.840921
```

```python
df4['labor_share_of_income'].plot()
plt.savefig('labor_share.png')
```

![]('labor_share.png')

## PMI

<a name="pmi"></a>

```python
import quandl, os, datetime
from datetime import timedelta

bdays = int(180)
today = datetime.datetime.now()
end_d=datetime.datetime(today.year, today.month, today.day)
start_d = end_d - timedelta(days=bdays)
today = datetime.datetime.now()
df = quandl.get("ISM/MAN_PMI-PMI-Composite-Index", 
                returns="pandas",
                start_date=start_d.strftime('%Y-%m-%d'),
                end_date=today.strftime('%Y-%m-%d'),
                authtoken=open(".quandl").read())

df['PMI'].plot()
plt.savefig('pmi.png')
```

![](pmi.png)

# GDP YoY

<a name="gdpyoy"></a>

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1950, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['GDPC1']
df = data.DataReader(cols, 'fred', start, end)

df['gdpyoy'] = (df.GDPC1 - df.GDPC1.shift(4)) / df.GDPC1.shift(4) * 100.0
print (df.tail(10))
```

```text
                GDPC1    gdpyoy
DATE                           
2017-01-01  17925.256  2.098424
2017-04-01  18021.048  2.163513
2017-07-01  18163.558  2.416026
2017-10-01  18322.464  2.795257
2018-01-01  18438.254  2.861873
2018-04-01  18598.135  3.202294
2018-07-01  18732.720  3.133538
2018-10-01  18783.548  2.516496
2019-01-01  18927.281  2.652241
2019-04-01  19023.820  2.288859
```







