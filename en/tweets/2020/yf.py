# https://stackoverflow.com/questions/57538976/web-scraping-of-yahoo-finance-statistics-using-bs4/57540063#57540063
import requests, re, json, pprint
import numpy as np

p = re.compile(r'root\.App\.main = (.*);')

def conv(x):
    if x[-1] == 'T': return np.float(x[:-1])*1e12
    elif x[-1] == 'B': return np.float(x[:-1])*1e9

def get_financials(tickers):
    results = {}
    with requests.Session() as s:
        for ticker in tickers:
            r = s.get('https://finance.yahoo.com/quote/{}/key-statistics?p={}'.format(ticker,ticker))
            data = json.loads(p.findall(r.text)[0])
            key_stats = data['context']['dispatcher']['stores']['QuoteSummaryStore']
            res = {
                'Enterprise Value' : key_stats['defaultKeyStatistics']['enterpriseValue']['fmt']
                ,'Trailing P/E' : key_stats['summaryDetail']['trailingPE']['fmt']
                ,'Forward P/E' : key_stats['summaryDetail']['forwardPE']['fmt']
                ,'PEG Ratio (5 yr expected)' : key_stats['defaultKeyStatistics']['pegRatio']['fmt']
                , 'Return on Assets' : key_stats['financialData']['returnOnAssets']['fmt']
                , 'Quarterly Revenue Growth' : key_stats['financialData']['revenueGrowth']['fmt']
                , 'EBITDA' : key_stats['financialData']['ebitda']['fmt']
                , 'Diluted EPS' : key_stats['defaultKeyStatistics']['trailingEps']['fmt']
                , 'Total Debt/Equity' : key_stats['financialData']['debtToEquity']['fmt']
                , 'Current Ratio' :  key_stats['financialData']['currentRatio']['fmt']
            }
            results[ticker] = res

    return results

def get_EVEbit(ticker):
    """ working with rounded up values so this ratio is approximate"""
    results = get_financials([ticker])
    eb = conv(results[ticker]['EBITDA'])
    ev = conv(results[ticker]['Enterprise Value'])
    return np.round(ev / eb,2)
