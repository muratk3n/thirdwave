# Bruce bd Mesquita's Game Theoretical Method

Bruce bd Mesquita (BdM) developed a method to predict how decisions
are formed within a group of people, nations, alliances, parliaments
so forth. It does not matter whether the group has rivalry or consists
of generally like-minded actors; the method still works. See links at
the bottom of the post for the successes.

The first version of the method took 3 data points per stakeholder to
to base further computation on. Per issue, these measurements are 1)
clout (how much influence an actor has on the issue), 2) his/her
position represented on a 0-100 scale, and 3) a salience measure, how
much an actor cares about that issue. Later versions added hawkish /
doveness as well.

Then BdM processes this data as part of a repeated game in which he
finds the optimum decision point for all parties involved, across all
dyads, taking into account whether actors are hawks, doves, passives,
etc. At every iteration all actors try to bring someone else to their
position, whether successful or not, or how much depends on the 3
attributes shown earlier, and BdM's special algorithm. if someone has
high salience on an issue for example, has lots of influence, this
person might not be swayed, but can be if some of the base numbers
change, etc. Performing this many iterations, a group optimality is
reached, and that is the final decision.

A very important feature of the method is that clout, position and
salience data points need not be researched. Any observer who reads
enough papers, follows politics can come up with them. This is in
favor of the method, that its base data is commonplace.

"Can representing positions between 0-100 scale work?". It does
surprisingly.  In fact I'd suggest anyone who thinks about issues to
think of this scale, in a way we all use it in our heads, no matter
how complex, if granular enough the issue can be represented as
numbers between 0 and 100. 


The Mean Voter Position

A very rough version of this computation would be simply computing the
mean voter position, just to demonstrate the base data of the method.

For example will the EU give debt foregiveness to Greece during this crisis [in 2015]?

Ran some numbers on Greece/EU negotations, using Predictioneer's Game format,

```
     Stakeholder  Clout  Position  Salience
0         Greece    100        40       100
10           USA     30        60       100
1            IMF     20        70       100
2        Juncker     10        80       100
3        Germany    100       100        80
4         France     70       100       100
5   Dijsselbloem     70       100        40
6           Tusk     70       100        40
7          Italy     50       100       100
8            ECB     20       100        70
9          Spain     20       100       100 
```

mean voter 82
weighted mode 100.0

The positions are,

```
0 Debt Relief No Reform
30 Debt Relief Half Reform
60 Debt Relief, Full Reform
80 Debt Relief Soon, Full Reform
100 No Debt Relief, Full Reform
```

I calculate mean voter position 82 and weighted median voter position
is 100 from this -- the final outcome being somewhere btw those
numbers, which contains reform in all cases, and, very unlikely but,
some debt relief in near future. Juncker apparenty dangled this
concession in front of Tsipras, debt relief "sometime this year" as a
last-minute effort to salvage some deal last week, but was declined
(reportedly Juncker was rebuked from the EU side for this action). It
is clear T. does not want spending cuts / programs imposed on himself
/ his government.

```python
def weighted_mode(df):
    df['w'] = df.Clout*df.Salience 
    df['w'] = df['w'] / df['w'].sum()
    df['w'] = df['w'].cumsum()
    return float(df[df['w']>=0.5].head(1).Position)    
def mean(df):
    return (df.Clout*df.Position*df.Salience).sum() / \
           (df.Clout*df.Salience).sum()
```


```python
import pandas as pd
df = pd.read_csv('greece.csv',sep=',')
df = df.sort_index(by='Position')
print df, '\n', 'mean voter', mean(df)
print 'weighted mode', weighted_mode(df)
```

```text
     Stakeholder  Clout  Position  Salience
0         Greece    100        40       100
10           USA     30        60       100
1            IMF     20        70       100
2        Juncker     10        80       100
3        Germany    100       100        80
4         France     70       100       100
5   Dijsselbloem     70       100        40
6           Tusk     70       100        40
7          Italy     50       100       100
8            ECB     20       100        70
9          Spain     20       100       100 
mean voter 82
weighted mode 100.0
```

Shocks

Latest version also introduced a concept of "shocks" by sometimes
randomly altering some salience values, or dropping actors out of the
game to see if the optimum point is "stable", if these changes effect
the final outcome. BdM says he had to introduce this trick after a
project he did analyzing Clinton's Healthcare reform bill and failed
to foresee one scenario, he has since fixed the problem. The details
can be found in *Predictioneer's Game*.

<a name='inborn'/>

Inborn Ability

Some ppl do have natural skillz on predictive social dynamics meaning
basically an ability to run BdM's computations in their head. When BdM
put the algo up for competition against international politics
analysts, he saw some people consistenly tied the machine. Such
people, then, basically had that internal machinery for social
dynamics prediction wired into them.

Links

[B. Mesquita and Iran](../../2015/04/mesquita-iran.md)

[B. Mesquita and India](../../2015/04/mesquita-india.md)

