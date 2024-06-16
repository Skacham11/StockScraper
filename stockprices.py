import yfinance as yf
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

def fetch_stock_data(stock_ticker):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    url = f'https://finance.yahoo.com/quote/{stock_ticker}/'
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.text
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"OOps: Something Else: {err}")
    return None

def parse_stock_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = {}
    try:
        price = soup.find('div', {'class': 'container svelte-mgkamr'}).find_all('span')[0].text
        price_change_dollars = soup.find('div', {'class': 'container svelte-mgkamr'}).find_all('span')[1].text
        price_change_percentage = soup.find('div', {'class': 'container svelte-mgkamr'}).find_all('span')[2].text
        data['Current Price'] = price
        data['Price Change in Dollars'] = price_change_dollars
        data['Price Change in Percentage'] = price_change_percentage
    except (AttributeError, IndexError) as e:
        print(f"Error extracting price information: {e}")
        return None
    try:
        quote_stats_div = soup.find('div', {'data-testid': 'quote-statistics'})
        if not quote_stats_div:
            raise ValueError("Quote statistics div not found")

        for li in quote_stats_div.find_all('li', class_='svelte-tx3nkj'):
            label_span = li.find('span', class_='label svelte-tx3nkj')
            value_span = li.find('span', class_='value svelte-tx3nkj')

            if label_span and value_span:
                label = label_span.get_text(strip=True)
                value = value_span.get_text(strip=True)
                data[label] = value

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
            
    except Exception as e:
        print(f"Error extracting statistics: {e}")
        return None

    return data

def plot_stock_history(stock_ticker, buffer):
    stock = yf.Ticker(stock_ticker)
    hist = stock.history(period="1y")  
    dates = hist.index.to_numpy()  
    close_prices = hist['Close'].to_numpy()  

    plt.figure(figsize=(10, 5))
    plt.plot(dates, close_prices, label='Close Price')
    plt.title(f'{stock_ticker.upper()} Stock Price - Last 1 Year')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.legend()
    plt.grid()
    plt.savefig(buffer, format='png')
    plt.close()

def getData(stock_ticker):
    html = fetch_stock_data(stock_ticker)
    if html:
        data = parse_stock_data(html)
        if data:
            #print(data)
            plot_stock_history(stock_ticker)


#ticker = input("Enter Stock Ticker: ")
#getData(ticker)