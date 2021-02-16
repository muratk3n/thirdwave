from quakefeeds import QuakeFeed
import requests, time, datetime

def get_eq1():
    today = datetime.datetime.now()
    days = 90
    start = today - datetime.timedelta(days=days)

    req = 'https://earthquake.usgs.gov/fdsnws'
    req+='/event/1/query.geojson?starttime=%s&endtime=%s'
    req+='&minmagnitude=4.5&orderby=time&limit=1000'
    req = req % (start.isoformat(), today.isoformat())
    qr = requests.get(req).json()
    res = []
    for i in range(len(qr['features'])):
        lat = qr['features'][i]['geometry']['coordinates'][1]
        lon = qr['features'][i]['geometry']['coordinates'][0]
        rad = qr['features'][i]['geometry']['coordinates'][2]
        d = datetime.datetime.fromtimestamp(qr['features'][i]['properties']['time']/1000.0)
        s = np.float(qr['features'][i]['properties']['mag'])
        diff = (d-start).days
        res.append([d,s,lat,lon,rad,diff])

    import pandas as pd
    df = pd.DataFrame(res).sort_values(by=0)
    df = df.set_index(0)
    df.columns = ['mag','lat','lon','rad','ago']
    return df

def get_eq2():
    feed = QuakeFeed("4.5", "month")
    res = []
    for i in range(len(feed)):
        d = datetime.datetime.fromtimestamp(feed[i]['properties']['time']/1000.0)
        s = feed[i]['properties']['mag']
        res.append([d,s])
    df = pd.DataFrame(res).sort_values(by=0)
    df = df.set_index(0)
    df.columns = ['Magnitude']
    return df



