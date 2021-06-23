# Week 25


"@josheidelson

Speaking of 'cancelation,' U.S. workers can legally be fired for
almost any reason, or no reason. A groundbreaking NYC law changes that
for 70,000 in fast food"

---

UCDP/PRIO May file [is out](2019/05/confstats.md). Afganistan, Yemen,
Nigeria deaths increased. 

---

I looked in this general region bcz the Navy deploy map said that carrier
was in the Atlantic coast.

---

I bet it was here.

Gotcha

<img width="340" src="https://pbs.twimg.com/media/E4ahdzaXwAMJ1x7?format=jpg&name=small"/>

---

Output at the bottom

[Earthquake Stats](2019/05/earthquakes.md)

---

Ok.. ok.. you'll get an earthquake map

---

F24: "The United States Geological Survey recorded the explosion as a
3.9 magnitude earthquake on Friday."

---

18 tons of TNT equivalent. No joke. 1 kg can destroy a car. 

BBC: "US Navy uses 40,000lb explosive to test warship .. against its
aircraft carrier, the USS Gerald R. Ford"

---

Number 1 motor vehicle parts supplier in the world.

"Fuel-cell stack: mass production starting 2022: Bosch"

---

Number 2 motor vehicle parts supplier in the world.

"Hydrogen fuel cells to compete with diesel truck engines by 2030: Cummins"

---

CNBC: "Jaguar Land Rover is developing a hydrogen-powered vehicle and
plans to test it out this year"

---

I see .. The overall quality of teachers, especially in US, [is low](2021/03/unrivaled-beckley.md#ed).
Therefore they come across as unskilled workers, "wage earners" which
makes progs want to protect them.

But this is a bad decision point to be stuck with. Do we care for the
switchboard operators, want them to be "happy", "well-paid"?. No.
This particular job is gone, outdated.

---

Yes it is an either-or; either give kids prerecorded lectures, or teachers

---

I see some progs support teachers but not poor kids. Why is dat

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/Hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#Hydrogen</a> was recently featured in a speech by Trinidad &amp; Tobago&#39;s Prime Minister, Keith Rowley. With the Caribbean joint island nation said to be exploring feasibility and regulatory aspects of a hydrogen economy.<br><br>Read more here: <a href="https://t.co/7RZUIg4wZq">https://t.co/7RZUIg4wZq</a><a href="https://twitter.com/hashtag/hazergroupltd?src=hash&amp;ref_src=twsrc%5Etfw">#hazergroupltd</a> <a href="https://t.co/MuDaYRzDJI">pic.twitter.com/MuDaYRzDJI</a></p>&mdash; Hazer Group Ltd (@hazergroupltd) <a href="https://twitter.com/hazergroupltd/status/1406748843195179009?ref_src=twsrc%5Etfw">June 20, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

There!

"Artificial Photosynthesis Promises A Clean, Sustainable Source Of
Energy--Biophysicist is building own artificial leaf analog that
collects light and splits water molecules to generate hydrogen"

[Link](https://bit.ly/3wKIljY)

---

Brain uploading to machines.. these are Silicon Valley shitlib pipe
dreams..

---

My movie recommender came up with *Irrational Man*.. Was ok.. I liked
the backdrop.. Joachim digs these weirdo psychodramas eh?

---

A company..?

USA Today: "This company's permissive policies are behind high-profile
police shootings of Black men in the US... The Texas-based company,
Lexipol LLC, markets its policies as a way to protect local
governments from frivolous lawsuits. That message has attracted
clients all over the country, making Lexipol an influential player in
the world of law enforcement"

[Link](https://www.msn.com/en-us/news/us/this-company-has-provided-permissive-policies-behind-high-profile-police-shootings-of-black-men-in-the-us/ar-AAL5JmQ)

---

Like I said data file isnt completely accurate, but there can be some
interesting, even tangential hits sometimes. See above

---

More GDELT parsing.. new script goes back a month, scans for the
shooting of black people by the police..

[Output](2019/05/blm-out.html), [Script](2019/05/blm.py)

---

"@HYPOS_GreenH2 Germany Planning a Cross-Country Hydrogen Network"

---

"Chile Minister Jobet Welcomes Mega Agreement to Produce Hydrogen and
Green Ammonia in Magallanes.. 'Through #greenhydrogen we will begin to
clean up our agriculture and maritime transport'"

---

"@Lecocq_dom

Situated in the city of Kawasaki the [Tokyu Hotels] is 30% powered by
H2 derived from waste plastics"

---

Some Venezuella level shit is always possible of course but doesnt
seem to be the case for US. So its not accurate to say '*there we go
again*, printing begins and currency debased, inflation goes up, as
before!'.

---

<img width="340" src="https://pbs.twimg.com/media/E4WaZFuXIAE5YLO?format=png&name=small"/>

---

It appears there is little correlation btw gov spending (deficit) and
inflation for US.


```python
import matplotlib.pyplot as plt
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1970, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
# FYFSGDA188S surplus (+) or deficit (-) as percent of GDP
df = data.DataReader(['CPIAUCNS','FYFSGDA188S'], 'fred', start, end)
df['infyoy'] = (df.CPIAUCNS - df.CPIAUCNS.shift(12)) / df.CPIAUCNS.shift(12) * 100.0
df['FYFSGDA188S'] = df['FYFSGDA188S'].fillna(method='ffill').rolling(window=10).mean()
df1 = df[['FYFSGDA188S','infyoy']]
print (df1.corr())
df1.columns = ['Gov Surp or Def','Inflation']
df1.plot()
```

```text
             FYFSGDA188S    infyoy
FYFSGDA188S     1.000000  0.231844
infyoy          0.231844  1.000000
```

---

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

Conflict stats [update](../../2019/05/confstats.md#gdelt)

---

Infl expectation for next year is at 4.0, down from 4.6. Can be
important, expecting higher prices ppl can start ask higher wages, or
raise prices in stores, etc.

But I still dont see a runaway process here.

---

Let's [take a look](../../2019/05/stats.md#infexp)

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



