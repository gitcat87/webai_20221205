'''
    선형회귀...
'''

from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

np.set_printoptions(precision=1 ,suppress=True)

x=[[10,20],[30,40],[50,60]]
y=[15,35,55]

poly = PolynomialFeatures(include_bias=False,degree=5)
x_poly = poly.fit_transform(x)
print(np.round(x_poly,2))

lr=LinearRegression()
lr.fit(x_poly,y)

new=[[25,30]]
new = poly.transform(new)
print(new)
print()

prd = lr.predict(new)
print(prd)

print()
print()

print(lr.coef_, np.round(lr.intercept_))