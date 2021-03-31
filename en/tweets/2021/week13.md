# Week 13

France 24: "Glimpse of a post-Covid future? Masks ditched as Gibraltar
nears total vaccination... Signs reminding people to wear a face mask
in public were taken down by workmen in Gibraltar on Sunday in the
latest indication that life is slowly returning to something close to
normal in the small British overseas territory. Gibraltar is one of
the first places in the world to have vaccinated virtually its entire
adult population against Covid-19 and may now offer a clue as to how
other nations will fare when their own populations are inoculated"

---

Peter Beck of Rocketlab on Venus. RocketLab has delivered successful
payloads to space, solid outfit. 

[Link](https://youtu.be/SjuxmH7eWHc?t=1581)

---

WSJ: "WHO Report Into Covid-19 Origins Leaves Key Questions
Unanswered... A World Health Organization-led team investigating the
origins of the Covid-19 pandemic found that data examined during a
recent mission to China was insufficient to answer critical questions
as to when, where and how the virus began spreading"

---

"Stanford Scientists Reverse Engineer Moderna Vaccine, Post Code on Github"

[Link](https://www.vice.com/amp/en/article/7k9gya/stanford-scientists-reverse-engineer-moderna-vaccine-post-code-on-github)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">📢The UK is planning to have its first hydrogen town by 2030! The fuel cell sector is looking forward.<br>✅No CO2 emissions<br>✅High efficiencies<br>✅Empowered local communities<br>➡️<a href="https://t.co/ifIsrdNk54">https://t.co/ifIsrdNk54</a> <a href="https://t.co/KMD7X9bTn1">pic.twitter.com/KMD7X9bTn1</a></p>&mdash; PACE (@PACEmCHP) <a href="https://twitter.com/PACEmCHP/status/1376496265337450496?ref_src=twsrc%5Etfw">March 29, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I don&#39;t know what people expect here. There is no co-ordinated state or global effort that has any control over these vaccines, and no serious non marketized alternative. This is HOW the market delivers--by stripping state assets. <a href="https://t.co/Va7lEpeXAC">https://t.co/Va7lEpeXAC</a></p>&mdash; Stephen Buranyi (@stephenburanyi) <a href="https://twitter.com/stephenburanyi/status/1364179702831792134?ref_src=twsrc%5Etfw">February 23, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

My approach allows for it..  We cant rule out schools tho, or "that
other place where kids can go to outside their home", or whatever it
may be called in the future, bcz it doubles as a daycare center for
many working parents (the pandemic made this clear), and especially in
poorer neighborhoods, if there is trouble at home, etc it can work as
a sanctuary of sorts, kids go there, to a well-known place where other
adults are present.

"But a lot of new ed approaches are around homeschooling, why aren't
you for homeschooling?"

---

"@MobilityPragma

Hello @villedenice !!! 😎🌞Le vélo à #hydrogène Alpha de passage sur
la promenade des anglais. #baiedesanges #nice #bikelife #h2bike #h2now
@provencealpescotedazur à Nice Ville - Promenade des Anglais"

<img width="340" src="https://pbs.twimg.com/media/ExqAP64WQAkjHK_?format=jpg&name=small"/>

---

Huge actv spike in DR Congo, Mozambique. Lot of deaths in Mali, MSA is
French aligned right?

---

UCDP Feb 2021 data is out. Looking at IS activity. 

```python
import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv('https://ucdp.uu.se/downloads/candidateged/GEDEvent_v21_0_2.csv')
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_colwidth', 20)
df1 = df[(df['side_a'] == 'IS' )]
g = df1[['side_b','deaths_b','country']].\
    groupby(['side_b','country']).\
    agg({'country':'count', 'deaths_b': 'sum'})
g.columns = ['incidents','deaths']    
print (g)
```

```text
                                       incidents  deaths
side_b               country                            
Civilians            Afghanistan               3       0
                     Burkina Faso              6       0
                     DR Congo (Zaire)         13       0
                     Egypt                     1       0
                     Mozambique                7       0
                     Nigeria                   1       0
                     Syria                     5       0
JNIM                 Burkina Faso              3       4
Jama'atu Ahlis Su... Niger                     1       0
                     Nigeria                   1       3
MSA                  Mali                      1      10
SDF                  Syria                     9       9
Taleban              Pakistan                  1       1
Yan Gora             Nigeria                   3       0
```

---

I realized Seshat data file had some columns "scaled", so they dont
reflect the raw value. Where is the raw value? I find the original,
which has column values spread out to multiple *rows*. Woha. Scrubbing
now.

---

"@mercoglianos

[Via @Splash_247] have the word-ship is fully afloat & free to
navigate. Her engine is available but they will not use
it. \#Evergiven will be towed into the Lake to open up the lane & get
traffic moving. They will clear the lake & then livestock carriers"

---

"@man_integrated

Pertamina (Indonesia's state-owned oil company) signed a deal with CPC
[Taiwan's state-owned oil and petrochemical company] in June 2020 to
double this refinery's capacity... This marks two of Taiwan's most
strategically important companies [along with Evergreen] to be hit in
the past five days.

'@disclosetv JUST IN - Massive explosion at the Balongan oil refinery in Indonesia'"

---

Hey I'm all into that contra jive, but this one is little out of whack.

"[Aero] lift is generated due to Coanda effect, not pressure
differential as a consequence of Bernoulli's Theorem"

---

Walk before you can run. Glide before you.. motor fly?

"Orville and Wilbur Wright integrated and safely flew the first
successful, controlled, powered airplane. The process they used was
one of progressive design and was successful to a large degree because
of their experience with gliders. Previous attempts at powered flight
were unsuccessful because the inventors tried to fly first with power
before the subtleties of control were addressed. The Wrights instead
first learned how to fly using gliders as tools to solve the
challenges of actutator control, and then added power to invent the
airplane"

[Link](https://journals.sfu.ca/ts/index.php/ts/article/viewFile/247/230)

---

Dude can rearrange shit at a molecular level.. It's not even fair.

---

[Doh!](https://pbs.twimg.com/media/ExjsLenXEAISkRY?format=jpg&name=small)

---

Who is the baddest mofo in Marvel Uni? Warlock? Molecule Man?

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Are for-profit scientific publishers good for science? No. Well, don’t they provide some useful services to scientists? No. Is there anything redeemable about them? Still, no. 🤷‍♂️ <a href="https://t.co/UVAobgDptY">https://t.co/UVAobgDptY</a></p>&mdash; Aaron Clauset (@aaronclauset) <a href="https://twitter.com/aaronclauset/status/1369673135176314883?ref_src=twsrc%5Etfw">March 10, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"@BDMurray

Russia definitely *wants* to be a critical force in Myanmar, and
elsewhere in ASEAN. Such a status would certainly be welcomed in the
region as a counterbalance against China and the U.S. But, as I wrote
last summer, it has trouble delivering"

---

"Flipping the classroom" decsription doesnt do justice.. I dont want
to flip the classroom around the same avg teacher, but flip it around
the bestest, for every subj (thr prerec lectures). 

---

We like seeing people toiling away, actively, busily 'doing
stuff'. Our current view of work is faulty. The grader position in my
ed system will admittedly not be too 'busy', simply sitting around in
the study halls, answering the occas question. But combined with
pre-recorded delivery of lectures to all kids, this system will create
better results compared to now where the teacher is "busily"
lecturing, "doing stuff" all the time.

---

The answer is "historical statistics" apparently... It's true, a lot
of internal dev stats cld be gleaned from wars.

---

Ha good title

"What Studying War Is Good for"

---

"@tomgara

An amazing little subplot in the Suez thing is that Egyptian media,
which basically reached North Korean levels in recent years, has been
reporting that the problem was solved and done with days ago"

---
