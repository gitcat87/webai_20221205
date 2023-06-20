'''
    크림빵500원
    새우깡700원
    콜라400원
    잔돈을 하나도 남기지 않고 세가지 물건을 하나 이상 반드시 구매해야 한다.
    3500원이 되는 경우의 수

    >최소 물건을 하나씩은 사야 한다
'''
a=3500 - 500 - 700 - 400
print(a)
file1 = open("result.txt","a",encoding="UTF=8")

#1900 - (500*x + 700*y + 400*z)=0

for  x in range(5):
    for y in range(4):
        for z in range(5):
            if (1900 - (500*x + 700*y + 400*z))==0:
                print(f"크림빵 = {x+1}개 새우깡 = {y+1}개 콜라 = {z+1}개")
                print(f"x = {x} y = {y} z = {z}")
                file1.write(f"크림빵 = {x+1}개 새우깡 = {y+1}개 콜라 = {z+1}개\n")



print("무엇을 고르시겠습니까")


file1.close()
