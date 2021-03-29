
```python
import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('seshat-row.csv')
df = df[df.NGA == 'Konya Plain']
df1 = df[df['Variable'] == 'Polity territory'][['NGA','Polity','Date.From','Value.From']]
df2 = df[df['Variable'] == 'Polity Population'][['NGA','Polity','Date.From','Value.From']]
df1 = df1.dropna()
df2 = df2.dropna()
df1.to_csv('out1.csv')
df2.to_csv('out2.csv')
print (df2)
```

```text
               NGA   Polity Date.From Value.From
40220  Konya Plain  TrByzM1     630CE   11000000
40221  Konya Plain  TrByzM1     700CE    4500000
40222  Konya Plain  TrByzM1     800CE    5000000
40369  Konya Plain  TrByzM2     900CE    7500000
40370  Konya Plain  TrByzM2    1000CE   10000000
41027  Konya Plain  TrERom*     400CE   15000000
41028  Konya Plain  TrERom*     500CE   20000000
41029  Konya Plain  TrERom*     600CE   15000000
42198  Konya Plain  TrOttm1    1325CE     200000
42199  Konya Plain  TrOttm1    1350CE     700000
42200  Konya Plain  TrOttm1    1400CE    5000000
42351  Konya Plain  TrOttm2    1450CE    7000000
42352  Konya Plain  TrOttm2    1500CE    9000000
42489  Konya Plain  TrOttm3    1600CE   28000000
42888  Konya Plain  TrRomDm     300CE   40000000
```

```python
df3 = df1.merge(df2, left_on=['NGA','Date.From'], right_on=['NGA','Date.From'])
df3 = df3.rename(columns={"Value.From_x": "area", "Value.From_y": "pop"})
df3['date'] = df3['Date.From'].str.replace("CE","").astype(float)
df3['pop'] = df3['pop'].astype(float)
df3['area'] = df3['area'].astype(float)
df3 = df3.sort_values('date', ascending=True)
```

```python
df3['pop_scaled'] = (800000.0 / df3['area']) * df3['pop'] / 1e6
df3[['area','date','pop_scaled']].to_csv('out3.csv')
```

(1347–1351).[4][5] The latter was much shorter, but still killed an
estimated one-third to one-half of Europeans.

```python
df4 = df3.set_index('date')
df4['pop_scaled'].plot()
plt.axvspan(541, 549, color='y', alpha=0.5, lw=0)
plt.axvspan(1200, 1250, color='r', alpha=0.5, lw=0)
plt.axvspan(1347, 1351, color='y', alpha=0.5, lw=0)
plt.savefig('tst_01.png')
```

![](tst_01.png)
