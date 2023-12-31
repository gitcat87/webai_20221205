import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 
     1000.0, 1000.0]
     )

#plt.plot(perch_length,perch_weight)
#plt.plot([10,25,55],[10,33,111])
#plt.scatter([10,25,55],[10,33,111])
# plt.scatter(perch_length,perch_weight)
plt.xlabel('length')
plt.xlabel('weight')
#plt.show()


x1,x2,y1,y2 =train_test_split(perch_length,perch_weight,random_state=42)
x1 = x1.reshape(-1,1)
x2 = x2.reshape(-1,1)
print(x1.shape)
print(x2.shape)
print(y1.shape)
print(y2.shape)

print()

print(x1[:5])
print(x2[:5])
print(y1[:5])
print(y2[:5])

myscore = []

for n in range(1,20):
    knr =KNeighborsRegressor(n_neighbors=n)
    knr.fit(x1,y1) #학습을 진행해라

    result = knr.predict([[10],[30],[50]])
    # print(result)

    my_perdict_y = knr.predict(x2,)
    # print(x2.reshape(-1))
    # print(y2)
    # print(my_perdict_y)
    
    
    print("이웃되는 점",n)
    mae =  mean_absolute_error(y2,my_perdict_y)
    print(mae)
    myscore.append(mae)
    mse =  mean_squared_error(y2,my_perdict_y)
    print(mse,end="\n\n")

print(myscore)

plt.plot(range(1,20),myscore)
plt.show()

# plt.scatter(perch_length, perch_weight)
# plt.scatter(x2,y2,marker='^')
# plt.scatter(x2,my_perdict_y,marker='D')
# plt.plot(sorted(x2),sorted(my_perdict_y))
# plt.xlabel('length')
# plt.xlabel('weight')
# plt.show()

