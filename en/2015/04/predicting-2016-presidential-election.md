# Predicting the 2016 Presidential Election
Here is some crazy code. We will use this model to predict past elections (by canceling out that year's  so it cannot tilt the prediction in any way). We will also use it for the 2016 election prediction. [geek] The fit is crazy good, Prob F near zero, R^2 at 90%, all predictors are significant [/geek].

from StringIO import StringIOimport statsmodels.formula.api as smfimport pandas as pds="""year,gdp_growth,net_approval,two_terms,incumbent_vote2012,1.3,-0.8,0,522008,1.3,-37,1,46.32004,2.6,-0.5,0,51.22000,8,19.5,1,50.31996,7.1,15.5,0,54.71992,4.3,-18,1,46.51988,5.2,10,1,53.91984,7.1,20,0,59.21980,-7.9,-21.7,0,44.71976,3,5,1,48.91972,9.8,26,0,61.81968,7,-5,1,49.61964,4.7,60.3,0,61.31960,-1.9,37,1,49.91956,3.2,53.5,0,57.81952,0.4,-27,1,44.51948,7.5,-6,1,52.4"""df = pd.read_csv(StringIO(s))regr = 'incumbent_vote ~ gdp_growth + net_approval + two_terms'results = smf.ols(regr, data=df).fit()

def f(year):    df2 = df[df['year'] != year]    results2 = smf.ols(regr, data=df2).fit()    conf = results2.conf_int()    pred = np.array(df[df['year'] == year])[0][:-1]; pred[0] = 1.    return np.dot(pred, conf)print 'bush/clinton'; print f(1992)print 'gore/bush'; print f(2000)print 'bush/kerry'; print f(2004)print 'mccain/obama'; print f(2008)print 'obama/romney'; print f(2012)

Once you run this on past elections, and using 95% confidence interval for the coefficients, the results for the popular vote percentage is, 

bush/clinton[ 43.68  52.47]gore/bush[ 48.31  60.68]bush/kerry[ 50.66  55.79]mccain/obama[ 41.05  46.15]obama/romney[ 49.81  54.45]

Bush / Clinton guess [43% 52%] points to a likely Bush loss. Clinton won. Bush/Kerry points to a definite Bush win, he won. Mccain / Obama says definite McCain loss, he lost. Bama / Romney, definite Bama win, he did.

The freak event is Bush / Gore. Two things there - there was some possibility for Bush win, and second, well.. the election was stolen. Plus, Gore won the popular vote (that's what the model predicts). 

For the future, we ran couple of scenarios.

We used different  GDP growth and approval rating scenarios for current adminstration come June; These are growth 1% net popularity 0, growth 3% popularity 10, and growth %5 and popularity 30. The last two cases are pretty out there, yes; Right now Bam has 0 net popularity. We based this on here and here. GDP can get better - maybe.

conf = results.conf_int()pred = [1., 1.0, 0., 1]print np.dot(pred, conf), np.dot(pred, results.params)pred = [1., 3.0, 10., 1]print np.dot(pred, conf), np.dot(pred, results.params)pred = [1., 5.0, 30., 1]print np.dot(pred, conf), np.dot(pred, results.params)

Based on this, you get

[ 43.48  51.95] 47.71[ 44.66  55.06 ] 49.86[ 46.39   59.60] 52.99

For the first scenario Hillary's chances of winning are between 43% and 52%, likely loss. The second one at 3% growth and net popularity 10 makes it a toss-up, better campaigner, the one with the better plan can win (or you can pull a Dubya and steal the election). Third is better for Dems.

It is interesting to note that Bill Clinton, known as a good campaigner,  had significant advantages going into the 1992 election. It is also interesting so much hinges on a very rough number such as growth and general popularity. But in a way this makes sense; Voting for a single person  is a blunt instrument really, hence, the basis people use to judge it is also pretty general. Intuitively it makes sense; if a party stays in da house too long, people want to throw you outa there, if there is no growth, the incumbent  is not popular, the climb for the candidate from that party becomes steeper and steeper. 







at

April 10, 2015















