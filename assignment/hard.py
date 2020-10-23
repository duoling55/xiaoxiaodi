import requests
from bs4 import BeautifulSoup
import bs4
import json
import re
url="http://www.mca.gov.cn//article/sj/xzqh/2020/2020/2020092500801.html"
r=requests.get(url)
r.raise_for_status()
encoding=r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,"html.parser") 
province=[]
shi=[]
xiann=[]

resultall=[]
for tr in soup.find_all('tr',height=re.compile('19')):
    td=tr.find_all('td')
    if td[1].string[-4:]=='0000':
        province=[td[1].text,td[2].text]
        shi=[]
    elif td[1].string[-2:]=='00':
        shi=[td[1].text,td[2].text]
    else:
        xiann=[td[1].text,td[2].text]   #
        if shi==[]:
           shi[0]=xiann[0],shi[1]=xiann[1]
        
        result={
        '名称:'province[1]+shi[1]+xian[1],
        province[0],shi[0],xiann[0] }

        resultall.append(result)
with open('resultall.json','w',encoding='utf-8')as file:
    file.write(json.dumps(resultall,ensure_ascii=False,indent=2))




    