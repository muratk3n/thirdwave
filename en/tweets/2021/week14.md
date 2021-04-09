# Week 14

"@josheidelson

New: After years of mostly unsuccessful efforts, Uber, Lyft and peers
are poised to secure deals with major unions, just in time to help
defuse threats from the new Biden Administration"

---

"@hazergroupltd

A new report has detailed exactly how Australia’s current gas
regulations can be modernised to facilitate the future use of
hydrogen, biomethane and other potential future fuels"

[Link](http://ow.ly/uAHO50EhgEg)

---

Util code to report attacks on a specific country on a specific
month. Israel attacks Syria regularly it seems, w some hard kills
too.. Dam

```python
import pandas as pd

def country_attacked(mon, country):
   url = 'https://ucdp.uu.se/downloads/candidateged/GEDEvent_v21_0_%d.csv' % mon
   df = pd.read_csv(url)
   df1 = df[(df['side_b'] == 'Government of %s' % country)]
   g = df1[['side_a','deaths_b','side_b']].\
       groupby(['side_a','side_b']).\
       agg({'side_b':'count', 'deaths_b': 'sum'})
   g.columns = ['incidents','deaths']
   return g

print (country_attacked(1, 'Syria'))
print (country_attacked(2, 'Syria'))
```

```text
                                          incidents  deaths
side_a               side_b                                
Government of Israel Government of Syria          2      57
                                          incidents  deaths
side_a               side_b                                
Government of Israel Government of Syria          2       9
```
---

K.. as long as there is FCEV refueling next to these BEV chargers,
it's fine. BEVtards will get crushed in due course.

"US Senate Committee Introduces Clean Vehicle Charging
Legislation.. Earlier this week, a group of cross-party US senators
introduced the Securing America’s Clean Fuels Infrastructure Act (the
Act) to promote investments in clean vehicle infrastructure. The types
of infrastructure supported by the legislation include electric
vehicle charging stations and hydrogen refueling stations for fuel
cell vehicles"

[Link](https://www.natlawreview.com/article/us-senate-committee-introduces-clean-vehicle-charging-legislation)

---

"@SecYellen

By choosing to compete on taxes, we’ve neglected to compete on the
skill of our workers and the strength of our infrastructure. It’s a
self-defeating competition, and neither President Biden nor I are
interested in participating in it anymore.

We want to change the game"

---

Context? There was huge contraction due to pand so it shld not be
surprising to expect growth, just going back to where econ was
previously wld give major "growth".

"Record growth is expected this year, all around the world, w rates
not seen since 60s"

---

Good docu on Soviets, Russia

[Moscow's empire - rise and fall (2/4)](https://youtu.be/fSqMpZ5qhz0)

[Moscow's empire - rise and fall (3/4)](https://youtu.be/DCgDChqQZwk)

[Moscow's empire - rise and fall (4/4)](https://youtu.be/DCgDChqQZwk)

---

\#2021PortugalEU

"@H2Europe

\#GreenHydrogen is in our view one of the most promising techs to
eliminate hard to abate emissions from industrial & transport
sectors. - R. Mourinho Felix, VP, [European Inv Bank]"

---

2018 trade balance with CH top trading [partners](https://en.wikipedia.org/wiki/List_of_the_largest_trading_partners_of_China),
Neg for deficit, pos for surplus; so simple sum shld give the net received,
in billions,

```python
defc = [419.6,275.8,177.1,-28.6,206.1,-74.8,-112,-53.6,21.3,-12.7,\
       -29.9,52,1.5,-3.1,10.8,6.2,10.9,12.8,-13.4,16.4,-9.5]
np.sum(defc)
```

```text
Out[1]: 872.9
```

This USD u can spend, to buy the steel for those ghost cities.. But
export-dependency is just another dependency, it can get cut

---

"@gideonrachman

Soros-backed Central Europe University (CEU) is forced out of
Budapest. In its place comes Fudan University from China

'@eublogo \#Hungary will make 1 of the largest investments in the
higher education in decades financed by #China'"

---

"@gabriel_zucman

Global effective corporate income tax rate (all taxes included:
federal + state + foreign) of the largest US companies, as printed in
their 2020 annual reports:

- Amazon: 11.8%
- Apple: 14.4%
- Alphabet: 16.2%
- Facebook: 12.2%"

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Stellantis to deliver Europe&#39;s first series manufactured vehicles to European markets still this year:<a href="https://t.co/AUNs2Wny1b">https://t.co/AUNs2Wny1b</a><br>with large volume mass manufactured FC stacks in the coming years:<a href="https://t.co/IfZFpeDsxw">https://t.co/IfZFpeDsxw</a></p>&mdash; Reiner (@H2FCEV) <a href="https://twitter.com/H2FCEV/status/1379543235211714562?ref_src=twsrc%5Etfw">April 6, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

BTC specifically is badly designed but the next crypto cld remedy
that, fix the warts.

---

Maybe 1 cld see a crypto as holding a ticket that gets u into a
payment system, and the system is the value.. It is sorta circular
tho.. why would someone want to pay with a crypto? Bcz there are
others on it.. U get on it, then more might choose it for payments..

---

NR never runs out of ways of hitting this thing, BTC.

"@business

Bitcoin is a 'speculative self-fulfilling bubble' without any feature
of an asset, says Nouriel Roubini"

[Link](https://twitter.com/business/status/1362305213269442560)

---

"@ForeignAffairs

Nothing less than a bold new regime of domestic and international
taxes will save wealthy democracies and economies from the distortions
and dangers of rampant inequality, write @JosephEStiglitz,
@toddntucker, and @gabriel_zucman"

[Link](https://twitter.com/ForeignAffairs/status/1379470434551394313)

---

The solution is more / better speech. Meddling with section 230 wld
hamper it IMO.

"Disinfo Wars: Fixing the Media’s Fake News Problem A toxic focus on
misinformation has taken over the media ecosystem"

[Link](https://thereboot.com/disinfo-wars-fixing-the-medias-fake-news-problem/)

---

It's like arguing for the price of oil is high or low disregarding the
entire security apparatus to bring it into the market.

---

Water is more abundant and easy to process, jagoff. Even if water was
tad more harder to find, process, one is still needed more than the
other. Effin fin guy.. Sees only what he is allowed to "bet" on, that
is his world... 

Finance guy: "They say water is in nature and it's free. Diamonds also occur in
nature but they are not free"

---

The worst *Mission Impossible* is the second..? Nah man... it is
definitely the third. The Jar Jar one... It is objectively bad.

---

I have zero interest in approaches that cannot be scaled up. Works on
little toy examples in 2D not 3D? Pass.

---

Sounds like a culture code is in play here. French cultural tug of war
is between freedom and privelege. See [Rapaille](../../2014/06/the-culture-code.md#france).

"Covid: Paris police probe 'secret luxury dinner parties'"

---

"@BFMTV

Covid-19: seven in ten French people approve of the measures announced
by Emmanuel Macron, but almost half plan to break the new rules"

---

Unions [lost a lot of power](../../2019/08/focus-group-democracy.md) after
70s. The left sufered due to losing org structure and
leadership. Politicians themselves like that single contact to be
lobbied by, u cant have bunch of random ppl running around trying to
make policy, some kind of filter is necessary.

---

BTW the so-called Turkish coffee is actually Greek coffee, and that
itself is similar to a espresso, clearly all originating from
Aegy/Medi region; bunch of punks from distant whereever did not bring
it with them... Off-the-boat, or off-the-goat types like everyone else
who arrived and assimilated, picked these things up from their region.

---

Haha.. few Byzantian music samples below.. sounds awfullly like the
so-called "Turkish" art music, *sanat müziği*.

[Song 1](https://youtu.be/Da9FeNoFIm0),
[Song 2](https://youtu.be/kOhCB4RUc8U),
[Song 3](https://youtu.be/9_8aSrsTlCE),
[Song 4](https://youtu.be/lR4E7XrS9gI),
[Song 5](https://youtu.be/JSHiM36GmkY),
[Song 6](https://youtu.be/k_srWY7hddw)

---

Not surprisingly the same company caught cheating in an emission
scandal.. Biatch!

---

Hah

"@H2_MOBILITY_DE

3 out of the 5 biggest automakers worldwide have started serial
production of FCEVs. And yet Volkswagen AG still claims, that
\#hydrogen and \#fuelcells cells have 'no market maturity'"

---

All of a sudden I want to listen to Winger 😶

---

Bcz of Bono? That's funny 

"@meatheadsadie

Every - single - time I hear 'Mysterious Ways' by U2, my brain always
yells “BONERRRRR! BONERRRRRR! TIME FOR DINNERRRR!” like Beavis"

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">A high global minimum tax can change the face of globalization—by making its main winners (multinational companies) pay more in taxes, instead of them paying less and less<br><br>I&#39;m old enough to remember when this idea was deemed utopian, so could not be happier to see this! <a href="https://t.co/tDSZGEkLXt">pic.twitter.com/tDSZGEkLXt</a></p>&mdash; Gabriel Zucman (@gabriel_zucman) <a href="https://twitter.com/gabriel_zucman/status/1379115765194846209?ref_src=twsrc%5Etfw">April 5, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Words like "summation" can be misleading.. We are computing a "smart
sum", a sum that takes into account the upper boundary. Or a [smart
multiplication](https://betterexplained.com/articles/a-calculus-analogy-integrals-as-multiplication/).

---

How about the top part? They are not the same. Their upper boundary
changes as we go to right, depending on the function we are
integrating, so it's not simple sum.

Pay attn that integration result too, anything above first degree will
give you polynomial of deg higher and including than 2 = nonlinearity.

<img width="200" src="https://pbs.twimg.com/media/EyNNfspWEAQht1Y?format=jpg&name=small"/>

"If we think of integration of regular functions, they look like
addition of simple components, side by side, wout flipping"

---

"@mattblaze

Mark my words, this API decision from the Supreme Court is going to
lead straight to gangs of lawless youth roaming the streets and
downloading cars"

---

"Google v Oracle: Supreme Court declares Google's code copying fair"

---

New streaming device counts ppl in the room? Seriously.

"@Sean8UrSon

just got this frightening press email 

IT COUNTS PEOPLE IN THE ROOM SO IT CAN CHARGE PER PERSON??!?!

capitalism is fucking exhausting"

[Link](https://twitter.com/Sean8UrSon/status/1379156103557120001)

---

"Big Pharma did not save the day.. The industry is celebrating a great
PR win—but Big Pharma's iron grip on intellectual property could
hinder the achievement of worldwide protection against Covid-19"

[Link](https://www.prospectmagazine.co.uk/politics/big-pharma-covid-19-vaccine-uk-revenue-stephen-buranyi)

---

Sure I tie lots of thing into a digi payment, eg UBI. Monetary system
is at the center of many things \#muneee

---

Patreon is not good enough, ppl still have to signup to this
particular service. Monetized likes, naming all needs to be integrated
into an omnipresent payment scheme.

---

Docu shows challenges around paying for content in a post-industrial
era. My take: we need voluntery, "monetized likes" scheme tied to a
new crypto. Fast payment tech, connect to a naming system (akin to
Twitter checkmark), then while listening to a song (downloaded from
.. wherever), if liked, u send small payment to just a name. Bee Gees?
Weekend? Send it to that name and it gets routed to the artist. Or
even send it to a work (a song, or a movie), and payment gets divided
up automatically behind the scenes according to a formula.

---

Great Bloomberg docu on history of file sharing, MP3, its effect on
the music biz.

[Part 1](https://www.youtube.com/watch?v=OHVRItc38-c)

[Part 2](https://www.youtube.com/watch?v=01DOCnCA1j0)

[Part 3](https://www.youtube.com/watch?v=392B71DgBCY)

---

Archimedes circle area formula invention is not covered at
schools.. Sad state of our ed system.. Stuff that should be taught
first arrives last. It is as if they don't want innovative,
free-thinking people.

---

Ill Boogs - Super Suede \#music

[Link](https://youtu.be/7o8q81-bkew)

---

[Answer](../../2021/04/sum-greater-than-whole-reductionism.md#circle)

"I read somewhere that Calculus is all about dividing something into
pieces and putting it back together.. In terms of the basis of
innovation, doesn't that sound like simple addition?"

---

It's true. [See](../../2021/04/suez-aftermath-ike-didnt-like.md)

"@rabrowne75

'Years later,' Richard Nixon wrote in the 1980s, 'I talked to
Eisenhower about Suez; he told me it was his major foreign policy
mistake.'"

---

Were they waiting for muneee? The Benjamins?

---

A year ago? Why did it take so long for a wider rollout?  Testing
shouldn't have taken that long.

"@ichaydon

A year ago I tried the Moderna vaccine to see if it was
safe. (Spoiler: It is!) "

---

"Uniper Site in Wilhelmshaven Set to Cease Coal-Based Power Generation this Year
and Focus Attention on Hydrogen"

[Link](https://fuelcellsworks.com/news/uniper-site-in-wilhelmshaven-set-to-cease-coal-based-power-generation-this-year-and-focus-attention-on-hydrogen/)

---

V awesome.. Laudato Si

"It's a Mirai-cle: the Pope has a hydrogen Toyota"

[Link](https://www.topgear.com/car-news/future-tech/its-mirai-cle-pope-has-hydrogen-toyota)

---
