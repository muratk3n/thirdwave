

```python
import pandas as pd
import zipfile
with zipfile.ZipFile('corona-time.zip', 'r') as z:
    df =  pd.read_csv(z.open('time-series-19-covid-combined.csv'),parse_dates=['Date'])
print (len(df))
df = df[df['Country/Region'] != "China"]
df = df[['Date','Confirmed']]
confirmed = df.groupby('Date').sum()
print (len(df))
```

```text
27144
25230
```

```python
from scipy.optimize import curve_fit

x = np.linspace(0,1,len(confirmed))
y = np.array(confirmed.T)[0]

def exponential(x,a,b,c):
    return a*np.exp(b*(x-c))

def logistic(v, m, n, a, t):
    return a * (1 + m * np.exp(-v/t))/(1 + n * np.exp(-v/t))

popt1, pcov1 = curve_fit(exponential,x,y,p0=[1.,1.,1.])
popt2, pcov2 = curve_fit(logistic,x,y,p0=[0,1,1,1])

print ('rmse exp', np.sqrt(((y-exponential(x, *popt1))**2).mean()))
print ('rmse log', np.sqrt(((y-logistic(x, *popt2))**2).mean()))
```

```text
rmse exp 1145.2191803212754
rmse log 1097.2579830256955
```

```python
plt.figure()
plt.plot(x, confirmed)
plt.plot(x, exponential(x, *popt1))
plt.savefig('exp.png')

plt.figure()
plt.plot(x, confirmed)
plt.plot(x, logistic(x, *popt2))
plt.savefig('log.png')
```







