Three timing schedule:
1. Crawling recommendation stocks of the stock tickers in the yahoo_tikcer_us.txt from the website of yahoo finance
Timing: Every 5am and 5pm, daily. (name the filename as yahoo_ticker_recommend_2017100605,yahoo_ticker_recommend_2017100617 )
Script: run_yahoo_crawler_stock.bat yahoo_crawler_stock.py

2. Crawing recommendation stocks of the stock tickers in the Russel_3000_format.txt from the website of yahoo finance
a. Timing 1: Every 2 hours, daily(name the filename as russel_10002, russel_10004)
script: run_russel_3000_continuous.bat russel_crawler.py

b. Timing 2: Every 2 hours, daily(name the filename as russel_10001, russel_10003)
script: run_russel_3000_continuous_2h.bat russel_crawler_2h.py
