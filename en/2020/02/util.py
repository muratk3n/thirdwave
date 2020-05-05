import pandas as pd, zipfile, numpy as np
import matplotlib.pyplot as plt

def retrieve_cor_data(bins,colors):
    df = pd.read_csv('corona.csv',sep=r'\t',header=None)
    df1 = df[[0,1,3,5]]
    df1.columns = ['Country','Confirmed','Deaths','Recovered']
    df1['Country'] = df1['Country'].str.replace("S. Korea","South Korea")
    df1['Country'] = df1['Country'].str.replace("USA","United States")
    df1['Country'] = df1['Country'].str.replace("UAE","United Arab Emirates")
    df1['Country'] = df1['Country'].str.replace("UK","United Kingdom")
    df1['Country'] = df1['Country'].str.replace("Czechia","Czech Republic")

    df1['Confirmed'] = df1['Confirmed'].str.replace(",","").astype(np.float)
    df1['Deaths'] = df1['Deaths'].str.replace(",","").astype(np.float)
    df1['Recovered'] = df1['Recovered'].str.replace(",","").astype(np.float)    
    df1['NewCases'] = df1.Confirmed - (df1.Deaths+df1.Recovered)
    
    #d1 = df1[['Country','Confirmed']].set_index('Country').to_dict()
    d1 = df1[['Country','NewCases']].set_index('Country').to_dict()
    df2 = pd.read_csv('alpha3country.csv',sep=',', skipinitialspace=True)
    
    d2 = df2[['Country','Alpha-3 code']].set_index('Country').to_dict()

    res = []
    #for c in d1['Confirmed'].keys():
    for c in d1['NewCases'].keys():
        code = d2['Alpha-3 code'].get(c.strip())
        #val = float(d1['Confirmed'][c].replace(",",""))
        val = d1['NewCases'][c]
        if code: res.append([val, code])

    df = pd.DataFrame(res)

    df['colors'] = pd.cut(np.array(df[0]), bins=bins, labels=colors)
    col_dict = df.set_index(1)['colors'].to_dict()
    
    return df1, col_dict
