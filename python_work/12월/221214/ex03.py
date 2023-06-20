'''
    계속 반복이 되도록
    입력받은 숫자에 대한
    while 구문으로 구구단을 출력하자

'''
info = '''
    1. 몇단의 구구단을 출력하시겠습니까?
    종료를 원하시면 음수를 입력하세요.
'''
while True:
    print(info)
    gugudan = input()
    gugudan = int(gugudan)
    if gugudan < 0:
        print("종료합니다")
        break
    elif gugudan ==0:
        print("0단은 보여줄 수 없습니다.")
    else:
        a = 1
        while(a < 10):
            print(f"{gugudan}*{a}={gugudan*a}")
            a +=1

