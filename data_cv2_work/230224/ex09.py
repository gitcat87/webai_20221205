import cv2

cat = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
cat1 = cat.copy()
cat1 = cat1[:,:,0]
cv2.imshow('cat',cat1)
cv2.imwrite('cat1.jpg',cat1)

cat2 = cat.copy()
cat2 = cat2[:200,:200]
cv2.imshow('cat2', cat2)
cv2.imwrite('cat2.jpg', cat2)

dog = cv2.imread('dog.jpg',cv2.IMREAD_COLOR)
dog =cv2.resize(dog,(600,600))
dog =cv2.cvtColor(dog,cv2.COLOR_BGR2GRAY)
print(dog)
cv2.imshow('dog',dog)
cv2.waitKey(0)
cv2.imwrite('dog.jpg',dog)