import requests
from bs4 import BeautifulSoup
import bs4
import re
url="http://223.4.64.202/zjqxkqfb/index"
r=requests.get(url)
r.raise_for_status()
encoding=r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,"html.parser") 
iii=soup.find_all(class_='top-val')

#for div in soup.find_all(class_='top-val'):
 #   print(div.find_all(name='span'))
  #  for span in div.find_all(name='span'):
   #     print(span.string)
#写多重循环，找共性           或者直接用正则 
for li in soup.find_all(class_='ui-datalist-item'):
    for div in li.find_all(name='div'):
        for span in div.find_all(name='span'):
            print(span.string)
