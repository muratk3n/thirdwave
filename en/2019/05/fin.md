
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
df1 = pd.read_csv('/tmp/quandl-gdp.csv',index_col=0,parse_dates=True)
df2 = pd.read_csv('/tmp/quandl-inf.csv',index_col=0,parse_dates=True)
df1['gdpyoy'] = (df1.Value - df1.Value.shift(4)) / df1.Value.shift(4) * 100.0

print ('GDP YOY')
print (df1.gdpyoy.tail(1))
print ('Inflation YOY')
print (df2.Value.tail(1))
```

```text
GDP YOY
Date
2019-01-01    3.210894
Name: gdpyoy, dtype: float64
Inflation YOY
Date
2019-04-30    1.996
Name: Value, dtype: float64
```






