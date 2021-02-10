# Week 6

"BioNTech-Pfizer COVID vaccine effective against 2 variants"

---

We cld parse DJT statements all day long, but the moment you question
to legitimacy of an election, and say "fight" somewhere in speech,
that is opening the door to violence. People are not smart on pol
nuance (completely normal), so leadership carries responsibility.

"Trump impeachment: Supporters rioted 'of their own accord'"

---

The H2 power paste sounds like a fantastic innovation.. shows
potential rewards for betting on the right tech; if car company made
investm in fuel cells, they cld still get ROI from that after a new
delivery method is discovered. Power paste is just another way of
providing H2 gas into the FC, replacing H2 tanks, and everything else
stays the same. Indiv parts get innnovated on seperately = stronger
overall architecture.

---

"Researchers at the Fraunhofer Institute for Manufacturing Technology
and Advanced Materials IFAM in Dresden have developed a paste for
hydrogen storage. The institute is calling the mass 'power paste'.

The researchers also claim their paste to offer high energy densities
and be suitable for all vehicles from electric scooters to
cars. According to Fraunhofer IFAM, the power paste, based on the
solid magnesium hydride, should allow hydrogen to be chemically stored
at room temperature and ambient pressure and rereleased as
required. Since the power paste only decomposes above about 250
degrees Celsius, this works without any issues even if, for example, a
scooter equipped with the paste is left in the summer sun for hours.

The storage paste’s starting material is only magnesium in powder
form, which is a very common element. At 350 degrees Celsius and five
to six times atmospheric pressure, this is reacted with hydrogen to
form magnesium hydride. The power paste is then produced with ester
and metal salt.

<img width="340" src="https://pbs.twimg.com/media/EtrzYmdWYAASk1-?format=png&name=small"/>

The power paste replaces the cylindrical pressure tank used in fuel
cell cars and buses. Therefore, the institute says that this solution
is suitable for hydrogen drives in smaller vehicles in cases where a
pressure tank would be difficult to implement.

According to the Fraunhofer researchers, the refuelling process is
straightforward. Instead of driving to a filling station, the scooter
driver changes a cartridge and fills tap water into a water tank. In
the vehicle itself, the paste is pressed out of the cartridge and
mixed with a precisely measured amount of water, depending on the
required power. This reaction produces gaseous hydrogen, which can
then be converted into electricity for the electric motor.

Only half of the hydrogen comes from the power paste, the other half
from the water in the reaction. 'The energy storage density of the
power paste is therefore enormous: it is much higher than that of a
700 bar pressure tank,' says Marcus Vogt, a scientist at Fraunhofer
IFAM. 'Compared to batteries, it even has ten times the energy storage
density.' The Fraunhofer scientists even say that the driver should
achieve a similar range with the power paste extrapolated to a car as
they would with the same amount of petrol, if not greater"

[Link](https://www.electrive.com/2021/02/02/fraunhofer-develops-hydrogen-storage-paste/)

---

I dont like these funky math tricks around carbon consumption. I fly
on a polluting plane, but plant a tree, voila I am net zero
emission. This is a hard to manage process. Actors will cheat,
regulation will be hard. We need to solve emissions at the
source. Make flying green, then there is no need to balance anything
anywhere.

---

Dog Perignon 🤣

Chew toy that looks like a champaign bottle... Very good

<img width="150" src="https://pbs.twimg.com/media/Ett3gfBWQAQB-f1?format=jpg&name=240x240"/>

---

Vaccine 'jab' of UK english.. always makes me think someone got
stabbed.

But then vaccine 'shot' is similarly martial.

Americans like guns, Brits knives? 

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Many countries including Canada, France, Germany, Norway and more have future plans to rollout green hydrogen production. Learn more in <a href="https://twitter.com/POWERmagazine?ref_src=twsrc%5Etfw">@POWERmagazine</a>. <a href="https://twitter.com/hashtag/greenhydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#greenhydrogen</a> <a href="https://twitter.com/hashtag/hydrogenproduction?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogenproduction</a> <a href="https://t.co/pVa0MGMiij">https://t.co/pVa0MGMiij</a></p>&mdash; SunHydrogen (@SunHydrogen) <a href="https://twitter.com/SunHydrogen/status/1358795324748357634?ref_src=twsrc%5Etfw">February 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---


"@h2_view

.. British magazine #GQ has named the #hydrogen-powered #Hyundai #Nexo
among its fastest, sleekest and most innovative rubber-burners on #UK
roads and racetracks in 2021"

---

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

Quick doomsday check, if there r any spikes in earthquakes globally

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

If grouped on, wonder how Top 10 wld look.. could show interesting
patterns... a weekly report maybe?

---

Sample output from ICEWS. 

```python
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
df = pd.read_csv("20200719-icews-events.tab", sep="\t")
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

<blockquote class="twitter-tweet"><p lang="und" dir="ltr">Via <a href="https://twitter.com/gazettedotcom?ref_src=twsrc%5Etfw">@gazettedotcom</a><a href="https://t.co/J3qyp16So2">https://t.co/J3qyp16So2</a></p>&mdash; SunHydrogen (@SunHydrogen) <a href="https://twitter.com/SunHydrogen/status/1358130409335377922?ref_src=twsrc%5Etfw">February 6, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"Missile purchase prepares [Oz Defence Force] for Taiwan
contingency.. This week the government announced that it will invest
$1 billion in outfitting the Navy with new missile capabilities to
‘project and maintain sea control’ as tensions over Taiwan heat
up.. In a press release, Minister for Defence Linda Reynolds said the
[Royal Oz Navy] will get 'leading-edge long-range anti-ship missiles,
extended range surface-to-air missiles, advanced light weight
torpedoes, and maritime land strike capabilities with ranges in excess
of 370 kilometres for anti-ship and surface-to-air missiles, and 1,500
kilometres for maritime land strike missiles.'"

[Link](https://www.australiandefence.com.au/news/missile-purchase-prepares-adf-for-taiwan-contingency)

---

NatSec Adv Sullivan: "We’re not about trying to make the world safe
for multinational investment; we’re about creating jobs and raising
wages here in the United States.  So our priority is not to get access
for Goldman Sachs in China; our priority is to make sure that we are
dealing with China’s trade abuses that are harming American jobs and
American workers in the United States"

[Link](https://www.whitehouse.gov/briefing-room/press-briefings/2021/02/04/press-briefing-by-press-secretary-jen-psaki-and-national-security-advisor-jake-sullivan-february-4-2021/)

---

[Ph.D. is about depth](2011/10/phd-graduate-studies.md), not breadth.
The joke is "a PhD knows more and more about less and less until he
knows everything about nothing.". But then, there is something of
everything in that nothing :), so you'll have learned a lot, at the
very least develop brain muscles for that depth. It is also about
adding something new to world knowledge, not merely knowing more, its
not "undergrad times 10".

"I want to get a PhD. Should I?"

---

From [The Mathematical Reality Why Space and Time are an Illusion](https://www.amazon.com/Mathematical-Reality-Space-Time-Illusion/dp/B0849ZXQB1):
"As early as the 1930s, the Dutch physicist and close friend of
Einstein, Paul Ehrenfest, wondered why the wave functions for matter
(complex numbers) and light (vector fields) were mathematically so
different. The importance of this profound question is still
underestimated today. If one follows the mission to explain natural
phenomena in a unified picture, light and matter must be contained in
a single formalism. This means that there has to be a mathematical
object that on the one hand, must be a little more complicated than
vectors and complex numbers, but on the other hand must incorporate
their properties...

Hamilton..  one of the most brilliant mathematicians of all time
.. started to study complex numbers. If it was possible to define a
multiplication in two dimensions in such an amazing way, was it also
possible in three dimensions?... On 16 October 1843, while walking
along the Royal Canal in Dublin, Hamilton finally came up with the
answer. In three dimensions it was indeed impossible; but at that
moment, he realized that the tricky multiplication of complex numbers
could be transferred to a four-dimensional number system called
quaternions that had three imaginary units $i$, $j$, $k$ instead of
just one $i$. Whether Hamilton could already have imagined the
fascinating rotations that occur in this number system, we do not
know. In any case, overjoyed at his idea, he carved the constituting
equations into a stone of a nearby bridge

$$
i^2 = k^2 = j^2 = i \cdot j \cdot k = -1
$$

... If we come back to the philosophical question of what mathematical
structure could potentially describe all physical phenomena,
quaternions are a strikingly simple possibility. Since they contain
both complex numbers and conventional vectors as a subset,
quaternions, in principle, can represent all the number systems
physicists have used in their description of the elementary phenomena
light and matter"

---

No, encouraging useless work just so people are employed is a
no-go. That might equal pollution, ppl doing weird shit bcz they are
small entities, hard to regulate in the many.

---

Then maybe there'll be less [stubble burning](https://www.dw.com/en/india-pollution-how-a-farming-revolution-could-solve-stubble-burning/a-51166417)
and less smoke blanketing the capital city.

If fewer f-ing farmers implies less smoke, that option is a good option.

"New farm law will mean fewer farmers in India"

---

"AstraZeneca Vaccine Effective Against U.K. Variant in Trial"

---

One rotation can supply two households for a day. W-O-W

"'Back of envelope' calculation shows on a windy day the #HaliadeX 13
MW #offshorewind turbine produces 24hrs x 13,000kW = 312,000 kWh. In
one day the rotor turns c.11,000 times, yielding 27.8 kWh per
rotation. Double the amount of energy that a typical UK household
requires daily"

---

"A 4-day working week might be edging closer... With Spain set to test
a four-day working week in response to the pandemic, experts have said
it could signify a more permanent shift in attitudes to work"

---

CNBC: "GameStop mania may not have been the retail trader rebellion it
was perceived to be, data shows"

---

"US calls out human rights abuses in China. While talking to Beijing,
US top diplomat Antony Blinken pressed for accountability on human
rights abuses in Xinjiang, Tibet and Hong Kong"

---

"@ossoff

And with Vice President @KamalaHarris casting the crucial tie-breaking
vote, at 5:30am after 14 hours of debate, the Senate has passed a $1.9
trillion budget for COVID relief. Georgia voters made this possible"

---


"@josheidelson 

Democrats including @BobbyScott, @PattyMurray, and @chuckschumer today
re-introduced the PRO Act, a sweeping labor law overhaul that aims to
undo much of Taft-Hartley and the subsequent rulings and
transformations that together devastated U.S. unions"

---

"Airbus proposes detachable hydrogen propulsion pods for
aircraft... Each of the six pods along the wings of the ZEROe concept
includes a liquid hydrogen tank, a cooling system, a fuel cell, power
electronics, electric motors, an eight-bladed lightweight composite
propeller and all the necessary auxilliary equipment to run it as a
standalone propulsion unit"

[Link](https://newatlas.com/aircraft/airbus-detachable-hydrogen-propulsion-pods/)

---

<blockquote width="300" class="twitter-tweet"><p lang="en" dir="ltr">my cat has become OBSESSED with sitting in on my zoom calls and has now perfected the art of glaring straight down the camera <a href="https://t.co/RbFSQSlkV6">pic.twitter.com/RbFSQSlkV6</a></p>&mdash; Abby Tomlinson (@twcuddleston) <a href="https://twitter.com/twcuddleston/status/1352664361517641733?ref_src=twsrc%5Etfw">January 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

They used to say about Oliver Stone that in his movies, it's like "he
is standing by your ear with a megaphone and yelling at you what to
think". If those crits saw these bizarre Trek shows they'd never
complain about Oliver Stone ever again. In comparison OS is the
motherbleeping grand bleeping master of subtelty.

---

The gentlest crit directed at such shows from our side has been "they
are not painting an optimistic future". I dont think that does justice
how badly these shows suck. The backdrop of *Firefly* was pretty drab
but everyone liked its characters, stories. No these weird shows lean
on an artificial message to insert agenda.

---

From EW, daam bro

---

Yep, that's the guy, co-destroyed Trek

"The Silence of the Lambs becomes another bland procedural... *Clarice*'s
other co-creator is Alex Kurtzman, a practiced IP hack known for
Transformers, various Star Treks, a failed Mummy, and the worst
Spider-Man. That's a lot of money made off other people's
originality. Can't we institute some kind of limit on this stuff, like
maybe a person can only work in four pre-existing universes per
decade?"

[Link](https://ew.com/tv/tv-reviews/clarice-review/)

---

Obviously ppl blame Renzi for crashing the coalition; but what did
this guy not get that he wanted? In repr democracies with coalitions,
small parties like his can be kingmakers. FDP played that role in
Germany for years.

---

You can still do journalism wout being physically at a place, all the
time; just watched a Renzi interview, Channel 4 did it remote, it was
good.

---

The deficit / thrift decision is a political one, so by definition it
cannot be de-politicized, taken out of the realm of discussions,
turned into some kind of TINA law. Parallels here to Bitcoin "not
printing money", depoliticizing that decision, disqualifying itself as
a national / global fiat currency.

"Should austerity be embedded in European law?"

---
