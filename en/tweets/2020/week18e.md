# Tweets - Week 18e

"@RoryVanLoo

'The New Gatekeepers' is up. It shows how the government increasingly
requires giants like Facebook, Citibank, Exxon, & Gilead to regulate
smaller businesses"

[Link](https://mobile.twitter.com/RoryVanLoo/status/1255853230409625601)

*2020-5-1 19:16:51*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hydrogen Industry: The Dawning Of The <a href="https://twitter.com/hashtag/Hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#Hydrogen</a> <a href="https://twitter.com/hashtag/Economy?src=hash&amp;ref_src=twsrc%5Etfw">#Economy</a> <a href="https://t.co/WD8L1rYcWX">https://t.co/WD8L1rYcWX</a></p>&mdash; BayoTech On-Site Hydrogen Generation (@H2Bayo) <a href="https://twitter.com/H2Bayo/status/1256192516094939136?ref_src=twsrc%5Etfw">May 1, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-5-1 19:15:55*

---

The three UFO videos

[Link](https://youtu.be/Q7jcBGLIpus)

*2020-5-1 17:9:39*

---

So this thing basically runs on its own - making energy out of thin
air.. How is this not a replacement for the current way we generate
energy?

"A solar-powered hydrogen station has been built in the Japanese town
of Namie, which can power 560 fuel-cell cars a day"

*2020-5-1 16:33:1*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">St Petersburg University Students Develop a <a href="https://twitter.com/hashtag/Hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#Hydrogen</a> Fuel Cell to Replace Lithium-Ion Batteries--This new <a href="https://twitter.com/hashtag/fuelcell?src=hash&amp;ref_src=twsrc%5Etfw">#fuelcell</a> is expected to be 30% cheaper“ and uses an innovative nanostructured nickel mesh as a catalyst--<a href="https://t.co/6MuEsy2x4i">https://t.co/6MuEsy2x4i</a> <a href="https://twitter.com/hashtag/hydrogennow?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogennow</a> <a href="https://twitter.com/hashtag/fuelcells?src=hash&amp;ref_src=twsrc%5Etfw">#fuelcells</a> <a href="https://twitter.com/hashtag/zeroemissions?src=hash&amp;ref_src=twsrc%5Etfw">#zeroemissions</a> <a href="https://twitter.com/hashtag/h2?src=hash&amp;ref_src=twsrc%5Etfw">#h2</a> <a href="https://t.co/wLqFBBDRC9">pic.twitter.com/wLqFBBDRC9</a></p>&mdash; FuelCellsWorks (@fuelcellsworks) <a href="https://twitter.com/fuelcellsworks/status/1256199864578453511?ref_src=twsrc%5Etfw">May 1, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Looks fun

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">GOOD NEWS guys, not ALL the <a href="https://twitter.com/hashtag/sports?src=hash&amp;ref_src=twsrc%5Etfw">#sports</a> are canceled!<br>But: is this a game, a manly duel, or a bad romance? <a href="https://twitter.com/hashtag/bunnyhop?src=hash&amp;ref_src=twsrc%5Etfw">#bunnyhop</a> <a href="https://t.co/t4KRhi5osc">pic.twitter.com/t4KRhi5osc</a></p>&mdash; Elizabeth Withey (@lizwithey) <a href="https://twitter.com/lizwithey/status/1255726551154360320?ref_src=twsrc%5Etfw">April 30, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-5-1 11:9:22*

---

Italians killed Jesus, not the Jews. The other narrative is the
biggest propaganda shtick even constructed in history, to push
teachings of Jesus under centralized state control. Goebbels would
have been impressed - but then again, their Heil Hitler salute was
taken from Romans.

"I don't like Jews because they killed Jesus"

*2020-5-1 11:42:3*

--

You got that [backwards](https://muratk3n.github.io/thirdwave/en/2020/05/roman-anatolia.html)

"Paraphrasing: the arriving ppl from Central As changed Anatolia"

*2020-5-1 11:34:2*

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

*2020-5-1 10:5:7*

---

<blockquote class="twitter-tweet"><p lang="de" dir="ltr"><a href="https://twitter.com/search?q=%24DGB&amp;src=ctag&amp;ref_src=twsrc%5Etfw">$DGB</a> vs <a href="https://twitter.com/search?q=%24NANO&amp;src=ctag&amp;ref_src=twsrc%5Etfw">$NANO</a> <a href="https://t.co/fJcMc6XYHJ">https://t.co/fJcMc6XYHJ</a> <a href="https://t.co/mgCNDUwE7L">pic.twitter.com/mgCNDUwE7L</a></p>&mdash; IdealFog (@IdealFog) <a href="https://twitter.com/IdealFog/status/1254815512715919365?ref_src=twsrc%5Etfw">April 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-5-1 10:2:27*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">21 USC §§331, 333, 343(g) &amp; 21 CFR §133.154 make it a federal crime to sell high-moisture jack cheese if it isn&#39;t moist enough, but not too moist.</p>&mdash; A Crime a Day (@CrimeADay) <a href="https://twitter.com/CrimeADay/status/1256061343167176705?ref_src=twsrc%5Etfw">May 1, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-5-1 7:39:30*

---

World oil [production](https://www.eia.gov/outlooks/steo/xls/Fig6.xlsx), from [IEA](https://www.eia.gov/outlooks/steo/data.php) 

I guess data for production before April are real, but the rest is
projection. It'd be great to supply data as one CSV, and a CSV per
concept, like `world-production.csv`. 

```python
# Unit million bbls per day
import pandas as pd
df = pd.read_excel('/tmp/Fix6.xlsx')
arr = np.array(df)[25:50,3:5]
#arr = arr[25:50,3:5]
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

*2020-5-1 7:25:3*

---

Emacs! 👍

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Typing.<br>Emacs.<br>Measure theory/Lebesgue integration. <a href="https://t.co/2wPIH8QJLI">https://t.co/2wPIH8QJLI</a></p>&mdash; Dirk L. (@Dirque_L) <a href="https://twitter.com/Dirque_L/status/1256257898050658304?ref_src=twsrc%5Etfw">May 1, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-5-1 7:24:1*

