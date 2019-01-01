# Rivalry Check

Why would this rivalry exist? More importantly, for the data investigation, how would this rivalry leave its mark in data so it can be caught?

Let's look at the  evolutionary landscape: we are transitioning to a supersymbolic economy in which the most precious resource is talent. US wants talent, does not want to lose it to EU. Talent wants nice cities, safe environment, nice parks. That means if US suffers a terror attack of any kind, it would have a bad image for talent. Then, the theory goes US' shadowy pukes would instigate an attack  in Europe in short time, in response, to balance their image. 

My plan was I would get terror attack data, look at US-EU pairing first, for each US attack, calculate the difference in days to the closest EU attack. These collection of numbers are "waiting times" for this supposed tit-for-tat scenario. Then I calculate the same numbers for US-South America, US-China so forth. Now we have bunch of numbers for each pairing representing their distributions. We then check if US-EU numbers are smaller than all the rest of the regional waiting times, and if that smallness is statistically significant. [geek] The statistical test to use for this is two sample Wilcoxon test, as the waiting time data is distributed non-normally -exponentially- [/geek].

First I wanted to use GDELT data in this analysis, Google provides access to it, but  it turns out GDELT has a lot of repeats, i.e. for Charleston attack people mourning about it, commenting etc. would appear  as data points with an incorrect status code indicating an actual attack. The GDELT option would need a lot of dedup code. So I looked for other data sources, and found GTD available in Excel format covering attacks between 1970-2014. I converted it into CSV and zipped it, code and data below:

Data, Notebook

[geek]Me not like binary formats like Excel, oddly it turns out zipped up CSV is smaller than xlsx, and processed by Python Pandas at the same speed [/geek].

The analysis showed, at first, looking at all data, US-EU attack delays are smaller than all the rest, and the difference was significant.

The wait times were smaller than even for US-South America pairing where one would expect drug related crimes would be common. But the moment we change date filter to look at data after 1980, things change. Then US-EU and US-SA are not statistically different from eachother (but still smaller from other regions, China, Russia, Australia, Canada). 70s must have been a bad time in Europe. Also, removing UK from Europe list, even for the entire time periods, again causes a US-SA tie, possibly due to all these IRA attacks there. But since UK is part of Europe (heh heh) I kept its data in the US-EU calc.

In conclusion though, using the assumptions above, the hypothesis is disproved.

Other methods to use here: time-series analysis to identify dependence between time-lagged EU vs US attack data. I cannot get into that at the moment, as I have no time.






