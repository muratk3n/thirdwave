# Princes of Mayhem

[Link](https://youtu.be/p5Ac7ap_MAY)

Executive summary: if, per Richard Werner, countries should not direct
credit to speculation, then, if one wanted to, one could create
bubbles (which must later burst) in order to spur artificial
recessions. The video claims that is exactly what happened in Japan to
force structural change, and in EU (Greece, Ireland, Spain, Portugal)
to force a European unification (ECB is at fault). The Krauts would
not be fine with that plan, so the deed probably originated from a
"splinter cell" based in France which is known to house a sizeable
elite who really wants to see a greater EU unification.

This explains Japan and its perennial recession: they could get out of
recession at any point if they wanted to, but their financial elite
chose not to. J easily could have carried toxic assets from banks to
the central bank (an accounting slight of hand, does not create money,
simply increases a bank's reserve at the CB), helping banks to lend
again. He credits Bernanke to take this step quickly in US. ECB could
do the same but they too, like Japan, want recession in the periphery.

Historically, the data does not suggest lower / higher interest rates
cause higher / lower economic activity, central banks are mostly
followers of growth rather than the other way around.

Math

Some math and data work based on Werner's book

Crowding out

Start with the main equation

$$ P_R Y = V_R C_R $$

$C_R$ is the credit going to the real sector. Look at differences

$$ \Delta (P_R Y) = V_R \Delta C_R $$

$P_rY$ is real gdp. Note $V_R$ was not differenced bcz it is assumed constant.

To reach $P_rY$, we define

$c$ nominal consumption

$g$ nominal government expenditure

$i$ nominal investment

$nx$ nominal net exports

So

$$ \Delta (P_RY) = \Delta c + \Delta i + \Delta g + \Delta nx $$ 

We plug in two above into one above

$$ \Delta (c +  i +  nx) = V_R\Delta C_R - \Delta g$$

LHS represents rise in demand. What the eqn further says is if credit
issuance is constant, increases in $g$ must be cause decrease in demand
bcz $\Delta g$'s coefficient is -1. We can test that, if empirically
we find a coefficient -1 we are good to go.

$$ \Delta p_R + \Delta y = \Delta c_R$$

Small caps is log'd vars. Think of one period's credit creation
effecting the next's growth,

$$ \Delta p_{Rt} + \Delta y_{t} = \Delta c_{Rt-1}$$

or

$$ \Delta GDP_t = \Delta C_{Rt-1}$$

Add $\Delta GDP_{t-1}$ to both sides

$$ \Delta GDP_t + \Delta GDP_{t-1} = \Delta C_{Rt-1} + \Delta GDP_{t-1} $$

Plug in to two above

$$ \Delta GDP_t + \Delta GDP_{t-1} = \Delta C_{Rt-1} + \Delta C_{Rt-2}  $$

$$ \Delta GDP_t = - \Delta GDP_{t-1} + \Delta C_{Rt-1} + \Delta C_{Rt-2}  $$

Assign coefficients

$$ \Delta GDP_t = \alpha + \beta_1 \Delta GDP_{t-1} + \gamma_0 \Delta C_{Rt-1} + 
$$
$$
\gamma_3 \Delta C_{Rt-2} + \epsilon_t 
$$

$$ 
\Delta (c_t + i_t + nx_t) = 
\alpha + \beta_0 \Delta g_t + \beta_1 \Delta GDP_{t-1} +
$$
$$
\gamma_0 \Delta C_{Rt-1} + \gamma_3 \Delta C_{Rt-2} + \epsilon_t 
$$

```python
import pandas as pd
df = pd.read_csv('crowd.csv',parse_dates=True)
df = df.dropna(axis=0)
df = df.set_index('DATE')
df['gdp'] = df.gdp / 1000.0
df['govexp'] = (df['gov1exp'] + df['gov2exp']) / 1000.0
df['lhs'] = (df.consump + df.invest + df.netexp).pct_change() 
df['dgt'] = df.govexp.pct_change() 
#df['dcrt'] = (df.nonfinloan - df.constructloan).diff() / 1000.0
df['dcrt'] = (df.nonfinloan).diff() / 1000.0
df['dcrt1'] = df.dcrt.shift(1)
df['dcrt2'] = df.dcrt.shift(2)
df['dcrt3'] = df.dcrt.shift(3)
df['dgdpt'] = df.gdp.pct_change()
df['dgdpt1'] = df.dgdpt.shift(1)
df['dgdpt2'] = df.dgdpt.shift(2)
df = df.dropna(axis=0)

import statsmodels.formula.api as smf
results = smf.ols('lhs ~ dgt +  dgdpt1 + dcrt1  + dcrt2 ', data=df).fit()
print results.summary()
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    lhs   R-squared:                       0.106
Model:                            OLS   Adj. R-squared:                  0.086
Method:                 Least Squares   F-statistic:                     5.346
Date:                Wed, 20 Jun 2018   Prob (F-statistic):           0.000432
Time:                        20:45:57   Log-Likelihood:                 358.03
No. Observations:                 185   AIC:                            -706.1
Df Residuals:                     180   BIC:                            -690.0
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
Intercept      0.0138      0.006      2.185      0.030         0.001     0.026
dgt           -0.5671      0.183     -3.101      0.002        -0.928    -0.206
dgdpt1         0.5867      0.271      2.165      0.032         0.052     1.122
dcrt1          0.0375      0.034      1.101      0.272        -0.030     0.105
dcrt2         -0.0754      0.034     -2.208      0.028        -0.143    -0.008
==============================================================================
Omnibus:                        6.056   Durbin-Watson:                   2.107
Prob(Omnibus):                  0.048   Jarque-Bera (JB):                7.103
Skew:                          -0.245   Prob(JB):                       0.0287
Kurtosis:                       3.825   Cond. No.                         108.
==============================================================================
```

Exchange Rate, MV=PY

$$ M_1V_1 = P_1Y_1, \quad M_2V_2 = P_2Y_2 $$

$$ \frac{P_2}{P_1} = \frac{M_2}{M_1} \cdot \frac{Y_1}{Y_2} \cdot \frac{V_2}{V_1} $$

$$ \log \left( \frac{P_2}{P_1} \right) = 
\log \left( \frac{M_2}{M_1} \right) + 
\log \left( \frac{Y_1}{Y_2} \right) +
\log \left( \frac{V_2}{V_1} \right) 
$$

$$
= \log(M_2) - \log(M_1) + \log(Y_1) - \log(Y_2)  + 
$$
$$
\log(V_2) - \log(V_1)
$$

Drop V differences bcz if V's are costant, that diff is a constant as well. 

$$ = \log(M_2) - \log(M_1) + \log(Y_1) - \log(Y_2)  $$

```python
df = pd.read_csv('exch.csv',parse_dates=['DATE'])
df = df.set_index('DATE')
df = df.interpolate(method='linear')
k = 5
df['lm1'] = np.log(df.nonfinloanus).shift(k)
df['lm2'] = np.log(df.nonfinloanjp).shift(k)
df['ly1'] = np.log(df.realgdpus).shift(k)
df['ly2'] = np.log(df.realgdpjp).shift(k)
df['lxjpus'] = np.log(df.xjpus)

df = df.dropna(axis=0)
import statsmodels.formula.api as smf
results = smf.ols('lxjpus ~ lm1 + lm2 + ly1 + ly2', data=df).fit()
print results.summary()
```

```python
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 lxjpus   R-squared:                       0.432
Model:                            OLS   Adj. R-squared:                  0.424
Method:                 Least Squares   F-statistic:                     53.88
Date:                Wed, 30 May 2018   Prob (F-statistic):           1.00e-33
Time:                        20:09:26   Log-Likelihood:                 249.15
No. Observations:                 288   AIC:                            -488.3
Df Residuals:                     283   BIC:                            -470.0
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
Intercept    -35.7050      4.321     -8.263      0.000       -44.211   -27.199
lm1           -0.5512      0.118     -4.663      0.000        -0.784    -0.318
lm2            1.2863      0.190      6.768      0.000         0.912     1.660
ly1            1.7492      0.305      5.732      0.000         1.148     2.350
ly2            0.8758      0.408      2.146      0.033         0.073     1.679
==============================================================================
Omnibus:                       13.370   Durbin-Watson:                   0.067
Prob(Omnibus):                  0.001   Jarque-Bera (JB):                9.922
Skew:                          -0.346   Prob(JB):                      0.00701
Kurtosis:                       2.409   Cond. No.                     1.67e+04
==============================================================================
```

Granger Test, rates and growth

From Reconsidering Monetary Policy: An Empirical Examination of the
Relationship Between Interest Rates and Nominal GDP Growth in the
U.S., U.K., Germany and Japan

[Link](https://www.sciencedirect.com/science/article/pii/S0921800916307510)

```python
import statsmodels.tsa.stattools as t
import pandas as pd

df = pd.read_csv('rates.csv',parse_dates=['DATE'])
df = df.set_index('DATE')
df = df.resample('AS').last()
df['gdpinc'] = df.gdp.pct_change()*100.0
df = df.dropna(axis=0)
res = t.grangercausalitytests(df[['gdpinc','shortrate']],maxlag=2)
res = t.grangercausalitytests(df[['shortrate','gdpinc']],maxlag=2)
```

```
Granger Causality
('number of lags (no zero)', 1)
ssr based F test:         F=0.0062  , p=0.9378  , df_denom=43, df_num=1
ssr based chi2 test:   chi2=0.0066  , p=0.9353  , df=1
likelihood ratio test: chi2=0.0066  , p=0.9353  , df=1
parameter F test:         F=0.0062  , p=0.9378  , df_denom=43, df_num=1

Granger Causality
('number of lags (no zero)', 2)
ssr based F test:         F=0.2645  , p=0.7689  , df_denom=40, df_num=2
ssr based chi2 test:   chi2=0.5952  , p=0.7426  , df=2
likelihood ratio test: chi2=0.5913  , p=0.7440  , df=2
parameter F test:         F=0.2645  , p=0.7689  , df_denom=40, df_num=2

Granger Causality
('number of lags (no zero)', 1)
ssr based F test:         F=14.0199 , p=0.0005  , df_denom=43, df_num=1
ssr based chi2 test:   chi2=14.9980 , p=0.0001  , df=1
likelihood ratio test: chi2=12.9812 , p=0.0003  , df=1
parameter F test:         F=14.0199 , p=0.0005  , df_denom=43, df_num=1

Granger Causality
('number of lags (no zero)', 2)
ssr based F test:         F=9.2853  , p=0.0005  , df_denom=40, df_num=2
ssr based chi2 test:   chi2=20.8919 , p=0.0000  , df=2
likelihood ratio test: chi2=17.1609 , p=0.0002  , df=2
parameter F test:         F=9.2853  , p=0.0005  , df_denom=40, df_num=2
```

```python
import scipy.stats as stats
df['gdpinc1'] = df.gdpinc.shift(1)
df2 = df.dropna(axis=0)
print stats.pearsonr(df2.shortrate, df2.gdpinc1)
```

```
(0.75710287451587455, 1.1393168782627738e-09)
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    lhs   R-squared:                       0.106
Model:                            OLS   Adj. R-squared:                  0.086
Method:                 Least Squares   F-statistic:                     5.346
Date:                Mon, 21 May 2018   Prob (F-statistic):           0.000432
Time:                        16:52:34   Log-Likelihood:                 358.03
No. Observations:                 185   AIC:                            -706.1
Df Residuals:                     180   BIC:                            -690.0
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
Intercept      0.0138      0.006      2.185      0.030         0.001     0.026
dgt           -0.5671      0.183     -3.101      0.002        -0.928    -0.206
dgdpt1         0.5867      0.271      2.165      0.032         0.052     1.122
dcrt1          0.0375      0.034      1.101      0.272        -0.030     0.105
dcrt2         -0.0754      0.034     -2.208      0.028        -0.143    -0.008
==============================================================================
Omnibus:                        6.056   Durbin-Watson:                   2.107
Prob(Omnibus):                  0.048   Jarque-Bera (JB):                7.103
Skew:                          -0.245   Prob(JB):                       0.0287
Kurtosis:                       3.825   Cond. No.                         108.
==============================================================================
```

Interest rates

```python
import pandas as pd
df = pd.read_csv('jpy.csv',parse_dates=['DATE'])
df = df.set_index('DATE')
df2 = pd.read_csv('jpypos.csv',parse_dates=['DATE'])
df2 = df2.set_index('DATE')
df = df.join(df2)
df = df.interpolate(method='linear')
df = df.dropna(axis=0)

df['S'] = df.nonclong - df.noncomshort
df['N'] = df.comlong - df.comshort
df['T'] = df['exp'] - df['imp']
df['e'] = df.jpyus
df['i'] = df.jpyrate - df.usrate
df = df.dropna(axis=0)
print df.tail(5)
```

```
               jpyus  jpyrate  usrate          exp           imp  nonclong  \
DATE                                                                         
2017-09-01  110.7760    0.056    1.25  5968.324745  10807.305850   12596.0   
2017-10-01  112.9148    0.063    1.26  5617.537774  12047.994224   12596.0   
2017-11-01  112.8190    0.063    1.32  5773.435680  11529.345754   12596.0   
2017-12-01  112.9405    0.063    1.53  6433.521691  11960.532667   12596.0   
2018-01-01  110.8710    0.068    1.67  5650.378604  11302.129766   12596.0   

            noncomshort  comlong  comshort       S        N            T  \
DATE                                                                       
2017-09-01       3985.0   3043.0   17632.0  8611.0 -14589.0 -4838.981105   
2017-10-01       3985.0   3043.0   17632.0  8611.0 -14589.0 -6430.456450   
2017-11-01       3985.0   3043.0   17632.0  8611.0 -14589.0 -5755.910074   
2017-12-01       3985.0   3043.0   17632.0  8611.0 -14589.0 -5527.010976   
2018-01-01       3985.0   3043.0   17632.0  8611.0 -14589.0 -5651.751162   

                   e      i  
DATE                         
2017-09-01  110.7760 -1.194  
2017-10-01  112.9148 -1.197  
2017-11-01  112.8190 -1.257  
2017-12-01  112.9405 -1.467  
2018-01-01  110.8710 -1.602  
```

```python
import statsmodels.formula.api as smf
results = smf.ols('e ~ N + T + S ', data=df).fit()
print results.summary()
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      e   R-squared:                       0.228
Model:                            OLS   Adj. R-squared:                  0.215
Method:                 Least Squares   F-statistic:                     18.01
Date:                Sun, 27 May 2018   Prob (F-statistic):           2.76e-10
Time:                        18:49:21   Log-Likelihood:                -727.68
No. Observations:                 187   AIC:                             1463.
Df Residuals:                     183   BIC:                             1476.
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
Intercept     94.2969      5.178     18.210      0.000        84.080   104.514
N             -0.0004   7.55e-05     -4.994      0.000        -0.001    -0.000
T             -0.0017      0.001     -2.000      0.047        -0.003 -2.29e-05
S             -0.0005   9.29e-05     -5.448      0.000        -0.001    -0.000
==============================================================================
Omnibus:                        6.112   Durbin-Watson:                   0.066
Prob(Omnibus):                  0.047   Jarque-Bera (JB):                3.317
Skew:                          -0.059   Prob(JB):                        0.190
Kurtosis:                       2.358   Cond. No.                     4.13e+05
==============================================================================
```

```python
import statsmodels.formula.api as smf
results = smf.ols('S ~ e + i', data=df).fit()
print results.summary()
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      S   R-squared:                       0.067
Model:                            OLS   Adj. R-squared:                  0.057
Method:                 Least Squares   F-statistic:                     6.621
Date:                Sun, 27 May 2018   Prob (F-statistic):            0.00167
Time:                        18:46:25   Log-Likelihood:                -2248.2
No. Observations:                 187   AIC:                             4502.
Df Residuals:                     184   BIC:                             4512.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
Intercept   6.083e+04   2.61e+04      2.329      0.021      9307.175  1.12e+05
e           -718.8629    261.650     -2.747      0.007     -1235.084  -202.642
i           1094.9441   2094.571      0.523      0.602     -3037.520  5227.409
==============================================================================
Omnibus:                       15.134   Durbin-Watson:                   0.136
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               10.560
Skew:                          -0.459   Prob(JB):                      0.00509
Kurtosis:                       2.283   Cond. No.                         926.
==============================================================================
```

```python
import statsmodels.formula.api as smf
results = smf.ols('N ~ e + i', data=df).fit()
print results.summary()
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      N   R-squared:                       0.037
Model:                            OLS   Adj. R-squared:                  0.026
Method:                 Least Squares   F-statistic:                     3.492
Date:                Sun, 27 May 2018   Prob (F-statistic):             0.0325
Time:                        18:46:43   Log-Likelihood:                -2285.3
No. Observations:                 187   AIC:                             4577.
Df Residuals:                     184   BIC:                             4586.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
Intercept  -6.139e+04   3.18e+04     -1.928      0.055     -1.24e+05  1443.275
e            842.4412    319.101      2.640      0.009       212.874  1472.008
i           3905.6002   2554.474      1.529      0.128     -1134.225  8945.426
==============================================================================
Omnibus:                       20.995   Durbin-Watson:                   0.122
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               12.730
Skew:                           0.492   Prob(JB):                      0.00172
Kurtosis:                       2.185   Cond. No.                         926.
==============================================================================
```

```python
import statsmodels.tsa.stattools as t
res = t.grangercausalitytests(df[['i','e']],maxlag=2)
res = t.grangercausalitytests(df[['e','i']],maxlag=2)
```

```
Granger Causality
('number of lags (no zero)', 1)
ssr based F test:         F=2.3413  , p=0.1277  , df_denom=183, df_num=1
ssr based chi2 test:   chi2=2.3797  , p=0.1229  , df=1
likelihood ratio test: chi2=2.3646  , p=0.1241  , df=1
parameter F test:         F=2.3413  , p=0.1277  , df_denom=183, df_num=1

Granger Causality
('number of lags (no zero)', 2)
ssr based F test:         F=4.7366  , p=0.0099  , df_denom=180, df_num=2
ssr based chi2 test:   chi2=9.7363  , p=0.0077  , df=2
likelihood ratio test: chi2=9.4888  , p=0.0087  , df=2
parameter F test:         F=4.7366  , p=0.0099  , df_denom=180, df_num=2

Granger Causality
('number of lags (no zero)', 1)
ssr based F test:         F=0.0087  , p=0.9259  , df_denom=183, df_num=1
ssr based chi2 test:   chi2=0.0088  , p=0.9252  , df=1
likelihood ratio test: chi2=0.0088  , p=0.9252  , df=1
parameter F test:         F=0.0087  , p=0.9259  , df_denom=183, df_num=1

Granger Causality
('number of lags (no zero)', 2)
ssr based F test:         F=0.3957  , p=0.6738  , df_denom=180, df_num=2
ssr based chi2 test:   chi2=0.8134  , p=0.6659  , df=2
likelihood ratio test: chi2=0.8116  , p=0.6665  , df=2
parameter F test:         F=0.3957  , p=0.6738  , df_denom=180, df_num=2
```

```python
import pandas as pd, datetime
from pandas_datareader import data

start=datetime.datetime(1970, 1, 1)
end=datetime.datetime(2018, 5, 1)
df = data.DataReader(['CRDQUSAPABIS','REALLN','CRDQJPAPABIS','JPNRGDPEXP','GDPC1','EXJPUS','MYAGM2USM052S','MYAGM2USM052S'], 'fred', start, end)
df.columns = ['nonfinloanus','constructloanus','nonfinloanjp','realgdpjp','realgdpus','xjpus','m2us','m2jp']
df.to_csv('exch.csv')

start=datetime.datetime(1970, 1, 1)
end=datetime.datetime(2017, 1, 1)
df = data.DataReader(['GDP','IR3TIB01USM156N'], 'fred', start, end)
df.columns = ['gdp','shortrate']
df.to_csv('rates.csv')

import pandas as pd, datetime
from pandas_datareader import data
start=datetime.datetime(1970, 1, 1)
end=datetime.datetime(2017, 1, 1)
df = data.DataReader(['M2SL','GDP','CRDQUSAPABIS','REALLN'], 'fred', start, end)
df.columns = ['m2cd','gdp','nonfincred','realest']
df.to_csv('money.csv')

import pandas as pd, datetime
from pandas_datareader import data
start=datetime.datetime(1970, 1, 1)
end=datetime.datetime(2017, 1, 1)
df = data.DataReader(['DPCERD3Q086SBEA','W019RCQ027SBEA','W079RCQ027SBEA','GPDIC1','NETEXP','GDP','CRDQUSAPABIS','REALLN'], 'fred', start, end)
df.columns = ['consump','gov1exp','gov2exp', 'invest','netexp','gdp','nonfinloan','constructloan']
df.to_csv('crowd.csv')

#####
# speculative traders, noncommercial open position
# wget http://www.cftc.gov/files/dea/history/deacot2002.zip
# use year 2012, 2015, etc in the file name
# put them under jpy directory

if os.path.isdir("jpy"):
    res = []    
    for y in range(2002,2018):    
        print y
        with zipfile.ZipFile('cad/deacot%d.zip' % y, 'r') as z:
            df = pd.read_csv(z.open('annual.txt'))     
            df = df[df["Market and Exchange Names"].str.contains("JAPANESE YEN")]
            df = df[["As of Date in Form YYYY-MM-DD","Noncommercial Positions-Long (All)","Noncommercial Positions-Short (All)","Commercial Positions-Long (All)","Commercial Positions-Short (All)"]]
            res.append(df.copy())

    df2 = pd.concat(res)
    print df2
    df2.to_csv('jpypos.csv',index=None)
```






