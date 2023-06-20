# 로또 번호 조회 프로그램

* 최신 게임과 원하는 게임의 당첨번호와 상금 내역을 조회할 수 있습니다.

## 제작환경

* Python(requests, beautifulsoup, openpyxl)
* QT Designer

## 동작개요

* Python 기반 requests, beautifulsoup, openpyxl 라이브러리를 활용하여 웹 크롤링을 통해 데이터를 추출 및 가공을 할 수 있다.
* 가공한 데이터를 QT Designer로 응용 어플리케이션 형태로 제작해 보여준다.

<br>
<br>

#

![](https://github.com/gitcat87/Lottery/blob/main/images/image1.png?raw=true)
<br>


```python

class FirstClass(QWidget) :
    def __init__(self) :
        super().__init__()
        self.ui = uic.loadUi("lotto/number.ui",self)

        self.num1.setText("")
        self.num2.setText("")
        self.num3.setText("")
        self.num4.setText("")
        self.num5.setText("")
        self.num6.setText("")
        self.bns1.setText("")

        DateTime= datetime.datetime.now()

        self.date.setText('오늘 날짜: %s년 %s월 %s일' %(DateTime.year, DateTime.month, DateTime.day))
        

        self.calllottery.clicked.connect(self.doA) #최근조회 실행
        self.numbutton.clicked.connect(self.doB) #직접입력 조회 실행
        self.data1.clicked.connect(self.doD) #통계조회 실행
        self.show() 

```
* 파일 구동 후 QT Designer로 작성한 Form이 출력됩니다.

<br>
<br>

#

![](https://github.com/gitcat87/Lottery/blob/main/images/image2.png?raw=true)

![](https://github.com/gitcat87/Lottery/blob/main/images/image3.png?raw=true)

<br>
```python
import requests
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook, load_workbook


def lot2(self):
    url ="https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="

    req = requests.get(url)

    req.encoding="euc-kr"

    bs = BeautifulSoup(req.text,"html.parser")

    turn =bs.select("#article > div:nth-child(2) > div > div.win_result > h4 > strong")
    numbers= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span")
    bonus= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span")
    potmoney = bs.select("#article > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td:nth-child(4)")
    pot = potmoney[0].text
    print("제",turn[0].text)
    print("당첨번호",numbers[0].text,numbers[1].text,numbers[2].text,numbers[3].text,numbers[4].text,numbers[5].text)
    print("보너스번호입니다.",bonus[0].text)
    print()
    if potmoney[0].text=='0원':
        print("1등 당첨자가 없었습니다")
    else:
        print("1등 당첨금",potmoney[0].text)


    wb= Workbook()
    ws= wb.active


    ws.append(['제',turn[0].text])
    ws.append([numbers[0].text,numbers[1].text,numbers[2].text,numbers[3].text,numbers[4].text,numbers[5].text,'+',bonus[0].text])

    if potmoney[0].text=='0원':
        ws.append(['1등 당첨자가 없었습니다'])
    else:
        ws.append(['1등 총 당첨금은',pot])

    wb.save("lotto/lotto4.xlsx")
    wb.close()
```

* request, beautiful로 사이트의 raw data를 가져온 후 정제하여 openpyxl 라이브러리를 이용해 엑셀시트에 저장합니다.


