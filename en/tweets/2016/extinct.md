
Download file

https://en.wikipedia.org/wiki/File:Extinction_intensity.svg

Convert file to pgm with

convert  -crop 495x245+29+54 -resize 900x400 Extinction_intensity.svg  extinct.pgm

```python
import pandas as pd
from PIL import Image

im2=Image.open("extinct.pgm")
grady,gradx = np.gradient(im2)
grady = (grady>0).astype(float)
extin = np.argmax(grady,axis=0)
df = pd.DataFrame(extin)
df2 = df.max()-df
mymin = 1.
mymax = 52. - mymin
df3 = df2 / df2.max() * mymax
df3 = df3 + mymin
idx = np.linspace(542,1,len(df3))
df4 = df3.set_index(idx)
df4[0].to_csv('extinct.csv',header=None,index=None)
```

```python
ext = pd.DataFrame(pd.read_csv('extinct.csv',header=None))
ext = ext.set_index(np.linspace(542,1,len(ext)))
ext[0].plot()
ext = ext[0]
plt.savefig('ex1.png')
```

```python
from astroML.time_series import lomb_scargle

dy = 0.5 + 0.5 * np.random.random(len(ext))
omega = np.linspace(10, 100, 1000)
sig = np.array([0.1, 0.01, 0.001])
PS, z = lomb_scargle(ext.index, ext, dy, omega, generalized=True, significance=sig)

plt.plot(omega,PS)
plt.hold(True)

xlim = (omega[0], omega[-1])
for zi, pi in zip(z, sig):
    plt.plot(xlim, (zi, zi), ':k', lw=1)
    plt.text(xlim[-1] - 0.001, zi - 0.02, "$%.1g$" % pi, ha='right', va='top')
    plt.hold(True)
plt.title('Extinction Periods')
plt.savefig('ex2.png')
```





