import numpy as np

a = np.arange(16).reshape(-1,4)
b=a<10

print(a)
print()
print(b)
print()

print(a[b])
#a에서 true로 표시된 것만 출력해줘
a[b] =100
#a에서 true로 표시된 것에 100을 넣어줘
print(a)