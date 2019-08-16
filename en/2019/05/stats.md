# Calculations, Data

## Trump

Latest net-aproval = -11.0 %

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

gdg_growth = 2.0
pred = [1., gdg_growth, -11.0, 0]
print (np.dot(pred, conf), np.dot(pred, results.params))

gdg_growth = 0.0
pred = [1., gdg_growth, -11.0, 0]
print (np.dot(pred, conf), np.dot(pred, results.params))
```

```text
[49.73937141 53.28163696] 51.51050418692104
[49.09061549 51.61086215] 50.350738818591935
```

## Financial Summary Data

```python
import pandas as pd
import quandl, os

fname = '%s/.quandl' % os.environ['HOME']
if not os.path.isfile(fname):
    print ('Please create a %s file ' % fname)
    exit()
auth = open(fname).read()

df1 = quandl.get("FRED/GDPC1-Real-Gross-Domestic-Product", returns="pandas",authtoken=auth)
df2 = quandl.get("RATEINF/INFLATION_USA-Inflation-YOY-USA", returns="pandas",authtoken=auth)
df1.to_csv('/tmp/quandl-gdp.csv')
df2.to_csv('/tmp/quandl-inf.csv')
```

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
df1 = pd.read_csv('/tmp/quandl-gdp.csv',index_col=0,parse_dates=True)
df2 = pd.read_csv('/tmp/quandl-inf.csv',index_col=0,parse_dates=True)
df1['gdpyoy'] = (df1.Value - df1.Value.shift(4)) / df1.Value.shift(4) * 100.0

print ('GDP YOY')
print (df1.gdpyoy.tail(2))
print ('Inflation YOY')
print (df2.Value.tail(2))
```

```text
GDP YOY
Date
2019-01-01    2.652241
2019-04-01    2.288859
Name: gdpyoy, dtype: float64
Inflation YOY
Date
2019-05-31    1.790
2019-06-30    1.648
Name: Value, dtype: float64
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












