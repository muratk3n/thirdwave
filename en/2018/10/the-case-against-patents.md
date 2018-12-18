# The Case Against Patents

[Paper](https://files.stlouisfed.org/files/htdocs/wp/2012/2012-035.pdf)

The case against patents can be summarized briefly: there is no
empirical evidence that they serve to increase innovation and
productivity, unless the latter is identified with the number of
patents awarded – which, as evidence shows, has no correlation with
measured productivity. This is at the root of the “patent puzzle”: in
spite of the enormous increase in the number of patents and in the
strength of their legal protection we have neither seen a dramatic
acceleration in the rate of technological progress nor a major
increase in the levels of R&D expenditure [..]

A closer look at the historical and international evidence suggests
that while weak patent systems may mildly increase innovation with
limited side-effects, strong patent systems retard innovation with
many negative side-effects. Both theoretically and empirically, the
political economy of government operated patent systems indicates that
weak legislation will generally evolve into a strong protection and
that the political demand for stronger patent protection comes from
old and stagnant industries and firms, not from new and innovative
ones. Hence the best solution is to abolish patents entirely through
strong constitutional measures and to find other legislative
instruments, less open to lobbying and rent-seeking, to foster
innovation whenever there is clear evidence that laissez-faire
under-supplies it [...]

A second widely cited benefit of patent systems – although not so much
in the economics literature – is the notion that patents are a
substitute for socially costly trade secrecy and improve communication
about ideas. From a theoretical point of view the notion that patents
are a substitute for trade secrecy fails even in the simplest
model. If a secret can be kept for N years and a patent lasts M years
then an innovator will patent exactly when N <= M. Hence, only those
things will be patented for which the secret would have emerged before
the patent expired, while those for which the secret can be kept will
not be patented. [..] It is also the case that modern “disclosure” in
patents is negligible – it is essentially impossible to build a
functioning device or software program from a modern patent
application [..]

The related idea that patents somehow improve communication about
ideas – a notion key to the “public-private” partnership between
governments and private research organization in which the government
funds the research and then gives the private organization a monopoly
over anything developed in the course of research – is backed neither
by theory or evidence. It is impossible to study the history of
innovation without recognizing that inventors and innovators exchange
ideas as a matter of course and that secrecy occurs, in those cases in
which it occurs, only in the final stages of an innovation process,
when some ambitious inventors hope to corner the market for a
functioning device by patenting it. A good case in point is that of
the Wright brothers, who made a modest improvement in existing flight
technology which they kept secret until they could lock it down on
patents, then used their patents both to monopolize the U.S. market
and to prevent innovation for nearly 20 years [..] The role that
Marconi and his patent played in the development of the radio is
altogether similar [..]

The conventional view starts with competitive equilibrium and observes
that welfare losses from small price variations are quadratic as a
function of the price, hence grow very slowly as the price
increases. In the case of full monopoly – as is the case with patents
– we are not interested in small price deviations from competition but
rather we are interested in pricing near the top of the profit
function. Witness for example the fact that patented pharmaceutical
products often sell for hundreds of times the marginal cost of
production as some astonishing pricing differences between the US and
the European markets show. Here social loss increases nearly linearly
with prices, while the deviation of profits from the maximum are
quadratic. Hence small price increases have a only a small effect on
profits – although still worthwhile from the perspective of the
monopolist – with substantial social loss. It is impossible to observe
the behavior of modern IP monopolists without recalling this
theoretical prediction. Most of the copyright wars revolve around
measure to prevent piracy, empirically a relatively minor factor as
far as profits of media corporations are concerned [..] In the case of
patents, and particularly pharmaceutical patents, the situation is
even more severe [..T]he empirical study of the Quinolones family of
drugs [..] measures the economic consequences to India of the
introduction of pharmaceutical patents for this family of drugs and
concludes that the consequence to third world India will be nearly 300
million USD in welfare losses [..]

Patenting has exploded over the last decades. [..]. In less than
thirty years, the flow of patents roughly quadrupled. By contrast,
neither innovation nor R&D expenditure have exhibited any particular
upwards trend, not to speak of factor productivity [..]

One could argue that purely defensive patenting is pretty harmless –
after all it costs only about $40,000 to file a successful patent
application, and doing it on a large scale may make it
cheaper. However the acquisition of large patent portfolios by
incumbents creates huge barriers to entry. [..]

There is little dispute among economists that a well-designed patent
system would serve to encourage innovation [..] but, again, there is
little dispute among economists that the patent system as it exists is
broken. ... As we will document in the next section, in our view the
evidence is instead clear that the patent system taken as a whole does
not play an important role in spurring innovation [..].

If a well-designed patent system would serve the intended purpose, why
recommend abolishing it? Why not, instead, reform it? To answer the
question we need to investigate the political economy of patents: why
has the political system resulted in the patent system we have? Our
argument is that it cannot be otherwise: the “optimal” patent system
that a benevolent dictator would design and implement is not of this
world and it is pointless to advocate it as, by doing so, one only
offers an intellectual fig-leaf to the patent system we actually have,
which is horribly broken. [..]

Now we need to provide some support for that initial empirical
statement: if there is to be any rationale for patent systems, with
all their ancillary costs, it must be that they actually do manage to
increase innovation and productivity. What is the evidence? How can we
say so definitively that there is no evidence that patents have the
desired effect? [..]

Except for two of the possible specifications (see below) there is, in
general, no statistically significant correlation between measures of
productivity (both labor and TFP) and patenting activity (both number
and citations). This is a more surprising result than one would expect
on the basis of purely theoretical considerations. In fact, one would
expect patents to be at least a decent predictor of productivity
growth across sectors, certainly for the last couple of decades during
which their use was extended to more and more sectors. This finding
leads us to conjecture that the use of patents either as a defensive
or as a rent seeking tool [..]

---

I was able to [replicate](patents-code.md) the regression [geek] with
fixed effects, accounting for year and industry [/geek] between TFP
and number of patents per year - see code, data ref is also there. TFP
is total factor productivity [geek] the portion of output not
explained by the amount of inputs used in production, so its level is
determined by how efficiently and intensely the inputs are utilized in
production [/geek].

Indeed as the paper says the relationship is weak as to be
non-existent.






