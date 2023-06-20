from selenium import webdriver
import time
import pyautogui

# requests 화면 크롬 x없이 실행
# beautifulsoup

inputvalue=pyautogui.prompt('상품 이름을 입력하세요')
print(inputvalue)

brow = webdriver.Chrome() #크롬 브라우저 시작
brow.get(f'https://www.coupang.com/np/search?q={inputvalue}channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=6&backgroundColor=')

# inpu = brow.find_element('id','headerSearchKeyword')
# inpu.send_keys('퓨마 운동화')
#
# btn=brow.find_element('id','headerSearchBtn')
# btn.click()

#네이버 홈페이지 호출

brow.find_element('xpath','/html/body/div[3]/section/form/div[2]/div[2]/div[5]/span[1]/a[2]').click()

time.sleep(3) #3초쉬기
print(brow.current_url)

