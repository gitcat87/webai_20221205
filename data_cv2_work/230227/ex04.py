import cv2
import time

cat = cv2.imread('230227/cat.jpg',cv2.IMREAD_COLOR)


startTime =time.time()
print(startTime)

for i in range(300):
    for j in range(300):
        cat[i,j] = [255,255,255]
print(f"time.time() -starttime = {time.time() - startTime}")

startTime = time.time()
cat[:300,:300] =[0,0,0]
print(f"time.time() -starttime = {time.time() - startTime}")


cv2.imshow('cat',cat)
cv2.waitKey(0) == ord('q')


print('종료됨')
cv2.destroyAllWindows()