import numpy as np
import matplotlib.pyplot as plt

li = np.array([1,2,3,4])

test = li.reshape(-1,2)
print(test)

plt.imshow(test)
plt.show()

# ali = np.array([[0,1],[1,0]])
# ali = ali.astype(np.uint8)

# import cv2

# cv2.imshow('test',ali)
# cv2.waitKey(-1)