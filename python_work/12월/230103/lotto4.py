import requests
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook, load_workbook


url ="https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=1"

req = requests.get(url)

req.encoding="euc-kr"

bs = BeautifulSoup(req.text,"html.parser")

turn =bs.select("#article > div:nth-child(2) > div > div.win_result > h4 > strong")
numbers= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span")
bonus= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span")
potmoney = bs.select("#article > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > strong")

print("제",turn[0].text)
print("당첨번호",numbers[0].text,numbers[1].text,numbers[2].text,numbers[3].text,numbers[4].text,numbers[5].text)
print("보너스번호입니다.",bonus[0].text)
print()
if potmoney[0].text=='0원':
    print("1등 당첨자가 없었습니다")
else:
    print("1등 총 당첨금",potmoney[0].text)
print()

wb= Workbook()
ws= wb.active

# ws.append(['11','22'])
ws.append([numbers[0].text,numbers[1].text,numbers[2].text,numbers[3].text,numbers[4].text,numbers[5].text,'+',bonus[0].text])


wb.save("lotto4.xlsx")
wb.close()