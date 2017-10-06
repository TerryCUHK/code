# -*- coding: utf-8 -*-
import requests
from lxml import html
import time

class Yahoo_Crawler(object):

    """
     crawl data of etf , timing: 6 am
    """
    def get_recommend(self, ticker):
        recommend_ticker = ""
        url = 'https://finance.yahoo.com/quote/'+ticker
        try:
            session_requests = requests.session()
            r = session_requests.get(url)
            tree = html.fromstring(r.text)
        except Exception as e:
            print(e)
            return ""
        recommend1 = tree.xpath('//*[@id="rec-by-symbol"]/a[1]/text()')
        recommend2 = tree.xpath('//*[@id="rec-by-symbol"]/a[2]/text()')
        recommend3 = tree.xpath('//*[@id="rec-by-symbol"]/a[3]/text()')
        recommend4 = tree.xpath('//*[@id="rec-by-symbol"]/a[4]/text()')
        recommend5 = tree.xpath('//*[@id="rec-by-symbol"]/a[5]/text()')
        if len(recommend1) != 0:
            recommend_ticker = recommend1[0]
        if len(recommend2) != 0:
            recommend_ticker += "\t" + recommend2[0]
        if len(recommend3) != 0:
            recommend_ticker += "\t" + recommend3[0]
        if len(recommend4) != 0:
            recommend_ticker += "\t" + recommend4[0]
        if len(recommend5) != 0:
            recommend_ticker += "\t" + recommend5[0]
        print(ticker + "\t" + recommend_ticker)
        return recommend_ticker

if __name__ == "__main__":
    start = time.time()
    day = time.strftime("%Y%m%d%H")
    print("start time: " + str(start))
    instance = Yahoo_Crawler()
    #file = "../yahoo_finance/ticker.txt"
    ## windows上开启定时任务必须引用完整路径
    file = "D:\Terry\Project\DataCrawler\yahoo_finance\yahoo_ticker_us\yahoo_ticker_us.txt"
    output_file = "D:\program\Dropbox\Dropbox\yahoo ticker\stock\yahoo_ticker_recommend_" +str(day)+".txt"
    f = open(file, 'r')
    output_f = open(output_file, 'w')
    i = 0
    for line in f:
        ticker = line.strip()
        recommend_ticker = instance.get_recommend(ticker)
        output_f.write(ticker+"\t"+recommend_ticker + "\n")
        i += 1
        if i % 100 == 0:
            print(i)
    f.close()
    output_f.close()
    print("success")
    print("exit")
    stop = time.time()
    print("stop time" + str(stop))
    cost_time = float(stop - start) / 60
    print(str(cost_time) + "分钟")