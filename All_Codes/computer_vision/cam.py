import cv2

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        print("Can't receive frame")
        break
    cv2.imshow("video",frame)
    if cv2.waitKey(1) == 27: # if you press esc
        break
cap.release()
cv2.destroyAllWindows()