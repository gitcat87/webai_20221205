class MyError(Exception):
    def __str__(self):
        return "바보 닉네임은 설정 할 수 없습니다."

def sayNick(nick):
    if nick == '바보':
        raise MyError
    else:
        print(f"{nick}(이) 설정되었습니다")

sayNick('천사')
try:
    sayNick('바보')
except MyError as e:
    print('바보 닉네임은 설정 할 수 없습니다')
