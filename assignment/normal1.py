from urllib import request
from bs4 import BeautifulSoup
import bs4
import re
    #网站有反爬措施，使用付费代理爬取页面 ， 此代理已到期，可换其他代理爬取      
    # 要访问的目标页面
    targetUrl = "https://www.hzqx.com/hztq/index.html"

    # 代理服务器
    proxyHost = "http-dynamic.xiaoxiangdaili.com"
    proxyPort = "10030"

    # 代理隧道验证信息
    proxyUser = "636399826455908352"
    proxyPass = "Mj3YpV3J"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxy_handler = request.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = request.build_opener(proxy_handler)

    request.install_opener(opener)
    resp = request.urlopen(targetUrl).read()
    soup=BeautifulSoup(resp,"html.parser") 
    result=soup.find_all(class_='right')
    html='''<1i class="right"id="live right"><span>当前实况(11时35分)</span> <br>
<b>19.8℃</b>
 <br>
span>湿度:</span>
 <span>64%</span>
 <br/>
span>体感温度:</span>
span>19.6</span>
 <br/>
<span>气压:</span>
 (span>1012hpa</span>
 <br/>
<span>西北风,<span>
<span>2级</span>
 <br>
<span>(1.9米/秒)</span>
/1i>'''
number=re.search('<br>(.*?)</b>',html,re.S)
print(result.group(1))
#19.8℃




