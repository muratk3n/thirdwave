# Tweets

"@Cummins

@Cummins is locating one of the world’s largest electrolyzer plants in
Spain to produce green hydrogen"

[Link](https://twitter.com/Cummins/status/1396765441020899331)

---

"[MMEX Resources Corp] .. signed agreement to purchase additional 324
acres in Pecos County Texas"

[Link](https://bit.ly/3hSqPWv)

---

"The Eiffel Tower will be illuminated with certified #renewablehydrogen
electricity on Tuesday evening"

[Link](https://bit.ly/3wwn5Ol)

---

"Momentum Grows in Queensland’s Hydrogen Sector With Addition of Two
More Technology Clusters.. The two new clusters join the #H2TCA, the
national network of 13 clusters unveiled in February"

[Link](https://bit.ly/2ThzRCd)

---

"@H2MobilityAus

Significant announcement at the #AusHydrogenConf with @DrLarryMarshall
unveiling @CSIRO's new Hydrogen Industry Mission. The $68m research
mission will support the world’s transition to decarbonisation, create
new jobs and help position Australia as a #renewable energy leader"

[Link](https://twitter.com/H2MobilityAus/status/1397424107260571648)

---

TR is beaten by MEXICO. Mexico, with all its problems with drug
cartels is better off.. But then again, according to some recent
revelations TR is becoming a major drug center of her own.

Innovators go out, coke dealers come in.

---

The solution isnt "more people", or importing bunch of f-ing morons
from abroad, with their chicken coops and shit, in a crooked trucks...
The truck hits a bump and the chicken jump "bwak bwak bwak bwak! bwak
bwak bwak bwak!"... stuff like that.

Must aim for quality.

---

Democracy goes, innovative people leave.. 

---

GDP Per Capita fell for TR dramatically, a trend since 2013. Probably
coincides with degradation of its democracy. WB API doesnt have
numbers for 2020, but most state it did not get better. Some estimates
even place the current number to be around $7000. Sad.


```python
from pandas_datareader import data, wb
import pandas as pd

dat = wb.download(indicator='NY.GDP.PCAP.CD', country=['TR','GR','MX'], start=2010, end=2020)
df = dat.reset_index()
df = df.sort_values('year')
df = df.set_index('year')
pd.set_option('display.max_columns', None)
df2 = pd.concat((df[df['country']=='Greece'],\
                 df[df['country']=='Turkey'],\
                 df[df['country']=='Mexico']),axis=1)
df2.columns = ['c1','GR','c2','TR','c3','MX']
print (df2[['GR','MX','TR']].dropna().tail(3))
df2[['GR','TR','MX']].plot()
plt.savefig('out.png')
```

```text
                GR           MX            TR
year                                         
2017  18930.218628  9287.849736  10591.474371
2018  20324.304992  9686.513783   9455.593654
2019  19580.988331  9946.033829   9126.561346
```

<img width="340" src="https://pbs.twimg.com/media/E2TzbPCXMAAAKdP?format=png&name=small"/>

---

That's a good idea.

"The European Parliament’s annual report on Turkey suggests placing
Turkey’s far-right Grey Wolves on the EU terrorist list."

---

The upcoming movie is ruined for me now.. I thought was going to watch
a bad, tough guy, but he mopes and cries like a little girl. 

---

🤣 Big tough guy.. money talked bro squirmed

"John Cena: Fast and Furious star ... posts a video apology in Chinese
after describing Taiwan as a "country""

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


