import cv2

catcolor = cv2.imread('230227/cat.jpg',cv2.IMREAD_COLOR)
catgray = cv2.imread('230227/cat.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('catcolor',catcolor)
cv2.imshow('catgray',catgray)
cv2.waitKey(0)

cv2.destroyAllWindows

print(catcolor.shape)
print(catgray.shape)