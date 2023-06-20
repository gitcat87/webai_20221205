import cv2
import numpy as np

cat =cv2.imread('230227/cat.jpg')
cv2.imshow('cat',cat[:,:,0])
cv2.waitKey(0) == ord('q')
cat2 = np.copy(cat)

cat[:,:,1] = 200
cv2.imshow('cat',cat)
cv2.waitKey(0) == ord('q')

cat[:,:,2] = 0
cv2.imshow('cat',cat)
cv2.waitKey(0) == ord('q')


cv2.destroyAllWindows()