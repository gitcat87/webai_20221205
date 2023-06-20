from selenium import webdriver
import time
import pyautogui
from bs4 import BeautifulSoup
import re
import products as product
from openpyxl import Workbook

# requests 화면 크롬 X 없이 실행
# beatifulsoap

# inputvalue = pyautogui.prompt('상품이름을 입력하세요.')
# print(inputvalue)

inputvalue = '퓨마 운동화'

brow = webdriver.Chrome()   # 크롬브라우저 시작otepad
brow.get(f'https://www.coupang.com/np/search?q={inputvalue}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=6&backgroundColor=')  # www.naver.com 네이버 홈페이지 호출

html = brow.page_source
html = str(html).strip()
html = BeautifulSoup(html,'html.parser')

dl = html.find_all('dl',{'class','search-product-wrap'})
products = []
for tag in enumerate(dl):
    img =tag.find('img')
    price = tag.find('strong',{'class','price-value'})
    name = img.get('alt')
    imgsrc= img.get('data-img-src')
    price = price.text
     
    product.append=(product(name,imgsrc,price,f'a{idx}'))
                    
print(products)

wb = Workbook()
ws = wb.active

    
# print(html)
img = html.find_all('img',{'class','search-product-wrap-img'})
print(img)
print(brow.current_url)



# brow.close() # 현재탭 닫기
# brow.quit() # 크롬브라우저 종료
