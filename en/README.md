# Tweets

France 24: "Glimpse of a post-Covid future? Masks ditched as Gibraltar
nears total vaccination... Signs reminding people to wear a face mask
in public were taken down by workmen in Gibraltar on Sunday in the
latest indication that life is slowly returning to something close to
normal in the small British overseas territory. Gibraltar is one of
the first places in the world to have vaccinated virtually its entire
adult population against Covid-19 and may now offer a clue as to how
other nations will fare when their own populations are inoculated"

---

Peter Beck of Rocketlab on Venus. RocketLab has delivered successful
payloads to space, solid outfit. 

[Link](https://youtu.be/SjuxmH7eWHc?t=1581)

---

Venezuella and TR near the top.. 

<img width="340" src="https://pbs.twimg.com/media/ExobutwXIAEznKF?format=png&name=small"/>

---

WSJ: "WHO Report Into Covid-19 Origins Leaves Key Questions
Unanswered... A World Health Organization-led team investigating the
origins of the Covid-19 pandemic found that data examined during a
recent mission to China was insufficient to answer critical questions
as to when, where and how the virus began spreading"

---

"Stanford Scientists Reverse Engineer Moderna Vaccine, Post Code on Github"

[Link](https://www.vice.com/amp/en/article/7k9gya/stanford-scientists-reverse-engineer-moderna-vaccine-post-code-on-github)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">📢The UK is planning to have its first hydrogen town by 2030! The fuel cell sector is looking forward.<br>✅No CO2 emissions<br>✅High efficiencies<br>✅Empowered local communities<br>➡️<a href="https://t.co/ifIsrdNk54">https://t.co/ifIsrdNk54</a> <a href="https://t.co/KMD7X9bTn1">pic.twitter.com/KMD7X9bTn1</a></p>&mdash; PACE (@PACEmCHP) <a href="https://twitter.com/PACEmCHP/status/1376496265337450496?ref_src=twsrc%5Etfw">March 29, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I don&#39;t know what people expect here. There is no co-ordinated state or global effort that has any control over these vaccines, and no serious non marketized alternative. This is HOW the market delivers--by stripping state assets. <a href="https://t.co/Va7lEpeXAC">https://t.co/Va7lEpeXAC</a></p>&mdash; Stephen Buranyi (@stephenburanyi) <a href="https://twitter.com/stephenburanyi/status/1364179702831792134?ref_src=twsrc%5Etfw">February 23, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

My approach allows for it..  We cant rule out schools tho, or "that
other place where kids can go to outside their home", or whatever it
may be called in the future, bcz it doubles as a daycare center for
many working parents (the pandemic made this clear), and especially in
poorer neighborhoods, if there is trouble at home, etc it can work as
a sanctuary of sorts, kids go there, to a well-known place where other
adults are present.

"But a lot of new ed approaches are around homeschooling, why aren't
you for homeschooling?"

---

"@MobilityPragma

Hello @villedenice !!! 😎🌞Le vélo à #hydrogène Alpha de passage sur
la promenade des anglais. #baiedesanges #nice #bikelife #h2bike #h2now
@provencealpescotedazur à Nice Ville - Promenade des Anglais"

<img width="340" src="https://pbs.twimg.com/media/ExqAP64WQAkjHK_?format=jpg&name=small"/>

---

Huge actv spike in DR Congo, Mozambique. Many deaths in Mali, MSA is
French aligned right?

---

UCDP Feb 2021 data is out.

Looking at IS activity. First total is incidence count, other is
deaths total.

```python
import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv('https://ucdp.uu.se/downloads/candidateged/GEDEvent_v21_0_2.csv')
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_colwidth', 20)
df1 = df[(df['side_a'] == 'IS' )]
print (df1[['side_b','deaths_b','country']].\
      groupby(['side_b','country']).\
      agg({'country':'count', 'deaths_b': 'sum'}) )
```

```text
                                       country  deaths_b
side_b               country                            
Civilians            Afghanistan             3         0
                     Burkina Faso            6         0
                     DR Congo (Zaire)       13         0
                     Egypt                   1         0
                     Mozambique              7         0
                     Nigeria                 1         0
                     Syria                   5         0
JNIM                 Burkina Faso            3         4
Jama'atu Ahlis Su... Niger                   1         0
                     Nigeria                 1         3
MSA                  Mali                    1        10
SDF                  Syria                   9         9
Taleban              Pakistan                1         1
Yan Gora             Nigeria                 3         0
```

---

I realized Seshat data file had some columns "scaled", so they dont reflect
the raw value. Where is the raw value? I find the orig, but it has columns
seperated to *rows*. Woha. Scrubbing now.

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


