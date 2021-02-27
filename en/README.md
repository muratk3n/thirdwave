# Tweets

<img width="340" src="https://pbs.twimg.com/card_img/1364925382311489540/CCjbXwd_?format=jpg&name=small"/>

[Link](https://www.alexander-dennis.com/media/news/2021/february/adl-s-british-built-h20-next-generation-hydrogen-bus-to-deliver-up-to-300-zero-emission-mile-range/)

---

<blockquote width="340" class="twitter-tweet"><p lang="en" dir="ltr">Happy to see <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> cooperation also outside Europe! Our colleague <a href="https://twitter.com/SabrineEU?ref_src=twsrc%5Etfw">@SabrineEU</a> spoke at &quot;EU-Korea green partnership: Connecting Korea and EU&#39;s <a href="https://twitter.com/hashtag/GreenDeal?src=hash&amp;ref_src=twsrc%5Etfw">#GreenDeal</a>&quot; about hydrogen strategies at EU and national level, w/ a focus on <a href="https://twitter.com/hashtag/mobility?src=hash&amp;ref_src=twsrc%5Etfw">#mobility</a> aspects. 🇪🇺🇰🇷<br>Recording <a href="https://t.co/nGmgj0kbKc">https://t.co/nGmgj0kbKc</a> <a href="https://t.co/IA5UEo2zMV">pic.twitter.com/IA5UEo2zMV</a></p>&mdash; Hydrogen Europe (@H2Europe) <a href="https://twitter.com/H2Europe/status/1365216728045608960?ref_src=twsrc%5Etfw">February 26, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

I remember this fine innovation from 2019.. Aliminium hydride stores
H2, then just add water and H2 comes out?

A patent was granted on it, a start-up founded set to produce.. News
of peaceful applications of it wld be nice.

US DOE: "Ideal [military] equipment weight is 30% of a person’s body
weight, but some soldiers have to carry more than 100 pounds. To
lighten the load, the Army is looking into replacing lithium-ion
batteries with fuel cells for power generation—decreasing battery
weight by 50%. These 'wearable power systems' for the dismounted
solider can produce 20 watts (W) of continuous output and 35W of peak
power. To aid this effort, the U.S. Department of Energy (DOE) is
working to drive down the cost of aluminum hydride—a promising
material that can be used for storing hydrogen to utilize in these
portable fuel systems"

[Link](https://www.energy.gov/eere/articles/4-ways-fuel-cells-power-us-military)

---


<iframe width="300" src="https://www.youtube.com/embed/caYHHcP6jrs?start=29&end=114" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

"What is the reflation trade?"

---

Gold is deemed as "safe haven" during downturns (as in
finance/liquidity and part macro sense, not in currency,
end-of-the-world scare sense), it is prefered during such times.

Once possibility of growth appears, rates go up, gold goes down.

Will some pundits who constantly "stan gold" (and bitcoin) in that
currency alternative way update their fin knowledge now?

---

Gold and the 10 year treasury.. It doesn't get any more opposite then
this... One is up other is down, one is down other is up.. They are
comically negatively correlated.

```python
from pandas_datareader import data
import datetime

today = datetime.datetime.now()
start=datetime.datetime(2000, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
df = data.DataReader(['DGS10', 'GOLDAMGBD228NLBM'], 'fred', start, end)
print (df.tail(5))
ax1 = df.DGS10.plot(color='blue', grid=True, label='10Y')
ax2 = df.GOLDAMGBD228NLBM.plot(color='red', grid=True, label='GOLD',secondary_y=True)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.legend(h1+h2, l1+l2, loc=2)
plt.savefig('10yrgld.png')
```

```text
            DGS10  GOLDAMGBD228NLBM
DATE                               
2021-02-19   1.34           1773.75
2021-02-22   1.37           1798.80
2021-02-23   1.37           1809.50
2021-02-24   1.38           1807.25
```

<img width="340" src="https://pbs.twimg.com/media/EvJK3X_WYAAN3Hx?format=png&name=small"/>

---

Gold and treasury rates move in opposites..

---

But the gold price went down recently. Shouldnt even the talk of more
stimulus keep the price up? Well it didnt.

"They are printing money, so gold price will soar"

---

I wonder if u can model earthquakes with a plate staying / swirling on
a rod. An active quake region is "the plate", and it's like quakes are
weights dropped on that plate, plate wants to be in equilibrium, at
level, hit on one side needs to be balanced with another hit on the
other..? 🤔

---

S. Strogatz's new Cornell lecture, Asymptotics and perturbation methods, on YouTube.

[Link](https://www.youtube.com/watch?v=KZsk8B_z8pI&list=PL5EH0ZJ7V0jV7kMYvPcZ7F9oaf_YAlfbI)

---

Movie summary: "In the final days of World War II, a secret experiment
to weaponize sharks is shut down and destroyed by the Third Reich. But
now 60 years later, a small ocean town is plagued by a bloodthirsty,
mysterious creature, one built and reanimated using parts of the
greatest killers to ever inhabit in the sea - the Sharkenstein
monster!"

---

*Sharkenstein* 😆 I have to see this shit.

---

"NPROXX can provide a hydrogen storage solution best suited to the
needs, pressures and the range of the vehicle"

[Link](https://www.nproxx.com/how-hydrogen-powers-different-vehicles/)

---

Dat $tick - not bad chigga

"Fuck a Crip walk, hit the strip like in Bangkok ♪♬

Never ever see me ever trip 'bout a lil' broad

See me on the TV screamin', 'Bitch, you a damn fraud'

And you don't wanna fuck with a chigga like me"

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


