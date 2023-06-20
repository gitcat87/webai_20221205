import numpy as np

li = np.arange(8).reshape(-1,4)
print(li)
print()

left, right = np.split(li,[2],axis=1)

print(left.shape)
print(right.shape)

print(right[1][1])