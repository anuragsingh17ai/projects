import requests
from bs4 import BeautifulSoup as bs
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url="https://www.hindustantimes.com/editorials"

def fetchAndSaveToFile(url,path,headers):
    r=requests.get(url,headers=headers)
    with open(path,'r+',encoding='utf-8') as f:
        f.write(r.text)

def printhtml(path):
    with open(path,'r',encoding='utf-8') as f:
        html_doc=f.read()
    soup=bs(html_doc,'html.parser')
    # print(soup.text)
    # print(soup.title.string)
    # print(soup.div)
    print(soup.find(div='div-gpt-ad-1522659065797-0'))

printhtml('hi.html')

# fetchAndSaveToFile(url,'hi.html',headers)