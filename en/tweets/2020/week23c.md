# Tweets - Week 23c

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Do you need accurate rainfall data?<br>Here (<a href="https://t.co/NxYw7zoPOS">https://t.co/NxYw7zoPOS</a>) our free global dataset GPM+<a href="https://twitter.com/hashtag/SM2RAIN?src=hash&amp;ref_src=twsrc%5Etfw">#SM2RAIN</a> 2007-2018<br>👇Map shows regions 🔵 where we expect to be better than ERA5: Africa, Brazil+Argentina, East US, India, N.Australia<br>🙏<a href="https://twitter.com/ESA_EO?ref_src=twsrc%5Etfw">@ESA_EO</a> SMOS+Rainfall<br>🔗<a href="https://t.co/H7AF7MuLS2">https://t.co/H7AF7MuLS2</a> <a href="https://t.co/TSXQuEeWsY">pic.twitter.com/TSXQuEeWsY</a></p>&mdash; Hydrology IRPI-CNR (@Hydrology_IRPI) <a href="https://twitter.com/Hydrology_IRPI/status/1267376128668446722?ref_src=twsrc%5Etfw">June 1, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-06-01 12:14:39*

---

I have two other methods to run that difference, significance check,
and could probably dig up a third. Interested parties need to learn
this shit before talking shop on cause and effect.

*2020-06-01 12:08:38*

---

Of course statistical significance is one thing, practical
significance is another. That's another level of critical judgement
that needs to applied to the result. As the Gelman / Hill book says

>Statistical significance does not equal practical significance. For
>example, if the estimated predictive effect of height on earnings were
>10 dollar per inch with a standard error of 2 dollar, this would be
>statistically but not practically significant. Conversely, an estimate
>of 10,000 dollar per inch with a standard error of 10,000 dollar would
>not be statistically significant, but it has the possibility of being
>practically significant (and also the possibility of being zero; that
>is what “not statistically significant” means)."

*2020-06-01 12:00:54*

---

Impeachement was on 2019-12-18? We look at approval data before and
after, 6 months before, 2 months after,

[Data](https://projects.fivethirtyeight.com/trump-approval-data/approval_topline.csv)

```python
import pandas as pd
df = pd.read_csv('/tmp/approval_topline.csv',parse_dates=True,index_col='modeldate')
df = df[['approve_estimate','disapprove_estimate']]
df = df.sort_index(by='modeldate')

df['net'] = df.approve_estimate - df.disapprove_estimate
event = '2019-12-18'; d1 = '2019-06-01'; d2 = '2020-03-01'
df1 = df[(df.index > d1) & (df.index < event)]
df2 = df[(df.index > event) & (df.index < d2)]
print (df1['net'].mean())
print (df2['net'].mean())
```

```text
-11.725994522613066
-9.786354182648402
```

Net approval was lower before impeachement than after.

Is this significant? Let's compare means of both samples, using Welch
two sample t-test,

```python
from statsmodels.stats.weightstats import ttest_ind
print ( ttest_ind(df1['net'], df2['net']) )
```

```text
(-14.416007336365869, 3.970177267005474e-42, 814.0)
```

The hypothesis that they are the same is rejected. Statistically these
numbers are different. So impeachement helped Trump by 2% points.

*2020-06-01 11:50:4*

---

One needs to look at the data and run statistical tests to answer that
question. See above.

"Impeachement hurt Trump"

*2020-06-01 11:49:04*

---

Trump was never the guy to calm things down. He was the agent of chaos
himself.. But I dont think that's the US Presidency.

*2020-06-01 7:41:49*

---

@uncrushedvelvet

a government that can’t mobilize to house and feed us during a
pandemic but can mobilize to beat us whenever we rise up tells you
exactly where their priorities are

*2020-06-01 7:41:46*

---

@tobaccodad

There's a neo Nazi serving life plus 400 years for doing exactly what
I've seen multiple videos of cops doing in different cities right now

*2020-05-31 22:12:3*

---

"@kthalps

No one who identifies as liberal should want Facebook/Twitter/Youtube
to censor people. Nobody who IDs as Leftist should either bc but
principles aside, these companies are not benevolent & most targeted
are free Palestine supporters"

[Link](https://youtu.be/MxbOLZq91NA?t=3265)

*2020-05-31 22:11:9*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Some of the sites deleted by Facebook were legitimate businesses that had spent thousands if not tens of thousands on the platform&#39;s boosting tools to build up their media businesses. Wiped out in one stroke as &quot;inauthentic&quot; <a href="https://t.co/yOx901gjAt">https://t.co/yOx901gjAt</a></p>&mdash; Matt Taibbi (@mtaibbi) <a href="https://twitter.com/mtaibbi/status/1267228337338007553?ref_src=twsrc%5Etfw">May 31, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-05-31 22:09:1*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Minority and oppositional sites are routinely removed from Internet platforms around the world, Israel/Palestine being a classic example: <a href="https://t.co/3FUgEdmPxL">https://t.co/3FUgEdmPxL</a> <a href="https://t.co/off7FZqP1a">https://t.co/off7FZqP1a</a></p>&mdash; Matt Taibbi (@mtaibbi) <a href="https://twitter.com/mtaibbi/status/1267226049303195650?ref_src=twsrc%5Etfw">May 31, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-05-31 22:07:3*

---

"@ThisGuyGetsLit

Hey guys. President and CEO of Antifa here. I tried to change our name
to avoid the presidents classification as a terrorist group, but the
name I chose was al-Nusra Front and then the CIA immediately gave us
500 BGM-TOW antitank missiles and 2 Bearcats. I regret the error"

*2020-05-31 22:05:1*

---

"@H2Bjorn

Fathi Birol said, '...We are not talking about the clean electricity
transitions, we are talking about the clean energy transitions. Hence,
investment in hydrogen, carbon capture, and storage will be critically
important'"

*2020-05-31 22:02:4*

---

"@justinamash

'No justice, no peace.' Is this a threat? A call to violence? No. It
is an acknowledgment that without justice, peace is illusory. There is
no state of peace in a society that condones injustice. The victims of
such injustice, though they may remain silent, do not live in peace"

*2020-05-31 21:59:1*

---

[Revelation 17](https://www.biblegateway.com/passage/?search=Revelation+17&version=NIV)

>The seven heads are seven hills on which the woman sits. They are
>also seven kings. Five have fallen, one is, the other has not yet
>come; but when he does come, he must remain for only a little
>while.  The beast who once was, and now is not, is an eighth king

Daaaaam. Like I said religion is politics, and is against Roman
politics. Guy is talking about Rome in disguise, straight up.

*2020-05-31 21:58:45*

---

"@brianschatz

I will be introducing an amendment to the National Defense
Authorization Act to discontinue the program that transfers military
weaponry to local police departments"

*2020-05-31 21:58:6*

---

"@samswey

For those who are interested in research-based solutions to stop
police violence, here’s what you need to know - based on the facts and
data. A thread"

[Link](https://twitter.com/samswey/status/1180655701271732224)

*2020-05-31 21:29:53*

---

That song was one old-skool rap... Good rhymes, but boring notes. I
almost prefer mumble rap. Foh dat biih..

*2020-05-31 21:28:1*

---

"@ZakkFlash

Somebody stole an encrypted Chicago police radio and is disrupting
their communications by blasting 'Fuck the Police' by the legendary
NWA"

*2020-05-31 21:27:41*

---

"@HelenGymPHL

It's time. Almost three years after Charlottesville, the Rizzo statue
will come down - and the fight for greater justice must continue"

*2020-05-31 21:26:39*

---

"Rumsfeld: Looting is transition to freedom"

[Link](https://www.upi.com/Defense-News/2003/04/11/Rumsfeld-Looting-is-transition-to-freedom/63821050097983/)

*2020-05-31 21:25:36*

---

Bloody hell.. Looks bad

"@KevinRKrause

She says she was walking home with her groceries when police fired
some sort of pellet in her face. Says she’s not a
protester. \#DallasProtests"

[Link](https://mobile.twitter.com/KevinRKrause/status/1266898396339675137)

*2020-05-31 21:24:31*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Salt Lake City cops shove down an elderly man with a cane for the crime of standing along the street: <a href="https://t.co/PCLkHqQtJg">pic.twitter.com/PCLkHqQtJg</a></p>&mdash; Timothy Burke (@bubbaprog) <a href="https://twitter.com/bubbaprog/status/1266908354821206016?ref_src=twsrc%5Etfw">May 31, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-05-31 21:23:29*

---

Man I feel for Americans.. Getting hit from all directions these
days.

*2020-05-31 21:22:26*

---

"@ThisGuyGetsLit

Hey guys. President and CEO of Antifa here. I tried to change our name
to avoid the presidents classification as a terrorist group, but the
name I chose was al-Nusra Front and then the CIA immediately gave us
500 BGM-TOW antitank missiles and 2 Bearcats. I regret the error"

*2020-05-31 22:05:1*

---

"@H2Bjorn

Fathi Birol said, '...We are not talking about the clean electricity
transitions, we are talking about the clean energy transitions. Hence,
investment in hydrogen, carbon capture, and storage will be critically
important'"

[Link](https://energy.economictimes.indiatimes.com/amp/news/renewable/wont-take-long-for-clean-energy-investments-to-rebound-fatih-birol-iea/76072687)

*2020-05-31 22:02:4*

---

@justinamash

“No justice, no peace.” Is this a threat? A call to violence? No. It
is an acknowledgment that without justice, peace is illusory. There is
no state of peace in a society that condones injustice. The victims of
such injustice, though they may remain silent, do not live in peace.

*2020-05-31 21:59:1*

---

[Revelation 17](https://www.biblegateway.com/passage/?search=Revelation+17&version=NIV)

>The seven heads are seven hills on which the woman sits. They are
>also seven kings. Five have fallen, one is, the other has not yet
>come; but when he does come, he must remain for only a little
>while.  The beast who once was, and now is not, is an eighth king

Daaaaam. Like I said religion is politics, and is against Roman
politics. Guy is talking about Rome, straight up.

*2020-05-31 21:58:45*

---

"@brianschatz

I will be introducing an amendment to the National Defense
Authorization Act to discontinue the program that transfers military
weaponry to local police departments"

*2020-05-31 21:58:6*

---

"@samswey

For those who are interested in research-based solutions to stop
police violence, here’s what you need to know - based on the facts and
data. A thread"

[Link](https://twitter.com/samswey/status/1180655701271732224)

*2020-05-31 21:29:53*

---

That song was one old-skool rap... Good rhymes, but boring notes. I
almost prefer mumble rap. Foh dat biih..

*2020-05-31 21:28:1*

---

"@ZakkFlash

Somebody stole an encrypted Chicago police radio and is disrupting
their communications by blasting 'Fuck the Police' by the legendary
NWA"

*2020-05-31 21:27:41*

---

"@HelenGymPHL

It's time. Almost three years after Charlottesville, the Rizzo statue
will come down - and the fight for greater justice must continue"

*2020-05-31 21:26:39*

---

"Rumsfeld: Looting is transition to freedom"

[Link](https://www.upi.com/Defense-News/2003/04/11/Rumsfeld-Looting-is-transition-to-freedom/63821050097983/)

*2020-05-31 21:25:36*

---

Bloody hell.. Looks bad

"@KevinRKrause

She says she was walking home with her groceries when police fired
some sort of pellet in her face. Says she’s not a
protester. \#DallasProtests"

[Link](https://mobile.twitter.com/KevinRKrause/status/1266898396339675137)

*2020-05-31 21:24:31*

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Salt Lake City cops shove down an elderly man with a cane for the crime of standing along the street: <a href="https://t.co/PCLkHqQtJg">pic.twitter.com/PCLkHqQtJg</a></p>&mdash; Timothy Burke (@bubbaprog) <a href="https://twitter.com/bubbaprog/status/1266908354821206016?ref_src=twsrc%5Etfw">May 31, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

*2020-05-31 21:23:29*

---

Man I feel for Americans.. Getting hit from all directions these
days.

*2020-05-31 21:22:26*

---

I bet [you can't](https://muratk3n.github.io/thirdwave/en/2020/04/turks-culture-national-narrative.html#population)

"Tigger: But I bet I can find our nat roots in the population data"

*2020-05-31 21:20:6*

---

