# Week 9

<iframe width="340" src="https://www.youtube.com/embed/YNKehLXpLRI?start=214" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

"The U.S. Department of Energy (DOE) is funding a demonstration of the
design, build and operation of the country's first dedicated renewable
hydrogen network, starting in Texas"

[Link](https://www.forbes.com/sites/mitsubishiheavyindustries/2021/02/25/how-the-lone-star-state-is-building-a-green-hydrogen-future/amp/?sh=38354eae7e8a)

---

Newer is usually better.. I'd much rather watch *The Island* than *Logans Run*

---

Printing can cause crash in certain cases, if ur President is the bus
driver and the country is f-ing Venezuella.

---

Calc on past 40 years below. See a -0.89 correlation between gold and
treasuries.

```python
import pandas as pd
import pandas_datareader.data as web
pd.set_option('display.max_columns', None)
today = datetime.datetime.now()
start=datetime.datetime(1980, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
df = web.DataReader(['GC=F', '^TNX','DX-Y.NYB'], 'yahoo', start, end)['Adj Close']
df.columns = ['gold','treasuries','dollar']
df = df.dropna()
print (df.tail(4))
```

```text
                   gold  treasuries     dollar
Date                                          
2021-02-23  1804.400024       1.362  90.169998
2021-02-24  1796.400024       1.389  90.180000
2021-02-25  1774.400024       1.518  90.129997
2021-02-26  1728.099976       1.460  90.930000
```

```python
print (df.corr())
```

```text
                gold  treasuries    dollar
gold        1.000000   -0.891583 -0.395122
treasuries -0.891583    1.000000  0.197605
dollar     -0.395122    0.197605  1.000000
```

---

The highest correlation among the triplet dollar, gold, and treasuries
is between treasuries and gold. This corr is **highly** negative. The
correlation between dollar and gold is much weaker. This means growth
(and inflation) expectations are the main drivers, not some
end-of-the-world currency collapse scenario.

"But printing money will crush the dollar, that's what I know!"

---

"New York Governor Andrew Cuomo announced Thursday Plug Power will
invest $290 million in the construction of a state-of-the-art green
hydrogen fuel production facility [which] will produce 45 tons of
green hydrogen daily. Construction is expected to begin this summer."

[Link](https://www.wkbw.com/news/local-news/green-hydrogen-fuel-production-facility-to-bring-68-jobs-to-genesee-county)

---

The Bernal sphere, the Stanford Torus, O'Neill Cylinder.. A lot of
different names for the same thing. There must be excellent stories
behind each 1 cld learn, had I the time to dive in

---

The "planet chauvinism" comment by Isaac Asimov 

<iframe width="340" src="https://www.youtube.com/embed/GQ98hGUe6FM?start=1078&end=1118" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Just look at FED [GPDNow](https://www.frbatlanta.org/cqer/research/gdpnow) estimate..
As of 3/1 the estimate is 10% growth for Q1.

I am sure they use many base indicators to calculate this.. some
widely known ones [ISM PMI](2019/05/stats.md#gdpism) for ex. That's
how I knew a month ago growth was coming.

"How can some people know GDP will grow?"

---

Better believe it ... See [calc](2019/03/wirespipes.md#10calc)

"I can't believe H2 pipeline can transmit 10x faster than electrical grids"

---

"Hyzon Motors to Build United States’ Largest Fuel Cell Material
Production Facility.. Hyzon Motors chooses Chicago Area as Location
for High-Volume Fuel Cell Membrane Electrode Assembly (MEA) Production
Line"

---

Reuters: "Nikola Corp on Tuesday disclosed details for the rollout of
its hydrogen fuel-cell-powered product lineup, including vehicles with
a driving range of up to 900 miles"

---

Jacobin: "Finland Had a Patent-Free COVID-19 Vaccine Nine Months Ago —
But Still Went With Big Pharma. A team of leading Finnish researchers
had a patent-free COVID-19 vaccine ready last May, which could have
allowed countries all over the world to inoculate their populations
without paying top dollar. Yet rather than help the initiative,
Finland's government sided with Big Pharma — showing how a
patent-based funding model puts profit over public health"

---

Gravity is the [main issue](../../2020/09/space-exploration-goals-colonization.md).
Must have a near-Earth gravity.

"Why not go to any ol' place in space and colonize?"

---

Started using an alternate browser on YouTube, wout logging to GOOG,
works just fine. Recommendations, to the extent they worked before,
continue to work, YT keeps track prev watched vids using browser
cookie, wout knowing true ID. If I manually remove the cookie, the
memory is gone, clean slate.

---

Report was prepared by H2 Council and McKinsey.

The council is made up of >100 companies, w some [well-known](https://pbs.twimg.com/media/EvS25tLXYAAnWCA?format=jpg&name=small)
names.

"Longer-term, a hydrogen pipeline network offers the most
cost-efficient means of distribution. For example, pipelines can
transmit 10 times the energy at one-eighth the costs associated with
electricity transmission lines and have capex costs similar to those
for natural gas. The industry can partially reuse existing gas
infrastructure, but even newly constructed pipelines would not be cost
prohibitive (assuming leakage and other safety risks are properly
addressed). For example, we estimate the cost to transport hydrogen
from North Africa to central Germany via pipeline could amount to
about USD 0.5 per kg of H2 – less than the cost difference of domestic
renewable hydrogen production in these two regions"

[PDF](https://hydrogencouncil.com/wp-content/uploads/2021/02/Hydrogen-Insights-2021-Report.pdf)

---


Air can be DIY compressed in plastic soda bottles, or any other
regular item.

Just saw this kid, pumps 45 psi into PVC pipe through car tire valve
and a hand pump, sealed one end with ball valve, once released the
thing shot a nail with such power it went in the whole 3 inches into
plywood... Dont try at home, jaw-jaw not war-war, etc but this stuff
is no joke... Gases, liquids can be extremely efficient.

---

Gases, liquids are awesome.

---

DIY compressed air turbine from aerodynamics engineer

<iframe width="340" src="https://www.youtube.com/embed/zXEnXEfVBA8?start=270" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

But there cld be true randomness present.. from outside actors, as in
players in a big simulation, whose choices r independent of any
self-contained stimuli.

---

A lot of random appearing stuff may not be random.. Chaos is similar,
but in multiple dimensions, like weather. Its unpredictability stems
tiny deviations causing large changes later, and we can never measure
the tiny starting point effectively, even if we had the perfect
formula describing everything.

---

<img width="340" src="https://pbs.twimg.com/media/EvSnG6IXcAAfkfU?format=png&name=small"/>

---

Creating randomness deterministicallly, sure. Pseudorandom numbers are
generated with algorithms, with the right code u can generate billions
of numbers, before the sequence repeats itself.

---

H2->engine could even be more efficient than H2->electricity->engine. 

"Japan’s Mitsubishi Heavy Industries Engine & Turbocharger, Ltd (MHIET)
is conducting tests on a pure hydrogen gas engine based on its
four-stroke diesel and gas engine technology"

[Link](https://www.rivieramm.com/news-content-hub/news-content-hub/mhi-tests-pure-hydrogen-gas-engine-63725)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Long-range over land hydrogen pipelines can transport 10 times more energy than long-distance electricity transmission lines at one eighth the cost. And existing pipelines can be retrofitted to handle hydrogen to vastly reduce the cost of pipeline projects.<a href="https://t.co/MfCwxjI1YT">https://t.co/MfCwxjI1YT</a></p>&mdash; At War With The Dinosaurs (@WarWithTheDinos) <a href="https://twitter.com/WarWithTheDinos/status/1365344645669093379?ref_src=twsrc%5Etfw">February 26, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Reminder: Abt 1600 miles of H2 pipelines are already [operational](../../2019/03/wirespipes.md#doe) in US
today. This is proven tech.

---

"What goes around comes around" while on a topic abt recycling. Not shabby \#f24

---

The main *Top Gear* host Jeremy Clarkson's [interest](https://www.hydrogenfuelnews.com/jeremy-clarkson-comes-out-in-support-of-hydrogen-fuel-cells/8528018/amp/)
in HFCs is also well-known.

---

JM was cohost of the world famous car show *Top Gear*.

"THE GRAND Tour host James May has written about .. fuel cell electric
vehicles ..  in a piece for the Sunday Times Magazine"

[Link](https://www.driving.co.uk/news/technology/james-may-written-hydrogen-manifesto-instead-reviewing-toyota-mirai/)

---

"@brianschatz

The filibuster was never in the constitution, originated mostly by
accident, and has historically been used to block civil rights. No
legislatures on earth have a supermajority requirement because that’s
stupid and paralyzing. It’s time to trash the Jim Crow filibuster"

---

Long-run consensus is still consensus!

"@ericawerner

219-212 , Biden $1.9T relief plan passes House. 

Zero R 'yes' votes.

Two D 'no' votes"

---

(Dont try at home, works in some cases not in all)

---

$\theta \approx \sin\theta \approx \tan\theta = \partial y/\partial x$? Hot damn!

---

Indigo Swing - Swing Lover \#music

[Link](https://youtu.be/OX9Qd-ri7ks?t=37)

---

UK vaccinated more than all of EU combined? First vaccine development
was partly based in Germany!  There are prod centers in Belgium! Were they
shipping it all to Britain? 

---

Nine great words in the English language; "I'm from the Government,
and I'm here to help".

---

Gov can work..

"@tomgara

I got vaccinated at the new FEMA site in Brooklyn today, and one thing
I didn’t expect was just how good it would feel seeing the kind of
mass public mobilization that’s been missing for the last year ...

The site is running like clockwork and just cranking through the
vaccinations, must've done hundreds in the 15 mins I was there. Was
staffed by a huge number of really delightful National Guard people
from all over the country - the people who gave me my shot were from
Georgia"

---

Our anatomy has largely remained unchanged in the past 300K years, so
yes, human history is much longer. 

---

Hah.. says "fig as old as humanity itself".. Another case of confusing
agro history with real history. We lived thousands of years before
this age.. doesnt that count? (Fig is only 5000 yrs old)

---

They have their stashhhhh, yeeeaaa.. they took their fill, they
stashed it, now they want its value to be maintained for that
stash. That's why they are "stans", and most are also "gold permabulls", is
it called?  Goldcucks? Sorry, goldbugs?

---

You have to wonder why so many millionaires, billionaires support Bitcoin.. 

---

The unemployment measurement problem was known at the FED, among the
various branches, at highest levels. Another Komlos paper
[here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3467994)
talks about alternative measurements proposed by the officials
themselves over the years.

---

Hey man, if it is possible to have SA rels wout the crazy stuff, Im
all for it. 

---

Retweeted by COS dam

"@MaxBoot

The crown prince is a dangerous loose cannon"

---

Khasoggi act .. fits the overall pro dem, pro-human rights stance.. 

---

The Atlantic: "Mars Is a Hellhole. Colonizing the red planet is a
ridiculous way to help humanity"

[Link](https://www.theatlantic.com/ideas/archive/2021/02/mars-is-no-earth/618133/)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">the US is already producing 10Mil. metric tons of <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> / year. there are 1,600 miles of <a href="https://twitter.com/hashtag/h2?src=hash&amp;ref_src=twsrc%5Etfw">#h2</a> pipelines in the US. Hydrogen that can be used for our Hydrogen Electric Cars (w/ Zero GHG <a href="https://twitter.com/hashtag/Emissions?src=hash&amp;ref_src=twsrc%5Etfw">#Emissions</a>) today &amp; meet the growing demand for years to come. <a href="https://twitter.com/ENERGY?ref_src=twsrc%5Etfw">@ENERGY</a> <a href="https://twitter.com/hashtag/FunFactFriday?src=hash&amp;ref_src=twsrc%5Etfw">#FunFactFriday</a> <a href="https://t.co/5BngJE4trS">pic.twitter.com/5BngJE4trS</a></p>&mdash; Energy Independence Now (@DriveH2) <a href="https://twitter.com/DriveH2/status/1002662705570836480?ref_src=twsrc%5Etfw">June 1, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---
