# Tweets

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The map shows how much tax revenue your country loses from corporations shifting profits to tax havens.<br><br>In total 40% of multinational profits are shifted to tax havens each year.<br>This reduces corporate income tax revenue by nearly $200 billion.<br><br>from <a href="https://t.co/Wa9aVaeikB">https://t.co/Wa9aVaeikB</a> <a href="https://t.co/4Y9HWXsrxj">pic.twitter.com/4Y9HWXsrxj</a></p>&mdash; Max Roser (@MaxCRoser) <a href="https://twitter.com/MaxCRoser/status/1356203389630218243?ref_src=twsrc%5Etfw">February 1, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

BTW by "average" yesterday I meant long-running average between two
(or more) views. One party cld be for 30% tax rate, another for
70%. Each enact their thing one in power, if they can, long-running
average is 50%.

---

Stiglitz: "By contrast, Biden’s proposed spending plan is urgently
needed. Recently released data show a slowdown in America’s recovery
both in terms of GDP and employment...

The economy would, of course, be better off without zero interest
rates. It would also be better if policymakers raised taxes by
imposing levies on pollution and restoring greater progressivity to
the tax system. There is no valid reason why the richest Americans
should pay lower taxes as a percentage of their income than those who
are far less well off. Given that wealthy Americans have been the
least affected, medically or economically, by the coronavirus
pandemic, America’s regressive tax system has never looked uglier...

Under President Donald Trump, the programs that focused on small
businesses were not as effective as they could or should have been –
partly because too much of the money went to businesses that were not
really small, and partly because of a rash of administrative problems"

[Link](https://www.project-syndicate.org/commentary/biden-right-to-launch-massive-rescue-plan-by-joseph-e-stiglitz-2021-02?referral=d582d5)

---

I wonder if all that sugar is added to marmalede to increase its
viscosity to add a kind of protective layer against air, etc
influence.. What if u just add olive oil?

---

"Sumitomo Corporation of Americas Makes Strategic Investment in Hydrogen Fuel Provider OneH2"

[Link](https://www.prnewswire.com/news-releases/sumitomo-corporation-of-americas-makes-strategic-investment-in-hydrogen-fuel-provider-oneh2-301216213.html)

---

"GM partnering with Navistar on hydrogen fuel cell semi trucks"

[Link](https://www.detroitnews.com/story/business/autos/general-motors/2021/01/27/gm-partnering-navistar-hydrogen-fuel-cell-semi-trucks/4265647001/)

---

Podcast from the University of California, Irvine, talking to Jack
Brouwer, a professor of mechanical and aerospace engineering at UCI,
also the director of the National Fuel Cell Research Center, as well
as the director of the Advanced Power and Energy Program.

"It’s much more reliable to have both a renewable fuel and renewable
electricity delivered in society. And we experience that today, for
example, when we have the public safety power shutoff events, and when
we have wildfires that shut electric grids down, or when electric
grids themselves cause fires because they become too overloaded. When
these things happen, we depend upon underground delivery of natural
gas, today. Of course, it’s going to have to be transformed to this
renewable hydrogen vector. And when we put those together, we can
envision a 100 percent renewable world that is also reliable"

[Link](https://news.uci.edu/2021/01/27/uci-podcast-solving-climate-change-with-clean-hydrogen-fuel/)

---

Both shooting, and weight guessing involves knowledge / skill BTW,
very important. Good noise around bullseye means person knows how to
shoot.  Judging weight by naked eye is possible bcz we have innate
knowledge of weights of things, through evolution, and part of growing
up, and the noise is normal. Stat ppl know this, when they apply a
model to data, they determine whether it is good by looking at its
residual (diff between model pred, and real data). If resid is
gaussian, they are happy. Bad models leave patterns in data. When dumb
people eff up you know why. There is pattern in their eff ups (usually
due to some bias).

Done.

Class dismissed

---

Height is normal of course.. many factors contribute to height. Some
ppl might have a fat ass, small back, others large back, skinny
ass. Large or small head.. All cld lead to same height.

---

Anyway; then, if shooting errors, weight guesses are `true value + normal noise`,
averaging removes noise, bcz average of zero-centered
Gaussian (which is noise) is zero. This is the magic.

---

But if I sum every 6 die throws and histogram,

```python
import random
n = 1000; b = 6
rolls = [random.randint(1,6) for i in range(b*n)]
rolls = np.array(rolls).reshape(n,b)
s = np.sum(rolls,axis=1)
plt.hist(s,bins=12)
plt.savefig('dice1.png')
```

<img width="200" src="https://github.com/muratk3n/thirdwave/blob/master/en/tweets/2021/dice1.png?raw=true"/>

Bell shaped. Normal.

Why? There are more chances to get a 6 than 2. I can get 6 with
4+2,2+4,1+5,3+3,etc.. Very low, very high nums are harder. Easy sums
form the bulk in the middle.

---

Demo. Throw a 6-sided die 1000 times (numbers below are from software
generator), histogram rolls,

```python
import random
n = 1000; b = 6
rolls = [random.randint(1,6) for i in range(b*n)]
rolls = np.array(rolls)
plt.hist(rolls,bins=6)
plt.savefig('dice2.png')
```

<img width="200" src="https://github.com/muratk3n/thirdwave/blob/master/en/tweets/2021/dice2.png?raw=true"/>

Nearly uniform (not normal), all equal chance,

---

Normal distribution is weird; it shows up everywhere. Take a group of ppl,
their height dist is normal.

Have someone shoot at a target, measure distance from each hit to
bulls eye, dist is normal.

Whenever many factors *contribute* to a thing, normality occurs.. bcz
sums of anything (random) approaches normal. And there are many things
like that in nature

---

To elaborate more on how consensus among (knowledgable) people can
result in correct decisions.. Remember earlier
[post](2020/07/crowd-wisdom.md) at a country fair 800 people estimated
the weight of an ox. Statistician Francis Galton observed that the
median guess, 1207 pounds, was accurate within 1% of the true
weight. Magic.

The reason is guesses have noise, the right kind of noise, around the
right answer. Averaging removes noise.

The noise distribution is bell-shaped, "normal" or a "Gaussian" (a
dist is the formulaic form of a histogram, occurence count, frequency).

---

IMO the general public is not the best place for this stuff.. but
hey.

Id rather sci ppl hit their peers harder in the head.

---

Haha.. Robitaille took an ad on *New York Times* about his findings in 2002.
I share it [here](2021/01/kirchoff-sun-bigbang.md).

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

[Religion](/2015/04/god-religion.md)

[Democracy, Parties](/2016/11/democracy.md)

[Economy](/2018/05/economy.md)

[Globalization](/2018/09/globalization.md)

[Rome, The First Wave](/2017/12/rome.md)

[Human Nature & Health](/2020/07/human-nature.md)

[Climate Change](/2018/12/climate.md)

[The Middle East](/2019/07/middleeast.md)

[TR](../tr)

## Browse

[By Year](years.md)

[Search](search.html)

[Tweet Archive](/tweets/README.md)


