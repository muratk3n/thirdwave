# Midterm 2018

```
import pandas as pd, io

csv = """
President,Year,Approve,Disprove,HGain,SGain
Obama,2014,40,54,13,9
Obama,2010,44,48,63,6
W,2006,38,56,31,5
W,2002,66,26,8,0
Clinton,1998,66,30,-4,0
Clinton,1994,46,46,54,9
HW,1990,54,35,7,1
Reagan,1986,64,28,5,8
Reagan,1982,42,47,26,1
"""

df = pd.read_csv(io.StringIO(csv))
df['Net'] = df.Approve-df.Disprove
import statsmodels.formula.api as smf
results = smf.ols('Net ~ HGain', data=df).fit()
print ("r^2", results.rsquared_adj)
djt = 40-55
print ("dem gains pred", results.params.Intercept + results.params.HGain*djt)

r^2 0.3079556950086001
dem gains pred 33.442389832274195
```

The model explains 30% of the variation, not bad. For DJT popularity
40 approve 55 disprove the prediction for Democrat gains were 33. For
2018, with most of the races called in, we see over 25 gains.

Why is this result so normal? To the extent that a simple, single
variable can predict it? Obama had a whopping 63 seat gain on him
once, abt the same for Clinton. I believe the problem is Democrats'
message is faulty. If people have to choose between right and lukewarm
right, that is not a choice. Dems will be left to pick crumbs, as they
do now, the usual back-and-forth of the political seasons will bring
them some gains, but nothing stellar. They are still playing the Rep
game. Absent a crisis a DJT reelection assured it will have been 28
years of Rep executive compared to 16 years for Dems for the past 44
years, 4 ppl vs 2 ppl.

Other interesting 2018 results were in Texas and Florida, for Senate
and governorship. The results there were just abysmal. Fucking
centrists need to be weeded out much more inside the party. Suave,
Holywood candidates don't cut it anymore.










