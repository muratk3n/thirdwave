# Tweets

Pinned Tweets

<img width="90%" src="https://pbs.twimg.com/media/EvdKNhvXAAE9Rr2?format=png&name=small"/>

---

"@dylanmatt

Still kind of stunned and heartened at the scale of the American
Rescue Plan. The 2009 stimulus was 5.5% of 2008 GDP. The Rescue plan
is 9.1% of 2020 GDP. And it creates a child allowance that will (knock
wood) be very hard to roll back"

---

Calibro 35 - You, Filthy Bastards! \#music

[Link](https://youtu.be/AZOQ8BucVck)

---

"Venezuela to introduce 1-million-bolivar bill"

---

US side softened then; that's good.

"The U.S. and the European Union agreed Friday to suspend tariffs on
wine, luggage, produce and other goods related to a longstanding
dispute over government subsidies to Boeing Co. and Airbus"

---

Here is an O'Neill Cylinder. Look at that thing turn.. Love it! Oh yeah!

<img width="340" src="https://drive.google.com/uc?export=view&id=13LegEelVGN4YNde44TfBcidL81fWBlOy"/>

---

Biden obviously knows all this.. So when he said "I spoke to the King,
not to the prince" it was to placate ppl in his own party who dont
like MBS. But in reality whether you are talking to the King or the
prince, you are always talking to the prince.

---

:) That's some funny shit.

"During the Obama presidency, I heard stories, since confirmed, of two
senior U.S. officials, on two separate occasions, meeting with King
Salman in his palace office. While talking, the king gazed at a
picture frame on his desk. Off in a corner, the crown prince sat at a
desk, diligently typing on a computer. The officials soon realized
what was going on: MBS was typing out what the king should say; the
picture frame was, in fact, a computer screen, and the king was
reading aloud the script by the crown prince"

[Link](https://slate.com/news-and-politics/2021/03/mbs-khashoggi-biden-punishment.html)

---

"The Parliamenterian" is an excuse.. The votes werent there for 15MW,
and WH didn't want to spend pol capital on it, that's why it's dead.

---

Jacobin: "Despite America’s two-party duopoly, third parties have played a
crucial role in shaping US politics for good and ill — from bringing
us pro-worker reforms and the welfare state"

[Link](https://jacobinmag.com/2021/03/third-parties-united-states-history/)

---

I find the way ppl just throw around random info as extremely
archaic. In the future journalists will perform the kind of analysis I
just did below; looking for legit, well curated datasets, and run
analysis' to base reporting on.

---

Looking at Jan 2021 (Feb data is not in yet)

```python
import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv('https://ucdp.uu.se/downloads/candidateged/GEDEvent_v21_0_1.csv')
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_colwidth', 20)
df1 = df[(df['side_a'] == 'IS' )]
print (df1[['side_b','deaths_b','country']])
```

```text
                  side_b  deaths_b       country
339            Civilians         0   Afghanistan
340            Civilians         0   Afghanistan
341            Civilians         0   Afghanistan
362              Taleban         5   Afghanistan
399            Civilians         0  Burkina Faso
400            Civilians         0  Burkina Faso
401            Civilians         0  Burkina Faso
411                 JNIM         0  Burkina Faso
570            Civilians         0          Iraq
714            Civilians         0    Mozambique
715            Civilians         0    Mozambique
716            Civilians         0    Mozambique
717            Civilians         0    Mozambique
718            Civilians         0    Mozambique
731            Civilians         0         Niger
737  Jama'atu Ahlis S...         3         Niger
768            Civilians         0       Nigeria
820             Yan Gora         0       Nigeria
837            Civilians         0      Pakistan
907            Civilians         0         Syria
950                  SDF         0         Syria
951                  SDF         0         Syria
952                  SDF         0         Syria
953                  SDF         0         Syria
954                  SDF         0         Syria
956                  HTS         1         Syria
```

I'd say attacks are lower than average. And just looking at Syria I
can't see how 66 number can be reached. Sounds too high.

(Also; IS killed 5 Taleban, in Afganistan??? WTF?)

---

Let's check 2020. I am going to use Uppsala Conflict datasets, montly
IS activity plot,

https://ucdp.uu.se/downloads/


```python
import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv('https://ucdp.uu.se/downloads/candidateged/GEDEvent_v20_01_20_12.csv',parse_dates=True)
df1 = df[(df['side_a'] == 'IS' )]
df1['date'] = pd.to_datetime(df1['date_start'])
df1['mon'] = df1.date.dt.month
df1.groupby('mon').size().plot()
g2 = df1.groupby('mon').sum()['deaths_b'].plot()
plt.legend(['Attacks','Deaths'])
plt.title('IS Activity')
plt.savefig('out.png')
```

<img width="340" src="https://pbs.twimg.com/media/Ev0SdqoXMAcQltI?format=png&name=small"/>

Occurence of attacks globally hover around 30.

---

🤔 What's missing here is context, what is the trend, and how many
deaths were there, etc. 

"North Press Agency counted 66 military operations, which the Islamic
State (ISIS) claimed responsible for, in north and east Syria during
January and February, 2021"

[Link](https://npasyria.com/en/55504/)

---

"‘Kill them’: Duterte wants to ‘finish off’ communist rebels"

[Link](https://www.aljazeera.com/news/2021/3/6/kill-them-all-duterte-wants-communist-rebels-finished)

---

<blockquote class="twitter-tweet" data-conversation="none"><p lang="und" dir="ltr"> <a href="https://t.co/jFaduNgME8">pic.twitter.com/jFaduNgME8</a></p>&mdash; Jim Salsman (@jsalsman) <a href="https://twitter.com/jsalsman/status/1367708192193482752?ref_src=twsrc%5Etfw">March 5, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

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


