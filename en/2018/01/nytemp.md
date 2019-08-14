
[Doc](https://www.weather.gov/media/okx/Climate/CentralPark/monthlyannualtemp.pdf)

```python
import pandas as pd
df = pd.read_csv('nytemp.csv',header=None,names=['temp'])
df['year'] = range(1869,2018)
print df.head()
plt.title('January Average NY Temparature')
df.temp.plot()
pd.rolling_mean(df.temp, window=9).plot(color='red')
plt.savefig('nytemp.png')

```

```text
   temp  year
0  35.1  1869
1  37.5  1870
2  28.3  1871
3  28.8  1872
4  28.6  1873
```

#####################################3
Some scraping code

```python
from datetime import datetime, timedelta
from urllib2 import urlopen
from bs4 import BeautifulSoup
import os

def parse_station(station, current_date):

        with open('{}/{}-{}-{}.html'.format(station,
                                            current_date.year,
                                            current_date.month,
                                            current_date.day)) as in_file:
            soup = BeautifulSoup(in_file.read(), 'html.parser')
            weather_data = soup.find(id='historyTable').find_all('span', class_='wx-value')
            weather_data_units = soup.find(id='historyTable').find_all('td')
            actual_max_temp = weather_data[2].text
            actual_min_temp = weather_data[5].text
            return actual_min_temp, actual_max_temp

def scrape_station(station):
    syear = 1970
    eyear = 2018
    current_date = datetime(year=syear, month=1, day=1)
    if os.path.isdir(station) == False: os.mkdir(station)
    lookup_URL = 'http://www.wunderground.com/history/airport/{}/{}/{}/{}/DailyHistory.html'
    fout = open("nytemp.csv","a")
    
    for yr in range(syear,eyear):
        current_date=current_date.replace(year=yr)
        for day in (range(1,30)):
                current_date=current_date.replace(day=day)
                out_file_name = '{}/{}-{}-{}.html'.format(station, current_date.year,
                                                          current_date.month,
                                                          current_date.day)

                formatted_lookup_URL = lookup_URL.format(station,
                                                         current_date.year,
                                                         current_date.month,
                                                         current_date.day)
                print formatted_lookup_URL
                if os.path.isfile(out_file_name)==False:                
                        html = urlopen(formatted_lookup_URL).read().decode('utf-8')
                        with open(out_file_name, 'w') as out_file: out_file.write(html)
                        min,max=parse_station('KNYC', current_date)
                        fout.write("%s,%s,%s\n" % (current_date,min,max))
                        fout.flush()
                else:
                        print 'skipping...'

scrape_station('KNYC')

```











