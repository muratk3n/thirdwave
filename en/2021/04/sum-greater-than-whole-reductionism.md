# Good Reductionism and Nonlinear Power

*Das Ganze ist etwas anderes als die Summe seiner Teile* (the whole
is something else than the sum of its parts) -- Kurt Koffka

I hear criticisms using the words "oh but that's too reductionist" on
analysis' that might involve break an issue into individual
components.. This criticism is usually misguided and I will try to
outline why. They miss the interaction, the nonlinearity of those
"pieces" and on the reverse side, the power that stems from the
combination of those little pieces that gave us much of the modern
world today. It's key we understand both sides of this equation.

In a system we see pieces, but how are they together? How were they
added? *Linear* addition of components is uninteresting.. They are
simple to see, and frankly will not achieve much beyond their domain.
Twice of something that do X, can do 2X. I have A, add B, I get
A+B. There is nothing to this. The analysis and creation of such
mechanisms yield to average results.

However when scientists analyze interesting systems, or engineers
build them, what they look for is individual components, yes, but also
the *nonlinear ways* they can interact. It is this interaction that
leads to power. Look at the way the V-engine shaft turns,

![](vengine.png)

It is a simple rotation, right. One shaft. There are two other axes
connected to it. But look at the connection, at different
angles. Rotation easy. Connecting easy. Rods easy. But connect two, to
the same shaft, at angle, gives you this,

[Video](https://drive.google.com/uc?export=view&id=18wE8NaHsydycnITM_OGuDX3WMrjndPgN)

We just created an orderly movement, one push after another, and guaranteed
certain force, using "simple components".

What if I wanted to create a push action at different intervals, not
just regular?

I immediately try to think of simple components, and try to achieve
nonlinearity through interactions.. Simple rotation. Simple rod. But
the rotating object is not round, has certain nonlinear shape which is
how it interacts with the rod, and that in turn gets pushed in an
interval I want.

[Video](diff-rhytm.gif)

Let's look at a subect I studied, optimization. In this subject, we
run our algorithms on "funky 3D shapes" that are famous for having
many ups and downs, we want tricky shapes bcz the minima searching
algs usually looks to its nearby region, we want to see if they will
"fall" into one of those holes and get stuck there. So the subject
over the years zoned in to a few of those funky shapes that are the
result of short, simple formulas, which gives us good examples now to
demo how complicated results can be the result of simple components.

Here is one of those famous functions, the Hölder table function,


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D    
from matplotlib import cm

L = 5
x = np.linspace(-L, L, 100)
y = np.linspace(-L, L, 100)
X, Y = np.meshgrid(x, y)                            
Z = -np.abs( np.sin(X)*np.cos(Y)*np.exp(np.abs( 1- np.sqrt(X**2+Y**2)/np.pi  ))  )

fig = plt.figure()
ax = fig.gca(projection='3d')                      
surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis)
plt.savefig('out.png')
```

![](holder.png)

Its formula is

$$
f(x,y) =
-
\bigg|
\sin(x) \cos(y) \exp \left( \bigg| 1 - \frac{\sqrt(x^2+y^2)}{\pi}  \bigg| \right)
\bigg| 
$$

Short and sweet. There is a boring cosine, boring sine, x and y, a few
additions.. But let's see how are these components put together;
Nonlinearly.

Sine *times* cosine, *squared* x and y, only then added. The result is
"the table we see, nothing that u could have guessed by looking at the
components. The whole is something else than the sum of its parts
(meaning linear sum).

Same with music. Here are the components that make up K-Pop band BTS's
song Dynamite, written by the British composer David Stewart [2]. 

<table>
<tr>
<td>
<audio controls="controls">
  <source src="https://drive.google.com/uc?export=view&id=12Jo-UCYO80oBnz2GDVf5HFldtapS3i5I">
</audio>
</td>
<td>
<audio controls="controls">
  <source src="https://drive.google.com/uc?export=view&id=1ooRjn-sHR8AfkTrGiUo2HQPJBgVbozGk">
</audio>
</td>
<td>
<audio controls="controls">
  <source src="https://drive.google.com/uc?export=view&id=1KLMiRvfR-8hDn_H1mg9ejw2d4TEavqng">
</audio>
</td>
</tr>
<tr>
<td>
<audio controls="controls">
  <source src="https://drive.google.com/uc?export=view&id=1f4rtgBiXMxaDcRFrt17VJ8JSOeIdUyu1">
</audio>
</td>
<td>
<audio controls="controls">
  <source src="https://drive.google.com/uc?export=view&id=1yabQPKCpt1f9EY3cXkERfE11MdhdI2Ya">
</audio>
</td>
<td>
<audio controls="controls">
  <source src="https://drive.google.com/uc?export=view&id=1wEg_g574E1EaOkIznjld2Q6P9u0Hdy4i">
</audio>
</td>
</tr>
<tr>
<td>
<audio controls="controls">
  <source src="https://drive.google.com/uc?export=view&id=1-6fDaf5y6L6Dhjhv3w1bjtJ_5zA974ss">
</audio>
</td>
<td>
<audio controls="controls">
  <source src="https://drive.google.com/uc?export=view&id=1-Z1mtAwsJ5TwYJPv8B0e4MV3-GCJ5roa">
</audio>
</td>
<td>
<audio controls="controls">
  <source src="https://drive.google.com/uc?export=view&id=1YHatoBHUfzY66L7QIkJjTUVUT6tpYzj9">
</audio>
</td>
</tr>
</table>

Simple, boring components right? But they are crafted in a certain way, so when
they are put together, this results,

<audio controls="controls">
  <source src="https://drive.google.com/uc?export=view&id=1MzNva_prkzCmM2O3FmhtotyOtU1AtHvD">
</audio>

Analyzing

When scientists analyze complex systems, and if they came up with
simple additive looking results, we need to be careful, look beyond
it, and see if they used nonlinearity elsewhere. $u_x + u_t = 0$ might
seem an seem inocuous looking statement, but that subscript hides
concept from differential calculus that took centuries to perfect. So
scientists sometimes smush, twist, bend a problem to get a "linear
superposition", lest be mistaken, there will be much nonlinearity
hidden in the path of getting there. It's like taking the log of
exponential data that gives you a simple, straight line. The act of
taking the log, and recognizing the exponential curve is what gave us
that linear line. 



References

[1] https://en.wikipedia.org/wiki/Test_functions_for_optimization

[2] [The Making of BTS Dynamite](https://youtu.be/qBCM1Fy-ByY)

