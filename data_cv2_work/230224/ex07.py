import qrcode

img = qrcode.make('가만두지 않겠싸')
img.save('a.png')

img = qrcode.make('http://naver.com')
img.save('b.png')