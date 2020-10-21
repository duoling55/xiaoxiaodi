import requests
from bs4 import BeautifulSoup
import bs4
import re
url="http://zhaobiao.hdu.edu.cn/82/list.htm"
r=requests.get(url)
r.raise_for_status()
encoding=r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,"html.parser") 
iii=soup.find_all(class_='all_count')

#print(iii)
sss='± <em class="all_count">2386</em> è®°å½ </span>, <em class="all_count">2386</em>]'
result=re.search('all.*?(\d+)',sss)
print(result.group(1))