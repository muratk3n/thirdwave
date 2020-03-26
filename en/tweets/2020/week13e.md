# Tweets - Log

<img width="240" src="https://iruntheinternet.com/lulzdump/images/seinfeld-kramer-screaming-blood-transplant-hospital-1415053295A.gif">

*2020-3-26 16:28:52*

---

Corona update, 93K in 2 days. Death rate 15.85 %. 

Average daily increase since March 1, 12.23 %.

[Link](https://muratk3n.github.io/thirdwave/en/2020/02/corona.html)

*2020-3-26 16:10:39*

---

Initial unemp claims. Over 3 million!

Dude that line upwards has no paralel. Effin freaky shit!

```2020-03-21  3,283,000```

[Link](https://muratk3n.github.io/thirdwave/en/2019/05/stats.html#claims)

*2020-3-26 15:54:49*

---

Very good

[Link](https://mobile.twitter.com/HoarseWisperer/status/1242879985024741382)

*2020-3-26 15:56:14*

---

Desync ASAP. Otherwise soc is bunch of ppl standing around with
fingers up eachother's ass forming a circle fine for kumbaya not for
anything else

"@djpardis

Still not sure if synchronized comms is where the future of work is at"

*2020-3-26 15:52:23*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Great news: New Zealand to develop its first <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> refueling network: <a href="https://t.co/UcWer0yY8C">https://t.co/UcWer0yY8C</a> <a href="https://twitter.com/hashtag/cleanfuel?src=hash&amp;ref_src=twsrc%5Etfw">#cleanfuel</a></p>&mdash; Ballard Power (@BallardPwr) <a href="https://twitter.com/BallardPwr/status/1242844185817907203?ref_src=twsrc%5Etfw">March 25, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-26 12:18:58*

---

"@waltshaub

I did not predict 2020 being the year that human sacrifice made a
comeback. I mean, having lived through the past 3 years nothing is
surprising anymore, but it's quite a thing to behold when you see them
calling for it"

*2020-3-26 10:37:30*

---

"@spectatorindex

UNITED KINGDOM: 21 year old woman with no pre-existing medical
conditions has died of coronavirus"

*2020-3-26 10:34:36*

---

Slowdown happens bcz of misallocation of credit (money). That misalloc
is due to ppl moving, improving in increments, follow the elevation to
go up but find self on top of a smaller hill, the bigger one is
elsewhere. Epitome of local optimum in optimization. What to do? Well
gotta climb down first and move over to the other mountain.

*2020-3-26 10:29:45*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Major retailers are telling landlords they&#39;re not going to pay rent. This is going to get messy real fast. <a href="https://t.co/CcPqiLJwHA">https://t.co/CcPqiLJwHA</a></p>&mdash; Kim Bhasin (@KimBhasin) <a href="https://twitter.com/KimBhasin/status/1242837500957204481?ref_src=twsrc%5Etfw">March 25, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-26 10:27:31*

---

Great Depression SP500 Overlay. Red 2020, blue 1929.

<img width="340" src="https://pbs.twimg.com/media/EUA-NN9XsAAcq1k?format=png&name=small"/>

Interesting, in terms of percentages what happened during Depression
happened much faster now. Because we are talking bigger market caps,
changes in absolute numbers are huge.


```python
import pandas as pd, datetime
import pandas_datareader.data as web

today = datetime.datetime.now()
start=datetime.datetime(1920, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
df = web.DataReader("^GSPC", 'yahoo', start, end)[['Adj Close']]
df2 = df.copy()
df2 = df[df.index > '1929-09-01']
df2 = df2.head(1000)
df2 = df2.reset_index()
tmp = np.array(df[df.index > '2020-01-01'])
df2.ix[range(len(tmp)),'dep2'] = tmp
df2 = df2.set_index('Date')
df2.columns = ['Depression 1','Depression 2']
ax1 = df2['Depression 1'].plot(color='blue', grid=True)
ax2 = df2['Depression 2'].plot(color='red', grid=True, secondary_y=True)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.savefig('dep.png')
```

@RheaButcher

2004: don’t eat French fries or else you hate America 

2008: wear a lapel pin or you don’t love your country

2016: kneel before the flag

2020: die for the economy

*2020-3-25 21:8:58*

---

Hammersley points are the shite biaaatch!! I just saw the freakiest
function being recreated from 20 Hammersley points. Twenty!

There is random and there is random, nam sayin?

*2020-3-25 20:48:22*

---

As demand goes, so does oil.. With growth exp low the demand for oil would be less

[Link](https://muratk3n.github.io/thirdwave/en/2019/05/stats.html#oil)

*2020-3-25 20:37:48*

---

"Oil price may fall to $10 a barrel as world runs out of storage space"
-- theguardian.com

*2020-3-25 20:24:37*

---

"But I know a company which can grow as much". Sure, that is
possible. Others might think the same about other companies and buy
their shares, expecting that kind of growth. My point is all of these
people cannot be right at the same time. Hence, winners and losers.

Or at least there has to be.. If gov steps in and saves all the losers
then there is no market. Enter socialism.

*2020-3-25 20:23:7*

---

It'd take 20 years to go to 150% with 2% growth.

```python
np.prod(np.ones(20)*1.02)
```

```text
Out[1]: 1.485947395978355
```

*2020-3-25 20:23:7*

---

Haha.. of course there is a Python package called `tulipy`. And it's a
"Financial Technical Analysis Indicator Library"!! 😂😂😂

[Link](https://pypi.org/project/tulipy/)

*2020-3-25 19:27:4*

---

In what future does the GDP increase to 150%? Every year it increases
2-3% if that. That "future" you speak of is too rosy, or "tulipy".

"So what if market cap / GDP was >150% Markets are about the future!"

*2020-3-25 19:26:1*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I can&#39;t believe Prince Charles ate a bat.</p>&mdash; Adam Liaw (@adamliaw) <a href="https://twitter.com/adamliaw/status/1242768514093436928?ref_src=twsrc%5Etfw">March 25, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-25 19:25:46*

---

"@wayne_vt

I know it’s time to short when all my friends who 'invest' start
telling me it’s time to go long on this 'HISTORIC BUYING OPPORTUNITY'".

*2020-3-25 19:14:1*

---

It's a vacation of sorts - all regular activities being frozen. From
that angle, and for those who will make it, not bad.

*2020-3-25 19:13:2*

---

I do the calculations but even I cant believe what I am seeing. I
publish almost mechanically, and look at it myself and go WTF?

*2020-3-25 18:18:32*

---

Politics was supposed to balance that but in many places politicians
sold their souls to corporatism (another definition of fascism BTW).

"@EternalDago

Capitalism relies 100% on constant, limitless growth. It can’t even
survive a 2 week slow down to adapt to the needs of human
lives. Imagine thinking this could last forever"

*2020-3-25 17:39:29*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">FuelCell Energy’s 20 Megawatt <a href="https://twitter.com/hashtag/FuelCell?src=hash&amp;ref_src=twsrc%5Etfw">#FuelCell</a> Park Exceeded All Performance Expectations at Korea Southern Power Company--<a href="https://twitter.com/FuelCell_Energy?ref_src=twsrc%5Etfw">@FuelCell_Energy</a> 20 megawatt highly reliable continuous clean platform serving customers in Incheon-<a href="https://t.co/xI2FLIyonD">https://t.co/xI2FLIyonD</a> <a href="https://twitter.com/hashtag/Hydrogennow?src=hash&amp;ref_src=twsrc%5Etfw">#Hydrogennow</a> <a href="https://twitter.com/hashtag/decarbonise?src=hash&amp;ref_src=twsrc%5Etfw">#decarbonise</a> <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> <a href="https://twitter.com/hashtag/h2?src=hash&amp;ref_src=twsrc%5Etfw">#h2</a> <a href="https://t.co/8RyqRnh8Dd">pic.twitter.com/8RyqRnh8Dd</a></p>&mdash; FuelCellsWorks (@fuelcellsworks) <a href="https://twitter.com/fuelcellsworks/status/1242802618524721153?ref_src=twsrc%5Etfw">March 25, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-25 16:22:41*

---

<blockquote class="twitter-tweet" data-conversation="none"><p lang="en" dir="ltr">India, UK, South Africa, New Zealand: We&#39;re locking down to prevent mass death<br><br>America: Were opening up, the capitalism gods demand blood sacrifice</p>&mdash; Oliver Willis (@owillis) <a href="https://twitter.com/owillis/status/1242772177872736257?ref_src=twsrc%5Etfw">March 25, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-25 14:38:33*

---

@IamKarenBoBaran

Capitalism 1970: " work hard, you too can be rich "

Capitalism 1990: " work hard & a few crumbs will fall down "  

Capitalism 2020: " you should be willing to die in order to save the economy for the top percent "  

Are you guys still all in for this?

*2020-3-25 10:21:22*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hyzon, Toyota-Hino, Nikola/IVECO and Hyundai are changing the world of trucking to literal zero emission transport and this contribute to drastic greenhouse gas emission reductions...<a href="https://t.co/mHmaEtSExm">https://t.co/mHmaEtSExm</a></p>&mdash; Reiner (@H2FCEV) <a href="https://twitter.com/H2FCEV/status/1242704315489320962?ref_src=twsrc%5Etfw">March 25, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-25 10:9:36*

---

"@notstevenwhite

I just talked to my grandparents and I didn't actually get the sense
they want to die to save capitalism"

*2020-3-25 8:31:4*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Today has made it very clear how many people would have absolutely justified slavery because “the economy”</p>&mdash; josie duffy rice (@jduffyrice) <a href="https://twitter.com/jduffyrice/status/1242275452183621633?ref_src=twsrc%5Etfw">March 24, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-25 8:17:15*

---

"@CaelainnH

Ireland has just effectively nationalised its health service in
response to the pandemic. Private hospitals are being taken
over. Everyone is now promised equal access to treatment, regardless
of insurance. A massive change"

*2020-3-25 8:17:15*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Enough is enough. To those who are still hanging out with friends or hosting dinner parties: Do the right thing and stay home. And while you’re at home, share this video to remind others they need to stay home too. <a href="https://twitter.com/hashtag/PlankTheCurve?src=hash&amp;ref_src=twsrc%5Etfw">#PlankTheCurve</a> <a href="https://t.co/b2q1fT81cO">pic.twitter.com/b2q1fT81cO</a></p>&mdash; Justin Trudeau (@JustinTrudeau) <a href="https://twitter.com/JustinTrudeau/status/1242602368748924931?ref_src=twsrc%5Etfw">March 25, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-25 7:58:53*

---

Trump net approval at -6%. It hasnt seen these levels for nearly three
years \#538

*2020-3-25 0:1:55*

---

"@JoSamps92

The Netherlands has unveiled a Multi-year Programmatic Approach for
Hydrogen (MPAH) which aims to accelerate implementation of #hydrogen
technologies and ensure they are “substantially embedded” by 2030"

*2020-3-24 23:46:22*

---

"@tixhonjm

Cummins Increases Investment in Loop Energy and Fuel Cells for
Commercial Transport Application"

[Link](https://mobile.twitter.com/tixhonjm/status/1242496265230913539)

*2020-3-24 23:44:44*

---

"@BrentBeshore

Business owner friend applied for disaster relief funds yesterday and
called me panicked. To get through the maze you had no choice but to
lie.

Kicker? Financials must be submitted by fax, mail or email. Email max
size could be 5 MB. His last year's financials alone were 18 MB"

*2020-3-24 23:22:5*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">India&#39;s lockdown is staggering. 1.3b people indoors for the next 21 days.</p>&mdash; Sriram Krishnan (@sriramk) <a href="https://twitter.com/sriramk/status/1242479115271155718?ref_src=twsrc%5Etfw">March 24, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-24 23:16:24*

---

"@girlsreallyrule

You should be willing to die at your shitty job so that rich people's
grandkids have minimal interruptions in their lifestyles-it's the
right thing to do. \#GOPDeathPanels"

*2020-3-24 23:14:32*

---

Russia is in the game, competing. Awesome.

EU will probably want to diversify since now sunshine can also produce
the "green fuel". Merkel was in Africa some time back... It's good for
Africa to have more $$ of course, from the EU standpoint, the next
door neighbor.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Russia’s hydrogen bet sets up contest with Australia for Japanese market-Report says that Russia would be able to offer <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> at a price of $3.38 per kg already between 2020-2025 and compete for 10-15% of world market by 2030-<a href="https://t.co/L0YFrp1tYG">https://t.co/L0YFrp1tYG</a> <a href="https://twitter.com/hashtag/hydrogennow?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogennow</a> <a href="https://twitter.com/hashtag/decarbonise?src=hash&amp;ref_src=twsrc%5Etfw">#decarbonise</a> <a href="https://t.co/o48oq3Fy7z">pic.twitter.com/o48oq3Fy7z</a></p>&mdash; FuelCellsWorks (@fuelcellsworks) <a href="https://twitter.com/fuelcellsworks/status/1242539296965394441?ref_src=twsrc%5Etfw">March 24, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-24 22:54:40*

---

That fine moment when u realize you need another, darker color for
covid cases bcz new cases might surpass the last bucket size on the
map.

*2020-3-24 22:16:48*

---

"@alexip

If schools are closed for a very long time, parents will find the
vaccine sooner than scientists"

*2020-3-24 22:1:10*

---
