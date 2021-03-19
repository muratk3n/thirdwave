# Tweets

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">NEW: I saved this one up for the US morning, because it’s a big &quot;good Covid news&quot; moment for our friends across the Atlantic<br><br>A &quot;vaccine effect&quot; is now clear in US data, with hospitalisations falling faster among the old (mostly vaccinated) than the young <a href="https://t.co/3qZYpUGClA">https://t.co/3qZYpUGClA</a> <a href="https://t.co/JOfIMbR85t">pic.twitter.com/JOfIMbR85t</a></p>&mdash; John Burn-Murdoch (@jburnmurdoch) <a href="https://twitter.com/jburnmurdoch/status/1372540703188860940?ref_src=twsrc%5Etfw">March 18, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

CNBC: "Hydrogen is currently the only solution to decarbonize some
industries, RWE exec says"

[Link](https://www.cnbc.com/amp/2021/03/16/hydrogen-only-current-solution-to-decarbonize-some-industries-exec-says.html)

---

[What of it?](2021/03/unrivaled-beckley.md#chru)

"But what of the China-Russia alliance?"

---

There r some weird storage methods .. eg "pumped hydro". They just
lift up bunch of water, thats it. Water's "potential energy" is
stored, to take back energy, just allow it to go down.  Not bad, but
just like the Li-on batteries, it is a circus monkey. Too specialized,
doing only one thing.

---

"@FORESIGHTdk

While there are electronic, mechanical, kinetic, and other creative
methods to store power, chemical #storage has the greatest propensity
for widespread use, says @ReshefRami, CEO at Israeli fuel cell
manufacturer @gencellenergy"

---

Light Through The Veins (Tom Middleton Remix) \#music

[Link](https://youtu.be/eo99GxHgseY?t=202)

---

Anti-lessons from TR; keep national narrative / identity as simple as
possible, dont overload it with [political preferences](2020/04/turks-culture-national-narrative.md#add1).
Imbuing political choices on identity can turn it into a fascist
propaganda tool.

---

Some components of GII.. 

```python
df.columns
```

```text
Out[1]: 
Index(['index', 'Country', 'GII', ' Innovation Efficiency Ratio',
       ' Innovation Input Sub-index', ' Innovation Output Sub-index',
       'Institutions(ranking)', 'Human capital and research(ranking)',
       'Infrastructure(ranking)', 'Market sophistication(ranking)',
       'Business sophistication(ranking)',
       'Knowledge and technology outputs(ranking)', 'Creative outputs',
       'Institutions(value)', 'Human capital and research(value)',
       'Infrastructure(value)', 'Market sophistication(value)',
       'Business sophistication(value)',
       'Knowledge and technology outputs(value)', 'Creative outputs(value)'],
      dtype='object')
```

---

Just found out about [Global Innovation Index](https://www.wipo.int/global_innovation_index/en/2020/). 

Someone shared its data on [GH](https://github.com/avinzons/GIIDataViz/), local
version [here](tweets/2021/GII-2021.csv).

```python
import pandas as pd

df = pd.read_csv('GII-2021.csv')
df = df.rename(columns={' Global Innovation Index':'GII', 'Unnamed: 0': 'Country'})
df = df.sort_values('GII',ascending=False)
df = df.reset_index()
df = df[df.Country.isin(['United States', 'Korea, Republic of', 'Netherlands', 'Turkey'])]
print (df[['Country']])
```

```text
               Country
2          Netherlands
3        United States
10  Korea, Republic of
42              Turkey
```

TR is just f-ing drownin.. NL, not bad. 

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


