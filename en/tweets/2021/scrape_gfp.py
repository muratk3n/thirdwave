import requests, time, datetime, re, pandas as pd

df = pd.read_csv("~/Documents/thirdwave/en/2020/07/gdpw.csv")
countries = list(df.country)
sl = []
for c in countries:
    ck = c.replace(" ","-").lower()
    print (ck)
    resp = requests.get("https://www.globalfirepower.com/country-military-strength-detail.php?country_id=%s" % ck)
    reg = \
          '<span class="textLarge textYellow textBold textShadow">(.*?)</span>.*?<br />.*?' + \
          '.*?textWhite.*?">(.*?)</span>'
    res = re.findall(reg, resp.text, re.DOTALL)
    d = {}
    d['country'] = c
    for k,v in res:
        k = k.replace(":","")
        v = v.replace('"','')
        v = v.replace(',','')
        v = v.replace(' km','')
        v = v.replace(' USD','')
        d[k] = v
    row = pd.Series(d)
    sl.append(row)

df = pd.concat(sl,axis=1)
df = df.T
df.to_csv('out.csv')

    
