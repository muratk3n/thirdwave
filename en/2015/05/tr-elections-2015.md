# TR Elections 2015

```
year,vote,two_term,party,gdp,gdp2,popularity
1983,23.3,0,Military/MDP,5.0,4.0,0
1987,36.3,0,ANAP,9.5,8.0,1
1991,24.0,1,ANAP,0.7,5.0,0
1995,19.0,0,CHP/DYP,7.9,1.5,0
1999,22.0,0,DYP/ANAP,2.3,0.5,0
2002,8.4,1,DSP/MHP,6.2,0.5,0
2007,46.6,0,AKP,4.7,5.0,1
2011,49.8,1,AKP,9.2,9.0,1
```

The data is for popular vote percentage for the incumbent, as it was
for the US case. The column gdp2 is a rough average of GDP growth of
the election year and the previous year. This was done because of the
turbulent nature of TR economics, for example year 2002 could have
growth of 6.2 but previous year there was a crisis with growth of
-5. I felt that this had to be reflected somehow in the
numbers. Column popularity is a rough 0/1 value of leader popularity -
Ozal had it, Demirel, Ecevit, Ozal caretaker Yilmaz didn't (for
Demirel and Ecevit, their post 90s versions didn't, at least).

In case of a coalition, the vote percentage for the largest piece in
coalition is counted. 

The two_terms column for TR has no effect - because this country
experienced so many coups, anyone who can remain in power for more
than 2 terms is probably pretty successful, so they don't get punished
for this.

The incumbent for 1983 election is taken to be MDP because this is the
party the generals of the 1980 coup "recommended" the public to vote
for. Since the generals were in power, the MDP vote is considered to
be a vote on them (the incumbent). They were ignored, Ozal won the
election.

[geek] The final model has Adjusted R^2=80%. [/geek]. For predictions;
For 2014/2015 GDP growth has been lukewarm, let's take this as
3.0. Leader popularity for AK, this is iffy, ex PM's popularity is not
what it used to be, and then there is the new PM. Let's take this as
0.6, then the absolute best case for the 95% confidence interval shows
40% for AK. This is the _best_ it can be according to the model,
chances are, it will be worse. Even .1 decrease in the popularity
causes dramatic decrease in the popular vote.


