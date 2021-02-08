# Tweets

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Python is winning big time, much of it through data science targeted at performance using NumPy arrays and derivatives. <a href="https://twitter.com/hashtag/HPC?src=hash&amp;ref_src=twsrc%5Etfw">#HPC</a> will follow. <br><br>Data centric Python <a href="https://twitter.com/hashtag/dace?src=hash&amp;ref_src=twsrc%5Etfw">#dace</a> may be the path. <a href="https://t.co/KpSbGqm9me">https://t.co/KpSbGqm9me</a></p>&mdash; Torsten Hoefler (@thoefler) <a href="https://twitter.com/thoefler/status/1358453243467153408?ref_src=twsrc%5Etfw">February 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Power paste 👍

"@hazergroupltd

Researchers at the Fraunhofer Institute for Manufacturing Technology
and Advanced Materials IFAM in Dresden have developed a paste for
hydrogen storage. The institute is calling the mass 'power paste'"

[Link](https://mobile.twitter.com/hazergroupltd/status/1358551286069739521)

---

Good.. At least be a Denmark. Democratize next.

"Cuba opens up its private sector in major economic reform.. Cuba
announced Saturday that private activity will be authorized in most
sectors, a major reform in the communist country where the state and
its companies dominate economic activity"

---

"Revealed: Queen lobbied for change in law to hide her private wealth"

[Link](https://www.theguardian.com/uk-news/2021/feb/07/revealed-queen-lobbied-for-change-in-law-to-hide-her-private-wealth)

---

Quick doomsday check, checking if any spikes in earthquakes globally, as time series.

No upward trend. Signal looks mean-reverting

```python
import pandas as pd
from quakefeeds import QuakeFeed
feed = QuakeFeed("4.5", "month")
m = [[feed[i]['properties']['time'], feed[i]['properties']['mag']] for i in range(len(feed))]
df = pd.DataFrame(m).sort_values(by=0)
mags = df[1].rolling(window=15).mean()
mags.plot()
plt.title('Monthly Earthquakes')
plt.savefig('quake-series.png')
```

<img width="340" src="https://pbs.twimg.com/media/EtrX4_wXIAE_NzV?format=png&name=small"/>

---

Equador election, hopefully the left wing guy wins.

---

"@tahirqadiry

Today, the shipment of 500K Made In India vaccine will arrive in \#Kabul"

---

I saw advection ♪♬ u say convection ♪♬

---

The `Event Text` column looks interesting.. its values r general enough.

If grouped on it wonder how Top 10 looks.. could show interesting
patterns... a weekly report maybe?

---

Sample output from ICEWS. 

```python
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
df = pd.read_csv("/tmp/20200719-icews-events.tab", sep="\t")
print (df[['Event Date','Source Name','Event Text','Target Name']])
```

```text
      Event Date                     Source Name                                   Event Text                                        Target Name
0     2020-06-26                     Mike Pompeo                    Make an appeal or request                                     European Union
1     2020-06-26                           Japan                                      Consult                                      United States
2     2020-06-26                   United States                                      Consult                                              Japan
3     2020-06-27                 Grigol Vashadze                               Make statement    People Associated with the Opposition (Georgia)
4     2020-06-28             Libyan Armed Forces                            Praise or endorse                                 Government (Libya)
...          ...                             ...                                          ...                                                ...
8694  2020-07-20  Royal Administration (Belgium)                      Make empathetic comment  Head of Government (Democratic Republic of Congo)
8695  2020-07-20  Royal Administration (Belgium)                      Make empathetic comment                       Democratic Republic of Congo
8696  2020-07-20            Armed Gang (Somalia)      fight with small arms and light weapons                                  Citizen (Somalia)
8697  2020-07-20    Head of Government (Somalia)                               Make statement                                            Somalia
8698  2020-07-20              Police (Australia)  Arrest, detain, or charge with legal action                                Citizen (Australia)

[8699 rows x 4 columns]
```

---

**Conflict Databases**

1) UCDP/PRIO Armed Conflict Dataset

[Link](https://www.prio.org/Data/Armed-Conflict/UCDP-PRIO/)

2) ICEWS

[Weekly Sample](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QI2T9A) 

[Historical](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/28075)

[Starter code](https://nbviewer.jupyter.org/gist/dmasad/f79ce5abfd4fb61d253b)

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

[Religion](/2015/04/god-religion.md)

[Democracy, Parties](/2016/11/democracy.md)

[Economy](/2018/05/economy.md)

[Globalization](/2018/09/globalization.md)

[Rome, The First Wave](/2017/12/rome.md)

[Human Nature & Health](/2020/07/human-nature.md)

[Climate Change](/2018/12/climate.md)

[The Middle East](/2019/07/middleeast.md)

[TR](../tr)

## Browse

[By Year](years.md)

[Search](search.html)

[Tweet Archive](/tweets/README.md)


