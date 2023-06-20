import requests

import bs4
import sys

URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(URL)
html = bs4.BeautifulSoup(raw.text, 'html.parser')

# sys.stdout = open('lotto23.txt','w',encoding="utf-8")
# print(html)
# sys.stdout.close()

target = html.find('div', {'class', 'nums'})
            # beautifulsoup로 갈무리한 html에서,  div태그 안에 class이면서 num이름
            #을 지닌 부분을 변수명 target에 넣어줘라
            #<div class="nums"> xxxxxxxxxxxxxxxxx </div>
# print("target",target)
# print(target)

balls = target.find_all("span", {'class', 'ball_645'})
for ball in balls:
    print(ball.text)


# for ball in balls:
#     print("당첨번호 : ", ball.text)
# print("보너스 번호 :", balls[-1].text)

