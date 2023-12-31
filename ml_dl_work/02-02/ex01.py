import numpy as np
import matplotlib.pyplot as mat
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
               31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
               35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
               10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
               500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
               700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
               7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = np.column_stack((fish_length,fish_weight))
fish_target =  np.concatenate(['bream'](35),'smelt'(14))

train_input, test_input, train_target, test_target =  train_test_split(fish_data,fish_target,random_state=42)


mat.scatter(train_input[:,0],train_input[:,1])
mat.scatter(test_input[:,0],test_input[:,1])
mat.scatter(25,150,marker='^')
mat.show()

knr = KNeighborsClassifier()
knr.fit(train_input,train_target)
result=  knr.predict([[25,150]])
pinrt=(result)

#(원값 - 평균값) / 표준점수
fish_scaled = (fish_data - np.mean(fish_data,axis=0)) /np.std(fish_data, aixis=0)

print(fish_scaled[:5])

new = (np.array([25,150]) - np.mean(fish_data,axis=0)) /np.std(fish_data,aix=0)
print(new)

#기계학습 진행
knr = KNeighborsClassifier()
knr.fit(fish_scaled,fish_target)



distances,indexs = knr.kneighbors(new)

plt.scatter(fish_scaled[:0], fish_scaled[:-1])
plt.scatter(new:[0], new:[-1], marker-'^')
plt.scatter(fish_scaled[indexs,0],fish_scaled[indexs,1],marker='D')

