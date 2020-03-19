import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def retrieve_cor_data():
    df = pd.read_csv('corona.csv',sep=r'\t',header=None)
    df1 = df[[0,1,3,5]]
    df1.columns = ['Country','Confirmed','Deaths','Recovered']

    d1 = df1[['Country','Confirmed']].set_index('Country').to_dict()
    df2 = pd.read_csv('alpha3country.csv',sep=',', skipinitialspace=True)
    d2 = df2[['Country','Alpha-3 code']].set_index('Country').to_dict()

    res = []
    for c in d1['Confirmed'].keys():
        code = d2['Alpha-3 code'].get(c.strip())
        val = float(d1['Confirmed'][c].replace(",",""))
        if code: res.append([val, code])

    df = pd.DataFrame(res)

    bins = [0, 20, 50, 100, 200, 1000, 2000, 100000]
    colors = ["mistyrose","lightsalmon","salmon", \
              "lightcoral","tomato","red","firebrick"]
    df['colors'] = pd.cut(np.array(df[0]), bins=bins, labels=colors)
    col_dict = df.set_index(1)['colors'].to_dict()
    return df, col_dict
