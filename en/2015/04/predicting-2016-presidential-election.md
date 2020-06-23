# Predicting the 2016 Presidential Election

One of the better known models in this area is the *Time for Change*
Model designed by A. Abramowitz. The model uses three factors—the
incumbent president’s net approval rating at the end of June (approval
minus disapproval), the change in real GDP for Q2 (as percentage) of
the election year [annualized](https://www.fool.com/knowledge-center/how-to-calculate-the-annual-growth-rate-for-real-g.aspx),
and a first term incumbency advantage (two terms for the incumbent
party becomes a disadvantage), to predict the winner of the national
popular vote, which can also be used as stand-in for electoral
collage.

Code is below. The fit is crazy good, Prob F near zero, R^2 at 90%,
all predictors are significant.

```python
import io, statsmodels.formula.api as smf, pandas as pd

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

df = pd.read_csv(io.StringIO(s))
regr = 'incumbent_vote ~ gdp_growth + net_approval + two_terms'
results = smf.ols(regr, data=df).fit()
print ('R^2',results.rsquared)
```

```text
R^2 0.9011858911763367
```

For the future, we ran couple of scenarios.

We used different GDP growth and approval rating scenarios for current
adminstration come June; These are growth 1% net popularity 0, growth
3% popularity 10, and growth %5 and popularity 30. The last two cases
are pretty out there, yes; Right now Bam has 0 net popularity. We
based this on here and here. GDP can get better - maybe.

Based on this, you get

```python
conf = results.conf_int()
pred = [1., 1.0, 0., 1]
print (np.dot(pred, conf), np.dot(pred, results.params))
pred = [1., 2.0, 5., 1]
print (np.dot(pred, conf), np.dot(pred, results.params))
pred = [1., 3.0, 10., 1]
print (np.dot(pred, conf), np.dot(pred, results.params))
```

```text
[43.48008619 51.95566396] 47.71787507411282
[44.07413046 53.50829153] 48.79121099512867
[44.66817473 55.0609191 ] 49.864546916144526
```

For the first scenario Hillary's chances of winning are between 43%
and 52%, likely loss. The second one at 2% growth and net popularity
5 is also likely loss. The third is a toss up.

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

[Past Elections Check](prez-loo.md)

