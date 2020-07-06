# Power

Power is measured in Watts, energy transferred per unit time (Joule
per second). We say someone is powerful, indicates transferring energy
(kick) to someone (the ass) in a short time. Boom, ass-kicked. In unit
(short) time. 

How long can this person keep kicking ass? That is capacity. How long
can a battery last? Same idea. This is Wh, Watt-hours. How many watts
can be given in one hour.

Now the marking on batteries can be weird. Another way to get to Watt
is Voltage times Ampere (per unit time thing is inside Ampere so it
works out). But you will see batteries are usually only marked in mAh
(mili ampere hour). Where is the volt?

https://www.bixpower.com/Battery-Cell-Chemistry-Comparison-s/2392.htm

This is a very misleading unit. When a battery is rated with mAh or
Ah, it should always associated with a voltage. A 10Ah @ 12V battery
capacity is bigger than a 10Ah @ 5V battery. However, there are a lot
lot of lithium batteries on market that do not state voltage when
claim their mAh ( or Ah) capacity. In these cases, most likely they
measure with lithium battery cell voltage, which is 3.6V or 3.7V. By
time 3.6 (or 3.7), then divided by 1000, it will be its accurate
Watt-hour capacity. For example, a 10,000mAh battery actual capacity
is 10000 x 3.6 /1000 = 36 Watt-hour.

Ex: my camping light, Fenix CL20R. It has 1600mAh battery. Voltage,
not sure. It says it compares with 7 AAA batteries. Bats have 1.5 V,
in series, 10.5 Volts.

How long will my light last? Light level measured in lumens,

300 lumens (6 hours)
130 lumens (12 hours)
40 lumens (20 hours)
1 lumen (200 hours)

I need Watts. How to convert to Watts?

https://www.rapidtables.com/calc/light/how-lumen-to-watt.html

LED lamp	80-100 lumens/W

Then, 300 lumens = 3 W

So, 1600 mah * 7 * 1.5 volts / 1000

```python
1600 * 7*1.5  / 1000
```

```text
Out[1]: 16.8
```

16.9 Wh. We have 3W lumens, how long does it last?

```python
np.round(16.8 / 3, 2)
```

```text
Out[1]: 5.6
```

Description seems correct. 

