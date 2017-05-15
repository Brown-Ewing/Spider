import urllib
import urllib2

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username': 'cqc', 'password': 'XXXX'}
referer = 'http://www.zhihu.com/articles'
headers = {'User-Agent': user_agent, "Referer": referer}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
try:
    response = urllib2.urlopen(request, timeout = 10)
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
else:
    print "OK"
page = response.read()