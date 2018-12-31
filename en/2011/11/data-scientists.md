# Data "Scientists"

There is a new breed of software developer / analyst who call themselves "data scientists" who are mostly bunch of ex-IT programmers with shoddy mathematics skills that managed to learn some statistics, but all they really do is throwing some tools at an analysis problem.

Kaggle.com is a place where the these "scientists" meet. For those who dont know, clients go to Kaggle with analysis problems and they typically attach an award to the best analysis. Kaggle "crowdsources" these problems to anyone who is interested, records, tracks submissions, and selects a winner.

Recently there was a traffic flow analysis problem on this site. There's been decades of research on traffic flow analysis, the area in general is very similar to fluid flow -- you could easily view traffic as a function u(x,y,t) at time t and position x,y, and build from there. But no "scientist" has knowledge about partial differential equations, so they go nuts using bunch of black box methods that somehow identifies "patterns". The winner? Two dudes who report a success rate "within 1 minute of real travel time" (and get this, it is the best part) %73 percent of the time.

How would you feel if the plane you fly in obeyed the laws of physics %73 of the time? Or your pressure cooker was only built to contain its food %73 of the time? OK, these are high-risk, high-annoyance situations, but still, there is something missing here. This data science crap is middle-class scientism at its worst. Do we call Isaac Newton an "apple scientist"? Wasn't he also analyzing data? So the label sucks.

It seems we are failing to teach in schools, in literature what it means to mathematically model things. Schools give students lots of rote for solving neat problems that are all cooked up, but noone shows how wave equation can be derived starting from few key assumptions.

There can be noise in the data. That's not a problem. What we try in modeling is coming up with the best model so that the noise is "normal" or Gaussian. Once you have that model, there are many fitting tools that can fit the data, but there are no shortcuts while defining that model.

These models are very challenging, smart, we should be teaching how they are created, but instead, we give rise to monkeys that try to circumvent "the noise" but are ironically slapped down by the same statistics that they supposedly respect. We shared a post earlier about funding way more physicists than necessary. Many of these physicists research particle physics and any of them could enter that competition at Kaggle and it would be a slapfest. But they dont. Why? Because they are trying to uncover the mysteries of particles, while data monkeys are busy looking for magic wands. Supply is not meeting the demand here.

Watch for buzzwords in this space. People go nuts on stochastic blah, or Monte Carlo methods. Well, Monte Carlo methods are great for calculating intractable integrals, but for that, you have to know what an integral is. Right Mr. G? Oh, and this method was invented during the Manhattan project by physicists, and is deeply mathematical itself. There are no shortcuts.
