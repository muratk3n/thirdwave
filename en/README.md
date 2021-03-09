# Tweets

Pinned Tweets

<img width="90%" src="https://pbs.twimg.com/media/EvdKNhvXAAE9Rr2?format=png&name=small"/>

---

Now if we can fix the energy side with renewable fuels that relies on
common ingredients, and physical goods side with truly substituting
knowledge for atoms, building everything on demand, that cld be a
route.. Absent these, might have to change incentives, funding to
encourage less growth.

---

Govs may want it bcz it means more taxes in the future, easing debt
repayment. Companies want growth bcz of their investors who need
returns. All that cld be fine but even with services dominating the
economy, more growth still means more shit. As in **physical shit**,
goods and materials, leading to resource extraction, planet plundered. See
[excerpts](2021/03/goods-materials-growth-hickel.md). 

"Why does everyone want growth?"

---

[Wired article](https://www.wired.co.uk/article/lithium-batteries-environment-impact)
on lithium production.

---

Was that RoyalExit? So many exits over there

---

ITM is a BUY

---

Lots of doubters, sure. Unfortunately I have to follow such characters
because the landscape is littered with dipshits in all walks of
sci/tech blowing smoke up everyone's ass.

---

"Quan. supremacy" is achieving a computation through quantum comp that
no regular computer can match. Kalai is raising doubts on Goog
supremacy claims.

"@GilKalai

[Scientists] proposed a general method for simulating quantum circuits
and announce that they could generate samples from the Sycamore
circuit with much better fidelity. This sheds doubts on Google's
'supremacy' claims"

---

More from UCDP conflict dataset...

"Yearly Datasets covering 1946 - 2019", "UCDP Dyadic Dataset version
20.1". Conflict records are (global) events where at least 25 ppl
died, for each dyad-year. "Dyads", meaning action pairs (A attacks B
is a dyad), are captured at yearly granularity (A attacks B in a year
N times, appears once in record). Simple plot here on all dyad action
occurences per year, it can give a general idea on violence level
throughout the world,


```python 
import pandas as pd, zipfile
with zipfile.ZipFile('ucdp-dyadic-201-csv.zip', 'r') as z:
      df =  pd.read_csv(z.open('ucdp-dyadic-201.csv'))
df = df[['year','side_a','type_of_conflict','intensity_level']]
df.groupby('year').size().plot()
plt.axvspan(2008,2008,color='y')
plt.axvspan(1989,1989,color='y')
plt.axvspan(2016,2016,color='y')
plt.savefig('out.png')
```

<img width="340" src="https://pbs.twimg.com/media/Ev9qgiUXMAIq6Br?format=png&name=small"/>

There was reduction soon after 1989, the fall of the Berlin Wall. Kept
on going down past 9/11, past 2001, past the invasion of Iraq.. But, I
guess bcz by 2008-10 Iraq became FUBAR, vio picked up. Started to
decrease little before 2016, but still did not go down to 2010 levels.

---

Bloomberg: "As governments and industries seek less-polluting
alternatives to hydrocarbons, the world’s biggest crude exporter
doesn’t want to cede the burgeoning hydrogen business to China, Europe
or Australia and lose a potentially massive source of income. So it’s
building a $5 billion plant powered entirely by sun and wind that will
be among the world’s biggest green hydrogen makers when it opens in
the planned megacity of Neom in 2025.

The task of turning a patch of desert the size of Belgium into a
metropolis powered by renewable energy falls to Peter Terium, the
former chief executive officer of RWE AG, Germany’s biggest utility,
and clean-energy spinoff Innogy SE...

That should mean plenty of potential customers for the plant called
Helios Green Fuels... Saudi Arabia possesses a competitive advantage
in its perpetual sunshine and wind, and vast tracts of unused
land. Helios’s costs likely will be among the lowest globally and
could reach $1.50 per kilogram by 2030, according to BNEF. That’s
cheaper than some hydrogen made from non-renewable sources today

For starters, Helios will produce 650 tons of hydrogen a day by
electrolysis – enough for conversion to 1.2 million tons per year of
green ammonia. Air Products will buy all of that ammonia, which is
easier to ship than liquid or gaseous hydrogen, and convert it back
upon delivery to customers...

Germany said it needs 'enormous' volumes of green hydrogen, and it
hopes Saudi Arabia will be a supplier"

[Link](https://www.bloomberg.com/news/articles/2021-03-07/saudi-arabia-s-plan-to-rule-700-billion-hydrogen-market)

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


