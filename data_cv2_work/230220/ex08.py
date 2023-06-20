import numpy as np

test= np.random.randint(1,10,4).reshape(-1,2)
#1부터 9까지 4개의 숫자를...
#뽑은 4개의 숫자로 2행 2열의 2차원 배열로 만들어라
print(test)


test =  test*10
#거기에 각 요소마다 곱하기 10을 하여라
print(test)
print()
a = np.arange(4).reshape(-1,2)
b = np.arange(2)

print(a)
print(b)
print(a+b)