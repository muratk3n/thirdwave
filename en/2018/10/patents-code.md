# Patent Codebook

[File 1](https://drive.google.com/open?id=1V3-TZNG5qBD5I2zO9kpdvzkzZzYhTYOL),
[File 2](https://drive.google.com/open?id=16tJOCsiAopWaizVBH-7bUFhCSAE8FF7Y),
[File 3](https://drive.google.com/open?id=1VGHOp5P6GyINU-NWSQqehNbjhVoPwIyP),
[File 4](https://drive.google.com/open?id=1n535aApoBMp8k2zAbX3hBB-ctY9hFIOf),
[File 5](https://drive.google.com/open?id=1kWC0FLJR3sLNOcpwIEn1tYzz79LoE-F5),
[File 6](https://drive.google.com/open?id=1KVCmmwCJoFm7yD_zvX-DkK2qY68t4HYx),
[File 7](https://drive.google.com/open?id=11_5HWHr4nfDYiY3WUEHkjd3a4VgaCkr9)


TFP is total factor productivity - the portion of output not explained
 by the amount of inputs used in production. As such, its level is
determined by how efficiently and intensely the inputs are utilized in
production.

Needs Python 3

Do `pip install linearmodels`


```python
import pandas as pd
dfcomp = pd.read_stata('compinn_BLS.dta')
dfpi = pd.read_stata('CapitalRentalPriceIndex2000.dta')
dfcs = pd.read_stata('PatentsCompustatImportsRPI.dta')
print (dfpi.columns)
print (dfcomp.columns)
print (dfcs.columns)
```

```
Index([u'naics', u'yr1987', u'yr1988', u'yr1989', u'yr1990', u'yr1991',
       u'yr1992', u'yr1993', u'yr1994', u'yr1995', u'yr1996', u'yr1997',
       u'yr1998', u'yr1999', u'yr2000', u'yr2001', u'yr2002', u'yr2003',
       u'yr2004', u'yr2005', u'yr2006', u'yr2007'],
      dtype='object')
Index([u'NAICS', u'year', u'lab_hrs', u'cap', u'cap_sh', u'cap_ind', u'mat',
       u'mat_sh', u'def', u'lab', u'lab_sh', u'tfp', u'lab_pr', u'out_ind',
       u'output', u'import', u'imp_problem', u'cap_stock', u'imp_pen',
       u'impdef', u'lnimp', u'lnimpdef', u'lntfp', u'lnlab_pr'],
      dtype='object')
Index([u'year', u'conm', u'oiadp', u'oibdp', u'ppegt', u'ppent', u'sale',
       u'xad', u'xrd', u'sich', u'sic', u'gvkey', u'allpats', u'allcites',
       u'allcites_cor', u'allnscites', u'allnscites_cor', u'gvkeyag',
       u'gallpats', u'gallcites', u'gallcites_cor', u'gallnscites',
       u'gallnscites_cor', u'gmtchflg', u'sic4', u'imports', u'merge_comp_imp',
       u'emp', u'pay', u'prode', u'prodh', u'prodw', u'vship', u'matcost',
       u'vadd', u'invest', u'invent', u'energy', u'cap', u'equip', u'plant',
       u'piship', u'pimat', u'piinv', u'pien', u'dtfp5', u'tfp5', u'dtfp4',
       u'tfp4', u'share', u'merge_compimp_nber', u'naics6', u'naics4',
       u'naics3', u'naics2', u'crp4', u'crp3', u'crp2', u'crp_index'],
      dtype='object')
```

```python
dfcs2 = dfcs[['year','allpats','tfp4','naics4']].dropna()
from linearmodels import PanelOLS
dfcs3 = dfcs2.set_index(['year','naics4'])
mod = PanelOLS(dfcs3.tfp4, dfcs3[['allpats']], entity_effects=True)
res = mod.fit(cov_type='clustered', cluster_entity=True)
print (res)
```

```
                          PanelOLS Estimation Summary                           
================================================================================
Dep. Variable:                   tfp4   R-squared:                        0.0058
Estimator:                   PanelOLS   R-squared (Between):              0.0439
No. Observations:               57314   R-squared (Within):               0.0058
Date:                Mon, Oct 15 2018   R-squared (Overall):              0.0140
Time:                        21:55:07   Log-likelihood                -1.569e+05
Cov. Estimator:             Clustered                                           
                                        F-statistic:                      334.66
Entities:                          37   P-value                           0.0000
Avg Obs:                       1549.0   Distribution:                 F(1,57276)
Min Obs:                       76.000                                           
Max Obs:                       2328.0   F-statistic (robust):             18.063
                                        P-value                           0.0000
Time periods:                      81   Distribution:                 F(1,57276)
Avg Obs:                       707.58                                           
Min Obs:                       2.0000                                           
Max Obs:                       8456.0                                           
                                                                                
                             Parameter Estimates                              
==============================================================================
            Parameter  Std. Err.     T-stat    P-value    Lower CI    Upper CI
------------------------------------------------------------------------------
allpats        0.0044     0.0010     4.2501     0.0000      0.0023      0.0064
==============================================================================

F-test for Poolability: 114.44
P-value: 0.0000
Distribution: F(36,57276)
```

```python
print (dfcs3.allpats.mean())
print (dfcs3.tfp4.mean())
print (dfcs3.tfp4.std())
```

```
10.96653522699515
1.6352721
3.8797197
```



