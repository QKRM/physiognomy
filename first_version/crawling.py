import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
from urllib.parse import quote_plus

file = pd.read_csv("players_21.csv", encoding = 'utf-8')
p_urls = file['player_url']
urls = p_urls.values.tolist()

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

n = 1
start = 7587
for i in urls:
    if(n >= start):
        html = get_html(i)
        soup = bs(html, "html.parser")
        img_url = soup.find('div', {'class': 'bp3-card player'}).find('img')['data-src']
        req = Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as f:
            print(n)
            with open('./imgs/' + str(n)+'.jpg','wb') as h: # w - write b - binary
                img = f.read()
                h.write(img)
    n = n + 1

print('Image Crawling is done.')

