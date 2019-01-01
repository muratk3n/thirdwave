# More on Brexit

In explaining the course of history, scholars like to look not only at immediate causes of an event, but the underlying trends that made it possible, if not inevitable. The assassination of Austrian Archduke Ferdinand in Sarajevo in 1914 may have sparked World War I, but the conflagration was the expression of longstanding geopolitical rivalries [..].

On their own, the EU’s failures need not have necessitated a vote to Leave. Despite these developments, there were strong arguments for staying in the EU. One could, on balance, decide that the good outweighed the bad, that the EU could be reformed, that the economic benefits of staying were not worth the political advantages of leaving [..]. 

But that would require knowledge of the positive case for staying. And over many years, the British public were treated to nothing but the negative: story after story — many exaggerated, some invented, others all too true — of the EU’s failings. Nobody in power spoke of the positive things Europe provided. There was no counter narrative, and there hadn’t been since the 1975 referendum to join the EU [..].

[T]he government never laid the ground for a pro-EU referendum, despite numerous examples of Britain’s ability to sway European policy. We put forward proposals that blazed the trail for a digital single market and the Energy Union that eventually became the EU’s response to Russia’s invasion of Crimea. And we rescued the Commission’s efforts to end mobile telephone roaming charges and pushed hard on improving airline safety. A Business Task Force with six prominent British businesspeople looked at all the EU regulations that should be scrapped — and managed to get two-thirds of their recommendations implemented within a year. 

But Cameron never turned these victories into high politics. He preferred highlighting achievements he knew would play well in the House of Commons — vetoing changes to the Lisbon Treaty, capping the EU’s budget, ensuring that the U.K. would not be liable for eurozone bailouts. These invariably portrayed him as defending the U.K. from the EU’s encroachments. We did not weave similar stories to show how EU membership helped the U.K.

---

So I guess in his own way, Cameron also kept "banging on" about Europe. Pity: The accomplishments on swaying EU policy are pretty good - it is unfortunate Britain will not be able to provide such input to EU anymore. 

But yes, the schism on EU is embedded deeply in British politics, Brexit is no random fluctuation. I remember reading a Game Theoretical paper on predicting the outcome of "the other" referandum,  about joining the monetary union, 1997. The paper uses Bruce. B. de Mesquita's method, the renowned Game Theorist, and they found, even under a Labor government, joining to EMU would be unlikely. This prediction was correct. Using this data, 

```
Actor,Capability,Position,Salience

Labor Party (Pro EU),1.0,8,40

Labor Party (Anti EU),0.5,4,40

Central Bank,0.1,5,60

Technocrats,0.1,10,40

Industrialists,0.1,5,40

Institute of Directors,0.1,4,40

Finance,0.1,9,60

Conservatives Anti-EU,0.3,1,95

Conservatives Pro-Eu,0.3,6,50
```

.. and [a code](bdm.py) that implements BBM's method, I found the same
result as well. Position coding: 0 means against, 10 means full
support for EMU. Note the abysmal level of support among pro-EU
convervatives, central bank, or even pro-EU Labor! This is 1997!

And of course I had to do the Brexit referandum. Using this data I
myself came up with,

```
Actor,Capability,Position,Salience

Labor Party (Corbyn),0.8,10,100

Labor Party (Others),0.3,10,100

ECB,0.1,10,100

Business,0.3,10,100

Finance,0.3,10,100

Tory (Pro EU),1.0,10,70

Tory (Anti EU),1.0,1,100

Murdoch,0.8,1,100

Monarchy,1.0,5,100
```

The result was 50/50. Note: The odd thing here was that there was no
give-and-take among actors, the result was a simple median
average. Not sure if this kind of thing happens a lot, maybe it was a
coding problem.. it was weird. If true, it could be interpreted that
the Pro-Anti-EU positions in Britain were too set in, noone would
compromise, it all came down to a stupid average.

Interesting points: Monarchy was neutral, absent and silent. Fuckin'
Murdoch media were incensed and half-mad as usual.  "But the data
above does not include 'the people'?". Yes - because the people are a
mere reflection of the stakeholders who know more about the
issues. Sorry - I know some idealistic politicians want things to be
the other way, every position, every trade issue, minutiae is followed
and judged by the people, but people do not know and do not care. Even
on presidential elections in US for example, they vote looking at 3
main attributes. That is why it is critical people holding public
offices to their damn job, and not keep badgering people on every
detail of their job. If more people involvement is needed, that will
be a different system, not this one.

Note: BBM has a newer method which is fully Game Theoretic (the one
implemented above was quasi GT). I would highly advise governments to
employ his services. 












