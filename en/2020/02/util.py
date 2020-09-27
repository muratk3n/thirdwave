import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import pandas as pd

def get_data():
    confirmed_df  = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    deaths_df     = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    recoveries_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    confirmed_df = confirmed_df.drop(columns=['Province/State','Lat', 'Long'])
    confirmed_df = confirmed_df.groupby('Country/Region').agg('sum')
    confirmed_df = confirmed_df.T
    return confirmed_df

def mortality_rate():

    covid_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    covid_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    covid_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

    covid_worldwide_confirmed = covid_confirmed.iloc[:, 4:].sum(axis=0)
    covid_worldwide_deaths = covid_deaths.iloc[:, 4:].sum(axis=0)
    covid_worldwide_recovered = covid_recovered.iloc[:, 4:].sum(axis=0)
    covid_worldwide_active = covid_worldwide_confirmed - covid_worldwide_deaths - covid_worldwide_recovered

    world_rate_df = pd.DataFrame({
        'confirmed': covid_worldwide_confirmed,
        'deaths': covid_worldwide_deaths,
        'recovered': covid_worldwide_recovered,
        'active': covid_worldwide_active
    }, index=covid_worldwide_confirmed.index)

    world_rate_df['recovered / 100 confirmed'] = world_rate_df['recovered'] / world_rate_df['confirmed'] * 100

    world_rate_df['deaths / 100 confirmed'] = world_rate_df['deaths'] / world_rate_df['confirmed'] * 100

    world_rate_df['date'] = world_rate_df.index

    print (world_rate_df['deaths / 100 confirmed'].tail(4))
    return world_rate_df

