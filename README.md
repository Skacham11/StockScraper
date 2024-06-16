## Discord Stock Bot
This Discord bot fetches stock information and plots stock history using Yahoo Finance and yfinance API. It utilizes Python with libraries such as discord.py, yfinance, matplotlib, BeautifulSoup, and requests.

## Features
**Fetching Stock Data:** Retrieves real-time stock information from Yahoo Finance using BeautifulSoup and requests.

**Parsing Data:** Parses HTML to extract current price, price change, percentage change, and additional statistics from the stock page.

**Plotting Stock History:** Generates a plot of the stock's closing prices over the last year using matplotlib and yfinance.

**Error Handling:** Handles various exceptions during data fetching, parsing, and plotting to ensure robust operation.

**Discord Integration:** Responds to user commands in Discord with formatted stock information and plots.

## Usage
**Command Syntax:** Use the command !stock 'ticker' in Discord to fetch stock information and plot history.

**Example:** !stock AAPL to get information and history for Apple Inc.

## Screenshot of running !stock AAPL
![Screenshot 2024-06-16 at 12 41 49 PM](https://github.com/Skacham11/StockScraper/assets/66738929/f4659600-4041-47a4-b1d3-6e7749f6e486)

## Screenshot of Appl Stock Price Graph - Last 1 Year
![Screenshot 2024-06-16 at 12 42 01 PM](https://github.com/Skacham11/StockScraper/assets/66738929/322af070-6dbc-4268-b168-1f6329e26b98)

## Screenshot of bot catching error #1: unlisted stock
![Screenshot 2024-06-16 at 12 43 24 PM](https://github.com/Skacham11/StockScraper/assets/66738929/ded0df52-41c2-48ad-a624-c33f61389f5b)

## Screenshot of bot catching error #2: incorrect starting command
![Screenshot 2024-06-16 at 12 51 14 PM](https://github.com/Skacham11/StockScraper/assets/66738929/38c4f12e-1664-4cd9-8bae-15ae9f06b796)
