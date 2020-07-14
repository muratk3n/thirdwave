# Tweets - Week 29b

Jazz Quintet, David Pastor & Smoothtime \#music

[Link](https://youtu.be/HS6L99Zf7kI?t=3200)

---

OS makers; I understand trying to be 'helpful' with regional
options. Time zone selection somehow alerted th OS I want my months in
Greek. Ιουλ? Malaka?

---

Fantastic piece of equipment for <400 dollars. This thing is a beast. 

---

Saw a nice Huewei notebook today, coulda bought it, but didn't bcz of
security fears. Not saying this to bash. Considered it, but a
Taiwanese hardware maker got the business instead.

---

"@Austen

After watching journalists uniformly rip on and warn about every
aspect of every app and every tech company for the last several years
years, watching them turn around and become apologists for TikTok is
really, really weird"

---


"@Newsweek

Texas teachers writing their wills as state promises to open schools
in fall"

---

"The new Hong Kong: Disappearing books, illegal words and arrests over
blank white paper"

[Link](https://www.latimes.com/world-nation/story/2020-07-10/this-is-a-cultural-purge-with-new-security-law-even-blank-paper-is-subversive-in-hong-kong)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Turns out the people who predicted the world ending in 2012 were optimists.</p>&mdash; Conan O&#39;Brien (@ConanOBrien) <a href="https://twitter.com/ConanOBrien/status/1282739574024867847?ref_src=twsrc%5Etfw">July 13, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

\#pinephone

<img width="340" src="https://pbs.twimg.com/media/Ec03D4EWsAEK1Lu?format=jpg&name=small"/>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hydraulic drilling companies across America are going bankrupt and letting methane spew into the atmosphere. Instead of spending to seal well heads they are just paying bonuses and dissolving. <a href="https://t.co/aWQ5PboKiu">https://t.co/aWQ5PboKiu</a></p>&mdash; Lee Fang (@lhfang) <a href="https://twitter.com/lhfang/status/1282554480274243584?ref_src=twsrc%5Etfw">July 13, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"@alert5

Japan to consider sharing air defense radar information with
Philippines in order to track Chinese aircraft"

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Meet the <a href="https://twitter.com/HEAVEN_FCH?ref_src=twsrc%5Etfw">@HEAVEN_FCH</a> Consortium <a href="https://twitter.com/DLRStuttgartTT?ref_src=twsrc%5Etfw">@DLRStuttgartTT</a><br>The German Aerospace Center acts as the system designer, developing a high power fuel cell system fuelled by liquid hydrogen for an electric powertrain of a 4 seater aircraft, the Hy4. More information: <a href="https://t.co/LtB7SzOKfT">https://t.co/LtB7SzOKfT</a> <a href="https://t.co/TyWKu1lv3n">pic.twitter.com/TyWKu1lv3n</a></p>&mdash; HEAVEN Project (@HEAVEN_FCH) <a href="https://twitter.com/HEAVEN_FCH/status/1282580676206825472?ref_src=twsrc%5Etfw">July 13, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"HyPoint, a company developing zero carbon emission hydrogen fuel cell
systems for air transportation and urban air mobility, has announced
that it has hired several new key executives to drive HyPoint’s
technology development and go-to-market strategy"

[Link](https://www.intelligent-aerospace.com/avionics/article/14179079/hydrogen-fuel-cell-air-transportation)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Saudi Arabia <a href="https://twitter.com/ACWAPower?ref_src=twsrc%5Etfw">@ACWAPower</a> joining the pack in a combi of efforts with Neom and Air Products to make a truly worldscale renewable/green <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> production plant. Estimated costs $5bn +$2 bn for infrastructure rollout. <a href="https://twitter.com/hashtag/h2?src=hash&amp;ref_src=twsrc%5Etfw">#h2</a> converted to Ammonia for transport <a href="https://t.co/GKyfLwd2Zm">https://t.co/GKyfLwd2Zm</a> <a href="https://t.co/3L4GvCs0Lx">pic.twitter.com/3L4GvCs0Lx</a></p>&mdash; Hydrogen Standard (@H2Standard) <a href="https://twitter.com/H2Standard/status/1282525156838002694?ref_src=twsrc%5Etfw">July 13, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"@JordanChariton

If you watch corporate Sunday morning news programs, you might have no
idea millions of people are facing evictions and homelessness in 2
weeks"

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">&quot;WE SIMPLY CAN&#39;T AFFORD UNIVERSAL HEALTH CARE,&quot; they scream at me over the military jet display</p>&mdash; Georgia (@nationalparke) <a href="https://twitter.com/nationalparke/status/1279568261307404295?ref_src=twsrc%5Etfw">July 5, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

@zackkanter

Facebook & TikTok privacy issues are easy for NYT reporters to mix up. One way to keep them straight is to apply 'the Uyghur test' - if you're a Uyghur using the app in its country of origin, are you in danger of: 1) being targeted w/a desk ad, or 2) having your organs harvested?

---

Little scraping.. got 10 random numbers btw 1 and 10.

Seems to work.

Good shit.

```python
import urllib.request as req, re

URL = "https://www.random.org/integers/?num=10&min=1&max=10" + \
      "&col=1&base=10&format=html&rnd=newb" 
r = req.urlopen(URL).read().decode('utf-8')
dd = re.findall(r'<pre class=\"data\">(.*?)</pre>', r, re.DOTALL)[0]
[int(x) for x in dd.split("\n") if len(x) > 0]
```

```text
Out[1]: [3, 1, 5, 2, 5, 9, 6, 7, 8, 9]
```

---

There it is

"RANDOM.ORG offers true random numbers to anyone on the Internet. The
randomness comes from atmospheric noise, which for many purposes is
better than the pseudo-random number algorithms typically used in
computer programs"

[Link](random.org)

---

Need some true number generation..

There used to be `random.org`. 

---

"Teens Flock To New App Where They Just Enter Own Personal Data Into
Form"

[Link](https://www.theonion.com/teens-flock-to-new-app-where-they-just-enter-own-person-1844339166)

---

LLAP 🖖

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The kids like eating Tide Pods too<br><br>Now you know who&#39;s running the NYT</p>&mdash; Fusilli Spock (@awstar11) <a href="https://twitter.com/awstar11/status/1282072490303348736?ref_src=twsrc%5Etfw">July 11, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Sister of Erik Prince of Blackwater.

"@la_louve_rouge_

Betsy DeVos says that "only" 0.02% of children will probably die as a
result of schools re-opening. That's 14,740 children"

---

Nice

"@HollywoodMev

If you could sacrifice one sport to end COVID-19, what would it be?
And why baseball?"

---

"H21 launched in 2016, to demonstrate that existing UK gas networks can
be converted to carry 100% hydrogen for use in homes and
businesses. ... “The H21 programme is demonstrating that
the UK's existing gas network can carry hydrogen, for use by homes and
businesses"

[Link](https://fuelcellworks.com/news/northern-gas-networks-ngn-uk-pioneering-hydrogen-project-takes-first-step-in-south-bank/)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">One of <a href="https://twitter.com/hashtag/H2View?src=hash&amp;ref_src=twsrc%5Etfw">#H2View</a>’s top stories this week saw the <a href="https://twitter.com/hashtag/EuropeanCommission?src=hash&amp;ref_src=twsrc%5Etfw">#EuropeanCommission</a> unveil its <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> strategy and officially launched the European Clean Hydrogen Alliance to deliver on it.<a href="https://t.co/QiSyk42XBe">https://t.co/QiSyk42XBe</a></p>&mdash; H2 View (@h2_view) <a href="https://twitter.com/h2_view/status/1281945336689258498?ref_src=twsrc%5Etfw">July 11, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---


His father killed a man, you know.. In South Africa.. Most likely a
black person too. That's right. SO guy is a psycho, and the father was
a psycho. The apple fell right by the tree. Nam sayin? This guy is
guiding your energy policy America, wake up.

"Elon Musk is unbalanced, weird"

---

Reuters: "The president’s demand for schools to fully reopen this fall
despite the coronavirus pandemic, his warnings on crime and civil
disorder and the touting of a vibrant stock market, are meant to make
him more appealing to suburban voters. There is little sign that the
approach is working"

---

"Local news is extremely easy to take for granted. It is, by
definition, narrow in its interests. But even beyond serving as the
core of America’s news ecosystem, local news can be the glue that
connects people in a given community. 'It’s the way a local columnist
can express a community’s frustration or triumph .. the way the local
music critic can review a concert, the deeply reported feature
stories, the assessment of a new restaurant, the obituaries, the
letters to the editor. The newspaper ties a region together, helps it
make sense of itself.”

[Link](https://www.theatlantic.com/culture/archive/2020/07/ghosting-news-margaret-sullivans-alarm-bell/614011/)

---

They had con radio.. this is a good point, such radio is mostly
centralized, "federal" in nature, they talk abt con issues but in
overarching, generalized tones, pushing broad buttons.. So they don't
really give a shit about your local problems, and in many ways, are
toxic for politics, especially the local kind.

*The Atlantic*: "McMurray’s opponent, the incumbent [congressman]
Chris Collins, had recently been indicted on charges of insider
trading. The Buffalo News ... broke the story of the indictment, and
some TV stations picked up the News’s reporting. Readers and viewers
in areas that had strong local news presences .. learned of the
indictment and, armed with that information, voted accordingly. But
many in the sprawling district were not so equipped. 'I’d be going
door to door,' McMurray [says] 'or meeting with people at a diner or a
fair, for example, and in the most isolated areas, a lot of people had
no idea that their own congressman had been indicted.' He notes that
Orleans County, a rural area of the district classified as a news
desert, was “one of the toughest places.' People there, according to
McMurray, had “gossip, conservative radio, or social media.' They had
echo chambers. They did not, however, have news. And so, by a
razor-thin margin, Chris Collins — who would go on to plead guilty to
two felonies, be sentenced to prison, and resign from Congress — won
the election"


