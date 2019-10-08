# Predicting the 2016 Presidential Election

One of the better known models in this area is the *Time for Change*
Model designed by A. Abramowitz. The model uses three factors—the
incumbent president’s net approval rating at the end of June (approval
minus disapproval), the change in real GDP for Q2 (as percentage) of
the election year, and a first term incumbency advantage (two terms
for the incumbent party becomes a disadvantage), to predict the winner
of the national popular vote.

Here is some crazy code. We will use this model to predict past
elections (by canceling out that year's so it cannot tilt the
prediction in any way). We will also use it for the 2016 election
prediction. [geek] The fit is crazy good, Prob F near zero, R^2 at
90%, all predictors are significant [/geek].

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

For the future, we ran couple of scenarios.

We used different GDP growth and approval rating scenarios for current
adminstration come June; These are growth 1% net popularity 0, growth
3% popularity 10, and growth %5 and popularity 30. The last two cases
are pretty out there, yes; Right now Bam has 0 net popularity. We
based this on here and here. GDP can get better - maybe.

```
conf = results.conf_int()
pred = [1., 1.0, 0., 1]
print np.dot(pred, conf), np.dot(pred, results.params)
pred = [1., 3.0, 10., 1]
print np.dot(pred, conf), np.dot(pred, results.params)
pred = [1., 5.0, 30., 1]
print np.dot(pred, conf), np.dot(pred, results.params)
```

Based on this, you get

```
[ 43.48  51.95] 47.71
[ 44.66  55.06 ] 49.86
[ 46.39   59.60] 52.99
```

For the first scenario Hillary's chances of winning are between 43%
and 52%, likely loss. The second one at 3% growth and net popularity
10 makes it a toss-up, better campaigner, the one with the better plan
can win. Third is better for Dems.

It is interesting to note that Bill Clinton, known as a good
campaigner, had significant advantages going into the 1992
election. It is also interesting so much hinges on a very rough number
such as growth and general popularity. But in a way this makes sense;
Voting for a single person is a blunt instrument really, hence, the
basis people use to judge it is also pretty general. Intuitively it
makes sense; if a party stays in da house too long, people want to
throw you outa there, if there is no growth, the incumbent is not
popular, the climb for the candidate from that party becomes steeper
and steeper.
