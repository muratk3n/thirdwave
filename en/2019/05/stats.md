y# Calculations, Data

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

## The Cycle

<a name="cycle"/>

![](cycle.png)

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1970, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)

fig, axs = plt.subplots(2)

df = data.DataReader(['GDPC1'], 'fred', start, end)
df['gdpyoy'] = (df.GDPC1 - df.GDPC1.shift(4)) / df.GDPC1.shift(4) * 100.0
df['gdpyoy'].plot(ax=axs[0])
axs[0].axvspan('01-09-1990', '01-07-1991', color='y', alpha=0.5, lw=0)
axs[0].axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
axs[0].axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
print (df[['gdpyoy']].tail(6))

df = data.DataReader(['CPIAUCNS'], 'fred', start, end)
df['infyoy'] = (df.CPIAUCNS - df.CPIAUCNS.shift(12)) / df.CPIAUCNS.shift(12) * 100.0
df['infyoy'].plot(ax=axs[1])
axs[1].axvspan('01-09-1990', '01-07-1991', color='y', alpha=0.5, lw=0)
axs[1].axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
axs[1].axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
print (df[['infyoy']].tail(6))
            
plt.savefig('cycle.png')
```

```text
              gdpyoy
DATE                
2018-07-01  3.133538
2018-10-01  2.516496
2019-01-01  2.652241
2019-04-01  2.278320
2019-07-01  2.073335
2019-10-01  2.334074
              infyoy
DATE                
2019-09-01  1.711305
2019-10-01  1.764043
2019-11-01  2.051278
2019-12-01  2.285130
2020-01-01  2.486572
2020-02-01  2.334874
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
df.nfpyoy.plot()
plt.grid(True)
plt.axvspan('01-09-1990', '01-07-1991', color='y', alpha=0.5, lw=0)
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.title('Non-Farm Payroll YoY Change %')
plt.savefig('nfp.png')
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

# Initial Unemployment Claims

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1995, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['ICSA']
df = data.DataReader(cols, 'fred', start, end)
df.ICSA.plot()
print (df.tail(4))
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.savefig('icsa.png')
```

```text
                 ICSA
DATE                 
2020-02-29        NaN
2020-03-07   211000.0
2020-03-14   282000.0
2020-03-21  3283000.0
```

![](icsa.png)

<a name="pmi"></a>

## PMI

```python
import quandl, os, datetime
from datetime import timedelta

today = datetime.datetime.now()
start=datetime.datetime(1985, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
today = datetime.datetime.now()
df = quandl.get("ISM/MAN_PMI-PMI-Composite-Index", 
                returns="pandas",
                start_date=start.strftime('%Y-%m-%d'),
                end_date=today.strftime('%Y-%m-%d'),
                authtoken=open(".quandl").read())

print (df['PMI'].tail(4))
df['PMI'].plot()
plt.axvspan('01-09-1990', '01-07-1991', color='y', alpha=0.5, lw=0)
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
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



<a name="cpyoy"></a>

# Profits

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1980, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['CPROFIT']
df = data.DataReader(cols, 'fred', start, end)
df['cpyoy'] = (df.CPROFIT - df.CPROFIT.shift(4)) / df.CPROFIT.shift(4) * 100.0
print (df.tail(4))
df.cpyoy.plot()
plt.grid(True)
plt.savefig('profit.png')
```

```text
             CPROFIT     cpyoy
DATE                          
2018-10-01  2085.603  4.208611
2019-01-01  2006.864 -2.212810
2019-04-01  2082.711  1.278730
2019-07-01  2077.979 -1.247722
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
2020-03-19    103.605
2020-03-20    103.502
2020-03-23    103.240
2020-03-24    102.247
Name: Settle, dtype: float64
[ 81.81092298 102.75447686]
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
2020-03-17           9.98
2020-03-18          10.86
2020-03-19          11.51
2020-03-20          11.66
2020-03-23          12.39
2020-03-24          12.11
```

![](junkbond.png)

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
2020-03-12    0.55
2020-03-13    0.66
2020-03-16    0.49
2020-03-17    0.83
2020-03-18    1.16
2020-03-19    1.08
Freq: B, Name: Yield Curve, dtype: float64
```

![](yield-curve.png)


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
print (df.tail(7))
plt.savefig('vix.png')
```

```text
Date
2020-03-17    75.910004
2020-03-18    76.449997
2020-03-19    72.000000
2020-03-20    66.040001
2020-03-23    61.590000
2020-03-24    61.669998
2020-03-25    61.099998
Name: Adj Close, dtype: float64
```

![](vix.png)

<a name="oil"></a>

# Oil

Futures, Continuous Contract, Front Month

```python
import datetime, quandl
today = datetime.datetime.now()
start=datetime.datetime(1980, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
df = quandl.get("CHRIS/CME_CL1-Crude-Oil-Futures-Continuous-Contract-1-CL1-Front-Month", 
                returns="pandas",
                start_date=start.strftime('%Y-%m-%d'),
                end_date=end.strftime('%Y-%m-%d'),
                authtoken=open(".quandl").read())
df = df['Settle']
print (df.tail(5))

df.plot()
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.savefig('oil.png')
```

```text
Date
2020-03-18    20.37
2020-03-19    25.22
2020-03-20    22.43
2020-03-23    23.36
2020-03-24    24.01
Name: Settle, dtype: float64
```

![](oil.png)

<a name="credit"/>

# Credit to GDP

```python
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1960, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)

df = data.DataReader(['GDPC1','QUSPAMUSDA'], 'fred', start, end)
df['Credit to GDP'] = (df.QUSPAMUSDA / df.GDPC1)*100.0
df['Credit to GDP'].plot()
plt.axvspan('01-09-1990', '01-07-1991', color='y', alpha=0.5, lw=0)
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.savefig('creditgdp.png')
```

![](creditgdp.png)




