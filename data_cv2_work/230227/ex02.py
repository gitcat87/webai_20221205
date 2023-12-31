import cv2

cap  = cv2.VideoCapture('230227/video.mp4')

while cap.isOpened():  #동영상 파일이 열려 있다면
    ret, frame = cap.read()
    if not ret:
        print("가져올 프레임 없음")
        break
    cv2.line(frame,(0,0),(200,200),(255,0,0),3)
    cv2.imshow('video',frame)
    
    if cv2.waitKey(1) ==ord('q'):
        print('종료 됩니다.')
        break
cap.release()
cv2.destroyAllWindows()