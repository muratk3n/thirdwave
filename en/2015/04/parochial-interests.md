# Parochial Interests

There's a very nicely prepared dataset associated with the book The
Logic of Political Survival (2003) written by Bruce B. Mesquita et
al. along with code that can reproduce its statistical results. BBM is
famous for The Predictioneer's Game (2009), where he detailed the use
of game theory for negotations / war. It turns out he had another
theory on governments, democracies, dictatorships in the earlier
book. In this earlier work the claim is that it is not enough to use
labels such as democracy, autocracy to describe / predict which
countries to develop and others not. His main thesis is that the two
most important variables in a country are W and S, the
winning-coalition size and the selectorate size.

[Original Dataset](http://www.nyu.edu/gsas/dept/politics/data/)

[My CSV Version](https://drive.google.com/open?id=13QdSpzbPaJXTr50fuwdKjHpS3iBD6n-c)

Winning coalition W is # of ppl whose support a leader needs to rule,
this is the group of people he needs to keep happy to stay in power,
selectorate S is the # of people from among which members of W are
recruited. With small W, leader only needs to keep a small group happy
paying them off is easier, with large W, bribe becomes harder so
leader must emphasize public services, striving to be elected on the
basis of policy. S in a democracy is the entire electorate, for
autocracies a much smaller group would do i.e. the military, or some
sort of "guard", or a single party out of which even a smaller W would
select the leader.

BBM hypothizes there is a dependence between kleptocracy and W, S; he
finds government theft is maximal when W is small and S is large,
signifying a rigged electoral system where the electorate is large but
their votes do not count, an inner circle decides everything. With
bigger W, kleptocracy decreases.

A counterargument could be there is a hidden effect of population size
on theft, more people, more revenue hence more chances to steal, or
even foreign aid can tip the balance, but BBM "accounts for those
variables (a statistics term)" in his calculations ,taking their
effect out, keeping the focus on W and S. Kleptocracy value itself is
the absolute value difference between tax revenue and expenditures in
proportion to GDP. Absolute value is used because both deficits and
surpluses can be a sign of theft; leader can steal surplus revenue
after its reported or, overspend (on cronies, on their insane pet
projects) which would result in deficit.

Another hypothesis is there is positive relationship between W and
income, countries with larger winning-coalitions are richer, and this
is also confirmed. With everything else the same a country going from
W=0 to W=1 would add 3.0% growth to per capita income. This could seem
small, but if you take per capita income 10,000 dollars in 10 years,

`R=0.03; print 10*1000 * ((1+R)**10.)`

it becomes a whopping 13,439 dollars. So increasing the winning
coalition to its maximum from the worst adds to per capita more than
3,000 dollars.

[geek]

I ran the regressions [myself](lops1.md), both as ordinary linear
regression and as a multilevel model using region/year as the group. I
was able to reproduce results close to what BBM reports, I say close
because I left out some variables (the stuff that BBM ended up finding
unimportant). In kleptocracy model for example R^2 is 20% (BBM gets
over 40%) which is very good. All variables are significant.

[Here](lops2.md) is how to reproduce W from scratch.

There is some mad skillz displayed in accounting for "traditional
democratic" effects that could be seperate from W and S. For that, BBM
take W,S into regression against Polity's democracy, takes the
residuals, feeds them into the main regression coupled with their
variable in question. This way traditional democratic effects, or what
Polity thinks as democracy is controlled for, only coalition and
selectorate size effect remain. F..in A.

I used a combination of Python and R. The book uses Stata (a closed
source software -nasty- but I was glad to have some software
accompanying the book).

[/geek]

Calculating actual W and S is the tricky business. Ideally you'd want
to know the exact size, let's say country X has a military
dictatorship, the military size is 100K, out of which a junta of size
10 rules the country, then S=100K and W=10. But this kind of data is
hard to collect, the authors decided to use another dataset's base
variables to derive W and S. This formula is educational on its
own. The dataset is [Polity
IV](http://www.systemicpeace.org/inscrdata.html), famous for capturing
some base variables on countries' democratic development which also
has its own `democracy` variable that BBM et. al did not use directly,
the variables used for W derivation are `RegimeType`, `xrcomp`, `xropen`,
`parcomp`.

Among these `parcomp` was interesting for me, getting a 5 on that adds
a 1 to your score, and many countries including Turkland has a 4, and
you look up the description for that in Polity manual which says: (4)
Transitional: Any transitional arrangement from [1,2,3] patterns to
fully [5] patterns [..]. Transitional arrangements are accommodative
of competing, parochial interests but have not fully linked parochial
with broader, general interests.  This is funny bcz the presence of
"parochial interests" is a good word to describe TR at the moment.

The best score for W is 1.0. Some surprises, Singapore is rightly
known for its lack of democracy and it gets a 0.4 from Polity, but its
W is 0.75, a score shared by Venezuella and TR. US before Civil War
scores 0.95 on democracy but 0.75 on W. In all these cases W does a
better job in capturing the essence of a regime.

The research in this book appears to have evolved into The Dictator's
Handbook, again by BBM.

