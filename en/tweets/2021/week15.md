# Week 15

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">European energy ministers have highlighted the need to create a stable regulatory framework for <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> in the <a href="https://twitter.com/hashtag/EuropeanUnion?src=hash&amp;ref_src=twsrc%5Etfw">#EuropeanUnion</a>, capable of attracting private investors into a competitive and predictable market. 💧🇪🇺<a href="https://twitter.com/hashtag/HydrogenNow?src=hash&amp;ref_src=twsrc%5Etfw">#HydrogenNow</a> <a href="https://t.co/pvJciLaYDd">https://t.co/pvJciLaYDd</a></p>&mdash; Hydrogen Europe (@H2Europe) <a href="https://twitter.com/H2Europe/status/1381290716891127812?ref_src=twsrc%5Etfw">April 11, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"@fuelcellsworks

Solar-to-#Hydrogen Tech Increase Shows 100-fold Improvement in #Solar
Energy Conversion [using] a BaTaO2N photocatalyst"

---

"Billions of dollars of Iranian money continues to be frozen in South
Korean banks as its prime minister heads for talks"

---

Guy had a stroke in 2016, so it could just be health related

"Deputy Prime Minister Heng Swee Keat shocked the nation on Thursday,
announcing he will step aside as the designated successor to Prime
Minister Lee Hsien Loong"

---

Added new page for conflict stats

[Link](2019/05/confstats.md)

---

WTF happened to dry parsley flakes? The prod disappeared all markets
all of a sudden. God dam..

---

Via Bloomberg

<img width="340" src="https://pbs.twimg.com/media/Eysbo2cWUAIpyb6?format=png&name=small"/>

---

Business Insider: "'Unions lose in 90% of the cases when management
opposes the organizing effort,' which Amazon's management did, Tom
Kochan, a professor of management at MIT, told Insider"

[Link](https://www.businessinsider.com/amazon-union-vote-bessemer-alabama-labor-law-experts-takeaways-2021-4)

---

Too bad the Amazon unionization effort failed.. But 'ppl have spoken'
is the wrong conclusion to draw here.. The system was favoring the
employer. Change of labor laws needed? AMZN clearly was the better
closer.

---

"Efficacy of a coronavirus vaccine from Sinovac has been found to be as
low as 50.4 percent by researchers"

---

It's possible GDELT missed something of course, it is an automated algo

---

Code

Flip the actors u can see the build-up (code 154) both ways.

Code 154 is "mobilization or increase of armed forces"

```python
import pandas as pd, zipfile
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth',-1)

dates = ['0331','0401'] # add more dates here w files

for dt in dates:
    with zipfile.ZipFile('gdelt/2021%s.export.CSV.zip' % dt, 'r') as z:
         df = pd.read_csv(z.open('2021%s.export.CSV' % dt),sep='\t',header=None)
    print (len(df.columns))
    urls = df[57]
    cols = ['GlobalEventID', 'Day', 'MonthYear', 'Year', 'FractionDate',\
           'Actor1Code', 'Actor1Name', 'Actor1CountryCode', 'Actor1KnownGroupCode',\
           'Actor1EthnicCode', 'Actor1Religion1Code', 'Actor1Religion2Code',\
           'Actor1Type1Code', 'Actor1Type2Code', 'Actor1Type3Code', \
           'Actor2Code', 'Actor2Name', 'Actor2CountryCode', 'Actor2KnownGroupCode',
           'Actor2EthnicCode', 'Actor2Religion1Code', 'Actor2Religion2Code',
           'Actor2Type1Code', 'Actor2Type2Code', 'Actor2Type3Code', \
           'IsRootEvent','EventCode', 'EventBaseCode']
    df2 = df[range(len(cols))]
    df2.columns = cols

    flt = (df2.EventCode==154) & (df2.Actor1Code=='RUS') & (df2.Actor2Code=='UKR')
    print (dt)
    df3 = df2[flt]
    if not df3.empty:
        print (df3[['Actor1Code','Actor2Code','EventCode','EventBaseCode']])
        url3 = urls[flt]
        print (url3)
```

---

I looked at GDELT [event files](http://data.gdeltproject.org/events/),
going back go March 1st; did not find any initial Ukraine
movement. The first time any build-up is reported in the region, in
the 1/3-1/4 timeframe, was April 1, by RUS. One of the news links
parsed by GDELT is [here](https://www.euractiv.com/section/global-europe/news/top-us-general-calls-russia-ukraine-amid-reported-moscow-troop-buildup/).

"In terms of the latest escalation, who is responsible? Who deployed
its military first?  Russia or Ukraine?"

---

Maybe the mechanical vs wild animal theme in scifi movies is a
throwback to that feeling, way of coping with insane recent
advances. It was mysterious to be scared of the beast? Now smaller
ones are causing more damage.


---

Largest whale in length, 30 meters. Aircraft carrier, over 300 meters
in length.  The masses dont even compare. Whale has no chance. Its
funny from a time where humans were afraid of monsters at sea, now we
have monsters of our own.

"Could a whale damage a ship? Like an aircraft carrier?"

---

Replacing lead pipes is a good thing sure.. Wasnt that the problem in
Flint Michigan?

---

"US senators on Thursday unveiled broad legislation on China that would
step up pressure over Beijing's alleged theft of intellectual property
and solidify US ties with Taiwan.

In a rare bipartisan initiative in the polarized Congress, the top
Democrat and Republican on the Senate Foreign Relations Committee
together presented the Strategic Competition Act which aims to govern
the fraught US relationship with Beijing.

'The United States government must be clear-eyed and sober about
Beijing's intentions and actions, and calibrate our policy and
strategy accordingly,' said Senator Bob Menendez, the Democrat who
leads the committee"

[Link](https://www.barrons.com/news/us-bill-to-pressure-china-on-trade-and-rights-back-taiwan-01617915009?tesla=y)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">A record-breaking commercial-scale <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> plane has taken off in the UK, with more set to join it soon. <a href="https://twitter.com/hashtag/HydrogenNow?src=hash&amp;ref_src=twsrc%5Etfw">#HydrogenNow</a> <a href="https://twitter.com/hashtag/Aviation?src=hash&amp;ref_src=twsrc%5Etfw">#Aviation</a> <a href="https://twitter.com/BBC_Future?ref_src=twsrc%5Etfw">@BBC_Future</a> <a href="https://t.co/idfW3qWXod">https://t.co/idfW3qWXod</a></p>&mdash; Hydrogen Europe (@H2Europe) <a href="https://twitter.com/H2Europe/status/1380784367354658816?ref_src=twsrc%5Etfw">April 10, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"Greece, Israel Seal $1.6 Billion Defense Deal"

[Link](https://www.voanews.com/europe/greece-israel-seal-16-billion-defense-deal)

---

Gobble gobble, though not a great power, displays some of the same
behaviours lately.. Kabuki theather power, throwing its little kabuki
tantrum on the way down.

---

Beckley: "Historically, when fast-growing great powers slow down, they
do not mellow out. Instead, they become more repressive at home and
aggressive abroad. They crack down on domestic dissent and expand
overseas to find new sources of wealth, rally citizens around the
ruling regime, and deter foreign rivals from exploiting their economic
problems. China is already on this path—as its growth slows, it is
repressing freedom in the mainland and in Hong Kong, ramping up
pressure on Taiwan, colonizing the South China Sea, building the
largest navy in the world, and buying assets and building ports all
over the world"

---

ABC Oz Planet America is pretty good. They catch some interesting angles.

---

Reps started culling out some unwanted leaders for 2024 already? Gaetz
is hit pretty bad, nobody is coming to his defense. Clearing the path
for Ted? Pompeo?

---

Nincompoop? 😶

---

The Spirit of '75 (feat. Mustafa Akbar) \#music

[Link](https://youtu.be/doFad9LdZ_k)

---

C its possible to advocate for opportunities for everyone wout
resorting to cuck

---

sounds like discrimination, likely an oversight, but not cool

DW: "Study unveils Facebook gender bias in job ads A new study examined
Facebook's ad-delivery algorithms and found that some ads were
directed to a particular gender "beyond what can be legally justified"
by differences in job qualifications"

---


