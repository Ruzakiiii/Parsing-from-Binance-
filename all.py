import requests
from bs4 import BeautifulSoup
import time
import re

while True:

    reponse = requests.get('https://ru.coinalyze.net/ripple/usdt/binance/price-chart-live/')

    supo = BeautifulSoup(reponse.text,'lxml')

    try:
        loou = supo.find('div',{'class':'hours1-pchange red'}).text

        a = re.sub('%', '', loou)
        print(a)
        if float(a) < -1.0:
            print(f'{a} снизился 1%')

    except:
        loou = supo.find('div', {'class': 'hours1-pchange green'}).text

        a = re.sub('%', '', loou)
        print(a)
        if float(a) > 1.0:
            print(f'{a} вырос больше на 1%')

    time.sleep(2.0)

