# Prez Prediction, Past Elections, Leave-One-Out Check

We will use this model to predict past elections (by canceling out
that year's so it cannot tilt the prediction in any way). We will also
use it for the 2016 election prediction.

```
from StringIO import StringIO
import statsmodels.formula.api as smf
import pandas as pd
s="""year,gdp_growth,net_approval,two_terms,incumbent_vote
2012,1.3,-0.8,0,52
2008,1.3,-37,1,46.3
2004,2.6,-0.5,0,51.2
2000,8,19.5,1,50.3
1996,7.1,15.5,0,54.7
1992,4.3,-18,1,46.5
1988,5.2,10,1,53.9
1984,7.1,20,0,59.2
1980,-7.9,-21.7,0,44.7
1976,3,5,1,48.9
1972,9.8,26,0,61.8
1968,7,-5,1,49.6
1964,4.7,60.3,0,61.3
1960,-1.9,37,1,49.9
1956,3.2,53.5,0,57.8
1952,0.4,-27,1,44.5
1948,7.5,-6,1,52.4
"""
df = pd.read_csv(StringIO(s))
regr = 'incumbent_vote ~ gdp_growth + net_approval + two_terms'
results = smf.ols(regr, data=df).fit()

def f(year):
    df2 = df[df['year'] != year]
        results2 = smf.ols(regr, data=df2).fit()
	    conf = results2.conf_int()
	        pred = np.array(df[df['year'] == year])[0][:-1]; pred[0] = 1.
		    return np.dot(pred, conf)
		    print 'bush/clinton'; print f(1992)
		    print 'gore/bush'; print f(2000)
		    print 'bush/kerry'; print f(2004)
		    print 'mccain/obama'; print f(2008)
		    print 'obama/romney'; print f(2012)
```

Once you run this on past elections, and using 95% confidence interval
for the coefficients, the results for the popular vote percentage is,

```
bush/clinton
[ 43.68  52.47]
gore/bush
[ 48.31  60.68]
bush/kerry
[ 50.66  55.79]
mccain/obama
[ 41.05  46.15]
obama/romney
[ 49.81  54.45]
```

Bush / Clinton guess [43% 52%] points to a likely Bush loss. Clinton
won. Bush/Kerry points to a definite Bush win, he won. Mccain / Obama
says definite McCain loss, he lost. Bama / Romney, definite Bama win,
he did.

The freak event is Bush / Gore. Two things there - there was some
possibility for Bush win, and second, well.. the election was
stolen. Plus, Gore won the popular vote (that's what the model
predicts).




