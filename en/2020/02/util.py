import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import pandas as pd

infected_dataset_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
recovered_dataset_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
deaths_dataset_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
countries_dataset_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv"

def estimate_Rt_for_country(country):
    countries = pd.read_csv(countries_dataset_url)
    infected_original = pd.read_csv(infected_dataset_url)
    recovered_original = pd.read_csv(recovered_dataset_url)
    deaths_original = pd.read_csv(deaths_dataset_url)
    countries.head()

    population = countries[countries['Province_State'].isnull()][['Country_Region','Population']].rename(columns={'Country_Region' : 'Country/Region'}).set_index('Country/Region')
    infected = infected_original.groupby('Country/Region').sum().reset_index().set_index('Country/Region').join(population,on='Country/Region')
    deaths = deaths_original.groupby('Country/Region').sum().reset_index().set_index('Country/Region').join(population,on='Country/Region')
    recovered = recovered_original.groupby('Country/Region').sum().reset_index().set_index('Country/Region').join(population,on='Country/Region')
    infected.head()

    def deriv(y, t, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

    def sir_model(infected,removed,N,beta,gamma,ndays):
        t = np.linspace(0,ndays,ndays)
        y0 = N-infected-removed,infected,removed
        ret = odeint(deriv, y0, t, args=(N, beta, gamma))
        return ret.T # S,I,R

    def model(V,R,N,beta,gamma):
        S,I,R = sir_model(V[0],R[0],N,beta,gamma,len(V))
        dV = np.diff(V)
        dI = np.diff(I+R)
        return np.linalg.norm(dV-dI)

    the_gamma = 1/30

    def fit(V,R,N):
        res = minimize(lambda x:model(V,R,N,x,the_gamma),x0=0.5,method='powell')
        return res.x,the_gamma

    def make_frame(country_name,smooth_window=3):
        f = pd.DataFrame([infected.loc[country_name],recovered.loc[country_name],deaths.loc[country_name]]).T
        population = f.iloc[-1,0]
        f = f.iloc[2:-1].reset_index()
        f.columns = ['Date','Infected','Recovered','Deaths']
        f['Removed'] = f['Recovered']+f['Deaths']
        f["Date"] = pd.to_datetime(f["Date"],format="%m/%d/%y")
        for x in ['Infected','Recovered','Deaths','Removed']:
            f[x+"_Av"] = f[x].rolling(window=smooth_window).mean()
        return population, f

    def get_start_index(df):
        return df[df['Infected_Av']>1000].index[0]

    def compute_params(df,population, start_index, ndays=8):
        for i in range(start_index,len(df)-ndays):
            V = df['Infected_Av'][i:i+ndays].to_numpy()
            R = df['Removed_Av'][i:i+ndays].to_numpy()
            beta,gamma = fit(V,R,population)
            df.loc[i,'Beta'] = beta
            df.loc[i,'Gamma'] = gamma

    def analyze(country_name,truncate_frame=True):
        population, df = make_frame(country_name)
        n = get_start_index(df)
        compute_params(df,population,n)
        df['Rt'] = df['Beta'] / df['Gamma']
        return population, df.iloc[n:] if truncate_frame else df

    pop, df = analyze(country)

    return pop, df
