import requests
from bs4 import BeautifulSoup
import re
import numpy as np
 
l1 = requests.get("https://www.dhlottery.co.kr/common.do?method=main") #requests를 이용해서 인터넷 홈페이지를 불러온다.
l2 = l1.content #l2는 l1의 내용으로 정의한다.
l3 = BeautifulSoup(l2, "html.parser") #BeautifulSoup를 이용해서 html을 분석한다."html.parser"
cl = re.compile('drwtNo.*') #홈페이지에 특정 문자열을 포함하는 것을 정의하기 위하여 re 이용
wn = [] #for 구문 시작 전에 빈 리스트로 정의해야한다.
for l4 in l3.find_all("span",{"id": cl}): #반복문을 통하여 특정 태그의 특정 id를 포함하는 태그열을 반복한다.
    wn.append(l4.get_text()) #리스트화
#print(wn)
#print("당첨번호 : " + l4.get_text()) #태그 안의 문자만 출력한다.
l5 = l3.find("span",{"id":"bnusNo"}).text #보너스 번호의 경우 별도로 떨어뜨린다.
bn = int(l5)
 
#print(bn) #보너스 번호 출력
# print("당첨번호는 %s 입니다." % (wn))
# print("보너스번호는 %s 입니다." % (bn))
 
wn = list(map(int, wn))
 
#print(l4)
#print(html) #모든 html의 태그를 보여준다.
#print(l2)
 
MyNum = [int(input("첫번째 번호 : ")), int(input("두번째 번호 : ")), int(input("세번째 번호 : ")), int(input("네번째 번호 : ")), int(input("다섯번째 번호 : ")), int(input("여섯번째 번호 : "))] #내 번호 입력
 
print ("당첨번호 : ",wn)
print ("보너스번호 : ",bn)
print ("내 번호 : ",MyNum)
 
k = 0
l = 0
for i in wn:
    if i in MyNum: #몇개 맞았나 확인
        k = k + 1
 
#print (k,"개 맞추셨습니다.")
 
if k == 5:
    if bn in MyNum:
        print ("2등")
    else:
        print ("3등")
elif k == 6:
    print ("1등")
elif k == 4:
    print ("4등")
elif k == 3:
    print ("5등")
else:
    print ("꽝")