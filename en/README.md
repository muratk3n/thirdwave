# Tweets

\#2021PortugalEU

"@H2Europe

H2Europe presented its #H2Act, representing a strategic collaborative
effort, giving an excellent contribution to the vision & development
of a future #hydrogeneconomy. We need collective focus and drive to
accelerate the implementation of #H2 market!"
 
---

K.. as long as there is FCEV refueling next to these BEV chargers,
it's fine. BEVtards will get crushed in due course.

"US Senate Committee Introduces Clean Vehicle Charging
Legislation.. Earlier this week, a group of cross-party US senators
introduced the Securing America’s Clean Fuels Infrastructure Act (the
Act) to promote investments in clean vehicle infrastructure. The types
of infrastructure supported by the legislation include electric
vehicle charging stations and hydrogen refueling stations for fuel
cell vehicles"

[Link](https://www.natlawreview.com/article/us-senate-committee-introduces-clean-vehicle-charging-legislation)

---

Util code to report attacks on a specific country on a specific
month. Israel attacks Syria regularly it seems, w some hard kills
too.. Dam

```python
import pandas as pd

def country_attacked(mon, country):
   url = 'https://ucdp.uu.se/downloads/candidateged/GEDEvent_v21_0_%d.csv' % mon
   df = pd.read_csv(url)
   df1 = df[(df['side_b'] == 'Government of %s' % country)]
   g = df1[['side_a','deaths_b','side_b']].\
       groupby(['side_a','side_b']).\
       agg({'side_b':'count', 'deaths_b': 'sum'})
   g.columns = ['incidents','deaths']
   return g

print (country_attacked(1, 'Syria'))
print (country_attacked(2, 'Syria'))
```

```text
                                          incidents  deaths
side_a               side_b                                
Government of Israel Government of Syria          2      57
                                          incidents  deaths
side_a               side_b                                
Government of Israel Government of Syria          2       9
```
---

"@josheidelson

New: After years of mostly unsuccessful efforts, Uber, Lyft and peers
are poised to secure deals with major unions, just in time to help
defuse threats from the new Biden Administration"

---

"@SecYellen

By choosing to compete on taxes, we’ve neglected to compete on the
skill of our workers and the strength of our infrastructure. It’s a
self-defeating competition, and neither President Biden nor I are
interested in participating in it anymore.

We want to change the game"

---

Context? There was huge contraction due to pand so it shld not be
surprising to expect growth, just going back to where econ was
previously wld give major "growth".

"Record growth is expected this year, all around the world, w rates
not seen since 60s"

---

"@hazergroupltd

A new report has detailed exactly how Australia’s current gas
regulations can be modernised to facilitate the future use of
hydrogen, biomethane and other potential future fuels"

[Link](http://ow.ly/uAHO50EhgEg)

---

Good docu on Soviets, Russia

[Moscow's empire - rise and fall (2/4)](https://youtu.be/fSqMpZ5qhz0)

[Moscow's empire - rise and fall (3/4)](https://youtu.be/DCgDChqQZwk)

[Moscow's empire - rise and fall (4/4)](https://youtu.be/DCgDChqQZwk)

---

\#2021PortugalEU

"@H2Europe

\#GreenHydrogen is in our view one of the most promising techs to
eliminate hard to abate emissions from industrial & transport
sectors. - R. Mourinho Felix, VP, [European Inv Bank]"

---

2018 trade balance with CH top trading [partners](https://en.wikipedia.org/wiki/List_of_the_largest_trading_partners_of_China),
Neg for deficit, pos for surplus; so simple sum shld give the net received,
in billions,

```python
defc = [419.6,275.8,177.1,-28.6,206.1,-74.8,-112,-53.6,21.3,-12.7,\
       -29.9,52,1.5,-3.1,10.8,6.2,10.9,12.8,-13.4,16.4,-9.5]
np.sum(defc)
```

```text
Out[1]: 872.9
```

Not bad.. It can change obviously, export-dependency is just another
dependency. CH is a basket case and has lotsa mouths to feed.

---

"@gideonrachman

Soros-backed Central Europe University (CEU) is forced out of
Budapest. In its place comes Fudan University from China

'@eublogo \#Hungary will make 1 of the largest investments in the
higher education in decades financed by #China'"

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


