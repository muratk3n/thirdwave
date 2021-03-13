# The Power of Nations Code

Checking if Michale Beckley's GDP x GDP Per Capita measure can predict
war outcomes. Excerpts from the article are [here](power-of-nations-beckley.md).
Data comes from [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/58KDCM)

`reiterwars.tab` has wars from past few centuries, `power1.tab`
carries `GDP`, `CINC`, total population `tpop` and MB's measure
`y`. We could reconstruct the measure from `GDP` and `tpop`
(double-checked, it works, same as `y`). Code was based on Stata `wars
do.do` code in the same repo.

My zipped version of the data is [here](https://drive.google.com/uc?export=view&id=1Gh2-Kq9EigyQ_llE_mwG-WS8Knyi7KQR)

In order to run the regression, MB creates fractions of each measure,
to compare two sides of the measure, through a value between 0 and 1.
These fractions can now 'decide' the outcome of the war, `win` 1 or 0,
whether the initiator (side a) won the conflict or not. The fractions
are in the form of,

$$
y_{frac} = \frac{y_A}{y_A + y_B}
$$

Same approach is used for CINC and GDP.

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
dfj2.to_csv('out.csv')
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

$R^2$ of the regression that predicts war outcome using the new
measure is 0.26 (highest score being 1), better than CINC or GDP.

Preprocessed data for the regression is [here](beckley-wars.csv).

