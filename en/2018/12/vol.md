

```python
from scipy.stats import norm
import datetime, numpy as np

def find_vol(target_value, call_put, S, K, T, r):
    MAX_ITERATIONS = 100
    PRECISION = 1.0e-5

    sigma = 0.5
    for i in range(0, MAX_ITERATIONS):
        price = bs_price(call_put, S, K, T, r, sigma)
        vega = bs_vega(call_put, S, K, T, r, sigma)
        price = price
        diff = target_value - price  # our root

        print (i, sigma, diff)

        if (abs(diff) < PRECISION): return sigma
        sigma = sigma + diff/vega # f(x) / f'(x)

    return sigma


n = norm.pdf
N = norm.cdf

def bs_price(cp_flag,S,K,T,r,v,q=0.0):
    d1 = (np.log(S/K)+(r+v*v/2.)*T)/(v*np.sqrt(T))
    d2 = d1-v*np.sqrt(T)
    if cp_flag == 'c':
        price = S*np.exp(-q*T)*N(d1)-K*np.exp(-r*T)*N(d2)
    else:
        price = K*np.exp(-r*T)*N(-d2)-S*np.exp(-q*T)*N(-d1)
    return price

def bs_vega(cp_flag,S,K,T,r,v,q=0.0):
    d1 = (np.log(S/K)+(r+v*v/2.)*T)/(v*np.sqrt(T))
    return S * np.sqrt(T)*n(d1)

def test1():
    
    V_market = 17.5
    K = 585
    T = (datetime.date(2014,10,18) - datetime.date(2014,9,8)).days / 365.
    S = 586.08
    r = 0.0002
    cp = 'c' # call option
    
    implied_vol = find_vol(V_market, cp, S, K, T, r)
    
    print ('Implied vol: %.2f%%' % (implied_vol * 100))
    
    print ('Market price = %.2f' % V_market)
    print ('Model price = %.2f' % bs_price(cp, S, K, T, r, implied_vol))

test1()

```

```text
0 0.5 -21.669539271534063
1 0.21879739316064523 0.03217154881230044
2 0.21921383628613422 1.9891615465894574e-08
Implied vol: 21.92%
Market price = 17.50
Model price = 17.50
```


```python
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date
import pandas_datareader.data as web

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 10) 
pd.set_option('display.width', 82) 
pd.set_option('precision', 3)
```


```python
aapl_options = web.Options('AAPL', 'yahoo')
aapl_options = aapl_options.get_all_data().reset_index()
aapl_options.to_csv('tmp-opout.csv')
```



```python
aapl_options = pd.read_csv('aapl_options.csv',  parse_dates=['Expiry'])
aapl_options['IV'].tail(4)
```

```text
Out[1]: 
1099    26.78%
1100    30.41%
1101    28.26%
1102    31.88%
Name: IV, dtype: object
```

```python
aos = aapl_options.sort_values(['Expiry', 'Strike'])[['Expiry', 'Strike', 'Type', 'IV', 'Bid', 'Ask', 'Underlying_Price']] 
aos['IV'] = aos['IV'].apply(lambda x: float(x.strip('%')))
aos[:5]
```

```text
Out[1]: 
        Expiry  Strike  Type      IV    Bid    Ask  Underlying_Price
158 2015-02-27    75.0  call  271.88  53.60  53.85            128.79
159 2015-02-27    75.0   put  193.75   0.00   0.01            128.79
190 2015-02-27    80.0  call  225.78  48.65  48.80            128.79
191 2015-02-27    80.0   put  171.88   0.00   0.01            128.79
226 2015-02-27    85.0  call  199.22  43.65  43.80            128.79
```

```python
aos['Expiry'].unique()
```

```text
Out[1]: 
array(['2015-02-27T00:00:00.000000000', '2015-03-06T00:00:00.000000000',
       '2015-03-13T00:00:00.000000000', '2015-03-20T00:00:00.000000000',
       '2015-03-27T00:00:00.000000000', '2015-04-02T00:00:00.000000000',
       '2015-04-17T00:00:00.000000000', '2015-05-15T00:00:00.000000000',
       '2015-07-17T00:00:00.000000000', '2015-10-16T00:00:00.000000000',
       '2016-01-15T00:00:00.000000000', '2017-01-20T00:00:00.000000000'],
      dtype='datetime64[ns]')
```

```python
aos.loc[158]
```

```text
Out[1]: 
Expiry              2015-02-27 00:00:00
Strike                               75
Type                               call
IV                                  272
Bid                                53.6
Ask                                53.9
Underlying_Price                    129
Name: 158, dtype: object
```

```python
calls1 = aos[(aos.Expiry=='2015-02-27') & (aos.Type=='call')]
calls1[:5]
```

```text
Out[1]: 
        Expiry  Strike  Type      IV    Bid    Ask  Underlying_Price
158 2015-02-27    75.0  call  271.88  53.60  53.85            128.79
190 2015-02-27    80.0  call  225.78  48.65  48.80            128.79
226 2015-02-27    85.0  call  199.22  43.65  43.80            128.79
265 2015-02-27    90.0  call  175.00  38.65  38.80            128.79
303 2015-02-27    93.0  call  160.16  35.65  35.80            128.79
```






















