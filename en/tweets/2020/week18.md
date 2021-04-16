# Tweets - Week 18a

"@RoryVanLoo

'The New Gatekeepers' is up. It shows how the government increasingly
requires giants like Facebook, Citibank, Exxon, & Gilead to regulate
smaller businesses"

[Link](https://mobile.twitter.com/RoryVanLoo/status/1255853230409625601)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hydrogen Industry: The Dawning Of The <a href="https://twitter.com/hashtag/Hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#Hydrogen</a> <a href="https://twitter.com/hashtag/Economy?src=hash&amp;ref_src=twsrc%5Etfw">#Economy</a> <a href="https://t.co/WD8L1rYcWX">https://t.co/WD8L1rYcWX</a></p>&mdash; BayoTech On-Site Hydrogen Generation (@H2Bayo) <a href="https://twitter.com/H2Bayo/status/1256192516094939136?ref_src=twsrc%5Etfw">May 1, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

The three UFO videos

[Link](https://youtu.be/Q7jcBGLIpus)

---

So this thing basically runs on its own - making energy out of thin
air.. How is this not a replacement for the current way we generate
energy?

"A solar-powered hydrogen station has been built in the Japanese town
of Namie, which can power 560 fuel-cell cars a day"

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">St Petersburg University Students Develop a <a href="https://twitter.com/hashtag/Hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#Hydrogen</a> Fuel Cell to Replace Lithium-Ion Batteries--This new <a href="https://twitter.com/hashtag/fuelcell?src=hash&amp;ref_src=twsrc%5Etfw">#fuelcell</a> is expected to be 30% cheaper“ and uses an innovative nanostructured nickel mesh as a catalyst--<a href="https://t.co/6MuEsy2x4i">https://t.co/6MuEsy2x4i</a> <a href="https://twitter.com/hashtag/hydrogennow?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogennow</a> <a href="https://twitter.com/hashtag/fuelcells?src=hash&amp;ref_src=twsrc%5Etfw">#fuelcells</a> <a href="https://twitter.com/hashtag/zeroemissions?src=hash&amp;ref_src=twsrc%5Etfw">#zeroemissions</a> <a href="https://twitter.com/hashtag/h2?src=hash&amp;ref_src=twsrc%5Etfw">#h2</a> <a href="https://t.co/wLqFBBDRC9">pic.twitter.com/wLqFBBDRC9</a></p>&mdash; FuelCellsWorks (@fuelcellsworks) <a href="https://twitter.com/fuelcellsworks/status/1256199864578453511?ref_src=twsrc%5Etfw">May 1, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Looks fun

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">GOOD NEWS guys, not ALL the <a href="https://twitter.com/hashtag/sports?src=hash&amp;ref_src=twsrc%5Etfw">#sports</a> are canceled!<br>But: is this a game, a manly duel, or a bad romance? <a href="https://twitter.com/hashtag/bunnyhop?src=hash&amp;ref_src=twsrc%5Etfw">#bunnyhop</a> <a href="https://t.co/t4KRhi5osc">pic.twitter.com/t4KRhi5osc</a></p>&mdash; Elizabeth Withey (@lizwithey) <a href="https://twitter.com/lizwithey/status/1255726551154360320?ref_src=twsrc%5Etfw">April 30, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

You got that [backwards](../../2020/05/roman-anatolia.md)

"Paraphrasing: the arriving ppl from Central As changed Anatolia"

--

Another dataset on democracies. BTI Transformation Index that
evaluates aspects of governance for selected countries is updated for
2020.

Data on [Downloads](https://www.bti-project.org/en/meta/downloads.html).  I
looked at TR vs RU (using the Stata file),

```python
import pandas as pd
df = pd.read_stata('BTI 2006-2020.dta')
df = df.set_index('year')
df1 = df[df.country == 'Russia'].dem_stat
df2 = df[df.country == 'Turkey'].dem_stat
df3 = pd.concat([df1,df2],axis=1)
df3.columns = ['RU','TR']
df3.plot()
plt.savefig('bti.png')
```

<img width="340"  src="https://pbs.twimg.com/media/EW6oGScWoAEtRYN?format=png&name=small"/>

TR approached RU values lately, major degradation. Still better than
RU but these ppl spent decades under one-party state while TR did
not. Shouldn't the difference be higher?

There are some interesting columns in there,

```python
print (list(df.columns))
```

```text
['country', 'country_code', 'region', 'rank_stat_ind',
'stat_ind', 'rank_dem_stat', 'dem_stat', 'stateness', 'monopoly',
'identity', 'no_dogmas', 'admin', 'pol_part', 'elect', 'power',
'assembly', 'express', 'ruleoflaw', 'separation', 'judiciary',
'prosecution', 'civ_rights', 'stab_dem', 'perf_dem', 'com_dem',
'integ', 'party_sys', 'int_group', 'approv_dem', 'soc_cap',
'rank_econ_stat', 'econ_stat', 'level_development', 'barriers',
'market', 'compet', 'comp_pol', 'for_trade', 'bank', 'stab_econ',
'infl', 'macro_stab', 'priv_prop', 'prop_rights', 'priv_ent',
'welfare', 'safety_nets', 'equal', 'perf_econ', 'output', 'sustain',
'envir', 'edu', 'rank_gov_ind', 'gov_ind', 'level_diff', 'constr',
'civil_trad', 'conflict_intens', 'GNI', 'UN_edu', 'state_rol',
'gov_perf', 'steering', 'priority', 'implement', 'learning',
'efficiency', 'assets', 'coord', 'anti_corrupt', 'consens', 'goals',
'veto', 'cleavage', 'civil_part', 'recon', 'int_coop', 'use_support',
'cred', 'reg_coop', 'trend_dem', 'trend_econ', 'trend_gov',
'core_stateness', 'state_failure', 'pol_sys', 'cat_stat_ind',
'cat_dem_stat', 'cat_trend_dem', 'cat_econ_stat', 'cat_trend_econ',
'cat_gov_ind', 'cat_trend_gov', 'cat_level_diff', 'stateness_cat',
'pol_part_cat', 'ruleoflaw_cat', 'stab_dem_cat', 'integ_cat',
'level_development_cat', 'market_cat', 'stab_econ_cat',
'priv_prop_cat', 'welfare_cat', 'perf_econ_cat', 'sustain_cat',
'level_diff_cat', 'steering_cat', 'efficiency_cat', 'consens_cat',
'int_coop_cat']
```

`judiciary`? `prop_right`? Looks interesting. 

This dataset can be useful for researchers. There is a codebook
describing all the columns.

---

<blockquote class="twitter-tweet"><p lang="de" dir="ltr"><a href="https://twitter.com/search?q=%24DGB&amp;src=ctag&amp;ref_src=twsrc%5Etfw">$DGB</a> vs <a href="https://twitter.com/search?q=%24NANO&amp;src=ctag&amp;ref_src=twsrc%5Etfw">$NANO</a> <a href="https://t.co/fJcMc6XYHJ">https://t.co/fJcMc6XYHJ</a> <a href="https://t.co/mgCNDUwE7L">pic.twitter.com/mgCNDUwE7L</a></p>&mdash; IdealFog (@IdealFog) <a href="https://twitter.com/IdealFog/status/1254815512715919365?ref_src=twsrc%5Etfw">April 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">21 USC §§331, 333, 343(g) &amp; 21 CFR §133.154 make it a federal crime to sell high-moisture jack cheese if it isn&#39;t moist enough, but not too moist.</p>&mdash; A Crime a Day (@CrimeADay) <a href="https://twitter.com/CrimeADay/status/1256061343167176705?ref_src=twsrc%5Etfw">May 1, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

There is data from Quandl on this but time series stops at 2018 for
some reason. Ideally I'd like to get it from them.

---

World oil [production](https://www.eia.gov/outlooks/steo/xls/Fig6.xlsx), from [IEA](https://www.eia.gov/outlooks/steo/data.php) 

I guess data for production before April are real, but the rest is
projection. It'd be great to supply data as one CSV, and a CSV per
concept, like `world-production.csv` with simple format so ppl dont
have to dig through the cells like I did.

```python
# Unit million bbls per day
import pandas as pd
df = pd.read_excel('/tmp/Fix6.xlsx')
arr = np.array(df)[25:50,3:5]
df2 = pd.DataFrame(arr)
df2.columns = ['date','oil']
df2['oil'] = df2.oil.astype(float)
df2['date'] = pd.to_datetime(df2.date)
df2 = df2.set_index('date')
print (df2.tail(8))
```

```text
                   oil
date                  
2019-04-01  100.305388
2019-07-01  100.063067
2019-10-01  101.605337
2020-01-01  100.112812
2020-04-01   99.416189
2020-07-01   98.735324
2020-10-01   99.314964
2021-01-01   99.011546
```

---

Emacs! 👍

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Typing.<br>Emacs.<br>Measure theory/Lebesgue integration. <a href="https://t.co/2wPIH8QJLI">https://t.co/2wPIH8QJLI</a></p>&mdash; Dirk L. (@Dirque_L) <a href="https://twitter.com/Dirque_L/status/1256257898050658304?ref_src=twsrc%5Etfw">May 1, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

BTW - who names a health insurance after one of the most deadliest
snakes in the world? These ppl are psychopaths.

---

I was thinking M4A a good compromise solution for affordable and
humane care but maybe UK method is even better (all health is managed
directly by gov, reports to PM). Johnson keeps saying how they work
hard to flatten the curve bcz "we had to prevent our NHS from being
overwhelmed" - now that's a thing a politician can observe and
optimize on, bcz it is directly under their purview in UK, which it
turns out to be something useful for the populace at large. It is
always good to have the right incentives in place... So pol can do
things to protect NHS which in turn protects the public.

In US federal pols could be like ... meh.. I dont know.. there are
bunch of hospitals out there and stuff, ppl can go there.. and like,
fend for themselves? And we'll, like, save COBRA or something.. Just
wave a hand and dismiss the problem bcz it doesnt effect any
bureucracy they control directly.

I am not saying pols necessarily dont care for people, but in some
instances it is not clear what to __do__ about the problem, which
gears to __turn__ to cause change. For UK it is very simple - protect
NHS. Expand NHS - if necessary. I am sure they have a lively research
arm and can put out some good solutions - well, that's great. Help NHS
to research, or coordinate research with others, unis so forth. The
research results too can then be used directly, through NHS, wout this
talk of patents, executive orders, etc. During the time of emergency
it is beyond distasteful to hear of this stuff.

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Finally.<a href="https://t.co/jBKwJh7Y63">https://t.co/jBKwJh7Y63</a></p>&mdash; Governor Jay Inslee (@GovInslee) <a href="https://twitter.com/GovInslee/status/1255900615353397250?ref_src=twsrc%5Etfw">April 30, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

The tech sucks - get out, pronto \#bitshitcoin

<img src="https://pbs.twimg.com/media/EW3sNJoXYAAH0tO?format=jpg&name=small"/>

---

"Lebanese elites flee as banks come under attack"

[Link](https://asiatimes.com/2020/04/lebanese-elites-flee-as-banks-come-under-attack/)

---

Interesting in Trek universe the ugliest looking motherfuckers are an
alien race of uber-capitalists. 

---

The main constitutional doc for Ferrengis is "Ferrengi Bill of
Opportunities" 😆😆😆

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The fuel of the future has become the fuel of the now. LA is replacing a coal-fueled power plant with one that will run completely on <a href="https://twitter.com/hashtag/greenhydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#greenhydrogen</a>: <a href="https://t.co/mfmg9euAwf">https://t.co/mfmg9euAwf</a> <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> <a href="https://twitter.com/hashtag/climate?src=hash&amp;ref_src=twsrc%5Etfw">#climate</a> <a href="https://twitter.com/hashtag/sustainability?src=hash&amp;ref_src=twsrc%5Etfw">#sustainability</a></p>&mdash; Ballard Power (@BallardPwr) <a href="https://twitter.com/BallardPwr/status/1255558466569199617?ref_src=twsrc%5Etfw">April 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

3.8 M more in jobless claims.

[Link](https://muratk3n.github.io/thirdwave/en/2019/05/stats.html#claims)

---

"@ddiamond

The first serious Covid-19 case in Minnesota was a 38-year-old Ironman
athlete who nearly died and still relies on oxygen five weeks later"

---

"Bosch intends to position itself successfully in another growth
market: As early as 2030, one in eight newly registered heavy trucks
could be powered by a fuel cell thanks to work Bosch is undertaking
with partner Ceres Power on stationary fuel cells.

These can supply buildings such as a computing centres with
electricity and Bosch anticipates that the market for fuel cell power
stations will be worth more than €20bn by 2030"

[Link](https://www.h2-view.com/story/bosch-ceo-calls-for-a-move-to-a-hydrogen-economy/)

---

<img width="240"  src="https://pbs.twimg.com/media/EW0HHtKXgAARPRD?format=jpg&name=small"/>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The populist right is far more real in advocating for actual people than any of the lefts grandstanding. <a href="https://t.co/2LssO5s65r">https://t.co/2LssO5s65r</a></p>&mdash; Dylan Ratigan (@DylanRatigan) <a href="https://twitter.com/DylanRatigan/status/1255573829491056641?ref_src=twsrc%5Etfw">April 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"@covidperspectiv

The Mayor of Los Angeles has announced that effective immediately, any
LA resident can get tested for coronavirus, regardless of whether they
have symptoms. The tests are free of charge. LA is the first major
city in America to offer this"

---

"@LeeCamp

The US government is flying expensive fighter jets over US
cities. They're not doing it to boost morale & thank workers. They're
doing it to remind us that the Military Industrial Complex will keep
gorging on our tax money while we're left to suffer through a
pandemic"

---

"Walmart’s distribution centre in Gordonsville, Virginia ... operates a
fleet of 273 hydrogen fuel cell forklifts"

[Link](https://www.h2-view.com/story/hydrogen-fuel-cells-playing-essential-role-in-keeping-food-on-shelves-in-the-us/)

---

Hah. Very partisan, colorful history. And former pharma lobbyst - of course.

"After law school [HHS Sec Azar] served as a law clerk under late
Supreme Court Justice Antonin Scalia... Azar moved on to work for
Kenneth Starr as an Associate Independent Counsel from 1994 to 1996,
where he primarily worked on the Whitewater investigation... Azar was
on [W's] legal team during the contentious Florida recount case
following the 2000 presidential election"

[Link](https://www.usnews.com/news/national-news/articles/2018-01-29/10-things-you-didnt-know-about-alex-azar)

---

Marco. Polo. 

Nikola. Tesla.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Patent Office gives Nikola a small victory in $2B lawsuit over Tesla Semi--<a href="https://t.co/6lKx4KtxNC">https://t.co/6lKx4KtxNC</a> <a href="https://twitter.com/nikolamotor?ref_src=twsrc%5Etfw">@nikolamotor</a> <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> <a href="https://twitter.com/hashtag/HydrogenNow?src=hash&amp;ref_src=twsrc%5Etfw">#HydrogenNow</a> <a href="https://twitter.com/hashtag/decarbonise?src=hash&amp;ref_src=twsrc%5Etfw">#decarbonise</a> <a href="https://twitter.com/hashtag/zeroemissions?src=hash&amp;ref_src=twsrc%5Etfw">#zeroemissions</a> <a href="https://twitter.com/hashtag/fuelcell?src=hash&amp;ref_src=twsrc%5Etfw">#fuelcell</a> <a href="https://twitter.com/hashtag/fuelcells?src=hash&amp;ref_src=twsrc%5Etfw">#fuelcells</a> <a href="https://twitter.com/fuelcellsworks?ref_src=twsrc%5Etfw">@fuelcellsworks</a> <a href="https://twitter.com/hashtag/h2?src=hash&amp;ref_src=twsrc%5Etfw">#h2</a> <a href="https://t.co/O2ZlJiKJZO">pic.twitter.com/O2ZlJiKJZO</a></p>&mdash; FuelCellsWorks (@fuelcellsworks) <a href="https://twitter.com/fuelcellsworks/status/1255509472849661954?ref_src=twsrc%5Etfw">April 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Well - the bad effects can stil stick on the incumbent. Think of
election 1980, Carter vs Reagan - the hostage crisis at the time was
too "external", there were gas lines, .. due to Iran, so external
again..?  But Carter lost. -8% GDP growth, net popularity -21%!

"But the econ crisis was the effect of something external"

---

Q1 GDP growth 0.32% YoY, -4.78% QoQ annualized. 😶

Trump's net approval is down to its abysmal low again, at -10%. If
this situation persists for Q2, even a sock puppet will win as a
challenger.

[Link](https://muratk3n.github.io/thirdwave/en/2019/05/stats.html)

---

<blockquote class="twitter-tweet"><p lang="und" dir="ltr">byeeeeeeeeeeeeeeeee <a href="https://t.co/7VHsTLHXNo">https://t.co/7VHsTLHXNo</a></p>&mdash; Dr Matt Cole (@MattColeWorks) <a href="https://twitter.com/MattColeWorks/status/1255449305151913985?ref_src=twsrc%5Etfw">April 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"The University of Queensland's COVID-19 vaccine has shown in
pre-clinical tests it can raise high levels of antibodies that can
neutralise the virus.

The university's project co-leader Professor Paul Young said the
results were an excellent indication the vaccine worked as expected"

[Link](https://www.9news.com.au/national/coronavirus-university-of-queensland-vaccine-shows-promising-results/6fc2cf99-3db5-4710-bf64-c5a9d68c79b5)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="https://twitter.com/search?q=%24NANO&amp;src=ctag&amp;ref_src=twsrc%5Etfw">$NANO</a> is THE fastest, decentralized cryptocurrency and it DOESN&#39;T have fees. <a href="https://t.co/ZLGdT8KY4o">pic.twitter.com/ZLGdT8KY4o</a></p>&mdash; CoinMoon🌎🌍🌏 (@CoinMoon5) <a href="https://twitter.com/CoinMoon5/status/1255431796688371714?ref_src=twsrc%5Etfw">April 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"Massive project gets green light after securing $300m investment in
Australia-Perth"

[Link](https://twitter.com/william_sw/status/1255401426433564672)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">the plot of every single episode of star trek ever <a href="https://t.co/ch4UyEYtXl">https://t.co/ch4UyEYtXl</a></p>&mdash; Tim Maughan (@timmaughan) <a href="https://twitter.com/timmaughan/status/1255256091396657153?ref_src=twsrc%5Etfw">April 28, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"@CMastication

If you’re building an API for analytical data I have a secret for you:
the answer is CSVs, not the goddamn ridiculous hierarchical restful
piece of bullshit you built"

---

I dont know.. 🤔 sounds suggestive to me.. 

>'Oh, I like it a lot!'
>
>Said the Cat in the Hat
>
>To the fish in the pot

---

Daam. What's next? Cat in a Hat?

"Alaska school board removed five famous — but allegedly
'controversial' — books from district classrooms ... 'I Know Why the
Caged Bird Sings' by Maya Angelou, 'Catch-22' by Joseph Heller, 'The
Things They Carried' by Tim O'Brien, 'The Great Gatsby' by F. Scott
Fitzgerald, and 'Invisible Man' by Ralph Ellison were all taken off an
approved list...

'If I were to read these in a corporate environment, in an office
environment, I would be dragged into EO,' an equal opportunity
complaint proceeding, Hart said....

[Link](https://www.nbcnews.com/news/amp/ncna1194436)

---

"@natashalennard

Based on mainstream news coverage alone you’d likely never know that
organizers and tenants in New York are preparing the largest
coordinated rent strike in nearly a century, to begin on May 1"

---

New breakfast regime going well, almonds, walnuts, dried apricot,
etc.. Extremely durable stuff. Tested bags of it in camp gear for
weeks, shit wont go bad. I can imagine going whole day on such breakf,
in outdoor conditions.

---

Wow

"@TheWorkshyFop

Peasants didn't 'bargain for better pay and conditions' after the
plague, they got them by killing tax collectors, executing the
chancellor, and burning down the Savoy"

---

BEVs - what a moronic f-ing tech.. Unbelievable it even came this far.

"Earlier this year, BMW announced the next generation of its hydrogen
fuel cell drivetrain, and casually mentioned that real world tests
would begin in the next couple of years.

For those drivers, hydrogen cars could be the easy answer, as fueling
is pretty. In the UK, industry bodies estimate that some 40% of
households don’t have access to off-street parking to charge EVs.

For those drivers, hydrogen cars could be the easy answer as fueling
is pretty much the exact same process as for a gasoline car"

[Link](https://thenextweb.com/shift/2020/04/20/scientists-electric-vehicle-hydrogen-storage-breakthrough-metallic-sponges/)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Researchers, led by scientists from <a href="https://twitter.com/NorthwesternU?ref_src=twsrc%5Etfw">@NorthwesternU</a>, say they have developed a metallic sponge-like material that’s capable of storing greater quantities of <a href="https://twitter.com/hashtag/HydrogenNow?src=hash&amp;ref_src=twsrc%5Etfw">#HydrogenNow</a> at much lower — and safer — pressures when compared to conventional tanks <a href="https://t.co/rwTqABhzCG">https://t.co/rwTqABhzCG</a>.</p>&mdash; IEA Hydrogen (@IEA_Hydrogen) <a href="https://twitter.com/IEA_Hydrogen/status/1255182523249954816?ref_src=twsrc%5Etfw">April 28, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---


"@aaronstein1

Russia has offloaded the management of HTS to Ankara, a cost free
outcome of Sochi 2.0. Still in wait and see mode, but this is quite
the pickle Ankara now finds itself in"

---

"@Jkylebass

The Controversial Experiments and Wuhan Lab Suspected of Starting the
Coronavirus Pandemic - US Defense Intelligence Agency"

---

"@fuelcellsworks

Hyosung & Linde Group Sign Agreement to Build the World’s Biggest
Liquid Hydrogen Plant-Plant will have an annual capacity of 13,000
tons of liquid \#hydrogen, enough to fuel 100,000"

---

*The Expanse* last season sucked. They shouldn't have saved this show
 (almost got canceled, last year)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Wolfenstein 3D render loop in pure hardware! No CPU, no instruction pointer, no opcodes, only wires and flip-flops. Here runs on a Mojo V3 board (Xilinx Spartan 6) + SDRAM. Reading <a href="https://twitter.com/fabynou?ref_src=twsrc%5Etfw">@fabynou</a> black books while learning about <a href="https://twitter.com/hashtag/FPGA?src=hash&amp;ref_src=twsrc%5Etfw">#FPGA</a> could only lead to this ;-)<br>(1/n) <a href="https://t.co/k70Nz5t3Iz">pic.twitter.com/k70Nz5t3Iz</a></p>&mdash; Sylvain Lefebvre (@sylefeb) <a href="https://twitter.com/sylefeb/status/1254711510812602368?ref_src=twsrc%5Etfw">April 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">With batteries not powerful enough for at least 30 percent of bus routes our green hydrogen buses are the practical option for long ranges. Up to 3,000 of our zero-emission hydrogen buses could take to the road in the next few years <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> <a href="https://twitter.com/hashtag/wecantwait?src=hash&amp;ref_src=twsrc%5Etfw">#wecantwait</a> <a href="https://t.co/3XoP2zgRPm">https://t.co/3XoP2zgRPm</a></p>&mdash; RyseHydrogen #wecantwait (@RyseHydrogen) <a href="https://twitter.com/RyseHydrogen/status/1255031522517794817?ref_src=twsrc%5Etfw">April 28, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"@zacharylipton

A relative's acct got hacked on Facebook today. Just 2-3 messages
(trying to seem innocuous) left me 99.9% sure the account was
cracked. Googled the message =>corroborating it's a known scam =>damn
near 100% sure. Super simple reasoning yet strangely beyond what ML
does reliably"

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The Volvo Group and Daimler Truck AG form joint venture for large-scale production of fuel cells. <a href="https://t.co/zf9Rvkv90f">https://t.co/zf9Rvkv90f</a><a href="https://twitter.com/hashtag/fuelcell?src=hash&amp;ref_src=twsrc%5Etfw">#fuelcell</a> <a href="https://twitter.com/hashtag/trucks?src=hash&amp;ref_src=twsrc%5Etfw">#trucks</a> <a href="https://twitter.com/hashtag/trucking?src=hash&amp;ref_src=twsrc%5Etfw">#trucking</a></p>&mdash; Keith Malone (@ANativeAngeleno) <a href="https://twitter.com/ANativeAngeleno/status/1254810149543456778?ref_src=twsrc%5Etfw">April 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">To be clear: I haven&#39;t filed anything. I authorized a letter of interest that was sent on my behalf to the Greens and I&#39;m testing the waters for Green Party nomination. I&#39;m an independent. I&#39;m not a Democrat or a Republican because I know they&#39;re not the solution.</p>&mdash; Jesse Ventura (@GovJVentura) <a href="https://twitter.com/GovJVentura/status/1254783040594702338?ref_src=twsrc%5Etfw">April 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Interesting they thought there'd still be waiters in the future 

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">PHOTO OF THE DAY. A vision of the future from a German Magazine (1930). <a href="https://t.co/DpeOy6NQ6B">pic.twitter.com/DpeOy6NQ6B</a></p>&mdash; Professor Frank McDonough (@FXMC1957) <a href="https://twitter.com/FXMC1957/status/1254688521404678145?ref_src=twsrc%5Etfw">April 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Germany: Gas Pipeline Operator OGE Plans Huge Hydrogen Network--&quot;Up to now we have been able to add up to two percent <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a>. The next step would be to switch to 100 percent hydrogen directly on certain lines&quot;--<a href="https://t.co/zlXhZp7uRh">https://t.co/zlXhZp7uRh</a> <a href="https://twitter.com/hashtag/hydrogennow?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogennow</a> <a href="https://twitter.com/hashtag/decarbonise?src=hash&amp;ref_src=twsrc%5Etfw">#decarbonise</a> <a href="https://twitter.com/hashtag/zeroemissions?src=hash&amp;ref_src=twsrc%5Etfw">#zeroemissions</a> <a href="https://t.co/tn7HZwoDfl">pic.twitter.com/tn7HZwoDfl</a></p>&mdash; FuelCellsWorks (@fuelcellsworks) <a href="https://twitter.com/fuelcellsworks/status/1254759882399588356?ref_src=twsrc%5Etfw">April 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">German start-up <a href="https://twitter.com/hashtag/HoellerElectrolyser?src=hash&amp;ref_src=twsrc%5Etfw">#HoellerElectrolyser</a> has one clear goal: <a href="https://twitter.com/hashtag/greenhydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#greenhydrogen</a> for less than €4 per kilogram.<a href="https://twitter.com/hashtag/H2View?src=hash&amp;ref_src=twsrc%5Etfw">#H2View</a> <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a><a href="https://t.co/X3orFz2YaT">https://t.co/X3orFz2YaT</a></p>&mdash; H2 View (@h2_view) <a href="https://twitter.com/h2_view/status/1254725642920361984?ref_src=twsrc%5Etfw">April 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Isaac Ben-Israel is an Israeli going around saying the pandemic will end in 70 days. He has a &quot;paper&quot; in Hebrew (I read Hebrew). Below is one of the graphs on which he is basing his prediction.<br><br>HE FIT A SIXTH ORDER POLYNOMIAL TO THE DATA <br>😱😱😱😱😱😱<br> (c=2E21 😱) <a href="https://t.co/N7tKmoHBk0">pic.twitter.com/N7tKmoHBk0</a></p>&mdash; Lior Pachter (@lpachter) <a href="https://twitter.com/lpachter/status/1254692980004274176?ref_src=twsrc%5Etfw">April 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"@passtrans

Plans for a UK-built, 3,000-strong hydrogen bus fleet across the
country, have been revealed today by Wrightbus owner Jo Bamford"

---

"The death toll from coronavirus may be almost 60 per cent higher than
reported in official counts, according to an FT analysis of overall
fatalities during the pandemic in 14 countries.

Mortality statistics show 122,000 deaths in excess of normal levels
across these locations, considerably higher than the 77,000 official
Covid-19 deaths reported for the same places and time periods.

If the same level of under-reporting observed in these countries was
happening worldwide, the global Covid-19 death toll would rise from
the current official total of 201,000 to as high as 318,000"

[Link](https://amp.ft.com/content/6bd88b7d-3386-4543-b2e9-0d5c6fac846c)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The company before last spent all their time writing wrappers for AWS tools</p>&mdash; Present (@shoecatladder) <a href="https://twitter.com/shoecatladder/status/1254511807806369792?ref_src=twsrc%5Etfw">April 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Solving a debt &amp; leverage problem with more debt doesn&#39;t work <a href="https://t.co/IVi9K4CZUY">https://t.co/IVi9K4CZUY</a></p>&mdash; Keith McCullough (@KeithMcCullough) <a href="https://twitter.com/KeithMcCullough/status/1254525742119096326?ref_src=twsrc%5Etfw">April 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"Now, with colleges shuttered, revenues reduced, endowment investments
plunging, and the added struggle of shifting from physical to virtual
education, Moody’s has downgraded the entire sector to negative from
stable. The American Council on Education believes revenues in higher
education will decline by $23bn over the next academic year"

[Link](https://amp.ft.com/content/e5d50e86-861a-11ea-b872-8db45d5f6714)

---

I bet momentum trading strategies did well for so long bcz chasing the
FED paid off handsomely. That's what these things do, go after the
herd, and FED created the perfect trend to follow.

---

<blockquote class="twitter-tweet" data-conversation="none"><p lang="en" dir="ltr">i haven’t spent my $1200 yet</p>&mdash; beth (@bethbourdon) <a href="https://twitter.com/bethbourdon/status/1254280299313315840?ref_src=twsrc%5Etfw">April 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"@TheBubbleBubble

Believe it or not, the U.S. student loan bubble temporarily lowered
the unemployment rate: many people who couldn't find jobs after the
Great Recession simply took on a ton of student loans and went back to
school. Voilà - they no longer counted as unemployed! It's magic!"

---

The NBER [paper](http://www.nber.org/papers/w21967.pdf)

---

"An NBER paper issued last year concluded that changes to federal
student loans are more than sufficient to explain tuition increases at
private nonprofit colleges...

Unlike most other student loan programs, PLUS loans are not
capped—parents may borrow up to the cost of attendance, which is
determined by the college. This creates incentives for colleges to
increase student charges, since the federal government will make sure
all eligible parents have access to the money"

[Link](https://www.forbes.com/sites/prestoncooper2/2017/02/22/how-unlimited-student-loans-drive-up-tuition/#1166275352b6)

---

Of course, David Hewlett. He called ZPM Zed-PM! 

Go ZED! Good job.

---

Which actor is from Canada with some accent so I can half-jokingly
mock the accent and congratulate?

---

Canada! 

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Canadians are receiving $2000/month and their GDP per capita is about 2/3 of ours. So when you&#39;re struggling to pay rent remember - it&#39;s not that they couldn&#39;t help us more, it&#39;s that they chose not to.</p>&mdash; Albert Lee For Congress 🌹 (@AlbertLee2020) <a href="https://twitter.com/AlbertLee2020/status/1254208161591857158?ref_src=twsrc%5Etfw">April 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"@adam_tooze

If Germany borrows money on capital markets, including from wealthy
Italians, and then channels that money to Italy by way of the EU
budget what does it amount to? A eurobond but one controlled by
Germany! Great from @KeineWunder"

---

"[T]here is another viewpoint [different from electric grids] from
which these possible new electric-power-demand-boosting developments
do not look such good news. It’s based on a rival assessment of what
makes sense in terms of meeting energy needs — the use of gas as an
energy vector. This option is claimed to be more efficient and less
costly than electricity for heating, and possibly for other purposes.

It is certainly easier to transmit gas with lower energy losses. And
it can be stored, unlike electricity"

[Link](https://physicsworld.com/a/rethinking-power-pipes-versus-wires/)

---

Yes some countries in fact do not allow free camping. This needs to
change.

"[Autotranslated] According to the World Bank, over 77 percent of
people in Germany live in cities. And these cities don't offer enough
space for everyone. If the Germans who love to travel stay in the
country this summer, .. there will be even less free terrain left
here, the double arm length will be a distant dream. Nature waits in
front of the city: forest and agriculture make up over 80 percent of
land use in Germany.

The townspeople just have to go outside. Not to the eternally the same
and soon overcrowded destinations such as Bastei Bridge, Drachenfels
or the Travemünder Ostseestrand, but in the nameless and contagious
forest, in the Weserbergland, the Elfringhauser Switzerland or the
Fläming.

It is therefore necessary to allow wild camping in the country. The
Scandinavian right of public could serve as a model: The allemansrätt
, as it is called in Sweden, not only allows free access to nature -
this is also known as the "right of access" in Germany. It also allows
camping in the wild and only imposes restrictions, such as a minimum
distance from the sleeping area to houses"

[Link](https://www.zeit.de/kultur/2020-04/zelten-coronavirus-krise-tourismus-umweltschutz-jedermannsrecht)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Can we all agree on how invasive getting someone&#39;s phone number is?<br><br>Shit&#39;s fucking oppressive.</p>&mdash; crummy (@crummysaint) <a href="https://twitter.com/crummysaint/status/1254266542033960961?ref_src=twsrc%5Etfw">April 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

<center>
<img width="140" src="https://pbs.twimg.com/media/ETZJzIkXgAAEi9Q?format=jpg&name=small"/>
</center>

