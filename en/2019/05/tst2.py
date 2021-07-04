from scipy import sin, cos, tan, arctan, arctan2, arccos, pi
import pandas as pd, datetime, numpy as np
from zipfile import ZipFile
from io import BytesIO
import urllib.request as urllib2
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request, folium, re, requests

headers = { 'User-Agent': 'UCWEB/2.0 (compatible; Googlebot/2.1; +google.com/bot.html)'}

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


url = "https://news.antiwar.com/2021/07/02/report-china-india-move-tens-of-thousands-of-troops-to-disputed-border/"
resp = requests.get(url, headers=headers, timeout=2)
s = text_from_html(resp.text)

print (s[:1000])

