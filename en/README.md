# Tweets

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


