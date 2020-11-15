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
11/11/20    2.464445
11/12/20    2.453431
11/13/20    2.440825
11/14/20    2.431413
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
11/5/20           22561.0   3.441277  24164.0  2.295915
11/6/20           22820.0   3.510528  23322.0  2.247599
11/7/20           14122.0   3.376844  24979.0  2.196411
11/8/20           14510.0   3.203444  20580.0  2.127480
11/9/20            6522.0   2.910066  21397.0  2.054349
11/10/20          26547.0   3.023831  20451.0  2.001665
11/11/20          22401.0   3.100720  23000.0  1.958350
11/12/20          24738.0   2.971985  33517.0  2.041599
11/13/20          22261.0   3.131554  27316.0  2.062794
11/14/20          14640.0   2.772572  26876.0  2.032224
```

<a name='Rt'/>

Reproduction Rate $R_t$

This calculation is based on [1]

```python
tau = 7 # length of time window
si_mean = 6.3 # mean of serial interval
si_std = 4.2 # standard deviation of serial interval
conf = 0.95 # confidence level of estimated Reff
c = df['US'].tail(200)
R = util.Reff(c, si_mean, si_std, tau, conf)
df2 = pd.DataFrame(R.T)
print (df2[1].tail(5))
# 0,2 indices 95% conf
df2[1].tail(70).plot()
plt.title('US')
plt.ylim(1.0,1.1)
plt.savefig('Rt-US.png')
```

```text
195    1.071632
196    1.073799
197    1.075977
198    1.078405
199    1.080834
Name: 1, dtype: float64
```

![](Rt-US.png)


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


