import cv2

cat = cv2.imread('230227/cat.jpg')


print(cat[100,100])
print(cat[100,100,2])


cv2.imshow('cat',cat)
cv2.waitKey(0) == ord('q')
print('종료됨')

cv2.destroyAllWindows()
