import requests, time, datetime, re, pandas as pd

#df = pd.read_csv("~/Documents/thirdwave/en/2020/07/gdpw.csv")
#countries = list(df.country)
countries = ['United States of America','Switzerland','Norway','Ireland','Qatar','Singapore','Denmark','Australia','Sweden','Netherlands','Austria','Finland','Germany','Belgium','Canada','United Arab Emirates','United Kingdom','New Zealand','Israel','France','Japan','Italy','Kuwait','Spain','Slovenia','Bahrain','Portugal','Saudi Arabia','Estonia','Czech Republic','Greece','Curaçao','Slovakia','Lithuania','Latvia','Uruguay','Oman','Hungary','Venezuela','Chile','Panama','Poland','Croatia','Romania','Argentina','Malaysia','Russia','Grenada','Kazakhstan','China','Mexico','Turkey','Bulgaria','Brazil','Montenegro','Cuba','Lebanon','Botswana','Dominican Republic','Gabon','Thailand','Serbia','Libya','Turkmenistan','Peru','Colombia','South Africa','Ecuador','Belarus','Suriname','Bosnia and Herzegovina','Namibia','Iraq','Paraguay','Iran','Albania','Azerbaijan','Georgia','Guatemala','Jordan','Armenia','Mongolia','Algeria','Sri Lanka','El Salvador','Indonesia','Bolivia','Tunisia','Angola','Bhutan','Moldova','Morocco','Philippines','Ukraine','Vietnam','Egypt','Laos','Honduras','Ghana','Zimbabwe','Nicaragua','Nigeria','India','Kenya','Bangladesh','Zambia','Cameroon','Uzbekistan','Cambodia','Pakistan','Myanmar','Kyrgyzstan','Mauritania','Tanzania','Nepal','Sudan','Yemen','Mali','Tajikistan','Ethiopia','Chad','Burkina Faso','Liberia','Uganda','Sierra Leone','Madagascar','Afghanistan','Mozambique','Central African Republic','Niger','Somalia']

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

    
