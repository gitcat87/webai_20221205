import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=1043%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8"

l1 = requests.get(url)
l1.encoding="utf-8"

l2 = l1.content
l3 = BeautifulSoup(l2, "html.parser")

wn=[]
for l4 in l3.find_all('span',{'class'})