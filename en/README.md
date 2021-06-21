# Tweets

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
print (df1)
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


