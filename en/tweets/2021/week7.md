# Week 7

<iframe width="340" src="https://www.youtube.com/embed/kir0DI9AnOc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Wind turbine freezing was not the main factor then.. 

"@GregAbbott_TX

The Texas power grid has not been compromised.

The ability of some companies that generate the power has been frozen. 

This includes the natural gas & coal generators.

They are working to get generation back on line"

---

Dude. Lumber futures..

[Link](https://mobile.twitter.com/crampell/status/1361699251827470338)

---

Business Insider: "This hydrogen paste has a similar range to that of
gasoline and could revolutionize the transport industry"

[Link](https://www.businessinsider.com/car-bike-tesla-amazon-gates-bezos-climate-change-fuel-drone-2021-2)

---

"@byHeatherLong

26 states had revenue declines last year The toll was felt by both Dem
& Repub-led states Gov't jobs cuts have occurred in nearly every state

26% NH

17% Colorado

14% Ohio

13% Wisconsin

12% Michigan

12% Maine

12% Kentucky"

---

"Say Hy to the home of the future"

[Link](https://cadentgas.com/future-of-gas/projects/hydrogen-home)

---

Name any city and that'll be plotted too. I can do this all
day.. let's go buddy.

---

[Data](https://www.ncdc.noaa.gov/cag/city/time-series)

```python
import pandas as pd

df = pd.read_csv('austin-feb.csv')
df.Date = pd.to_datetime(df.Date,format="%Y%m")
df = df.set_index('Date')
df.Value.plot()
df['Trend'] = df.Value.rolling(window=30).mean()
df['Trend'] = df['Trend'].fillna(method='backfill')
df.Trend.plot()
plt.savefig('austin-feb.png')
```

<img width="340" src="https://pbs.twimg.com/media/EuaOFq7XYAIWnP1?format=png&name=small"/>

---

Nice try genius. See above. Plotted February averages for Austin, TX
per year, since 1940. The trend is up.

"Aw man the weather is cold in TX, that means no glob warming"

---

Tax havens: ... Ankara must share its banking data with the Member
States of the European Union by the end of June, otherwise it will be
placed on a “black list”.

[Link](https://twitter.com/lemondefr/status/1361627449050738699)

---

"@StateDeptSpox

The Houthis’ assault on Marib shows they are not committed to peace or
to ending a war afflicting the people of Yemen"

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">FuelCell Energy’s baseload power solutions deliver grid reliability with efficient and clean energy in the most extreme weather conditions. No wind, no sun, no problem. FuelCell Energy, always on. Stay powered. Stay warm. Stay safe. <a href="https://twitter.com/ERCOT_ISO?ref_src=twsrc%5Etfw">@ERCOT_ISO</a> <a href="https://t.co/bcUxkClecA">https://t.co/bcUxkClecA</a></p>&mdash; FuelCell Energy (@FuelCell_Energy) <a href="https://twitter.com/FuelCell_Energy/status/1361392708695261185?ref_src=twsrc%5Etfw">February 15, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

They apparently installed a remote access software so system could be
controlled from anywhere... But if something is accessible, connected
to the Net, hackers can also access 

---

They need to take that shite off the Internet.

"Hacker tries to poison water supply of Florida city"

---

If an area as large as Texas was covered with panels today, it would
[provide](2019/05/bezos-space-infrastructure.md#energy) ample energy,
twice of what is required actually, for the entire world.

Colonization fine for other things, not urgent for energy.

"If we run out of solar panel space on Earth, should we colonize space
for sunlight (through Stanford torus / O'Neil cylinder)"

---

<blockquote width="200" class="twitter-tweet"><p lang="en" dir="ltr">MUST-WATCH: Prime Minister <a href="https://twitter.com/BorisJohnson?ref_src=twsrc%5Etfw">@BorisJohnson</a> confirms UK will be &quot;putting a big bet on <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a>&quot; <a href="https://twitter.com/KwasiKwarteng?ref_src=twsrc%5Etfw">@KwasiKwarteng</a> <a href="https://twitter.com/annietrev?ref_src=twsrc%5Etfw">@annietrev</a> <a href="https://twitter.com/ASollowayUK?ref_src=twsrc%5Etfw">@ASollowayUK</a> <a href="https://twitter.com/grahamstuart?ref_src=twsrc%5Etfw">@grahamstuart</a> <a href="https://twitter.com/grantshapps?ref_src=twsrc%5Etfw">@grantshapps</a> <a href="https://twitter.com/redditchrachel?ref_src=twsrc%5Etfw">@redditchrachel</a> <a href="https://twitter.com/JacobYoungMP?ref_src=twsrc%5Etfw">@JacobYoungMP</a> <a href="https://twitter.com/Alex_Stafford?ref_src=twsrc%5Etfw">@Alex_Stafford</a> <a href="https://twitter.com/Jesse_Norman?ref_src=twsrc%5Etfw">@Jesse_Norman</a> <a href="https://twitter.com/samuelhall0?ref_src=twsrc%5Etfw">@samuelhall0</a> <a href="https://twitter.com/griffitha?ref_src=twsrc%5Etfw">@griffitha</a> <a href="https://twitter.com/GregClarkMP?ref_src=twsrc%5Etfw">@GregClarkMP</a> <a href="https://twitter.com/darrenpjones?ref_src=twsrc%5Etfw">@darrenpjones</a> <a href="https://t.co/jgKppXExeS">pic.twitter.com/jgKppXExeS</a></p>&mdash; UK Hydrogen Strategy Now (@UKHydrogenNow) <a href="https://twitter.com/UKHydrogenNow/status/1361033188932526082?ref_src=twsrc%5Etfw">February 14, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Any gov trusting their regulatory pizzazz should think again. VW
emission cheat happened under gov which wasnt known for widespread
incomp, done by a company from a country associated with *ordnung*.

---

As policy megawatt scale of this tech to be used at a few power plants
is fine, easy to regulate. End-user level, no. Much harder to control,
and if reg is flaunted, side effects would be severe.

End-user gets the renewable fuel, ditto for pipelines.

"Bloom also intends to complete work on technology capable of
capturing and extracting carbon from the emissions of its
natural-gas-powered fuel cells. The company is 'working very hard to
demonstrate' the ability to combine 'blue hydrogen' production, or
turning methane into hydrogen and capturing the carbon emissions, with
electricity production"

---

You have to watch for these tech types.. even when they're scaring
you, they might be selling you. Like 'be scared of AI, boo!', the
indirect message being it is *that good*. U see.. ? Then seque into
'i've got some of that same tech that for your house, for your
lawnmower'.. (but no worries i had my people write it, and im the
caution guy here, so be afraid for other stuff but not my shit, and
buy it, quick!)'. So sad.. and bunk.

---

Some earthquake plotting.. EQ of past 90 days, old to new is colored
light to dark, circle width is severity. The hope was maybe seeing a
geo progression of eq culminating with a final big one at the end..
Always looking for an angle here..

But Japan surely gets a lot of quakes

Retrieval [code](https://muratk3n.github.io/thirdwave/en/tweets/2021/util.py)

```python
import cartopy.crs as ccrs, cartopy, util
df = util.get_eq1()
fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_global()
ax.stock_img()
ax.coastlines()
ago = np.max(df.ago)-df.ago
s = np.power(3,df.mag)
ax.scatter(df.lon, df.lat, c=df.ago, \
           cmap=plt.cm.Reds, s=s, alpha=0.7,  \
	   transform=ccrs.PlateCarree())
ax.set_extent([94, 161, -10, 54], crs=ccrs.PlateCarree())
plt.savefig('eq.png')
```

<img width="340" src="https://pbs.twimg.com/media/EuU1vkRXUAEAAcx?format=jpg&name=small"/>

---

Forbes: "Hyzon, A Hydrogen Fuel Cell Truck Maker, In SPAC Deal Valued At $2.6 Billion"

---

"Hydrogen pumping stations are all over California and could be in the
Denver metro area by the end of this year. "

[Link](https://coloradosun.com/2021/02/11/when-is-clean-hydrogen-fuel-coming-for-colorado-cars-and-who-needs-to-get-ready/)

---

"The H-Factor" 👍

"In a grand, clean energy strategy published in mid-December, a brain
trust of cross-sector Canadian savants predicted that hydrogen-powered
locomotion—already nicknamed “hydrail”—would be ready for testing some
time about 2025, first in the form of yard switchers, short-leashed to
their refueling stations.

The very next day, Dec. 18, Canadian Pacific (CP) smashed that
timeline, and woke the North American rail industry"

[Link](https://www.railwayage.com/mechanical/locomotives/the-h-factor/)

---

Chick Korea RIP. Through him we got to know the craziest drummer ever,
[Dave Weckl](https://youtu.be/G5pmoSOE9CU?t=193). 

---

Dadamnphreaknoizphunk - "Chemical Funk" \#music

[Link](https://youtu.be/cAMuvTVChgI)

---

Some early Zack Snyder buzz, on the Justice League recut (?) (soon to
be released). In trailer has a character say "we live in a society",
apparently a meme now come alive, ppl loving it. Meme based on

[Link](https://youtu.be/LHhbdXCzt_A)

.. then became a Joker thing, now Zack has a char voice it

It's good.. keeping the fans happy. I hope new JL pans out.

---

Average surface elevation of Earth is 840 meters... most know "sea
level" is not actually zero elevation level.. The real bottom is at
the bottom of some the sea, ocean.. And there is a lota ocean!

We all live on mountain tops IOW

---

Newton, other early modern phy computed all the time. It's fine to go
off in an abstract direction but most phy teaching by default must be
enmeshed with computation.

---

Landau wrote some fantastic books. Id listen to him.

Landau: "There can be little argument that computation has become an
essential element in all areas of physics, be it via simulation,
symbolic manipulations, data manipulations, equipment
interfacing... [E]ven though the style of teaching and organization of
subjects being taught by physics departments have changed in recent
times, the actual content of the courses has been slow to incorporate
the new-found importance of computation. Yes, there are now speciality
courses and many textbooks in Computational Physics, but that is not
the same thing as incorporating computation into the very heart of a
modern physics curriculum so that the physics being taught today more
closely resembles the physics being done today"

---

Creator is [more likely](2015/04/god.md)

"Which is likely? Creator or not?"

---

By turning something into a process, we dont automatically remove "an
omnipotent creator" from the picture. Everyone likes the invention of
evolution. "God did not create the final thing, it was an evolutionary
process". Boom. Darwin is world famous.

"Well now let's apply that to the universe".. thought some? "God did
not make it happen, it started from a small seed, turned into
everything we see"

Except the creator isnt exactly removed from the picture, ie the most
enthusiastic supporters of Big Bang were and are the Clergy. That one
one focused, 'big' creational event must have jelled more with their
view of the creator.

But an omnipo being can bring stuff into existence, close to what they
are now, just as easily as some magic process that will evolve stuff
into as they are now. Dont want to assume either way, what I am saying
is opting for long-running process just to remove the Big Guy is not
necessarily more scientific.

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">We are pleased to join a public and corporate initiative for developing a <a href="https://twitter.com/hashtag/European?src=hash&amp;ref_src=twsrc%5Etfw">#European</a> hub for <a href="https://twitter.com/hashtag/green?src=hash&amp;ref_src=twsrc%5Etfw">#green</a> <a href="https://twitter.com/hashtag/fuels?src=hash&amp;ref_src=twsrc%5Etfw">#fuels</a> in Denmark’s Trekantomraadet. Everfuel’s <a href="https://twitter.com/hashtag/HySynergy?src=hash&amp;ref_src=twsrc%5Etfw">#HySynergy</a> project in Fredericia is a leading facility in the hub and planning for its Phase II expansion is well underway. <a href="https://t.co/LGJkh1BRyD">pic.twitter.com/LGJkh1BRyD</a></p>&mdash; Everfuel (@EverfuelEU) <a href="https://twitter.com/EverfuelEU/status/1360163685990338561?ref_src=twsrc%5Etfw">February 12, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

BBC: "China refused to hand over key data to the World Health
Organization (WHO) team investigating the origins of Covid-19, one of
its members has said"

---

Rep senators did not want the politicking trouble.. vote on evidence 
wld cause a convict. Now the spin can favor DJT

"Donald Trump cleared by US Senate of inciting Capitol riots"

---

Eartquake data retrival [code](../../2021/02/equakes.md)

---

Soon after prev quake tweet, > 7.0 shake. Two of them.

<img width="340" src="https://pbs.twimg.com/media/EuH6wbhXIAI-FQU?format=png&name=small"/>

---

Thanks to content like *The Mandalorian* I bet..

"Disney returns to profit as streaming business offsets theme park losses"

[Link](https://youtu.be/MVuBMhXhLks)

---

<blockquote class="twitter-tweet" data-conversation="none"><p lang="en" dir="ltr">💧 Develop 5GW of low carbon hydrogen production capacity by 2030<br><br>🏘️ First town powered entirely by hydrogen by 2030<br><br>Read the full plan 👉🏾 <a href="https://t.co/QCJdAjTjSd">https://t.co/QCJdAjTjSd</a> <a href="https://t.co/3Pp6AOQjXK">pic.twitter.com/3Pp6AOQjXK</a></p>&mdash; Kwasi Kwarteng (@KwasiKwarteng) <a href="https://twitter.com/KwasiKwarteng/status/1360189726075060224?ref_src=twsrc%5Etfw">February 12, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"You said this was indo. Smell like outdo" :)

---

Daam

"France wades into the South China Sea with a nuclear attack submarine"

---

Pute fussing over this one guy hurts gov legitimacy. Makes it
difficult for democracies to deal with RU.

"Russia says it's ready to end ties with the European Union"

---

There are so many things to compute. Fantastic models out there that
actually demo stuff, connected to physical processes. No need to wank
off to weirdo bullshit.

---

"India and China begin troop pull back from disputed border area"

---

They have to care, there is a whole song and dance around creation of
particles, formation of heavier elements since the "beginning of
time", if that story is poppycock, then a major part of their
assumption is wrong.

"Particle physicists dont care, they dont deal with that stuff"

---

Robitaille: "Cosmology is not science"

---

Jacobin: "It’s Long Past Time to Abolish the Filibuster"

---

We know fluids of similar attributes even in the same canister stick together.

It is fascinating to see this at a large scale. Oceanic scale. The
Atlantic and the Pacific [do not mix](https://thumbs.gfycat.com/FlawedEuphoricIndianringneckparakeet-max-1mb.gif).

---

I was told during their conflict, RU media played [this
video](https://i.imgur.com/1RBuOEV.gif?1) on a loop. That's
Shakasvili, the then GE president

---

Strategically it makes sense to want to be depended upon by bigger
players, as an energy exporter, so next time maybe they wont get their
ass kicked that swiftly by Russia.

---

Quick term expl; they will use water (hydro) in a dam, let through
turbines to generate power. Green. How to store that power? H2; again
green (and hydro).

---

Hydropower to hydrogen.. It rhymes! Go Georgia.

[Link](https://www.pv-magazine.com/2020/09/28/georgia-explores-green-hydrogen/)

---
