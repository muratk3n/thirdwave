# Calculations, Data

Note: In order for Quandl retrieval to work, you need to get an API
key from Quandl, and place the key in a `.quandl` file in the same
directory as this file.

<a name="prezyoy"></a>

## Potus, Incumbent Elec. College Percentage Prediction (GDP YoY)

```python
from io import StringIO
import statsmodels.formula.api as smf
import pandas as pd

s="""year,gdp_growth,net_approval,two_terms,incumbent_vote
2012,2.3,-0.8,0,52
2008,1.09,-37,1,46.3
2004,4.2,-0.5,0,51.2
2000,5.2,19.5,1,50.3
1996,4.0,15.5,0,54.7
1992,3.1,-18,1,46.5
1988,4.4,10,1,53.9
1984,7.9,20,0,59.2
1980,-0.77,-21.7,0,44.7
1976,6.1,5,1,48.9
1972,5.2,26,0,61.8
1968,5.5,-5,1,49.6
1964,6.18,60.3,0,61.3
1960,2.05,37,1,49.9
1956,2.40,53.5,0,57.8
1952,3.60,-27,1,44.5
"""
df = pd.read_csv(StringIO(s))
regr = 'incumbent_vote ~ gdp_growth + net_approval + two_terms'
results = smf.ols(regr, data=df).fit()
print (results.rsquared)
conf = results.conf_int()
```

```text
0.8503762798952246
```

```python
conf = results.conf_int()
net_approv = -11.8

gdg_growth = 3.0
pred = [1., gdg_growth, net_approv, 0]
print (np.dot(pred, conf), np.dot(pred, results.params))

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
[46.81763238 55.80082374] 51.30922806106811
[46.61402821 54.19870793] 50.406368068424605
[46.41042404 52.59659212] 49.5035080757811
[46.20681986 50.9944763 ] 48.600648083137585
```

## 2016 Re-run

```python
bama_net_approv = 9.0
gdp_growth = 1.34
pred = [1., gdp_growth, bama_net_approv, 1]
print (np.dot(pred, conf), np.dot(pred, results.params))
```

```text
[40.0733668  55.07939153] 47.57637916830154
```

## Potus, Incumbent Elec. College Percentage Prediction (Old)

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

## Wages and Unemployment

<a name="unemp"></a>

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1986, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['PAYEMS']
df = data.DataReader(cols, 'fred', start, end)
df['nfpyoy'] = (df.PAYEMS - df.PAYEMS.shift(12)) / df.PAYEMS.shift(12) * 100.0
print (df.tail(7))
```

```text
            PAYEMS    nfpyoy
DATE                        
2019-08-01  151160  1.267519
2019-09-01  151368  1.352546
2019-10-01  151553  1.340029
2019-11-01  151814  1.423675
2019-12-01  151998  1.423281
2020-01-01  152271  1.423395
2020-02-01  152544  1.604556
```

```python
df.nfpyoy.plot()
plt.grid(True)
plt.axvspan('01-09-1990', '01-07-1991', color='y', alpha=0.5, lw=0)
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.title('Non-Farm Payroll YoY Change %')
plt.savefig('nfp.png')
```

![](nfp.png)


```python
import pandas as pd, datetime
from pandas_datareader import data

start=datetime.datetime(1950, 1, 1)
end=datetime.datetime(2019, 11, 1)
cols = ['ECIWAG','CIVPART']
df3 = data.DataReader(cols, 'fred', start, end)
df3 = df3.dropna()
df3['ECIWAG2'] = df3.shift(4).ECIWAG
df3['wagegrowth'] = (df3.ECIWAG-df3.ECIWAG2) / df3.ECIWAG2 * 100.
df3['unempl'] = 100.0 - df3.CIVPART
print (df3['wagegrowth'].tail(7))
```

```text
DATE
2018-04-01    2.945736
2018-07-01    3.000000
2018-10-01    3.134557
2019-01-01    2.954545
2019-04-01    2.936747
2019-07-01    2.987304
2019-10-01    2.965159
Freq: 3MS, Name: wagegrowth, dtype: float64
```

```python
plt.figure(figsize=(14, 5))
plt.subplot(121)
df3['wagegrowth'].plot(title='Wave Growth')
plt.subplot(122)
df3['unempl'].plot(title='Unemployment') 
plt.savefig('unemploy.png')
```

![](unemploy.png)

<a name="claims"></a>

# 4-Week Moving Average of Initial Unemployment Claims 

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1995, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['IC4WSA']
df = data.DataReader(cols, 'fred', start, end)
df.IC4WSA.plot()
print (df.tail(4))
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.savefig('initial-claims.png')
```

```text
            IC4WSA
DATE              
2020-02-15  209250
2020-02-22  209750
2020-02-29  212750
2020-03-07  214000
```

![](initial-claims.png)

<a name="pmi"></a>

## PMI

```python
import quandl, os, datetime
from datetime import timedelta

today = datetime.datetime.now()
start=datetime.datetime(1996, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
today = datetime.datetime.now()
df = quandl.get("ISM/MAN_PMI-PMI-Composite-Index", 
                returns="pandas",
                start_date=start.strftime('%Y-%m-%d'),
                end_date=today.strftime('%Y-%m-%d'),
                authtoken=open(".quandl").read())

print (df['PMI'].tail(4))
df['PMI'].plot()
plt.savefig('pmi.png')
```

```text
Date
2019-11-01    48.1
2019-12-01    47.8
2020-01-01    50.9
2020-02-01    50.1
Name: PMI, dtype: float64
```

![](pmi.png)

<a name="gdpyoy"></a>

# GDP YoY

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
2017-07-01  18163.558  2.416026
2017-10-01  18322.464  2.795257
2018-01-01  18438.254  2.861873
2018-04-01  18598.135  3.202294
2018-07-01  18732.720  3.133538
2018-10-01  18783.548  2.516496
2019-01-01  18927.281  2.652241
2019-04-01  19021.860  2.278320
2019-07-01  19121.112  2.073335
2019-10-01  19220.490  2.326195
```

<a name="infyoy"></a>

# Inflation

```python
import quandl
df = quandl.get("RATEINF/INFLATION_USA-Inflation-YOY-USA", 
                returns="pandas",authtoken=open(".quandl").read())
print (df.tail(6))
```

```text
            Value
Date             
2019-09-30  1.711
2019-10-31  1.764
2019-11-30  2.051
2019-12-31  2.285
2020-01-31  2.487
2020-02-29  2.335
```

<a name="cpyoy"></a>

# Profits

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1950, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['CPROFIT']
df = data.DataReader(cols, 'fred', start, end)
df['cpyoy'] = (df.CPROFIT - df.CPROFIT.shift(4)) / df.CPROFIT.shift(4) * 100.0
print (df.tail(4))
```

```text
             CPROFIT     cpyoy
DATE                          
2018-10-01  2085.603  4.208611
2019-01-01  2006.864 -2.212810
2019-04-01  2082.711  1.278730
2019-07-01  2077.979 -1.247722
```

```python
df.tail(60).cpyoy.plot()
plt.grid(True)
plt.savefig('profit.png')
```

![](profit.png)

# Dollar

<a name="dollar"></a>

```python
import pandas as pd, datetime
from pandas_datareader import data

import quandl
df = quandl.get("CHRIS/ICE_DX1-US-Dollar-Index-Futures-Continuous-Contract", 
                returns="pandas",authtoken=open(".quandl").read())
df = df['Settle']		
print (df.tail(4))
m,s = df.mean(),df.std()
print (np.array([m-s,m+s]).T)
df.tail(1000).plot()
plt.grid(True)
plt.savefig('dollar.png')
```

```text
Date
2020-03-11    96.492
2020-03-12    97.464
2020-03-13    98.764
2020-03-16    98.240
Name: Settle, dtype: float64
[ 81.8038263  102.74784694]
```

![](dollar.png)

<a name="wagepayroll"></a>

# Difference Between Wage Growth YoY and Payrolls (Hiring)

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1986, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['PAYEMS','AHETPI']
df = data.DataReader(cols, 'fred', start, end)
df['nfpyoy'] = (df.PAYEMS - df.PAYEMS.shift(12)) / df.PAYEMS.shift(12) * 100.0
df['wageyoy'] = (df.AHETPI - df.AHETPI.shift(12)) / df.AHETPI.shift(12) * 100.0
df[['wageyoy','nfpyoy']].plot()
plt.axvspan('01-09-1990', '01-07-1991', color='y', alpha=0.5, lw=0)
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
print (df['wageyoy'].tail(5))
print (df['nfpyoy'].tail(5))
plt.savefig('pay-wage.png')
```

```text
DATE
2019-10-01    3.755459
2019-11-01    3.521739
2019-12-01    3.248159
2020-01-01    3.331891
2020-02-01    3.320397
Freq: MS, Name: wageyoy, dtype: float64
DATE
2019-10-01    1.340029
2019-11-01    1.423675
2019-12-01    1.423281
2020-01-01    1.423395
2020-02-01    1.604556
Freq: MS, Name: nfpyoy, dtype: float64
```

![](pay-wage.png)

<a name="gdpism"></a>

# GDP vs ISM

```python
import pandas as pd, datetime
from pandas_datareader import data
import quandl

today = datetime.datetime.now()
start=datetime.datetime(1992, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['GDPC1']
df = data.DataReader(cols, 'fred', start, end)

df['gdpyoy'] = (df.GDPC1 - df.GDPC1.shift(4)) / df.GDPC1.shift(4) * 100.0

df2 = quandl.get("ISM/MAN_PMI-PMI-Composite-Index", 
                returns="pandas",
                start_date=start.strftime('%Y-%m-%d'),
                end_date=end.strftime('%Y-%m-%d'),
                authtoken=open(".quandl").read())

df['pmi'] = df2.PMI
plt.figure(figsize=(12,5))
ax1 = df.pmi.plot(color='blue', grid=True, label='ISM')
ax2 = df.gdpyoy.plot(color='red', grid=True, label='GDP',secondary_y=True)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.legend(h1+h2, l1+l2, loc=2)
plt.savefig('gdp-ism.png')
```

![](gdp-ism.png)

<a name="p2s"></a>

# SP 500 Price to Sales Ratio

```python
import datetime, quandl
today = datetime.datetime.now()
start=datetime.datetime(1980, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
df = quandl.get("MULTPL/SP500_PSR_QUARTER-S-P-500-Price-to-Sales-Ratio-by-Quarter", 
                returns="pandas",
                start_date=start.strftime('%Y-%m-%d'),
                end_date=end.strftime('%Y-%m-%d'),
                authtoken=open(".quandl").read())
print (df.tail(5))

df.plot()
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.savefig('price-sales.png')
```

```text
            Value
Date             
2019-09-30   2.14
2019-11-01   2.25
2019-12-31   2.32
2020-01-31   2.32
2020-02-28   2.12
```

![](price-sales.png)

<a name="sp500prof"></a>

# SP 500 vs Corporate Profits

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1990, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['CP']
df = data.DataReader(cols, 'fred', start, end)

import pandas_datareader.data as web
df2 = web.DataReader("^GSPC", 'yahoo', start, end)
df2 = df2[['Adj Close']]; df2['CP'] = df['CP']
df2 = df2.interpolate().dropna()
df2.columns = ['SP500','Corporate Profits']
df2.plot()
plt.axvspan('01-09-1990', '01-07-1991', color='y', alpha=0.5, lw=0)
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.savefig('sp500-profits.png')
```

![](sp500-profits.png)

<a name="wilshire"></a>

# Total Market Cap / GDP

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1980, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['WILL5000IND']
df = data.DataReader(cols, 'fred', start, end)
df.plot()
plt.axvspan('01-09-1990', '01-07-1991', color='y', alpha=0.5, lw=0)
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.savefig('wilshire.png')
```

![](wilshire.png)


<a name="junkbond"></a>

# Junk Bond Yields

```python
import pandas as pd, datetime
from pandas_datareader import data
import quandl

today = datetime.datetime.now()
start=datetime.datetime(1980, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['BAMLH0A2HYBEY']
df = data.DataReader(cols, 'fred', start, end)
print (df.tail(6))
df.plot()
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.savefig('junkbond.png')
```

```text
            BAMLH0A2HYBEY
DATE                     
2020-03-06           6.63
2020-03-09           7.69
2020-03-10           7.61
2020-03-11           7.92
2020-03-12           8.81
2020-03-13           8.72
```

![](junkbond.png)

<a name="vix"></a>

# VIX

```python
import pandas as pd, datetime
import pandas_datareader.data as web

today = datetime.datetime.now()
start=datetime.datetime(2000, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
df = web.DataReader("^VIX", 'yahoo', start, end)['Adj Close']
df.plot()
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
print (df.tail(5))
plt.savefig('vix.png')
```

```text
Date
2020-03-10    47.299999
2020-03-11    53.900002
2020-03-12    75.470001
2020-03-13    57.830002
2020-03-16    82.690002
Name: Adj Close, dtype: float64
```

![](vix.png)


# Yield Curve

<a name="curve"></a>

10 Year Treasury Yield - 3 Month Bills

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1980, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['DGS10','DGS3MO']
df = data.DataReader(cols, 'fred', start, end)
df['Yield Curve'] = df.DGS10 - df.DGS3MO
print (df['Yield Curve'].tail(6))
df['Yield Curve'].plot()
plt.axvspan('01-09-1990', '01-07-1991', color='y', alpha=0.5, lw=0)
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.savefig('yield-curve.png')
```

```text
DATE
2020-03-09    0.21
2020-03-10    0.32
2020-03-11    0.40
2020-03-12    0.55
2020-03-13    0.66
2020-03-16    0.49
Freq: B, Name: Yield Curve, dtype: float64
```

![](yield-curve.png)











