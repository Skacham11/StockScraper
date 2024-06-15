from bs4 import BeautifulSoup
import requests


def getData(stock_ticker):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    url = f'https://finance.yahoo.com/quote/{stock_ticker}/'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    quote_stats_div = soup.find('div', {'data-testid': 'quote-statistics'})

    data = {}

    for li in quote_stats_div.find_all('li', class_='last-sm last-lg svelte-tx3nkj'):
        label_span = li.find('span', class_='label svelte-tx3nkj')
        value_span = li.find('span', class_='value svelte-tx3nkj')

        if label_span and value_span:
            label = label_span.get_text(strip=True)
            value = value_span.get_text(strip=True)
            data[label] = value

    fifty_two_week_range = soup.find('li', class_='last-md svelte-tx3nkj').find('span', class_='value svelte-tx3nkj')
    if fifty_two_week_range:
        data['52 Week Range'] = fifty_two_week_range.get_text(strip=True)

    print(data)

# Example usage:
getData('AAPL')
