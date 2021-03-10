# Week 10

If we can fix the physical goods side by truly substituting knowledge
for atoms, building everything on demand, and the energy side with
renewable fuels (that relies on common ingredients), we could have a
route.. Absent these, might have to change incentives to encourage
less growth.

---

Govs may want it bcz it means more taxes in the future, easing debt
repayment. Companies want growth bcz their investors need returns. All
that cld be fine but even with services dominating the economy, more
growth still means more shit. As in **physical shit**, goods and
materials, leading to resource extraction, a plundered planet. See
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

Lots of doubters showcased, yes. Unfort'ly have to follow such
characters because the landscape is littered with dipshits in all
walks of sci/tech blowing smoke up everyone's ass.

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

1989, 2008 as beginning/end of certain ideologies? World is looking
for a new system, in a funk.

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

There was decrease soon after 1989, the fall of the Berlin Wall. Kept
on going down past 9/11, past the invasion of Iraq.. But, I guess bcz
by 2008-10 Iraq became FUBAR (one example), vio picked up. Started to
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

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Saudi Arabia is building a $5 billion hydrogen plant powered entirely by sun and wind to beat out China and Europe <a href="https://t.co/5RyXbhjrKG">https://t.co/5RyXbhjrKG</a></p>&mdash; Bloomberg (@business) <a href="https://twitter.com/business/status/1368542709238095873?ref_src=twsrc%5Etfw">March 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

This is how important the legal system is. I bet UEA set up this
English based seperate court system to pull in visitors, investment.

"[UAE] DIFC Courts began operations in 2006 and was established to
manage cases relating to companies licensed by the Dubai International
Financial Centre (DIFC) Free Zone. DIFC Courts is an English language
court based on those operating within the UK’s common law
system. Originally set up to manage cases for DIFC companies only,
today any company in the UAE can opt-in to use DIFC Courts for legal
matters; all that is required is a clause in a new contract or an
amendment to an existing one. Differing to onshore courts, DIFC Courts
hears cases in English"

[Link](https://bcbuae.com/2018/02/05/uaes-commercial-zones-legal-jurisdictions-part-two/)

---

WSJ: "Study of Aggressive Covid-19 Strain in Brazil Suggests Limits of China Vaccine"

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Blue Vs. Green Hydrogen: Which Will The Market Choose? via <a href="https://twitter.com/Forbes?ref_src=twsrc%5Etfw">@forbes</a> <a href="https://t.co/Jjl3xyd8Qh">https://t.co/Jjl3xyd8Qh</a></p>&mdash; Asia-Pacific Hydrogen Association (@APAC_Hydrogen) <a href="https://twitter.com/APAC_Hydrogen/status/1368416220647727104?ref_src=twsrc%5Etfw">March 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

It is somehow pleasant seeing Rob dealing with a random jagoff tuber. 

---

🤣 🤣 Robitaille answers a tuber claim

Claim
<iframe height="100" width="200" src="https://www.youtube.com/embed/JRrTvP95kf4?start=944&end=985" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
Answer
<iframe height="100" width="200" src="https://www.youtube.com/embed/JRrTvP95kf4?start=1152&end=1310" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

"@nickmartin

Replying to @OliviaMesser

I experienced something similar at the beginning of a period of being
uninsured. CVS wanted to charge 750D for a month's supply of a
medication. Thankfully I didn't pay, and I quickly learned that
Walmart sold it for $25. Mom and pop pharmacies are usually good about
this too"

---

"@OliviaMesser

Sans insurance for a few days bc paperwork issue. Pharmacy charged me
$500 for a month’s worth of medicine I *have* to take. With GoodRX the
same pharmacy would fill the same amount for 13ish. I HATE this. WHICH
IS IT?? If it’s not worth $500, WHY are you asking me to pay that

This country’s healthcare system is so broken, and sometimes you’re
randomly presented with irrefutable and absurd evidence of how
arbitrary the dollar amounts assigned to meds and services are. It
makes me want to scream"

---

*Ride Along* 👍. That part where IC corners a guy and he gets scared
starts singing "mamasay mamasa mamakusa". It was funny..

---

I see.. Whether The Line picks up or not, the area oppo to Sharm El
Sheik can still generate some returns.

<iframe width="340" src="https://www.youtube.com/embed/41sgRP0G6y4?start=174&end=313" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

I started patching up MIT Strang lecs.. this is some next level shit

---

TechCrunch: "Hyzon Motors' hydrogen fuel ambitions include two US factories"

---

"HyPoint has unveiled the first operable prototype version of its turbo
air-cooled hydrogen fuel cell system ... Testing has shown that
HyPoint’s turbo air-cooled hydrogen fuel cell system will be able to
achieve up to 2,000 watts per kilogram of specific power. Dr. Alex
Ivanenko, founder and CEO of HyPoint, told Avionics International that
their technology has drawn interest from a wide range of aircraft
developers"

[Link](https://www.aviationtoday.com/2021/03/02/hypoint-ceo-talks-new-hydrogen-fuel-cell-operable-prototype-electric-aircraft/)

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

Here is an O'Neill Cylinder. Look at that thing turn.. Oh yeah baby! Lookit!

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
archaic. In the future more journalists will do what I just did below;
looking for legit, well curated datasets, and run analysis on them.

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

Let's check 2020. I am going to use Uppsala Conflict [datasets](https://ucdp.uu.se/downloads/),
montly IS activity plot,


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

Monthly occurence of attacks globally hover around 30.

---

Was it that high? 🤔 Plus what's missing here is context, what
is the trend, and how many deaths were there, etc.

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
