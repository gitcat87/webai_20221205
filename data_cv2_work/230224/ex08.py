import cv2
import debugpy

cat = cv2.imread('cat.jpg')
print(cat.shape) 
#399,600,3 이렇게 나오는데 399줄에 600열이나 되는 데이터 3면이 겹쳐져 있다. 3차원으로 라는 뜻
#print(cat[::100])

cv2.imshow('cat',cat)
cv2.waitKey(0) #사용자 입력을 받는키 그런데 0을 주면 무한대기


dog = cv2.imread('dog.jpg')
dog  =cv2.resize(dog,(600,399))
print(dog.shape) 
#399,600,3 이렇게 나오는데 399줄에 600열이나 되는 데이터 3면이 겹쳐져 있다. 3차원으로 라는 뜻
#print(cat[::100])

cv2.imshow('dog',dog)
key = cv2.waitKey(0)
print(key)


shark = cv2.imread('shark.jpg')
shark =cv2.resize(shark,(600,399))
print(shark.shape) 
#399,600,3 이렇게 나오는데 399줄에 600열이나 되는 데이터 3면이 겹쳐져 있다. 3차원으로 라는 뜻
#print(cat[::100])

cv2.imshow('shark',shark)
key = cv2.waitKey(0)
print(key)


