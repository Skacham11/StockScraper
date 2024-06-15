from bs4 import BeautifulSoup
import requests


def getData(stock_ticker):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{stock_ticker}/'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('div', {'class': 'container svelte-mgkamr'}).find_all('span')[0].text
    price_change_dollars = soup.find('div', {'class': 'container svelte-mgkamr'}).find_all('span')[1].text
    price_change_percentage = soup.find('div', {'class': 'container svelte-mgkamr'}).find_all('span')[2].text
    print(price, price_change_dollars, price_change_percentage)
