import numpy as np

a1= np.arange(0,8).reshape(2,4)
a2= np.arange(0,8).reshape(2,4)

a3= np.concatenate([a1,a2],axis=0) # 각행을 더하지 말고 열을 이어 붙여줘
a4= np.arange(0,4).reshape(4,1) #4행 1열로 만들어줘

print(a1)
print(a2)
print()

print(a3)
print(a4)
print()

print(a3+a4) 