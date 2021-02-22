# LPG Cylinders, Energy, Taxis, Kitchens

You know, you can heat, light a house using portable LPG
cylinders. Such things are common in many kitchens in various
countries. Completely off-grid, cheap.

<img width="200" src="https://pbs.twimg.com/media/EurzkRsXEAUWPwi?format=jpg&name=small"/>

India, TR.. never saw in US, or DE, the image above was from an AU
site, cld be prevalent there

Standard cylinder < 15 dollars. Call a number, have one delivered at
home, like ordering pizza. These gas companies have
[stores](https://pbs.twimg.com/media/Eur2kgXXUAI9Yoy?format=jpg&name=small),
everywhere, they have those canisters stacked up, ppl see them passing
by. Even some taxi cabs converted to run on this thing..

One delivery company, Aygaz, [sold](https://www.aygaz.com.tr/uploads/yatirimci-iliskileri/yatirimci-sunumlari/25a0abbc_45db_4a83_a0d7_f495d521cfa9__aygaz-ir-presentation_february-2020.pdf)
25 million standard cylinder worth of this stuff in 2019.

Empty cylinders get refilled in a [plant](https://pbs.twimg.com/media/EuvTpEwWgAAh9ac?format=jpg&name=small).
Call the same number, cylinder gets picked up. Like reverse-delivery of pizza

They pack a punch (molecules better than electrons). Ex, standard size
12 kg, keg size cylinder based stove in kitchen, it can go for
years with medium to low usage.

Let's verify. High-heat flame energy from an all-electric, single
heater stove is 1500 Watts, which is 1/3 efficient compared to gas,
standard LPG cylinder = 12 kg LPG, LPG is 46-51 MJ/kg, 1 MJ = 277 Watt
hour

```python
print ('%0.2f h' % (46*12*277.7/(1500/3)))
```

```text
306.58 h
```

This rings true, if you left stove on at high heat, it can
continuously run for >300 hours, have it on 1 hr a day, lasts a year.

Think about how much energy that is, at such a cheap price.

Imagine using that energy to heat up a house, power all electronic items.

Annual energy required for typical house heating is 8,208 kWh,
electricity for all other items 3,700 kWh.

```python
energy_req = 8208 + 3700
cylinder = (4*16*46*277)/1000.
print (energy_req / cylinder)
```

```text
14.602299482027938
```

Every month, you get 4 of those cylinders (little bigger 16 kg size),
you'd be fine.

And just saw there are 45 kg versions

<img width="340" src="https://pbs.twimg.com/media/EuvTvxaXUAAgkJ9?format=jpg&name=small"/>

LPG is fossil of course. But same tech could be extended to renewable
gases, fuels. Portable cylinders could appeal to low end, for off-grid
type usage.

For high end, on-grid, pipelines are still way to go... Or in bulk, H2
is used on generator turbines to generate electricity. 
