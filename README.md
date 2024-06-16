Discord Stock Bot
This Discord bot fetches stock information and plots stock history using Yahoo Finance and yfinance API. It utilizes Python with libraries such as discord.py, yfinance, matplotlib, BeautifulSoup, and requests.

Features
Fetching Stock Data: Retrieves real-time stock information from Yahoo Finance using BeautifulSoup and requests.
Parsing Data: Parses HTML to extract current price, price change, percentage change, and additional statistics from the stock page.
Plotting Stock History: Generates a plot of the stock's closing prices over the last year using matplotlib and yfinance.
Error Handling: Handles various exceptions during data fetching, parsing, and plotting to ensure robust operation.
Discord Integration: Responds to user commands in Discord with formatted stock information and plots.

Usage
Command Syntax: Use the command !stock <ticker> in Discord to fetch stock information and plot history.
Example: !stock AAPL to get information and history for Apple Inc.
