import requests
from bs4 import BeautifulSoup


r = requests.get('http://naver.com')
bs = BeautifulSoup


bs(r.content,"html.parser")

print(bs)
