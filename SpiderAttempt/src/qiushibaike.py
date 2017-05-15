# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup

page = 1
url = "http://www.qiushibaike.com/hot/page/" + str(page)
useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
header = {"User-Agent": useragent}

#抓取网页内容
def fetchTxt():
    allContents = ''
    try:
        request = urllib2.Request(url, headers=header)
        response = urllib2.urlopen(request)
        allContents = response.read()
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason

    return allContents

#筛选文字类型段子
soup = BeautifulSoup(fetchTxt())
divlist = soup.find_all("div", {"class": "article block untagged mb15"})
for i in divlist:
    item = divlist[i]
    print item