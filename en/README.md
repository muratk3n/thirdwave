# Tweets

Pinned Tweets

<img width="96%" src="https://pbs.twimg.com/media/EvdKNhvXAAE9Rr2?format=png&name=small"/>

---

A certain generation of socsci researchers are just way into f-ing
Stata. And I am into reverse-engineering their .. wonderful code
.. and porting it into 🐍

---

Yoshinori Sunahara - Summer \#music

[Link](https://youtu.be/GrPQ_fzvW7Q)

---

Thucydides's Trap? Bih who dat Thucydides? Speaka English.

---

They are at 1/10th (which they got to with Western help), does it make
sense that ratio go up to 1/2th? It'd seem not. The obscene help so
far creates weird dynamics, even movies beome bizarre. 

---

China looks like a paper tiger. But countries -and themselves- seeing
CH otherwise can create problems. Spreading authoritarinism is not
a-ok.

---

Another ex of CINC problems [applied](2021/03/power-of-nations-beckley.md#ukch) to UK/CH.

---

Beckley says his method has 8 percentage points more success in
predicting results of conflicts, wars (who the winner will be) than CINC.

Let's use his method on a few countries,

```python
import pandas as pd
df = pd.read_csv('../../2020/07/gdpw.csv')
df['gdp'] = df.gdpcap * df.population
df['new index'] = (df.gdpcap * df.gdp)/1e14
df1 = df[df['country'].isin(['Turkey','Greece','United States','China']) ]
print (df1[['country','new index']])
```

```text
          country     new index
13  United States  12898.099255
51         Greece     43.463713
85          China   1363.010190
87         Turkey     68.576017
```

This is so sad... US has 10 times more pow than the next guy. My
tegros are drowning down there in the list, next to, like, Greece.

---

Hah. By CINC China is at the top. You know that shit aint true.

---

Instead MB's method is GDP x GDP Per Capita. This punishes population
size (GDP Per Capita is GDP divided by population), bcz the more
people you have the more you are spending as well (especially for
nondemocracies they spend on internal security). On the upside GDP Per
Capita rewards innovation, it's a sign of efficiency, being able to
produce more with less means there is innovation in the economy. The
gross obviously has to enter the picture, at some level, that's why it
gets multiplied.

---

MB doesnt like the widely used military capability index CINC either.
The famous Correlates of War project uses it, but I can see his point;
like the GDP, it's a gross measure, does not account for costs..

CINC is a combined measure of iron and steel production, energy
consumption, military expenditure, personel, etc.

---

M. Beckley: "Despite the widespread use of GDP, however, few people
know what it actually measures or recognize that it does not deduct
costs.  To begin, GDP counts production costs (inputs and
externalities) as output.  Spending money always increases GDP, even
if the funds are wasted on boondoggles; in fact, the most common
method of calculating GDP is called the 'expenditure method' and
involves simply adding up all of the spending done by the government,
consumers, and businesses in a country in a given time period. Thus,
hiring workers always increases GDP, even if they spend all day
getting drunk in the break room. Boosting production always increases
GDP, even if the goods rot on the shelf and tons of toxic waste are
released in the process. In fact, a country can increase its GDP by
dumping toxic waste into the streets and then spending billions of
dollars to clean it up...

Consequently, populous countries generate considerable economic
activity simply by existing. Even a nation caught in a Malthusian
hell, in which all output is immediately devoured, will post a large
GDP if it has a big population.  Finally, GDP counts security spending
as economic output. GDP does not distinguish between guns and
butter. It counts a 100 million dollar gulag the same as a $100 million
innovation center. Hence, GDP fails to account fully for the economic
costs of domestic instability and international conflict. In fact, GDP
usually rises when a country mobilizes for war... In general, however,
resources devoted to policing and protection drain wealth rather than
create it"

[Link](2021/03/power-of-nations-beckley.md)

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


