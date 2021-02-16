# Tweets

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">FuelCell Energy’s baseload power solutions deliver grid reliability with efficient and clean energy in the most extreme weather conditions. No wind, no sun, no problem. FuelCell Energy, always on. Stay powered. Stay warm. Stay safe. <a href="https://twitter.com/ERCOT_ISO?ref_src=twsrc%5Etfw">@ERCOT_ISO</a> <a href="https://t.co/bcUxkClecA">https://t.co/bcUxkClecA</a></p>&mdash; FuelCell Energy (@FuelCell_Energy) <a href="https://twitter.com/FuelCell_Energy/status/1361392708695261185?ref_src=twsrc%5Etfw">February 15, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

They apparently installed a remote access software so system could be
controlled from anywhere... But if something is accessible, connected
to the Net, hackers can access it too.

---

They need to take that shite off the Internet.

"Hacker tries to poison water supply of Florida city"

---

If an area as large as Texas was covered with panels today, it would
[provide](2019/05/bezos-space-infrastructure.md#energy) ample energy,
twice of what is required actually, for the entire world.

"If we run out of solar panel space on Earth, should we colonize space
for sunlight (through Stanford torus / O'Neil cylinder)"

---

<blockquote width="200" class="twitter-tweet"><p lang="en" dir="ltr">MUST-WATCH: Prime Minister <a href="https://twitter.com/BorisJohnson?ref_src=twsrc%5Etfw">@BorisJohnson</a> confirms UK will be &quot;putting a big bet on <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a>&quot; <a href="https://twitter.com/KwasiKwarteng?ref_src=twsrc%5Etfw">@KwasiKwarteng</a> <a href="https://twitter.com/annietrev?ref_src=twsrc%5Etfw">@annietrev</a> <a href="https://twitter.com/ASollowayUK?ref_src=twsrc%5Etfw">@ASollowayUK</a> <a href="https://twitter.com/grahamstuart?ref_src=twsrc%5Etfw">@grahamstuart</a> <a href="https://twitter.com/grantshapps?ref_src=twsrc%5Etfw">@grantshapps</a> <a href="https://twitter.com/redditchrachel?ref_src=twsrc%5Etfw">@redditchrachel</a> <a href="https://twitter.com/JacobYoungMP?ref_src=twsrc%5Etfw">@JacobYoungMP</a> <a href="https://twitter.com/Alex_Stafford?ref_src=twsrc%5Etfw">@Alex_Stafford</a> <a href="https://twitter.com/Jesse_Norman?ref_src=twsrc%5Etfw">@Jesse_Norman</a> <a href="https://twitter.com/samuelhall0?ref_src=twsrc%5Etfw">@samuelhall0</a> <a href="https://twitter.com/griffitha?ref_src=twsrc%5Etfw">@griffitha</a> <a href="https://twitter.com/GregClarkMP?ref_src=twsrc%5Etfw">@GregClarkMP</a> <a href="https://twitter.com/darrenpjones?ref_src=twsrc%5Etfw">@darrenpjones</a> <a href="https://t.co/jgKppXExeS">pic.twitter.com/jgKppXExeS</a></p>&mdash; UK Hydrogen Strategy Now (@UKHydrogenNow) <a href="https://twitter.com/UKHydrogenNow/status/1361033188932526082?ref_src=twsrc%5Etfw">February 14, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

As policy I'd encourage only megawatt scale of this tech, to be used
at a few power plants, easy to regulate. At end-user level, no, bcz it
would be much harder to control, and if reg is flaunted, its side
effects would be severe. End user only gets the renewable fuel,
pipelines transmit only renewable fuel.

"Bloom also intends to complete work on technology capable of
capturing and extracting carbon from the emissions of its
natural-gas-powered fuel cells. The company is 'working very hard to
demonstrate' the ability to combine 'blue hydrogen' production, or
turning methane into hydrogen and capturing the carbon emissions, with
electricity production"

---

You have to watch for these tech types.. even when they're scaring
you, they might be selling you. Like 'be scared of AI, boo!', the
indirect message being it is *that good*. U see.. ? Then seque into
'i've got some of that same tech that for your house, for your
lawnmower'.. (but no worries i had my people write it, and im the
caution guy here, so be afraid for other stuff but not my shit, and
buy it, quick!)'. Obviously they are full of shit, tech aint that
good, it's all hot air. 

---

Some earthquake plotting.. EQ of past 90 days, old to new is colored
light to dark, circle width is severity. The hope is maybe seeing a
geo progression of eq with a final big one culminating at the end..
Always looking for an angle here..

But Japan surely gets a lot of quakes

Retrieval [code](https://muratk3n.github.io/thirdwave/en/tweets/2021/util.py)

```python
import cartopy.crs as ccrs, cartopy, util
df = util.get_eq1()
fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_global()
ax.stock_img()
ax.coastlines()
ago = np.max(df.ago)-df.ago
s = np.power(3,df.mag)
ax.scatter(df.lon, df.lat, c=df.ago, \
           cmap=plt.cm.Reds, s=s, alpha=0.7,  \
	   transform=ccrs.PlateCarree())
ax.set_extent([94, 161, -10, 54], crs=ccrs.PlateCarree())
plt.savefig('eq.png')
```

<img width="340" src="https://pbs.twimg.com/media/EuU1vkRXUAEAAcx?format=jpg&name=small"/>

---

Industrial Age society, the Second Wave began in Western Europe with
the Industrial Revolution, and subsequently spread across the
world. Key aspects of Second Wave society are the nuclear family, a
factory-type education system and the corporation. The Third Wave is
the post-industrial society based on hi-tech with all its benefits and
adverse effects causing major attitude shifts in society. Institutions
are built around methods of production, so when a new wave arrives,
older structures around governance, education, health start to crumble
despite the best efforts of people working in them.

## For Members

[Link](https://thirdwave-members.herokuapp.com)

## Reference

[Nations and Nationalism, Culture, Narratives](/2013/02/nations-and-nationalism.md)

[The Fundamentals of Industrial Ideologies](/2011/04/fundamentals-of-industrial-ideologies.md)

[Education, Workplace](2017/09/education-workplace.md)

[Patents](/2018/09/patents.md)

[Democracy, Parties](/2016/11/democracy.md)

[Economy](/2018/05/economy.md)

[Globalization](/2018/09/globalization.md)

[Rome, The First Wave, Religion](/2017/12/rome.md)

[Human Nature & Health](/2020/07/human-nature.md)

[Climate Change](/2018/12/climate.md)

[The Middle East](/2019/07/middleeast.md)

[TR](../tr)

## Browse

[By Year](years.md)

[Search](search.html)

[Tweet Archive](/tweets/README.md)


