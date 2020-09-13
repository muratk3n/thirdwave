import matplotlib.pyplot as plt
import util

country = 'United Kingdom'
pop, df = util.estimate_Rt_for_country(country)
import matplotlib.dates as mdates
ax = df.plot('Date','Rt',linewidth=3,color='red',grid=True,ylim=(0,6),figsize=(12,8))
ax.xaxis.grid(True, which='minor')
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
plt.gcf().autofmt_xdate()
plt.legend(fontsize=16)
plt.savefig('Rt-%s' % country)
print (df[['Date','Rt']].tail(10))
