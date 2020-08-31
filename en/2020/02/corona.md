# The Coronavirus Map

```python
! wget https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv
! zip /tmp/corona-time.zip time-series-19-covid-combined.csv
! rm time-series-19-covid-combined.csv
```

```python
import pandas as pd, zipfile

with zipfile.ZipFile('/tmp/corona-time.zip', 'r') as z:
    df =  pd.read_csv(z.open('time-series-19-covid-combined.csv'),parse_dates=['Date'])
df = df[['Date','Confirmed']]
df = df.set_index('Date')
confirmed = df.groupby('Date').sum()
print (confirmed.tail(4))
confirmed.plot() # in millions
plt.savefig('timeseries.png')
```

```text
             Confirmed
Date                  
2020-08-15  21459699.0
2020-08-16  21672186.0
2020-08-17  21881858.0
2020-08-18  22136954.0
```

![](timeseries.png)


```python
pd.set_option('display.float_format', lambda x: '%.2f' % x) 
chg = confirmed.pct_change()*100.0
chg.plot()
print (chg.tail(5))
plt.title('Daily % Change')
plt.savefig('rate.png')
```

```text
            Confirmed
Date                 
2020-08-14       1.46
2020-08-15       1.17
2020-08-16       0.99
2020-08-17       0.97
2020-08-18       1.17
```

![](rate.png)

County Level Data (NYT)

```python
! wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
! zip /tmp/corona-county.zip us-counties.csv
! rm us-counties.csv
```

Files - [corona.csv](corona.csv), [alpha3country.csv](alpha3country.csv), [util.py](util.py)

[Colors](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)

[Reference](https://www.worldometers.info/coronavirus/)

