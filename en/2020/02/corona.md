# Coronavirus Data, Analysis

# Mortality Rate

Code is from [8]

<a mame='mortality'/>

```python
import pandas as pd

COVID_CONFIRMED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
covid_confirmed = pd.read_csv(COVID_CONFIRMED_URL)
COVID_DEATHS_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
covid_deaths = pd.read_csv(COVID_DEATHS_URL)
COVID_RECOVERED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
covid_recovered = pd.read_csv(COVID_RECOVERED_URL)

covid_worldwide_confirmed = covid_confirmed.iloc[:, 4:].sum(axis=0)
covid_worldwide_deaths = covid_deaths.iloc[:, 4:].sum(axis=0)
covid_worldwide_recovered = covid_recovered.iloc[:, 4:].sum(axis=0)
covid_worldwide_active = covid_worldwide_confirmed - covid_worldwide_deaths - covid_worldwide_recovered

world_rate_df = pd.DataFrame({
    'confirmed': covid_worldwide_confirmed,
    'deaths': covid_worldwide_deaths,
    'recovered': covid_worldwide_recovered,
    'active': covid_worldwide_active
}, index=covid_worldwide_confirmed.index)

world_rate_df['recovered / 100 confirmed'] = world_rate_df['recovered'] / world_rate_df['confirmed'] * 100

world_rate_df['deaths / 100 confirmed'] = world_rate_df['deaths'] / world_rate_df['confirmed'] * 100

world_rate_df['date'] = world_rate_df.index

print (world_rate_df['deaths / 100 confirmed'].tail(4))
world_rate_df['deaths / 100 confirmed'].plot(title='Worldwide Mortality Rate')

plt.savefig('mort.png')
```

```text
9/15/20    3.162778
9/16/20    3.149845
9/17/20    3.135215
9/18/20    3.126073
Name: deaths / 100 confirmed, dtype: float64
```

![](mort.png)


The SIR Model

$$
\frac{ds}{dt} = -\beta s i
$$

$$
\frac{di}{dt} = \beta s i - \gamma i
$$

$$
\frac{dr}{dt} = \gamma i
$$

Where does $R_0$ come from? Epidemic occurs if \# of infected ppl
increase, meaning $di / dt > 0$. That means (from 2nd eq above)

$$
\beta si - \gamma i > 0  \implies \frac{\beta s i }{\gamma} > i
$$

Then,

$$
\frac{\beta s }{\gamma} > 1
$$

At the beginning of the epidemic everyone is susceptible, so $s
\approx 1$. Substitute $s=1$

$$
\frac{\beta}{\gamma} = R_0 > 1
$$

To find $R_0$ from data, we fit the differential equation system above
to data, and using the found $\beta$ and $\gamma$ we calculate $R_0$.

<a name='Rt'/>

$R_t$ Estimate

Code is based on [7]

```python
import util

country = 'United Kingdom'
pop, df = util.estimate_Rt_for_country(country)
import matplotlib.dates as mdates
ax = df.plot('Date','Rt',linewidth=3,color='red',grid=True,ylim=(0,6),figsize=(12,8))
ax.xaxis.grid(True, which='minor')
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
plt.gcf().autofmt_xdate()
plt.legend(fontsize=16)
plt.title(country)
plt.savefig('Rt-%s' % country.replace(" ",""))
print (df[['Date','Rt']].tail(10))
```

```text
          Date        Rt
231 2020-09-09  0.256549
232 2020-09-10  0.263986
233 2020-09-11       NaN
234 2020-09-12       NaN
235 2020-09-13       NaN
236 2020-09-14       NaN
237 2020-09-15       NaN
238 2020-09-16       NaN
239 2020-09-17       NaN
240 2020-09-18       NaN
```

![](Rt-UnitedKingdom.png)

County Level Data (NYT)

```python
! wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
! zip /tmp/corona-county.zip us-counties.csv
! rm us-counties.csv
```

Files

[util.py](util.py)

References

[1] https://web.stanford.edu/~jhj1/teachingdocs/Jones-on-R0.pdf

[2] https://chengjunwang.com/post/en/2013-03-14-learn-basic-epidemic-models-with-python/

[3] https://medium.com/analytics-vidhya/covid19-transmission-forecast-in-italy-a-python-tutorial-for-sri-model-8c103c0a95b9

[4] https://web.stanford.edu/~jhj1/teachingdocs/Jones-on-R0.pdf

[5] https://chengjunwang.com/post/en/2013-03-14-learn-basic-epidemic-models-with-python/

[6] https://medium.com/analytics-vidhya/covid19-transmission-forecast-in-italy-a-python-tutorial-for-sri-model-8c103c0a95b9

[7] https://github.com/shwars/SlidingSir

[8] https://notebooks.ai/rmotr-curriculum/analyzing-covid19-outbreak-40c03c06


