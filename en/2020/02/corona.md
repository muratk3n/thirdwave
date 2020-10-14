# Coronavirus Data, Analysis

# Mortality Rate

Code is from [2]

<a mame='mortality'/>

```python
import util
world_rate_df = util.mortality_rate()
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

Daily Change

<a name='daily'/>

```python
import pandas as pd, util
df = util.get_data()
```

```python
df['Germany +'] = df['Germany'].diff()
df['UK +'] = df['United Kingdom'].diff()
df['Germany %'] = df['Germany'].pct_change().rolling(10).mean()*100.0
df['UK %'] = df['United Kingdom'].pct_change().rolling(10).mean()*100.0
```

```python
pd.set_option('display.width', 2000)
pd.set_option('display.max_columns', None)
print (df[['Germany +','Germany %','UK +','UK %']].tail(10))
```

```text
Country/Region  Germany +  Germany %     UK +      UK %
9/28/20            2292.0   0.623245   4056.0  1.291212
9/29/20            1840.0   0.624874   7156.0  1.339242
9/30/20            2442.0   0.671096   7117.0  1.398595
10/1/20            2626.0   0.702528   6929.0  1.440250
10/2/20            2835.0   0.731246   6994.0  1.468327
10/3/20            1653.0   0.728501  12885.0  1.590243
10/4/20            1546.0   0.696847  22965.0  1.904884
10/5/20            3100.0   0.715546  12603.0  1.989946
10/6/20            2454.0   0.749777  14557.0  2.128753
10/7/20            4010.0   0.834276  14173.0  2.262773
```

<a name='Rt'/>

Reproduction Rate $R_t$

This calculation is based on [1]

```python
tau = 7 # length of time window
si_mean = 6.3 # mean of serial interval
si_std = 4.2 # standard deviation of serial interval
conf = 0.95 # confidence level of estimated Reff
c = df['France'].tail(200)
R = util.Reff(c, si_mean, si_std, tau, conf)
print (R[0,:][-20:])
plt.semilogy(R[0,:], 'r', label='median')
plt.semilogy(R[1,:], 'k--')
plt.semilogy(R[2,:], 'k--', label='95% confidence')
plt.savefig('Rt-fr.png')
```

```text
[1.14126687 1.14473272 1.1471149  1.14840016 1.14757916 1.14656922
 1.14876181 1.14607636 1.141851   1.13761038 1.13359156 1.13227862
 1.13092702 1.13043802 1.13099026 1.13314191 1.13464789 1.13539282
 1.13742946 1.1410738 ]
```




County Level Data (NYT)

```python
! wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
! zip /tmp/corona-county.zip us-counties.csv
! rm us-counties.csv
```

Code

[util.py](util.py)

References

[1] https://github.com/tt-nakamura/Reff.git

[2] https://notebooks.ai/rmotr-curriculum/analyzing-covid19-outbreak-40c03c06

[4] https://web.stanford.edu/~jhj1/teachingdocs/Jones-on-R0.pdf


