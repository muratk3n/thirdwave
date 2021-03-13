# The Power of Nations Code

We can check if Beckley's GDP x GDP Per Capita can predict war outcomes.

The data comes from [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/58KDCM)

`reiterwars.tab` has wars from past few centuries, `power1.tab`
carries `GDP`, `CINC`, population and Beckley's measure `y`. We could
reconstruct it from `GDP` and `tpop` which I did to check, the results
are the same.

My zipped version is [here](https://drive.google.com/uc?export=view&id=1Gh2-Kq9EigyQ_llE_mwG-WS8Knyi7KQR)

```python
import pandas as pd
dfp = pd.read_csv('power1.tab',sep='\t')
dfw = pd.read_csv('reiterwars.tab',sep='\t')
dfw = dfw[dfw.joiner==0]

dfj1 = dfw.merge(dfp, left_on=['year','init_ccode'], right_on=['year','ccode'],how='left')
dfj1['tpopa'] = dfj1['tpop'] 
dfj1['cinca'] = dfj1['cinc'] 
dfj1['gdpa'] = dfj1['gdp']
dfj1['ya'] = dfj1['y']
cols = ['init_ccode','init_name','larger_war_name','target_ccode','target_name','year','tpopa','cinca','gdpa','ya','annual_outcome']
dfj1 = dfj1[cols]
dfj2 = dfj1.merge(dfp, left_on=['year','target_ccode'], right_on=['year','ccode'],how='left')
dfj2['tpopb'] = dfj2['tpop'] 
dfj2['cincb'] = dfj2['cinc'] 
dfj2['gdpb'] = dfj2['gdp']
dfj2['yb'] = dfj2['y']
dfj2 = dfj2[cols + ['tpopb','gdpb','cincb','yb']]
dfj2.loc[dfj2.annual_outcome==1,'win'] = 1
dfj2.loc[dfj2.annual_outcome==2,'win'] = 0
dfj2 = dfj2[dfj2.annual_outcome != 0]
dfj2['cincfrac']=dfj2.cinca/(dfj2.cinca+dfj2.cincb)
dfj2['gdpfrac']=dfj2.gdpa/(dfj2.gdpa+dfj2.gdpb)
dfj2['yfrac']=dfj2.ya/(dfj2.ya+dfj2.yb)
```

```python
import statsmodels.formula.api as smf
results = smf.ols('win ~ cincfrac', data=dfj2).fit()
print ('%0.2f' % results.rsquared)
results = smf.ols('win ~ gdpfrac', data=dfj2).fit()
print ('%0.2f' % results.rsquared)
results = smf.ols('win ~ yfrac', data=dfj2).fit()
print ('%0.2f' % results.rsquared)
```

```text
0.07
0.12
0.26
```

As we see the $R^2$ of the regression that predicts war outcome from
Beckley's measure is at 0.26 (highest is 1), is much higher than CINC
or GDP used on it own.


