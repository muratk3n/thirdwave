# Tweets - Week 16d

"@JordanUhl

Struggling to graph the psychopathy of a snake oil salesman posing as
a medical expert going on Hannity's show and arguing that 2—3%
mortality rate from sending kids back to school is a "tradeoff" some
will be willing to consider to get the economy open"

[Link](https://mobile.twitter.com/JordanUhl/status/1250815999835848708)

*2020-4-17 13:14:8*

---

"@YorukIsik

Kommersant: .. there are reports that Russia is recruiting Syrian
militants and relocating them to Libya to reinforce the positions of
the Libyan National Army"

*2020-4-17 9:29:35*

---

Attempted at an R0 estimate, if we [go
by](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6002118/) "[t]he
epidemiologicaldefinition of R0 is the average number of secondary
cases produced by one infected individual introduced into a population
of susceptible individuals", then say it takes N days for the symptoms
to occur after infection, then average of last N days would effect the
average of next N days, new cases then divided by the past average can
give an R0 estimate. The estimate shows the world has now R0 < 1. US
is not out of the woods (R0 around 1.2 but decreasing trend).

[Link](https://muratk3n.github.io/thirdwave/en/2020/02/corona_math.html#r0est)

*2020-4-17 8:40:52*

---
 
1st batch of green plums of the year. 

*2020-4-17 7:37:11*

---

"Air travel is bad for the environment – but shipping is not that great
either. James McKenzie wonders how best to decarbonize sea travel"

[Link](https://physicsworld.com/a/could-ammonia-be-the-secret-to-shipping-carbon-free/)

*2020-4-17 6:19:29*

---

"@MerrynSW

\#debtjubilee 'Matt Hancock faces calls to cancel student debt for
nurses tackling coronavirus' - Mirror Online"

*2020-4-16 22:4:40*

---

Haha

"Researchers Delay Coronavirus Vaccine Until They Figure Out How To
Make It Cause Autism"

[Link](https://mobile.twitter.com/CioEnd/status/1249395663613411328)

*2020-4-16 20:57:39*

---

I just saw this on the Polity data page; gov cut their funding? AFAIK
this data set is well-known in academia, and pretty useful for many
ppl.

"NOTICE

For the past twenty-five years, CSP/INSCR data resources, such as
Polity, have been generously supported with funding from the US
Government (through association with the Political Instability Task
Force); that financial support was terminated on 29 February 2020"

[Link](http://www.systemicpeace.org)

*2020-4-16 20:41:31*

---

1973 was the lowest point for democracy for the *entire* 20th
century. It holds the record.

A crazy year. A lot of things ended, collapsed, etc.

*2020-4-16 20:39:1*

---

Haas.. the name sounds familiar. Isn't u some kind of hot shot bro?
How can u eff this simplest observation up?

*2020-4-16 20:30:0*

---

That is actually incorrect. Democracy has been strengthening around
the world. To see that clearly, let's look at the data. The Polity
data set.

[Main Page](http://www.systemicpeace.org/inscrdata.html), [Data](http://www.systemicpeace.org/inscr/p4v2018.xls), [Data - Local](p4v2018.xls)

Their `DEMOC` and `AUTOC` columns contain the level of insititutional
leanings of a country, `POLITY` column is one subtracted from the
other, it ranges btw -10 and +10, the latter being full democracy.

If we group per year and average each country, we see where the world
is heading,


```python
import pandas as pd
df = pd.read_excel('p4v2018.xls')
df = df[df.polity > -10.0]
polity = df.groupby('year')['polity'].mean()
polity.plot()
plt.savefig('polity.png')
```

<img width="340" src="https://pbs.twimg.com/media/EVy9iHGXgAAtkQo?format=png&name=small"/>

It looks to me like things are improving. We are nowhere near +10, but
around a 4.

"@RichardHaass

The global spread of democracy began leveling off some 15 years ago"

[Link](https://mobile.twitter.com/RichardHaass/status/1250796366437199872)

*2020-4-16 20:32:48*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">At this pace Wall Street will make new record highs once everybody is unemployed. <a href="https://t.co/dWMoOCaQ9m">pic.twitter.com/dWMoOCaQ9m</a></p>&mdash; Sven Henrich (@NorthmanTrader) <a href="https://twitter.com/NorthmanTrader/status/1250764674762768389?ref_src=twsrc%5Etfw">April 16, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-4-16 20:13:22*

---

Haha there is a famour archeolog called Michael Shanks the same name
of an actor who played an archeologist on *Stargate*, the TV show.

*2020-4-16 19:23:20*

---

The [answer](https://coincentral.com/wp-content/uploads/2017/12/nano-2-874x437.png)

"@BCAppelbaum

Almost everything about the process of sending stimulus checks to
American families is slower than it needs to be.

Why? Because Congress and the Federal Reserve have failed to modernize
the payments system"

*2020-4-16 19:4:59*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Electricity use in the U.S. is way, way down because of <a href="https://twitter.com/hashtag/COVID19?src=hash&amp;ref_src=twsrc%5Etfw">#COVID19</a> 😦 <a href="https://t.co/TWM0pcSJP7">https://t.co/TWM0pcSJP7</a> <a href="https://twitter.com/hashtag/energyTwitter?src=hash&amp;ref_src=twsrc%5Etfw">#energyTwitter</a></p>&mdash; Choose Energy (@ChooseEnergy) <a href="https://twitter.com/ChooseEnergy/status/1250801552538963968?ref_src=twsrc%5Etfw">April 16, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-4-16 18:38:44*

---

"@mtaibbi

I think all the media figures who spent years wailing about Russian
interference should explain why they're so unconcerned by news that
the Steele report might have been Russian meddling. Is disinformation
only a problem when you didn't help spread it?"

*2020-4-16 18:37:25*

---

5.2 Mil more in initial claims. Wow.

*2020-4-16 18:22:8*

---

If there are systems in place to handle new cases, fine, but.. are they
in place?

"@KelseyTuoc

It's weird that "I'm personally willing to accept a 1-2% risk of death
to reopen the country" is such a common talking point. If somehow the
only cost of reopening the country were a 1-2% risk of me personally
dying, I'd be in favor of it too, obviously.

I am personally unwilling to accept a million people dying to reopen
the country. The thing that happens if we go back to uncontrolled
exponential spread is a 1-2% chance of you dying (depending on
demographics) AND a guarantee of ~ a million people dying"

*2020-4-16 18:21:7*

---



Miyagi - Fear of Missing Out \#music

[Link](https://www.youtube.com/watch?v=YpPOXfM45b0)

*2020-4-16 17:46:48*

---

"@BCAppelbaum

We're now at Great Depression levels of unemployment. We've never
experienced anything like this in the modern era.

25 percent of workers in Michigan are unemployed"

*2020-4-16 17:30:3*

---

"@fuelcellsworks

MHPS J-Series Gas Turbine Fleet Achieves One Million Commercial
Operating Hours--Achieves World Record Reliability of 99.5%"

*2020-4-16 17:28:34*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How much would it cost us to run our company each year if we used: <a href="https://twitter.com/hashtag/Fiat?src=hash&amp;ref_src=twsrc%5Etfw">#Fiat</a>? $566,445. <a href="https://twitter.com/hashtag/BTC?src=hash&amp;ref_src=twsrc%5Etfw">#BTC</a>? $9,443.28. <a href="https://twitter.com/hashtag/ETH?src=hash&amp;ref_src=twsrc%5Etfw">#ETH</a>? 2,481.27. <a href="https://twitter.com/hashtag/BCH?src=hash&amp;ref_src=twsrc%5Etfw">#BCH</a>? 48.18. We use <a href="https://twitter.com/hashtag/NANO?src=hash&amp;ref_src=twsrc%5Etfw">#NANO</a> and it costs us $0.00</p>&mdash; DropShip IO (@dropship_i) <a href="https://twitter.com/dropship_i/status/1250141541210845184?ref_src=twsrc%5Etfw">April 14, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-4-16 17:27:4*

---

"[A] reader from Down Under pointed me to recent research by
Australia's Commonwealth Scientific and Industrial Research
Organisation (CSIRO) that promises to address many of my concerns
regarding hydrogen distribution by making hydrogen from ammonia at the
pump.

These days hydrogen is typically shipped in ready-to-use liquid or gas
form, but the liquifying process consumes 30 percent of its eventual
energy content, and further losses occur from inevitable boil-off in
transit. What the Aussies are proposing is to transport it as liquid
ammonia and then convert it to hydrogen at the point of sale. Fun
fact: The density of hydrogen in liquid ammonia is about 45 percent
greater than in pure liquid hydrogen(!).

Oz has access to far more renewable energy than it knows what to do
with. It's the globe's most solar-energy-rich country, receiving
between 7-8 kW-hr/square meter of solar irradiation per day across the
entire continent; there's also abundant ocean tide energy and plenty
of wind, as well. So the government is keen to export that green
energy, and easily transportable liquid ammonia produced without
generating any CO2 looks like a great way to do so.

Most ammonia produced today involves hydrocarbon feedstocks and hence
produces CO2. CSIRO proposes producing hydrogen by electrolyzing water
and combining it with nitrogen separated from air. These gases are
then compressed and fed into the same Haber-Bosch synthesis reactor
used for hydrocarbon-based ammonia production (which involves
iron-based catalysts, temperatures of 750-930 degrees, and pressures
of 2,200-3,600 psi). Total energy input is roughly 10-12
kW-hr/kilogram of ammonia—all of it clean.

There are no ocean-going hydrogen tanker ships, but ammonia is
routinely shipped by sea. Now CSIRO, in conjunction with Fortescue
Metals Group, has developed a novel two-step process to convert
ammonia into pure hydrogen gas"

[Link](https://www.motortrend.com/news/fuel-cell-fix-making-hydrogen-from-ammonia-at-the-pump-technologue)

*2020-4-16 16:30:9*

---

Moon is pro for my favorite first element in the periodic table 👍 Glad
he won.

"South Korea's coronavirus battle propels Moon's party to election win"

*2020-4-16 11:21:58*

---

With all due respect to the late John Conway (passes away in NJ from
COV) the Free Will Theorem sounds like bunch of mental masturbation. I
think he confused noncomputability of universe with nonpredictability
imbuing the latter with "free will". Universe computes, it computes
itself - so to predict it to its tiniest element u'd need a computer
as large as the universe, see t' Hooft. 

*2020-4-16 7:30:3*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">AVL and Key Project Partners Develop Highly Efficient and Inexpensive Hydrogen Fuel Cell Drive System-Developed a highly efficient and inexpensive <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> <a href="https://twitter.com/hashtag/fuelcell?src=hash&amp;ref_src=twsrc%5Etfw">#fuelcell</a> drive system &amp; integrated it into a demo vehicle-<a href="https://t.co/ac0dszhx1H">https://t.co/ac0dszhx1H</a> <a href="https://twitter.com/hashtag/hydrogennow?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogennow</a> <a href="https://twitter.com/hashtag/decarbonise?src=hash&amp;ref_src=twsrc%5Etfw">#decarbonise</a> <a href="https://twitter.com/hashtag/zeroemissions?src=hash&amp;ref_src=twsrc%5Etfw">#zeroemissions</a> <a href="https://t.co/S3XJDozrhN">pic.twitter.com/S3XJDozrhN</a></p>&mdash; FuelCellsWorks (@fuelcellsworks) <a href="https://twitter.com/fuelcellsworks/status/1250398835085623296?ref_src=twsrc%5Etfw">April 15, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-4-16 6:52:49*

---

"@INVESTMENTSHULK

IF GLOBAL SUPPLY CHAINS CAN’T HANDLE MANUFACTURING A FEW SIMPLE N95
MASKS IN A JUNIOR VARSITY EMERGENCY, HOW DO YOU THINK HUMANITY WILL DO
IDENTIFYING AN INCOMING WORLDKILLER ASTEROID AND NUKING IT TO SHREDS?"

*2020-4-15 20:36:44*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Czechia has 5 days in a row R &lt; 1. Yesterday 5867 new tests and just 82 new cases of covid-19. Overall, 166 deaths. It means 16 deaths per 1M pop. (5x less than in the US, 7x less than Sweden or 24x less than Belgium). Mandatary masks from March 18th. <a href="https://twitter.com/hashtag/Masks4All?src=hash&amp;ref_src=twsrc%5Etfw">#Masks4All</a><a href="https://twitter.com/jeremyphoward?ref_src=twsrc%5Etfw">@jeremyphoward</a> <a href="https://t.co/f8wnlo3iEj">pic.twitter.com/f8wnlo3iEj</a></p>&mdash; Petr Ludwig #Masks4All (@PetrLudwig) <a href="https://twitter.com/PetrLudwig/status/1250459196681678848?ref_src=twsrc%5Etfw">April 15, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-4-15 19:24:58*

---

"Output cuts won't offset market rout": IEA

*2020-4-15 14:45:22*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">ARENA&#39;s $70 million funding round aims to drive down the cost of producing renewable hydrogen through commercial scale electrolyser projects. <a href="https://t.co/8ocKdTz1uD">https://t.co/8ocKdTz1uD</a> <a href="https://t.co/cNqD29tas7">pic.twitter.com/cNqD29tas7</a></p>&mdash; Australian Renewable Energy Agency (@ARENA_aus) <a href="https://twitter.com/ARENA_aus/status/1250333485652271104?ref_src=twsrc%5Etfw">April 15, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-4-15 14:33:56*

---
