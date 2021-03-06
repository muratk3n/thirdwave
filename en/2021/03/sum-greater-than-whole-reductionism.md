# Good Reductionism (Sum Is Greater Than Whole)

![](vengine.png)

[Link](https://drive.google.com/uc?export=view&id=18wE8NaHsydycnITM_OGuDX3WMrjndPgN)


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D    
from matplotlib import cm

L = 5
x = np.linspace(-L, L, 100)
y = np.linspace(-L, L, 100)
X, Y = np.meshgrid(x, y)                            
Z = -np.abs( np.sin(X)*np.cos(Y)*np.exp(np.abs( 1- np.sqrt(X**2+Y**2)/np.pi  ))  )

fig = plt.figure()
ax = fig.gca(projection='3d')                      
surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis)
plt.savefig('out.png')
```

Hölder table function

$$
f(x,y) =
-
\bigg|
\sin(x) \cos(y) \exp \left( \bigg| 1 - \frac{\sqrt(x^2+y^2)}{\pi}  \bigg| \right)
\bigg| 
$$

https://en.wikipedia.org/wiki/Test_functions_for_optimization

![](holder.png)






