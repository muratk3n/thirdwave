# Directions

There is something rotten about all the direction software.

How does a pedestrian go from point A to point B? I axed online, and
the result sucked something bad... I was at a train station so I went
to the train station's information desk, and axed the official. He
checked a similar direction software, and laughed at the result, and
said "this is crap, let me tell you how to go there".

The output was similar to this, but the output the man was looking at
was longer, it was like "get on bus, get off bus, walk, get on train"
etc. The directions the official had in mind was "get on train D,
change to C at X, done". Only two train lines were necessary,
utilizing only one form of transportation.

I can almost see the coding behind these things in my
head.. calculating shortest path is one of the oldest problems in
computer science. But having a "vertex" for a stop, and an "edge"
between  two nodes is not enough to compute a route
efficiently. Staying on one form of transport needs to be preferred,
this would require only a simple weighting change in the
optimization. Certain forms of transport also needs to be favored over
others, train better than bus (yuck), walking in the beginning and end
is okay, but not in the middle, etc. These additions are not that
hard.

And please, IT companies, do not let loose some monkey machine
learning algorithm on this problem hoping the algorithm will "learn"
routes from .. base pixels, people's movements, or whatever the flunk
is the most granular thing with the most available data.. The
optimization changes are doable. Code the shit in. TODAY.

![](rott.png)
