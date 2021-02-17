# Tweets

<iframe width="340" src="https://www.youtube.com/embed/kir0DI9AnOc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Wind turbine freezing was not the main factor then.. I saw some cons
jumped the shark.

"@GregAbbott_TX

The Texas power grid has not been compromised.

The ability of some companies that generate the power has been frozen. 

This includes the natural gas & coal generators.

They are working to get generation back on line"

---

Dude. Lumber futures..

[Link](https://mobile.twitter.com/crampell/status/1361699251827470338)

---

Business Insider: "This hydrogen paste has a similar range to that of
gasoline and could revolutionize the transport industry"

[Link](https://www.businessinsider.com/car-bike-tesla-amazon-gates-bezos-climate-change-fuel-drone-2021-2)

---

"@byHeatherLong

26 states had revenue declines last year The toll was felt by both Dem
& Repub-led states Gov't jobs cuts have occurred in nearly every state

26% NH

17% Colorado

14% Ohio

13% Wisconsin

12% Michigan

12% Maine

12% Kentucky"

---

"Say Hy to the home of the future"

[Link](https://cadentgas.com/future-of-gas/projects/hydrogen-home)

---

Name any city and that'll be plotted too. I can do this all day.. let's go.

---

[Data](https://www.ncdc.noaa.gov/cag/city/time-series)

```python
import pandas as pd

df = pd.read_csv('austin-feb.csv')
df.Date = pd.to_datetime(df.Date,format="%Y%m")
df = df.set_index('Date')
df.Value.plot()
df['Trend'] = df.Value.rolling(window=30).mean()
df['Trend'] = df['Trend'].fillna(method='backfill')
df.Trend.plot()
plt.savefig('atw_01.png')
```

![](atw_01.png)

---

Nice try genius. See above. I plotted February averages for Austin, TX
per year, since 1940. The trend is up.

"Aw man the weather is cold in TX, that means no glob warming"

---

Tax havens: ... Ankara must share its banking data with the Member
States of the European Union by the end of June, otherwise it will be
placed on a “black list”.

[Link](https://twitter.com/lemondefr/status/1361627449050738699)

---

"@StateDeptSpox

The Houthis’ assault on Marib shows they are not committed to peace or
to ending a war afflicting the people of Yemen"

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


