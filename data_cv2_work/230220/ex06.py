import numpy as np

li = np.arange(1,13)
print(li)

ali =  li.reshape(-1,4)
print(ali)

print('평균값')
print(np.mean(ali,axis=0)) #세로로 더해서 평균
print(np.mean(ali,axis=1)) #가로로 더해서 평균

print('더한값')
print(np.sum(ali,axis=0))
print(np.sum(ali,axis=1))

print('순위')
print(np.argmax(ali,axis=0))
print(np.argmax(ali,axis=1))