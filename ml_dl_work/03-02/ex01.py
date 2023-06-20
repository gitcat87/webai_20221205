from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import numpy as np

x1 =np.array([22,50,120,180,200])
x1 =x1.reshape(-1,1)
y1 =[44,70,140,200,500]

x2 =np.array([30,40])
x2 =x2.reshape(-1,1)

nkr =KNeighborsRegressor(n_neighbors=1)
nkr.fit(x1,y1)

result = nkr.predict(x2)
print(result)