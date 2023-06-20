from bs4 import BeautifulSoup
import requests

url ="https://dhlottery.co.kr/common.do?method=main"


req = requests.get(url)

req.encoding="utf-8"

bs = BeautifulSoup(req.text,"html.parser")

div = bs.find('div',{'id':'winnerId'}).text

turn = bs.find('strong',{'id':'lottoDrwNo'}).text
num1 = bs.find('span',{'id':'drwtNo1'}).text
num2 = bs.find('span',{'id':'drwtNo2'}).text
num3 = bs.find('span',{'id':'drwtNo3'}).text
num4 = bs.find('span',{'id':'drwtNo4'}).text
num5 = bs.find('span',{'id':'drwtNo5'}).text
num6 = bs.find('span',{'id':'drwtNo6'}).text

print(div)
print("이번회차는",turn,"회 입니다")
print(num1,num2,num3,num4,num5,num6)
# print("1등 당첨 금액 입니다 FirstPrize 원")

# from openpyxl import Workbook

# wb= Workbook()
# ws= wb.active

# ws.append(["로또번호"])
# ws.append(["번호1","번호2","번호3","번호4","번호5","번호6"])
# ws.append([sutja1,sutja2,sutja3,sutja4,sutja5,sutja6])
# ws.append(["1등 당첨 금액 입니다",FirstPrize])


# wb.save("lotto2.xlsx")
# wb.close()


