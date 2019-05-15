
# Financial Summary Data

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
2018-10-01    2.971385
2019-01-01    3.210894
Name: gdpyoy, dtype: float64
Inflation YOY
Date
2019-03-31    1.863
2019-04-30    1.996
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
plt.ylim(0,30)
plt.savefig('fin_unemploy.png')
```





