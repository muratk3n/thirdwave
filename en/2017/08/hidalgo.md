# Product-Item, Economic Complexity, Country Competitiveness, Hidalgo

Data From

[Link](http://atlas.media.mit.edu/en/resources/data/)

Curated version,

[Link](https://drive.google.com/uc?export=view&id=1gYwaE_aLDQIfcGxIKiRcroHBTsvguBxP)

Below we create a model that represents a country's economy based on
the products it produces, and the complexity of those
products. "Complexity" of both the country and products it produces
will essentially be based on the number of different product *types*,
but the chicken-egg aspect of the deeper model will be teased out of
the product export raw data using the method below.

Model

The complexity of an economy is proportional to the average complexity
of its products, and, vice versa, the complexity of a product is
proportional to the average complexity of its producers. 

We could say $m_{ij}=1$ if country $i$ makes product $j$ , and
$m_{ij}=0$, otherwise, but we need a preprocessing stage first. Let's
say $X_{ij}$ is exports (in dollar amounts) of product $j$ of country
$i$. The Revealed Comparative Advantage of that country $i$ is

$$
RCA_{ij} = \frac{X_{ij}}{\sum_i X_{ij}} / \frac{\sum_j X_{ij}}{\sum_{i,j} X_{i,j}}
$$

Then if $RCA_{ij} > 1.0$ we set $m_{ij}=1$, 0 otherwise. 

The weights are $v_{ij} = m_{ij} / d_i$, $w_{ij}=m_{ij}/u_j$ where
the diversification of country $i$ and the ubiquity of product $j$ are
simply $d_i = \sum_j m_{ij}$, $u_j = \sum_i m_{ij}$. So if $c_i$ is
the complexity of country $i$ and $p_j$ is the complexity of product
$j$

$$
c_i = \alpha \sum_j v_{ij}p_j
$$

$$
p_j  = \beta \sum_i w_{ij} c_i
$$

where $\alpha,\beta>0$. We see the chicken-egg problem here. We
collect variables inside matrices $c$, $p$, $V=[v_{ij}]$ and
$W=[w_{ij}]$, then $c = \alpha V p$ and $p = \beta W c$.  If we
subtitute second the latter in the former, $c = \alpha \beta (V^T W)
c$, or the former in the latter, $p = \alpha \beta (V W^T) p$. This
means the complexities of countries and products are given by an
eigenvector of $V^T W$ and $V W^T$ respectively.

Code

Looking only at 2014 trade data.


```python
import pandas as pd, zipfile
with zipfile.ZipFile('hidalgo.zip', 'r') as z:
      df =  pd.read_csv(z.open('hidalgo.csv'),sep='\t')
      gdp =  pd.read_csv(z.open('gdp1416.csv'),sep=',',index_col=0)
      hs =  pd.read_csv(z.open('hs.csv'),sep='|')
      hs2 =  pd.read_csv(z.open('hs2.csv'),sep=',',index_col='ProductCode_x')

print len(df)
print df.tail(10)
```

```
726013
        year origin    hs92  export_val  import_val  export_rca  import_rca
726003  2014    ven  961610     39395.0   2026297.0       0.011       0.947
726004  2014    ven  961620         NaN   1084958.0         NaN       2.413
726005  2014    ven  961700     29666.0   1701096.0       0.005       0.495
726006  2014    ven  961800      2066.0    113839.0       0.001       0.074
726007  2014    ven  970110    210867.0    385141.0       0.004       0.014
726008  2014    ven  970190    179993.0    118881.0       0.136       0.155
726009  2014    ven  970200    976805.0         NaN       0.563         NaN
726010  2014    ven  970300    717009.0    277338.0       0.068       0.045
726011  2014    ven  970500     12723.0         NaN       0.004         NaN
726012  2014    ven  970600         NaN      2484.0         NaN       0.000
```

```python
cp = df.pivot_table('export_val', index='origin', columns='hs92')
print cp.shape
print len(np.unique(df.hs92)), 'products'
```

```
(220, 4858)
4858 products
```

```python
denom = cp.sum(axis=1) / cp.sum().sum()
denom = cp.sum(axis=1) / cp.sum().sum()
cp2 = cp.div(cp.sum(axis=0).T)
cp2 = cp2.div(denom,axis=0)
cp2 = cp2.fillna(0)
cp2[cp2 > 1.0] = 1.0
cp2[cp2 != 1.0] = 0.0
cp3 = cp2
cp4 = cp3.div(cp3.sum(axis=1),axis=0)
cp5 = cp3.div(cp3.sum(axis=0),axis=1)
print cp4.shape, cp5.shape
```

```
(220, 4858) (220, 4858)
```

Country, Product Complexity Method using Eigenanalysis

Country ECI

```python
import scipy.linalg as lin
print cp4.shape
uc,vc = lin.eig(np.dot(cp4,cp5.T))
print vc.shape
eci = np.array(vc)[:,1]
print len(eci)
print np.argmax(eci)
top_countries = cp.index[np.argsort(eci)[:10]]
print top_countries
```

```
(220, 4858)
(220, 220)
220
181
Index([u'jpn', u'che', u'deu', u'kor', u'swe', u'xxb', u'usa', u'sgp', u'cze',
       u'fin'],
      dtype='object', name=u'origin')
```

Look at simple product sum, is the list the same?

Product PCI

Utilize sparsity, 

```python
import scipy.sparse.linalg as lin
import scipy.sparse as sps

scp4 = sps.lil_matrix(cp4)
scp5 = sps.lil_matrix(cp5)

A = scp4.T.dot(scp5)
up,vp = lin.eigs(A,k=2)
pci = np.array(vp)[:,1]
```

```python
top_prods = cp.columns[np.argsort(pci)[:10]]
print top_prods
pd.set_option('expand_frame_repr', False)
top_prods2 = [str(x) for x in list(top_prods)]
print hs2.ix[top_prods2][['Product Description_y','Product Description_x']]
```

```
Int64Index([848590, 870810, 848390, 841221, 852610, 840999, 847790, 847990,
            390940, 851410],
           dtype='int64', name=u'hs92')
                                           Product Description_y                              Product Description_x
ProductCode_x                                                                                                      
848590         (-2006) Machinery parts not specified or inclu...                                    (-2006) - Other
870810         Parts and accessories of the motor vehicles of...                        - Bumpers and parts thereof
848390         Transmission shafts (including cam shafts and ...  -Toothed wheels, chain sprockets and other tra...
841221                                 Other engines and motors.                       -- Linear acting (cylinders)
852610         Radar apparatus, radio navigational aid appara...                                  - Radar apparatus
840999         Parts suitable for use solely or principally w...                                           -- Other
847790         Machinery for working rubber or plastics or fo...                                            - Parts
847990         Machines and mechanical appliances having indi...                                            - Parts
390940         Amino-resins, phenolic resins and polyurethane...                                  - Phenolic resins
851410         Industrial or laboratory electric furnaces and...             - Resistance heated furnaces and ovens
```

Simple regression

```python
cindex = [x.upper() for x in cp.index]
ecigdp = pd.DataFrame(eci,index=cindex)
ecigdp = ecigdp.join(gdp)
print ecigdp.shape
ecigdp.columns = ['eci', u'gdp2014', u'gdp2016']
ecigdp['prods'] = np.array(cp3.sum(axis=1))
ecigdp = ecigdp.dropna()
print ecigdp.tail()
import statsmodels.formula.api as smf
results = smf.ols('np.log(gdp2014) ~ eci', data=ecigdp).fit()
print results.rsquared_adj
results = smf.ols('np.log(gdp2014) ~ prods', data=ecigdp).fit()
print results.rsquared_adj
```

```
(220, 3)
          eci      gdp2014      gdp2016  prods
WSM  0.025062  3761.912686  3524.649880  209.0
YEM  0.075479   679.667360  1101.117444  147.0
ZAF  0.008537  7504.295250  7627.851926  742.0
ZMB  0.048409  1622.409958  1620.823290  182.0
ZWE  0.063000   908.829980   932.548383  275.0
0.55503440264
0.230701679034
```

```python
plt.plot(ecigdp.eci,np.log(ecigdp.gdp2014),'.')
plt.savefig('eci_01.png')
```


HS conversion

```python
hs2['code4'] = hs.ProductCode.str.slice(0,4)
hs3 = hs2[(hs2.ProductCode.str.len()==4)]
hs4 = hs2.merge(hs3, how='left', left_on='code4', right_on='ProductCode')
hs4 = hs4[['ProductCode_x','Product Description_x','Product Description_y']]
```

GDP download

```python
import pandas as pd
from pandas_datareader import data, wb

countries = ['ABW', 'AFG', 'AGO', 'AIA', 'ALB', 'AND', 'ARE', 'ARG', 'ARM', 'ASM', 'ATF', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEN', 'BES', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLX', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'CAF', 'CAN', 'CCK', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COK', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'CXR', 'CYM', 'CYP', 'CZE', 'DEU', 'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESP', 'EST', 'ETH', 'FIN', 'FJI', 'FLK', 'FRA', 'FSM', 'GAB', 'GBR', 'GEO', 'GHA', 'GIB', 'GIN', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GRL', 'GTM', 'GUM', 'GUY', 'HKG', 'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IND', 'IOT', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LKA', 'LTU', 'LVA', 'MAC', 'MAF', 'MAR', 'MDA', 'MDG', 'MDV', 'MEX', 'MHL', 'MKD', 'MLI', 'MLT', 'MMR', 'MNE', 'MNG', 'MNP', 'MOZ', 'MRT', 'MSR', 'MUS', 'MWI', 'MYS', 'NCL', 'NER', 'NFK', 'NGA', 'NIC', 'NIU', 'NLD', 'NOR', 'NPL', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PCN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRK', 'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'ROU', 'RUS', 'RWA', 'SAU', 'SDN', 'SEN', 'SGP', 'SHN', 'SLB', 'SLE', 'SLV', 'SMR', 'SOM', 'SPM', 'SRB', 'SSD', 'STP', 'SUR', 'SVK', 'SVN', 'SWE', 'SYC', 'SYR', 'TCA', 'TCD', 'TGO', 'THA', 'TJK', 'TKL', 'TKM', 'TLS', 'TON', 'TTO', 'TUN', 'TUR', 'TUV', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'UZB', 'VCT', 'VEN', 'VGB', 'VNM', 'VUT', 'WLF', 'WSM', 'XXB', 'YEM', 'ZAF', 'ZMB', 'ZWE']
res = []
for i,c in enumerate(countries):
    try:
        print i,c
        dat = wb.download(indicator='NY.GDP.PCAP.KD', country=[c], start=2014, end=2016)
        gdp = list(dat['NY.GDP.PCAP.KD']) 
        res.append([c, gdp[0], gdp[2]])
        #if len(res) > 5: break
    except:
        print 'error'

df = pd.DataFrame(res)
df.columns = ['code','gdp2014','gdp2016']
df.to_csv('gdp1416.csv',index=None)
```

References

Inoua, <a href="https://arxiv.org/pdf/1601.05012.pdf">Simple Measure of Economic Complexity</a>

Hidalgo <a href="https://oec.world/static/pdf/atlas/AtlasOfEconomicComplexity_Part_I.pdf">The Atlas of Economic Complexity</a>
