# -*- coding: utf-8 -*-
import requests
from lxml import html
import time

class Russel_Crawler(object):

    """
     crawler stock recommendation
    """
    def get_recommend(self, ticker):
        """
        get recommendation stocks
        """
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
        #print(ticker + "\t" + recommend_ticker)
        return recommend_ticker

if __name__ == "__main__":
    instance = Russel_Crawler()
    file = "D:\Terry\Project\DataCrawler\yahoo_finance\Russel_3000_format.txt"
    num_temp = 10001

    month = time.strftime("%m")
    day = time.strftime("%d")
    hour = time.strftime("%H")
    if int(month) == 7:
        num = (int(day) - 18) * 24 + (int(hour) - 13) + num_temp
    elif int(month) == 8:
        num = (31 + int(day) - 18) * 24 + (int(hour) - 13) + num_temp
    elif int(month) == 9:
        num = (62 + int(day) - 18) * 24 + (int(hour) - 13) + num_temp
    elif int(month) == 10:
        num = (92 + int(day) - 18) * 24 + (int(hour) - 13) + num_temp
    elif int(month) == 11:
        num = (123 + int(day) - 18) * 24 + (int(hour) - 13) + num_temp
    print(num)

    start = time.time()
    print("start time: " + str(start))
    output_file = "D:\program\Dropbox\Dropbox\yahoo ticker\\russel_3000_2h\\russel_" + str(num) + ".txt"
    f = open(file, 'r')
    output_f = open(output_file, 'w')
    i = 0
    for line in f:
        temp = line.strip().split("\t")
        if len(temp) != 2:
            continue
        company = temp[0]
        ticker = temp[1]
        recommend_ticker = instance.get_recommend(ticker)
        #print(company + "\t" + ticker + "\t" + recommend_ticker)
        #output_f.write(company + "\t" + ticker + "\t" + recommend_ticker + "\n")
        output_f.write(ticker + "\t" + recommend_ticker + "\n")
        i += 1
        if i % 100 == 0:
            print(i)
    f.close()
    output_f.close()
    print("success")
    stop = time.time()
    print("stop time" + str(stop))
    cost_time = float(stop - start) / 60
    print(str(cost_time) + "分钟")
    #num += 1



