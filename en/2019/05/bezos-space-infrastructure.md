# Infrastructure for Space, Bezos

Good talk by Bezos. To get to space we need to build infrastructure;
our generation's work.

[![](http://img.youtube.com/vi/GQ98hGUe6FM/0.jpg)](http://www.youtube.com/watch?v=GQ98hGUe6FM)

He mentioned O'Neill stations, living environments with artificial
gravity. with a million ppl per, a thousand of these things could
house a billion. They could be placed at any sufficiently close
distances to Earth, it'll work.

Liquid hydrogen is mentioned; truly the energy storage mechanism of
the future. It is good for rockets, it is good for heating,
electricity, anything we can think of. Basically any place we humans
are interested in will have water anyway, with electrolysis we can
turn that water into fuel, using solar panels.

So we are not leaving Earth, simply stepping outside it for more
options, and even, for a little exercise. It's good to get used to
being in space, with bigger and bigger steps each time. Also these
stations will be Earth-like, not too far from Earth, best of both
worlds so to speak. Killer asteroid? Covered! Even with Earth gone a
few of these things would probably make it.

Blue Origin rockets, built for reuse, and the moon, a perfect
playground, is suitable for the task. It all seems to line up with WH
return-to-moon announcement, that'll work for their favor. 

<a name='energy'/>

## Energy

The energy use projections are iffy though. The 10,000 Watts / person
is probably from *Seeding the Universe with Life* By Michael Noah
Mautner. Let's take that as is,

```python
wattperPerson = 10000
pop = 8*1e9
print (wattperPerson * pop / 1e12, 'Terrawatts')
```

```text
80.0 Terrawatts
```

will be needed for everyone. How much does the Sun supply?

[Link](https://ag.tennessee.edu/solar/Pages/What%20Is%20Solar%20Energy/Sun's%20Energy.aspx)
"At the upper reaches of our atmosphere, the energy density of solar
radiation is approximately 1368 W/m2 (watts per square meter).  At the
Earth's surface, the energy density is reduced to approximately 1000
W/m2".

```python
texasArea = 700000 * 1e6 # meter square
sun = 1000 # Watts per meter square
eff = 0.50 # panel efficiency
print (sun*texasArea*eff / 1e12, 'Terrawatts')
```

```text
350.0 Terrawatts
```

Even with 50% panel efficiency, an area of Texas can supply more than
four times the energy needed.

Important point 10 KW / person is a first-world number. Not everyone
in the world is there yet.

Plus currently we live in luxurious consumption, and waste. Imagine
how much energy is wasted in commuting. People travel distances daily
that would be unthinkable 100 years ago, and it isn't advance. It is
waste.

No need to go to space for energy, because in space energy gain
becomes 1368 W/m2, from 1000 W/m2. It isn't doubling, or tripling
gain. World population will double in 70 years with 1% annual
population growth.  Until then, and for a long time, we can just
increase panel area.

Also there is such a thing as carrying capacity; in population models
this number is the threshold beyond which more life cannot be
supported, and there is no harm in that. That regulation will happen
on its own, we don't have to lose our minds thinking about it.



