# Tweets

Pinned Tweets

<img width="340" src="https://pbs.twimg.com/media/EvcqV3BWgAEvXtS?format=png&name=small"/>

---

<iframe width="340" src="https://www.youtube.com/embed/YNKehLXpLRI?start=214" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

"The U.S. Department of Energy (DOE) is funding a demonstration of the
design, build and operation of the country's first dedicated renewable
hydrogen network, starting in Texas"

[Link](https://www.forbes.com/sites/mitsubishiheavyindustries/2021/02/25/how-the-lone-star-state-is-building-a-green-hydrogen-future/amp/?sh=38354eae7e8a)

---

Newer is usually better.. I'd much rather watch *The Island* than *Logans Run*

---

Printing can cause crash in certain cases, if ur President is a bus
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
different names for the same thing. Im sure excellent stories behind
each, if I had the time to dive into.

---

The "Planet Chauvinism" comment by Isaac Asimov 

<iframe width="340" src="https://www.youtube.com/embed/GQ98hGUe6FM?start=1078&end=1118" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Just look at FED [GPDNow](https://www.frbatlanta.org/cqer/research/gdpnow) estimate..
As of 3/1 the estimate is 10%.

I am sure they use many base indicators to calculate this.. there are
some known ones, eg [ISM PMI](2019/05/stats.md#gdpism) That's how I knew
a month ago growth was coming.

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

Industrial Age society, the Second Wave began in Western Europe with
the Industrial Revolution, and subsequently spread across the
world. Key aspects of Second Wave society are the nuclear family, a
factory-type education system and the corporation. The Third Wave is
the post-industrial society based on hi-tech with all its benefits and
adverse effects causing major attitude shifts in society. Institutions
are built around methods of production, so when a new wave arrives,
older structures around governance, education, health start to crumble
despite the best efforts of people working in them.

## For Members

[Link](https://thirdwave-members.herokuapp.com)

## Reference

[Nations and Nationalism, Culture, Narratives](/2013/02/nations-and-nationalism.md)

[The Fundamentals of Industrial Ideologies](/2011/04/fundamentals-of-industrial-ideologies.md)

[Education, Workplace](2017/09/education-workplace.md)

[Patents](/2018/09/patents.md)

[Democracy, Parties](/2016/11/democracy.md)

[Economy](/2018/05/economy.md)

[Globalization](/2018/09/globalization.md)

[Rome, The First Wave, Religion](/2017/12/rome.md)

[Human Nature & Health](/2020/07/human-nature.md)

[Climate Change](/2018/12/climate.md)

[The Middle East](/2019/07/middleeast.md)

[TR](../tr)

## Browse

[By Year](years.md)

[Search](search.html)

[Tweet Archive](/tweets/README.md)


