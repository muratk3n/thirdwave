

```python
import pandas as pd
import zipfile
with zipfile.ZipFile('corona-time.zip', 'r') as z:
    df =  pd.read_csv(z.open('time-series-19-covid-combined.csv'),parse_dates=['Date'])
print (len(df))
df = df[df['Country/Region'] != "China"]
df = df[['Date','Confirmed']]
print (len(df))
```

```text
27144
25230
```

```python
df2 = df.set_index('Date')
confirmed = df2.groupby('Date').sum()
confirmed.plot()
plt.savefig('timeseries2.png')
```































exp_fit = curve_fit(exponential_model,x,np.array(confirmed.T)[0],p0=[10.,10.,10.])

https://towardsdatascience.com/covid-19-infection-in-italy-mathematical-models-and-predictions-7784b4d7dd8d

https://stackoverflow.com/questions/23004374/how-to-calculate-the-likelihood-of-curve-fitting-in-scipy

```python
import pandas as pd
import zipfile
with zipfile.ZipFile('/home/burak/Documents/thirdwave/en/2020/02/corona-time.zip', 'r') as z:
    df =  pd.read_csv(z.open('time-series-19-covid-combined.csv'),parse_dates=True)
df = df[['Date','Confirmed']]
df = df.set_index('Date')
confirmed = df.groupby('Date').sum()
```

```python

from scipy.optimize import curve_fit

x = np.linspace(0,1,len(confirmed))
#x = np.arange(0,len(confirmed))

def exponential(x,a,b,c):
    return a*np.exp(b*(x-c))

y = np.array(confirmed.T)[0]

popt1, pcov1 = curve_fit(exponential,x,y,p0=[1.,1.,1.])

def logistic(v, m, n, a, t):
    return a * (1 + m * np.exp(-v/t))/(1 + n * np.exp(-v/t))

popt2, pcov2 = curve_fit(logistic,x,y,p0=[0,1,1,1])    
```

```python
plt.figure()
plt.plot(x, confirmed)
plt.plot(x, exponential(x, *popt1))
plt.savefig('out1.png')

plt.figure()
plt.plot(x, confirmed)
plt.plot(x, logistic(x, *popt2))
plt.savefig('out2.png')
```



```python
print (pcov1)
print (pcov2)
```

```text
[[5.11661400e+13 9.43496099e+03 2.30414669e+12]
 [9.43512620e+03 1.34688058e-02 4.24908213e+02]
 [2.30414669e+12 4.24900778e+02 1.03761823e+11]]
[[ 3.27722923e-02  4.91336583e+12  1.55388104e+17 -1.95848249e-03]
 [ 4.91336728e+12 -2.84498906e+27 -8.99745047e+31 -6.56094901e+12]
 [ 1.55388150e+17 -8.99745047e+31 -2.84549828e+36 -2.07493964e+17]
 [-1.95848021e-03 -6.56094839e+12 -2.07493944e+17 -9.50329886e-03]]
```


```python
print ('rmse exp', np.sqrt(((y-exponential(x, *popt1))**2).mean()))
print ('rmse log', np.sqrt(((y-logistic(x, *popt2))**2).mean()))
```

```text
rmse exp 14143.538264147179
rmse log 13708.525652536877
```

```python
plt.hist((y-exponential(x, *popt1))**2,50)
plt.savefig('res1.png')
```

```python
plt.hist((y-logistic(x, *popt2))**2,50)
plt.savefig('res2.png')
```

