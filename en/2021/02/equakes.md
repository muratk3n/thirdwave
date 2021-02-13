# Earthquakes


```python
import pandas as pd, datetime

from quakefeeds import QuakeFeed
feed = QuakeFeed("4.5", "month")
res = []
for i in range(len(feed)):
    d = datetime.datetime.fromtimestamp(feed[i]['properties']['time']/1000.0)
    s = feed[i]['properties']['mag']
    res.append([d,s])

df = pd.DataFrame(res).sort_values(by=0)
df = df.set_index(0)
df.columns = ['Magnitude']
print (df.tail(5))
df.Magnitude.plot()
df.Magnitude.rolling(window=20).mean().plot()
plt.title('Monthly Earthquakes')
plt.savefig('quake.png')
```

```text
                         Magnitude
0                                 
2021-02-13 07:30:56.150        5.2
2021-02-13 08:09:12.552        4.9
2021-02-13 08:15:21.905        4.9
2021-02-13 08:18:33.479        5.3
2021-02-13 08:19:51.545        4.5
```

![](quake.png)















