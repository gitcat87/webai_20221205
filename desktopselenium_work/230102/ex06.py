import requests
from bs4 import BeautifulSoup

try:
    input_value='퓨마 운동화'
    html =requests.get(f'https://www.coupang.com/np/search?q={input_value}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=6&backgroundColor=')
    html.encoding='utf-8'

    html = BeautifulSoup(html,'html.parser')
    print(html)
except Exception as e:
    print(e)