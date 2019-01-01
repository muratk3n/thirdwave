# Greece/EU

Ran some numbers on Greece/EU negotations, using Predictioneer's Game format,

```
     Stakeholder  Clout  Position  Salience
0         Greece    100        40       100
10           USA     30        60       100
1            IMF     20        70       100
2        Juncker     10        80       100
3        Germany    100       100        80
4         France     70       100       100
5   Dijsselbloem     70       100        40
6           Tusk     70       100        40
7          Italy     50       100       100
8            ECB     20       100        70
9          Spain     20       100       100 
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

Salience is how much an actor cares about a decision. I calculate mean
voter position 83 and weighted median voter position is 100 from this
-- the final outcome being somewhere btw those numbers, which contains
reform in all cases, and, very unlikely but, some debt relief in near
future. Juncker apparenty dangled this concession in front of Tsipras,
debt relief "sometime this year" as a last-minute effort to salvage
some deal last week, but was declined (reportedly Juncker was rebuked
from the EU side for this action). It is clear T. does not want
spending cuts / programs imposed on himself / his government.

The input data is based on my impression of the situation, others
might have different ideas. Also, [da
masta](https://en.wikipedia.org/wiki/Bruce_Bueno_de_Mesquita)
processes this data as part of a repeated game in which he finds the
optimum point for all parties involved, across all dyads, taking into
account whether actors are hawks, doves, passives, etc. He can
introduce "shocks" by sometimes randomly altering some salience
values, or dropping actors out of the game to see if the optimum point
is "stable", if these changes effect the final outcome [1]. But my
guess is in this case a repeated game calculation would not make much
difference.

[Notebook](eu_greece.md)

---

[1] Da masta says he had to introduce this trick after a project he
did analyzing Clinton's Healthcare reform bill and failed to foresee
one scenario, he has since fixed the problem. The details can be found
in *Predictioneer's Game*.








at

July 08, 2015















