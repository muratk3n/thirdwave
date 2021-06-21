# Week 25

A change... not nothing. Good leadership from folks at @BtSIsrael

"@NewIsraelFund

Thanks to work by @YeshDin @PHRIsrael and @BtSIsrael , the IDF
practice of home invasions for 'intelligence gathering' is over"

---

"U.S. Military Steps Up Its Withdrawal From Middle East.. The Pentagon
is pulling antimissile batteries, aircraft and hundreds of troops from
the Mideast as it focuses the armed services on challenges from China
and Russia, administration officials said"

---

There are bleeping *ditches* dug in Novhorodske, Ukraine, like WWII
style, saw it on Oz ABC

---

Navy map update now catches carrier USS R Reagan near Malaysia. System working.

---

Hah. So US made a foray into SCS, RU in the Pacific. 

"Ahead of Biden-Putin summit, Russia conducts what it calls its
largest naval exercise in the Pacific since Cold War"

---

`pandas.to_datetime` works like magic

---

Conflict stats [update](2019/05/confstats.md#gdelt)

---

Infl expectation for next year is at 4.0, down from 4.6. Can be
important, expecting higher prices ppl can start ask higher wages, or
raise prices in stores, etc.

But I still dont see a runaway process here.

---

Let's [take a look](2019/05/stats.md#infexp)

"How about consumer's inflation expectation?"

---

"@USISPForum

We are delighted to announce the launch of the #USIndia Hydrogen
Taskforce with @ENERGY @mnreindia under the US-India Strategic Clean
Energy Partnership. The hydrogen task force will help scale up
technologies to produce hydrogen from renewable energy & fossil fuel
sources"

---

"The Palestinian Authority said Friday it cancelled a swap deal that
would have seen Israel provide it with one million Covid-19 jabs, as
the doses were 'about to expire'"

[Link](http://u.afp.com/UBRR)

---

"Australia is lodging a formal complaint with the World Trade
Organization over China's imposition of anti-dumping duties on
Australian wine exports, the government announces"

[Link](http://u.afp.com/UBRH)

---

Japan started the Meiji transformation around the same time as TR's
*Tanzimat* reforms. Italy has a similar repulsive agro empire
past. Yet both are way ahead. Why?

---

Italy has 9 times the capability of Asia Minor, Japan is at 27. Obscene high
numbers.

```python
import pandas as pd
df = pd.read_csv('../../2020/07/gdpw.csv')
df = df[df['country'].isin(['Turkey','Italy','Japan']) ]
df['gdp'] = df.gdpcap * df.population
df['mbindex'] = (df.gdpcap * df.gdp)/1e14

tr = float(df[df.country=='Turkey'].mbindex)
df['trbeaten'] = (df['mbindex'] / tr).astype(int)
print (df[['country','trbeaten']])
```

```text
   country  trbeaten
33   Japan        27
35   Italy         9
87  Turkey         1
```

---



