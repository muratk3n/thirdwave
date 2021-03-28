# Tweets

"@mattblaze

Actually, 'Evergreen' is the name of the company that operates the
ship. The name of the ship is 'Evergreen's Monster'"

---

"@gabriel_zucman

Your periodic reminder that 40% of the pre-tax income of the US
middle-class goes to taxes and health insurance premiums (a de facto
private head tax) today

... as opposed to less than 25% for billionaires"

[Link](https://twitter.com/gabriel_zucman/status/1375940908760231938)

---

"Myanmar security forces kill at least 114 people, including children"

---

Electricity is frequently misused. Elec is not suitable for power
transmission for instance, terribly inflexible in case of storage.. In
the future we will probably see less uses of it, not more.

---

"Northwestern University soft robot moves without hardware or electricity"

[Link](https://www.slashgear.com/northwestern-university-soft-robot-moves-without-hardware-or-electricity-10650521/)

---

"Soft robots are a growing trend in the industry...  DraBot works by
controlling the air pressure coming into its wings"

---

Quantitative history. Very awesome.

---

The 9 variables in the data file;

"Polity population (`PolPop`), extent of polity territory (`PolTerr`),
the size of the largest urban center, `CapPop`. Infrastructure
(`Infra`) captures the variety of observable structures and facilities
that are involved in the functioning of the polity. The variable
`texts`, which scales from 0 to 9, sums the number of securely
attested types of texts (that is, coded as 'present').  The idea here
is that the more sophisticated a society is informationally, the more
different types of texts it will have in circulation. economic
development is reflected in Monetary System (`Money`). Presence of
writing system is in `writing`"

[Link](https://escholarship.org/content/qt99x6r11m/qt99x6r11m_noSplash_0ec83bc0d39d185f00345309a3db5508.pdf)

---

Attempted repl of a plot from the scale and information-processing [paper](https://www.nature.com/articles/s41467-020-16035-9).
Similar output to Figure 2 is below. [Data](https://github.com/jaewshin/Holocene)

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

pnas_data1 = pd.read_csv('https://raw.githubusercontent.com/jaewshin/Holocene/master/data1.csv')

features = ['PolPop', 'PolTerr', 'CapPop', 'levels', \
'government','infrastr', 'writing', 'texts', 'money']

data_mat = pnas_data1.loc[:, features].values
scaler = StandardScaler()
scaler.fit(data_mat)
scaled = scaler.transform(data_mat)
mean = np.mean(data, axis=0)
data -= mean
P, D, Q = np.linalg.svd(data, full_matrices=False)
data = np.matmul(scaled, Q.T) 
X, Y = data[:, 0], data[:, 1]
p = np.poly1d(np.polyfit(X, Y, 4))
fig = plt.figure()
plt.scatter(X, Y, s=1)
plt.plot(X, p(X),'r.')
plt.xlabel('First PC')
plt.ylabel('Second PC')
plt.savefig('pnas.png')
```

<img width="340" src="https://pbs.twimg.com/media/ExgVXABWgAUEAG9?format=png&name=small"/>

---

"While the Wright brothers are credited with the first powered flight
of a heavier than air vehicle that could take off and land from level
ground, it was the German aviator, Otto Lilienthal, who first mastered
the aerodynamics of hang gliders. In fact, the experiments of
Lilienthal helped the Wright brothers a great deal in understanding
the basics of flight. Lilienthal himself built eighteen different hang
glider models over a period of five years and test flew them"

[Link](https://www.researchgate.net/publication/37179495_Powered_Hang_Gliding)

---

I agree. Spices are absolutely necessary to keep meat bacteria-free,
they are in fact healthy, not just tasty.


"Humans' use of antimicrobial spices developed in parallel with
food-spoilage microorganisms, Cornell University biologists have
demonstrated in a international survey of spice use in cooking... The
proximate reason for spice use obviously is to enhance food
palatability... But why do spices taste good? Traits that are
beneficial are transmitted both culturally and genetically, and that
includes taste receptors in our mouths and our taste for certain
flavors. People who enjoyed food with antibacterial spices probably
were healthier, especially in hot climates. They lived longer and left
more offspring. And they taught their offspring and others: 'This is
how to cook a mastodon.' We believe the ultimate reason for using
spices is to kill food-borne bacteria and fungi."

[Link](https://news.cornell.edu/stories/1998/03/food-bacteria-spice-survey-shows-why-some-cultures-it-hot)

---

It was all good when sugered water invent in US had its bottle
produced in Phillipines, cap in Singapore, soda in Mexico, bottled in
Spain, and shipped to US..  It aint so fine when vaccines, invented in
DE, bottled in Belgium, and all shipped to UK/US, is it?

Globalist centrist cuck libs and cons all be bitchin now. Where is
TINA?

---

"@james_oaten

Australia's ambassador to China says Beijing's trade behaviour is
'vindictive'"

---

"@unzicker_a

\#Corona München will Modellstadt werden, aber der nächsten
PCR-Testtermine gibt es im April?? Was sind heir für idioten am Werk?"

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


