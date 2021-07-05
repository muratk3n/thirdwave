from collections import defaultdict
import numpy.linalg as lin, numpy as np
import pandas as pd, re, mygeo

s = """
                       Antiwar.com Home  About Antiwar.com  Donate  Blog  US Casualties   Contact  Latest News    News From Antiwar.com  Original and up-to-date news          Report: China, India Move Tens of Thousands of Troops to Disputed Border  After deadly skirmish between Chinese and Indian troops last year, the US stepped up military cooperation with India     by Dave DeCamp  Posted on July 2, 2021 July 2, 2021 Categories News Tags China , India    According to a report from The Wall Street Journal , China and India have deployed tens of thousands of troops to their disputed border in the Himalayas. The report cited anonymous Indian officials who said China increased its troop presence from 15,000 to about 50,000 in the region, which was matched by India.  The report said most of the build-up has occurred in the eastern Ladakh region, where a deadly skirmish between Chinese and Indian troop
"""

tokens = re.split(r'.\s',s)
c_in_tokens = defaultdict(int)
for t in tokens: c_in_tokens[t] += 1
#print (c_in_tokens)

df = pd.read_csv('countries.csv')
df['latlon'] = df.apply(lambda x: list(x[['latitude','longitude']]),axis=1)
cdict = df.set_index('name')['latlon'].to_dict()
#print (cdict)

res = {}
for t in c_in_tokens: 
    if t in cdict: res[t] = c_in_tokens[t]

print (res)
total = []
for c in res:
    lat,lon = cdict[c]
    newcoord = mygeo.latlon2vec(lat,lon)
    total.append(list(newcoord * res[c]))

total = np.array(total)    
m = np.mean(total,axis=0)
m = m / lin.norm(m)
print (m)
lat,lon = mygeo.vec2latlon(m)
print (lat,lon)


