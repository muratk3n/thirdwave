
```python
import pandas as pd, urllib.request as urllib2, io
url = "ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt"
r = urllib2.urlopen(url).read()
file = io.BytesIO(r)
df = pd.read_csv(file,comment='#',header=None,sep='\s*')
g = df.groupby(0)[3].mean()
print (g)
```




