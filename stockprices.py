from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
url = 'https://finance.yahoo.com/quote/AAPL/'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
