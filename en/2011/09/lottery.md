# The Lottery

I sometimes hear scientists who are not good at math modeling to
justify why it's stupid to buy a lottery ticket. They calculate some
probabilities, and think "there are X number of tickets, and Y many
number combinations", etc and then say it's unlikely for anyone to
win, so why bother?

I argue their model is wrong. They are not taking into account cost /
benefit, and the probability of payoff properly. Here is an
alternative model:

Payoff = Benefit / Cost * probability of winning

In this model, if for example each lottery ticket is one in a million,
costs 1 dollar, potential payoff is 200K, calculation is

```python
benefit = 200000.

cost = 1.

prob = 1./1000000.

print ((benefit/cost)*prob)
```

```text
0.19999999999999998
```

But let's not leave it here. Let's calculate another entity to compare
this _to_. For example .. a paycheck. Guy earns 30K a year, and puts
in 100K of effort to earn that paycheck (employee has to be putting in
more than he gets, right, otherwise he is not a good employee), and he
gets that paycheck with probability 1. There is no chance he will
*not* get his paycheck, a paycheck in that sense is the opposite of a
lottery ticket -- it is almost impossible to win the lottery, it is
almost impossible not to get a paycheck. That calculation is

```python
benefit = 30000.
cost = 100000.
prob = 1.
print ((benefit/cost)*prob)
```

```text
0.3
```

The results are, for lottery 0.2, for paycheck 0.3. Paycheck wins, but
just barely. There is no difference in scale here, and numerical
difference certainly isn't something to sneer at. If our made up
numbers were massaged a little, the lottery ticket could well come
close. 

Then the question isn't why are so many people buying a lottery
tickets.. The question is why isn't everyone?

