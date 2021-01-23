# EU Greece code

0 Debt Relief, No Reform
30 Debt Relief, Half Reform
60 Debt Relief, Full Reform
80 Debt Relief Soon, Full Reform
100 No Debt Relief, Full Reform

```python
def weighted_mode(df):
    df['w'] = df.Clout*df.Salience 
    df['w'] = df['w'] / df['w'].sum()
    df['w'] = df['w'].cumsum()
    return float(df[df['w']>=0.5].head(1).Position)    
def mean(df):
    return (df.Clout*df.Position*df.Salience).sum() / \
           (df.Clout*df.Salience).sum()
```


```python
import pandas as pd
df = pd.read_csv('greece.csv',sep=',')
df = df.sort_index(by='Position')
print df, '\n', 'mean voter', mean(df)
print 'weighted mode', weighted_mode(df)
```

```text
     Stakeholder  Clout  Position  Salience
0         Greece    100        40       100
10           USA     30        60       100
1            IMF     20        70       100
2        Juncker     10        80       100
3        Germany    100       100        80
4         France     70       100       100
5   Dijsselbloem     70       100        40
6           Tusk     70       100        40
7          Italy     50       100       100
8            ECB     20       100        70
9          Spain     20       100       100 
mean voter 82
weighted mode 100.0
```

#################################################################
Current Account

```python
import pandas as pd, csv
df = pd.read_csv('greece_acct.csv',sep='\s+',index_col=0)
df['Current Account'] = df['Goods'] + df['Services'] + df['Income'] + df['Current Transfers']
df['Current Account and Capital Transfers'] = df['Current Account'] + df['Capital Transfers']
df['Direct Investment'] = df['Direct Investment Abroad'] + df['Direct Investment Home']
df['Portfolio Investment'] = df['Portfolio Inv Assets'] + df['Portfolio Inv Liabilities']
df['Other Investments'] = df['Other Investments Assets'] + df['Other Investments Liabilities']
df['Financial Account'] = df['Direct Investment'] + df['Portfolio Investment'] + df['Other Investments'] + df['Change in Reserve Assets']
df['Balancing Item'] = -1*(df['Current Account'] + df['Capital Transfers'] + df['Financial Account'])
print (df.T[[2000,2001,2002,2003]])
```

```text
Year                                      2000     2001     2002     2003
Goods                                 -21927.5 -21610.9 -22708.7 -22643.5
Services                                8711.1   9150.0  10755.4  11506.5
Income                                  -955.3  -1981.3  -2073.4  -3975.8
Current Transfers                       3553.3   3856.9   3822.0   3848.7
Capital Transfers                       2246.0   2416.0   1633.5   1239.4
Direct Investment Abroad               -2319.0   -688.5   -696.3   -365.2
Direct Investment Home                  1202.8   1776.1     53.4   1129.9
Portfolio Inv Assets                    -933.0   -514.7  -2230.0  -8737.9
Portfolio Inv Liabilities              10040.5   9979.5  13167.8  21071.8
Other Investments Assets               -1060.6  -1467.0  -7481.9  -4034.5
Other Investments Liabilities          -3796.2  -8327.6   9480.5  -3589.4
Loans of General Government             -437.7  -2809.7  -4510.1  -2618.4
Change in Reserve Assets                5771.7   6177.0  -1983.0   4409.0
Reserve Assets (Stock)                 13208.0   7031.0   9014.0   4605.0
Current Account                       -10618.4 -10585.3 -10204.7 -11264.1
Current Account and Capital Transfers  -8372.4  -8169.3  -8571.2 -10024.7
Direct Investment                      -1116.2   1087.6   -642.9    764.7
Portfolio Investment                    9107.5   9464.8  10937.8  12333.9
Other Investments                      -4856.8  -9794.6   1998.6  -7623.9
Financial Account                       8906.2   6934.8  10310.5   9883.7
Balancing Item                          -533.8   1234.5  -1739.3    141.0
```

```python
print (df.T[[2004,2005,2006,2007]])
```

```text
Year                                      2004     2005     2006     2007
Goods                                 -25435.8 -27558.9 -35286.3 -41499.2
Services                               15467.0  15391.1  15337.1  16591.7
Income                                 -4377.4  -5676.1  -7209.4  -9285.8
Current Transfers                       3629.0   3100.4   3399.9   1591.1
Capital Transfers                       2386.1   2048.6   3041.3   4332.3
Direct Investment Abroad                -828.8  -1180.4  -3224.4  -3832.9
Direct Investment Home                  1692.4    501.3   4268.8   1542.7
Portfolio Inv Assets                  -11489.4 -18459.7  -6961.2 -16351.1
Portfolio Inv Liabilities              25216.9  25782.3  15076.6  33792.8
Other Investments Assets               -6215.7  -6301.5  -5851.0 -16266.1
Other Investments Liabilities          -2888.4  12215.5  17369.5  29006.8
Loans of General Government            -1027.4   -447.0   -447.7  -2341.7
Change in Reserve Assets                2611.0     49.0   -224.0   -322.0
Reserve Assets (Stock)                  1994.0   1945.0   2169.0   2491.0
Current Account                       -10717.2 -14743.5 -23758.7 -32602.2
Current Account and Capital Transfers  -8331.1 -12694.9 -20717.4 -28269.9
Direct Investment                        863.6   -679.1   1044.4  -2290.2
Portfolio Investment                   13727.5   7322.6   8115.4  17441.7
Other Investments                      -9104.1   5914.0  11518.5  12740.7
Financial Account                       8098.0  12606.5  20454.3  27570.2
Balancing Item                           233.1     88.4    263.1    699.7
```

```python
print (df.T[[2008,2009,2010]])
```

```text
Year                                      2008     2009     2010
Goods                                 -44048.8 -30767.3 -28279.6
Services                               17135.6  12640.2  13248.5
Income                                -10643.0  -8984.3  -8143.4
Current Transfers                       2758.6   1292.6    198.9
Capital Transfers                       4090.8   2017.4   2071.5
Direct Investment Abroad               -1650.4  -1479.3   -738.8
Direct Investment Home                  3071.1   1753.8    281.4
Portfolio Inv Assets                    -268.9  -8973.0  13278.7
Portfolio Inv Liabilities              16696.9  31636.8 -34133.6
Other Investments Assets              -27823.3 -23875.7   7658.7
Other Investments Liabilities          39917.8  25438.8  34880.2
Loans of General Government             -572.7   2865.0  29978.2
Change in Reserve Assets                 -29.0   -106.0     97.0
Reserve Assets (Stock)                  2521.0   3857.0   4777.0
Current Account                       -34797.6 -25818.8 -22975.6
Current Account and Capital Transfers -30706.8 -23801.4 -20904.1
Direct Investment                       1420.7    274.5   -457.4
Portfolio Investment                   16428.0  22663.8 -20854.9
Other Investments                      12094.5   1563.1  42538.9
Financial Account                      29914.2  24395.4  21323.6
Balancing Item                           792.6   -594.0   -419.5
```













