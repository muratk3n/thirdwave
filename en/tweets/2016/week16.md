
But the success of [investment firm AHL's] machine learning experiments in recent years led the company to plough more money into the field, and it is now the single biggest investment area at AHL [..]. AHL has been researching machine learning — a field of artificial intelligence where dynamic algorithms pore over vast data sets for patterns — for five years, and has been using the technique in trading for the past three years. The results have been encouraging, according to executives at the hedge fund.

A machine learning strategy helped one of AHL’s funds swing from a narrow loss to a narrow gain in August last year, when markets were convulsed by concerns over China, by autonomously buying and selling stock at vital junctures in the turmoil. Many traders initially stood on the sidelines, unable to quantify rapidly-changing data.

“It learnt to buy the dip,” said Nick Granger, co-head of research at AHL and deputy chief investment officer. “No one taught it to do this, it learnt how to do this when we showed it a lot of data.

Genuine advances in this field are welcome, but watch out

Ernie Chan

There was an article in the New York Times a short while ago about a new hedge fund launched by Mr. Ray Kurzweil, a poineer in the field of artificial intelligence. (Thanks to my fellow blogger Yaser Anwar who pointed it out to me.) The stock picking decisions in this fund are supposed to be made by machines that "... can observe billions of market transactions to see patterns we could never see". While I am certainly a believer in algorithmic trading, I have become a skeptic when it comes to trading based on "aritificial intelligence".

At the risk of over-simplification, we can characterize artificial intelligence as trying to fit past data points into a function with many, many parameters. This is the case for some of the favorite tools of AI: neural networks, decision trees, and genetic algorithms. With many parameters, we can for sure capture small patterns that no human can see. But do these patterns persist? Or are they random noises that will never replay again? Experts in AI assure us that they have many safeguards against fitting the function to transient noise. And indeed, such tools have been very effective in consumer marketing and credit card fraud detection. Apparently, the patterns of consumers and thefts are quite consistent over time, allowing such AI algorithms to work even with a large number of parameters. However, from my experience, these safeguards work far less well in financial markets prediction, and over-fitting to the noise in historical data remains a rampant problem. As a matter of fact, I have built financial predictive models based on many of these AI algorithms in the past [Chan has a PhD in machine learning]. Every time a carefully constructed model that seems to work marvels in backtest came up, they inevitably performed miserably going forward. The main reason for this seems to be that the amount of statistically independent financial data is far more limited compared to the billions of independent consumer and credit transactions available. (You may think that there is a lot of tick-by-tick financial data to mine, but such data is serially-correlated and far from independent.)

This is not to say that quantitative models do not work in prediction. The ones that work for me are usually characterized by these properties:

• They are based on a sound econometric or rational basis, and not on random discovery of patterns;

• They have few or even no parameters that need to be fitted to past data;

• They involve linear regression only, and not fitting to some esoteric nonlinear functions;

• They are conceptually simple.

Only when a trading model is philosophically constrained in such a manner do I dare to allow testing on my small, precious amount of historical data. Apparently, Occam’s razor works not only in science, but in finance as well.

Yes

Chan is the author of two books on algorithmic / quantitative trading - so he knows what he is talking about. In another post he mentions of feeling unease whenever he hears of some neural net based trading model that'll have gazillion free parameters to fit, an obvious non-linear approach and prone to overfitting on serially dependent data. 

There is a lot of beautiful mathematics to use on finance and trading, but they might not always fall under the data mining / AI approach. If data mining approaches are used, they need to be handled with care - with a keen eye for the statistical aspects on how the algorithms behave on the data at hand. 

Overall though, more quantitative approaches are a welcome innovation - they bring more rationality to the market, and also more liquidity. Speculation is a good thing - and it is the kind that we want, mathematical, on open exchanges, rather than the ones through over-the-counter, and too-connected-and-big-to-fail sausage makers / banks. 

Question

But ppl in finance are not curing cancer.

Not everyone will work on that kind of research

.. no matter the incentive - not everyone should either. While on this topic, I must say I am a little frustrated by this constant degrading of finance, as if it the whole industry is born of an evil seed. Providing liquidity to grain, metal producers, buyers, sellers is a good thing. During the dot-com boom there were sites offering pet-services, or  things like "online-laundry". Are these truly essential services compared to finance? All this stuff is luxury at the end of the day, isn't it? So is getting a haircut, watching sports, sitting at Starbucks for that matter. If we scratch the surface on all economic activity a little, almost nothing will remain standing, except basic goods and services.

Question

But while these [online laundry, pet upkeep, etc] services are being developed, they spur innovation in related tech (coding of the backend, handling of data, prediction for CRM so forth), math, and management techniques. 

Right

But you can say that about anything. Side-innovation is especially potent in finance, since it is mostly if not all about information. 

Question

There is inequality. Health care is broken. People don't spend.

Give people free money

Knowledge driven 3W economy brings with it more uncertainties, non-permanent jobs / gigs, life is too dynamic. This is the result - on the one hand people are forced to fight a cage match to "earn", on the other hand they are asked to consume what are essentially luxury services.

No wonder company earnings are in a do-doo.

More innovation will also require a better safety net BTW. So however we look at it, it all comes to the same thing.

Washington Post

There’s little doubt that what has happened to America’s middle class has helped to create the climate that has fueled Trump’s [i.e. fascism's] sudden rise [..] For most families, the two recessions have wiped out previous gains and widened the wealth and income gap between the wealthiest and all others. “The losses were so large that only upper-income families realized notable gains in wealth over the span of 30 years from 1983 to 2013,” according to the Pew study.

And there is that

Question

Why not give people services?

Too old school

.. because the needs are too varied (see the answer above), and now we know about them (due to freer flow of information).

If my memory serves correctly, the first exampe of a "social" service took place a few centruries ago, the state delivered a bottle of milk at the doorstep of each home. A seemingly nice thing to do - but it also demonstrated the second-wave industrial age type of thinking. Nearly half the people in the world have an allergy for milk - they can't digest the shit. But 2W at the time was producing many such one-size-fits-all products, it saw the society that way, it saw life that way. The state simply took that milk that was being produced en masse, and gave it to people, en masse. Now we know this cannot work. It's better to give people money so some buy milk, but others a haircut, some healthcare, some bread, ..  whatever.

Question 

What will government do then?

Inspect food, watch borders, smart regulation, fund research









at

April 18, 2016
















There have been extinction level events triggered by asteroid hits on
the Earth, but it is also known Jupiter with its massive size
protected Earth before, pulling asteroids to itself. Are these views
contradictory?

No

With the Planet 9 explanation, it all makes sense. Jupiter is massive
(in fact some jokingly refer to our solar system as "Jupiter and some
debris"), it saved us before, but P9, being a planet itself, can enter
deep into the solar system, knocking stuff in the direction of
Earth. Jupiter would not be able to run interference against those.

Some more info on the subject: about the periodicity and measurement
of extinction events, paper. My notebook that looks at frequencies of
extinction events [geek] using the Lomb-Scargle method that computes
statistical significance of peaks, rather than direct Fourier Analysis
[/geek]. I reverse-engineered the graph here  with image processing to
get its raw data (who da man!) and compute the periods of extinction
events. The result is this, and periods in this. There is one period
of 25 million years, and one for around 70 - dinosaurs were wiped out
66 million years ago during one of these I assume.

[1](ex1.png)
[2](ex2.png)
[3](extinct.csv)
[4](extinct.md)

News

SpaceX succeeded landing a rocket on a boat.

Excellent

Congrats.

Question

Favorite phone prank?

[Bodankadonk](https://www.youtube.com/watch?v=-qVYi1bQ0zk) by Tracy Morgan. Still unsurpassed.









