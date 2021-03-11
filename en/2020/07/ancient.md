# Ancient

When people praise a region, a country being "ancient", "had
civilization" what they mean is that region had contact with
agriculture the longest, because only then you can have a mafia
(empire) who can tax (peasant is tied to land, can't run away), raise
armies, kill others and build arenas, roads which later generations as
tourist can gape at like morons.

However, and in the light of agriculture being the root ill of many of
the later predicaments [as we now know](../../2017/12/rome.md), one
could guess countries who were at the center of these "ancient"
developments would clearly be worse off. And they are. The Han,
Ottocuck, Egypt, Sassanid, Rome... agro-centric centralized mafia
empires, through their peasant/tax/opress cycle created a toxic
culture that still lingers in these regions, like a bad fart, which is
impeding the progress of their descendants. Lets's look at data.

We compare China, Italy, so-called Turkey, Greece, Egypt, Iran vs
others.

GDP per capita, them vs others (data from World Bank, [GDP](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita), [Population](https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)),[CSV](gdpw.csv))


```python
import pandas as pd
df = pd.read_csv('gdpw.csv')
df['gdpw'] = df.gdpcap * df.population
anc = ['China','Italy','Turkey','Greece','Egypt','Iran']
dfc1 = df[df.country.isin(anc)]
dfc2 = df[df.country.isin(anc) == False ]
print ('Mafia', np.round(dfc1.gdpw.sum() / dfc1.population.sum(),2))
print ('Others', np.round(dfc2.gdpw.sum() / dfc2.population.sum(),2))
```

```text
Mafia 10069.93
Others 11739.59
```

Significant difference.

Democratic progress, them versus the entire world,

```python
import pandas as pd
df = pd.read_excel('../../tweets/2020/p4v2018.xls')
df = df[df.polity > -10.0] # remove junk code -88
print ('Mafia',np.round(df[df.country.isin(anc)].polity.mean(),2))
print ('Others',np.round(df[df.country.isin(anc) == False].polity.mean(),2))
```

```text
Mafia -0.53
Others 0.44
```

Throught the *entire* 100+ years the Polity keeps track of, "ancient"
countries did worse democratically than the rest.

"But things would've changed recently". Ok, let's look at that.

```python
df3 = df[df.year == 2018]
print ('Mafia',np.round(df3[df3.country.isin(anc)].polity.mean(),2))
print ('Others',np.round(df3[df3.country.isin(anc) == False].polity.mean(),2))
```

```
Mafia -0.33
Others 4.73
```

Mafia improved only __tiny__ bit while still being in the red (< 0),
while the rest made significant advances.

The conclusion

There is nothing to be proud of for these countries... "Ancient"
simply means people people of those regions would have more chance to
be around a c--ksucker like Julius Ceasar or Otto Soleiman which would
poison the governance cultures of these lands irrevocably. I still
remember with horror when BBC reported that Egypt, until the 2012
election did not have a single day of democracy in its past. NOT A
SINGLE DAY. Think about that.. Would you rather have "ancient" grand
pyramids, or one day of democracy in your past..

I'd opt for the latter.
