import cv2


cat = cv2.imread('230227/cat.jpg')

logo =cat [100:200,100:200]
cv2.imshow('logo',logo)
cv2.waitKey(0) == ord('q')

cat[0:100,0:100] =logo

cv2.imshow('cat',cat)
cv2.waitKey(0) == ord('q')

cv2.destroyAllWindows()