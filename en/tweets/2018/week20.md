# Week 20

What is sales all about? How do you become better at it?

Easy

Sales is about creating contrasts, and simple messages. "I'm a uniter,
not a divider", "I am an outsider not an insider", "I am a lover not a
fighter"... These words are meaningless, but they work. This is how
sausage is made. The first two are from Dubya BTW the master at this
shite. See how he creates contrasts, "not this, but that". Simple
messages are needed so ppl remember what you are about.. In the
information age paradoxically ppl will know less about stuff, they are
being bombarded from all directions, you need to be repetitive to get
through. They'll see you on the Web, TV maybe 9,10 times, twice they
hear the same message, they'll know "okay this guy is about -blah-. "A
uniter not a divider. I get it!".

Second rule of politics: people are better at judging the person than
the issues. By hearing the same message they make the judgement that
"the politician is consistent" or even "decisive".

Why are contrasts important for sales? For people to buy something,
they need to know they will be better off from their current
situation. How better? That's the contrast. This pen (I am selling) is
much better than your old pen - so buy!

---

NYT

Milwaukee minorities didn’t vote Hillary & don’t regret it

It's Obama's Fault

Exactly as Time for Change model predicted; the incumbent President's
popularity directly effects the party's winning probability (duh). And
here is a great Obama impression.

---

Question

But... what if someone ideologically different was nominated from the
(unpopular) President's party?

That kind of nomination almost never happens

That's probably what the TfC model catches too, and why it works. The
nominee, if it is a different person than the Prez himself, is the
ideological continuation of the incumbent (that creates the signal in
the data that the model catches) which makes sense. Actually in Bam's
case the effect is in the other direction in a way, he was a Clinton
disciple, but same difference (the fact that he beat Hillary for 2008
nomination created the illusion that Bam was somehow independent from
the Clinton era, but this is false).

---

Question

But Democrats are different.. they are for all kinds of good stuff..

Really?

Most of the true changes, they don't talk about. Some of the stuff
they do talk about, they have no legitimacy on, like gerrymandering /
redistricting. Like, Obama redistricted.. yeahh... brother drew them
lines too... Mmmmm Hmmmm ... yes he diid. From New Yorker:

Like every other Democratic legislator who entered the inner sanctum,
Obama began working on his “ideal map.” Corrigan remembers two things
about the district that he and Obama drew. First, it retained Obama’s
Hyde Park base—he had managed to beat Rush in Hyde Park—then swooped
upward along the lakefront and toward downtown. By the end of the
final redistricting process, his new district bore little resemblance
to his old one. Rather than jutting far to the west, like a long thin
dagger, into a swath of poor black neighborhoods of bungalow homes,
Obama’s map now shot north, encompassing about half of the Loop, whose
southern portion was beginning to be transformed by developers like
Tony Rezko, and stretched far up Michigan Avenue and into the Gold
Coast, covering much of the city’s economic heart, its main retail
thoroughfares, and its finest museums, parks, skyscrapers, and
lakefront apartment buildings. African-Americans still were a
majority, and the map contained some of the poorest sections of
Chicago, but Obama’s new district was wealthier, whiter, more Jewish,
less blue-collar, and better educated. It also included one of the
highest concentrations of Republicans in Chicago. 

“It was a radical change,” Corrigan said. The new district was a
natural fit for the candidate that Obama was in the process of
becoming. “He saw that when we were doing fund-raisers in the Rush
campaign his appeal to, quite frankly, young white professionals was
dramatic.”

Notice the "professionals" aspect. This is the top 20% who don't have
a clue about what's going on in the rest of the country, shunned by
Trump, heavily courted by the Dems.

---

Question

How about that Michelle Wolf comedy?

She was great

I loved her style, half-whiny, little ditzy, naggy but beautifully
funny.. with some sharp material.

Note: da much-awaited Dennis Miller smackdown..

https://twitter.com/DennisDMZ/status/990505203043463168

https://youtu.be/ZfYGELMm97o?t=373

---

Comment

United States never defaulted on its debt obligations

Wrong

From New Paradigm in Macroeconomics: "Excess credit creation in the US
would also be reflected in increased foreign investment. [I]n the
1960s the US dollar was effectively the world’s currency, and thus
additional creation of dollars could be expected to be diffused around
the world, without any adjustment in exchange rates – until the world
rebels [US was basically printing excessive dollars and "buying up
Europe", the French caught on]. When France decided to convert US
dollars into gold at the official fixed price, as the Bretton Woods
system formally provided for [calling US's bluff], the US had to make
the decision whether to make good on its promise to redeem the
excessively created dollars into gold, or whether it should break its
promise – and with it bring down the Bretton Woods System of fixed
exchange rates. France proceeded to demand conversion of dollars into
gold, in an episode later called the ‘French raid on Fort Knox’. The
US leadership decided to break its promise. It ‘closed the gold
window’".

That is a default on debt. Money in this old system is an IOU for
gold, French wanted their gold for their IOU but did not get it.

You could argue of course then US switched to petrodollar system and
those dollars become even more valueable but still.. A default is a
default.

---

Question

Laurel or Yanni

He or She

[On the voice recording who some people hear as Laurel some as
Yanni]. Apparently gender is a major factor on what people hear. Dude
[here](https://youtu.be/M7QY4Gbz9uA?t=22) did the science (as much as
he could based on Twitter surveys),  women are 55%/45% Yanni,
men 60%/40% Laurel. Using actual counts, and Fisher's exact test


```python
fm = np.array([[65.0,80.0],[142.0,96.0]])
uo35 = np.array([[60.0,56.0],[21.0,22.0]])
import scipy.stats as stats
print (stats.fisher_exact(fm))
print (stats.fisher_exact(uo35))

(0.54929577464788737, 0.0059272092668501948)
(1.1224489795918366, 0.85850083655070586)
```

So the differences are significant for gender, but not for age.

---

Question

I hear about Web 3.0 all the time

Yes

That thing can hit like a freight train, all of a sudden and without
warning. Watch out.

---

News

![](03-02.png)

Good one

I think what the post means to say is Palestinian died because a
sniper shot him in the head. The sanitized wording above is like
saying "Jews died from lung complications during the Holocaust".

Please.

---

Question

Did YouTube policies improve after author complaints?

Dunno

Ask them.

https://youtu.be/1EQXvwUu4PE?t=2

https://www.youtube.com/watch?v=DbL-Y_JHDkU

---

Question

Was Martin Luther King killed because he pointed out racial
injustices?

No

He was most likely assassinated because he pointed out social
injustices. Both him and R. F. Kennedy were talking against social,
economic justice and the Vietnam War. Both were killed. 

---

Comment

It is also a relevant subject of future research to investigate how
central banks have exerted influence over the research conducted by
academics. For instance, the Swedish central bank established a
pseudo-‘Nobel Prize’ by awarding substantial sums of money to selected
economists – none of them supporters of the credit creation theory of
banking – and calling this prize the ‘Riksbank [Swedish central bank]
prize in economic sciences in honour of Alfred Nobel’. The fact that
journalists would abbreviate this as a ‘Nobel Prize’ in their
reporting of the award could neither have been a surprise nor
unwelcome to the Swedish central bank, which lobbied for the
involvement of the Nobel Foundation in the award of this
prize. Through the award of this central bank prize, a particular
branch of economics, usually based on the deductive methodology,
received a significant boost internationally.

Daaaaam

Oh no you didn't

---

Question

How do we grow an economy?

GDP, Credit

Better education, healthier citizens, or the kind of stuff that
Hidalgo recommends raise GDP potential. Then you provide the necessary
credit so that GDP potential can be actualized. Any less you get
deflation, any more you get inflation. Aiming for 2% and seeing it
happen is actually great, bcz then policymakers know the credit is
just right, inflation is also spurring people to spend.

---

Question

How was the mood in New York right after 9/11?

Okay

I was in NYC during the whole thing BTW - very uneventful for
me. Afterwards, also fine. A year later I went to Comedy Cellar, guy
was trying out new material - he had one joke on Bin Laden. He had Bin
Laden and Bill Clinton smoking hookah - Clinton takes a drag, then
says "Bin Laden? What kind of name is that? How about Been Lovin? How
about Been Fuckin?". It was a big joke. He did the whole accent and
everything, well by this time even I could do it... So the mood was
fine.

---

