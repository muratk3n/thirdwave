# Tweets - Week 13f

"@teatotalitarian

The damage without intervention is incalcuable.  You can't sell to
people with no $ or jobs.  The economy was struggling post fires. You
cant stimulate an economy by saddling all with more private debt. Be
like NZ 80% subsidies and rent mortgage/freezes. NZ will emerge
unscathed"

*2020-3-27 14:24:1*

---
Former Fed Chair Ben Bernanke: “Nothing is going to work, the Fed is
not going help, fiscal policy is not going to help, if we don’t get
the public health right — if we don’t solve the problem of the virus."

*2020-3-27 14:22:4*

---

Holy shit. Boris Johnson tested positive for COV. Hope he gets well soon.

*2020-3-27 14:19:14*

---

Covid update, 59K more cases in one day, death rate 16.2 %. US has now
highest confirmed cases. Daily change same, on avg 12.21% increase,
which is, crazy.

[Link](https://muratk3n.github.io/thirdwave/en/2020/02/corona.html)

*2020-3-27 14:18:55*

---


Maybe there is no need for most optimization, an interpolation does
huge amt of work already, there is a constant push-and-pull to explain
all the data, the global minimum can be a simple side product to that.

*2020-3-27 13:49:12*

---

Bcz I wanted to mimic work hours today feels like Friday - but at home 😐

*2020-3-27 12:8:46*

---

You can retaliate, kick Jean Claude Van Damme out of the country.

*2020-3-27 6:39:12*

---

Heee hehe - they just called u a waffle

"@michaelbirnbaum

Here's how Belgian media is describing the U.S.: 'In a country where
most workers receive meager unemployment benefits, where pensions
depend partly on the markets and where the savings rate is very low,
...the spread of the virus risks pushing millions into poverty.'"

*2020-3-27 6:38:22*

---

"@ConnorSouthard

Landlords mad about capitalism happening to them has to be the
funniest storyline in all of this"

*2020-3-27 0:43:24*

---

"@ianbremmer

More than a third of the world’s population is currently on some form
of coronavirus lockdown"

*2020-3-26 22:59:31*

---

The correct graph, SP500 1929/2020 overlay. If match is correct,
another fall is coming.

<img width="340" src="https://pbs.twimg.com/media/EUEGCdCWkAYsccK?format=png&name=small"/>


```python
import pandas as pd, datetime
import pandas_datareader.data as web

today = datetime.datetime.now()
start=datetime.datetime(1920, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
df = web.DataReader("^GSPC", 'yahoo', start, end)[['Adj Close']]

df2 = pd.DataFrame(df[df.index > '1929-09-30'].head(200))
df2 = df2.reset_index()
arr = np.array(df[df.index > '2020-02-15'].head(200))
df2.ix[np.arange(len(arr)),'dep2'] = arr
print (len(df2))

df2 = df2.set_index('Date')
df2.columns = ['Depression 1','Depression 2']
ax1 = df2['Depression 1'].plot(color='blue', grid=True)
ax2 = df2['Depression 2'].plot(color='red', grid=True, secondary_y=True)
h1, l1 = ax1.get_legend_handles_labels()
ax1.set_ylim(16,32)
h2, l2 = ax2.get_legend_handles_labels()
ax2.set_ylim(1700,3400)
plt.savefig('depress.png')
```

*2020-3-26 21:48:4*

---

Really? Youtube restricts ppl from using the word coronavirus, covid
etc? That's a bit draconian..

*2020-3-26 21:46:34*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">If you’re a parent, we’re boosting your Canada Child Benefit payment. If you’re worried about making ends meet, we’re increasing your GST Credit. And if you’ve lost your income because of COVID-19, we’ve introduced the Canada Emergency Response Benefit to help you even more. ⤵️ <a href="https://t.co/X0HIqpjuqm">https://t.co/X0HIqpjuqm</a></p>&mdash; Justin Trudeau (@JustinTrudeau) <a href="https://twitter.com/JustinTrudeau/status/1243239428241448960?ref_src=twsrc%5Etfw">March 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-26 21:38:20*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Mitsubishi Fuso to Begin Series Production of Fuel-Cell Trucks by late 2020s--Series production of <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> <a href="https://twitter.com/hashtag/fuelcell?src=hash&amp;ref_src=twsrc%5Etfw">#fuelcell</a> trucks to start by the late 2020s--<a href="https://t.co/azXKjawA7K">https://t.co/azXKjawA7K</a> <a href="https://twitter.com/hashtag/hydrogennow?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogennow</a> <a href="https://twitter.com/hashtag/fuelcells?src=hash&amp;ref_src=twsrc%5Etfw">#fuelcells</a> <a href="https://twitter.com/hashtag/decarbonise?src=hash&amp;ref_src=twsrc%5Etfw">#decarbonise</a> <a href="https://twitter.com/hashtag/zeroemissions?src=hash&amp;ref_src=twsrc%5Etfw">#zeroemissions</a> <a href="https://twitter.com/hashtag/hydrogeneconomy?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogeneconomy</a> <a href="https://twitter.com/hashtag/h2?src=hash&amp;ref_src=twsrc%5Etfw">#h2</a> <a href="https://twitter.com/hashtag/zeroemission?src=hash&amp;ref_src=twsrc%5Etfw">#zeroemission</a> <a href="https://twitter.com/fuelcellsworks?ref_src=twsrc%5Etfw">@fuelcellsworks</a> <a href="https://t.co/zAmMxVEGsl">pic.twitter.com/zAmMxVEGsl</a></p>&mdash; FuelCellsWorks (@fuelcellsworks) <a href="https://twitter.com/fuelcellsworks/status/1243232164067586051?ref_src=twsrc%5Etfw">March 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-26 20:45:15*

---


<blockquote class="twitter-tweet"><p lang="en" dir="ltr">One official explained that clean <a href="https://twitter.com/hashtag/H2?src=hash&amp;ref_src=twsrc%5Etfw">#H2</a> could become critical for powering <a href="https://twitter.com/hashtag/energy?src=hash&amp;ref_src=twsrc%5Etfw">#energy</a> heavy sectors <a href="https://twitter.com/hashtag/EUH2?src=hash&amp;ref_src=twsrc%5Etfw">#EUH2</a> <a href="https://twitter.com/hashtag/euhydrogenfuel?src=hash&amp;ref_src=twsrc%5Etfw">#euhydrogenfuel</a> <a href="https://twitter.com/hashtag/EUhydrogenfuelpartnership?src=hash&amp;ref_src=twsrc%5Etfw">#EUhydrogenfuelpartnership</a> <a href="https://twitter.com/hashtag/EuropeH2?src=hash&amp;ref_src=twsrc%5Etfw">#EuropeH2</a> <a href="https://twitter.com/hashtag/europehydrogenfuel?src=hash&amp;ref_src=twsrc%5Etfw">#europehydrogenfuel</a> <a href="https://twitter.com/hashtag/EuropeanCommission?src=hash&amp;ref_src=twsrc%5Etfw">#EuropeanCommission</a> <a href="https://twitter.com/hashtag/europeanunionhydrogenfuel?src=hash&amp;ref_src=twsrc%5Etfw">#europeanunionhydrogenfuel</a> <a href="https://twitter.com/hashtag/EuropeanUnionhydrogenfuelpartners?src=hash&amp;ref_src=twsrc%5Etfw">#EuropeanUnionhydrogenfuelpartners</a> <a href="https://t.co/adJLMfK8NQ">https://t.co/adJLMfK8NQ</a></p>&mdash; Hydrogen Fuel News (@hydrogenfuelnew) <a href="https://twitter.com/hydrogenfuelnew/status/1243211269433364485?ref_src=twsrc%5Etfw">March 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-26 19:33:40*

---

Watching ST TNG "Borg episode". Lesson to remember - if the going
gets tough, seperate the saucer section. 

*2020-3-26 19:25:37*

---

Ah of course u can top up phone internet quota through simple bank
app. One less unnecessary interaction.

*2020-3-26 18:40:40*

---

🔥🔥🔥

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Which one, Rome or the United States?</p>&mdash; Zito (@_Zeets) <a href="https://twitter.com/_Zeets/status/1243188256629501952?ref_src=twsrc%5Etfw">March 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-26 18:7:4*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Promising Results for Ammonia Tested in Combustion Engine - searching for the clean fuels of the future at <a href="https://twitter.com/wartsilacorp?ref_src=twsrc%5Etfw">@wartsilacorp</a> <a href="https://t.co/RnwyG747Eg">https://t.co/RnwyG747Eg</a></p>&mdash; Atte Palomäki (@attep) <a href="https://twitter.com/attep/status/1243100322622590977?ref_src=twsrc%5Etfw">March 26, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-3-26 17:2:0*

---
