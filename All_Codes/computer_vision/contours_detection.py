import cv2

cap = cv2.VideoCapture(r"C:\Users\Lenovo\Videos\a.mp4")
while True:
    ret,frame = cap.read()
    if not ret:
        print("Can't receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,100,255,0)
    con, heir = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, con, -1, (255,0,0), 1)
    cv2.imshow("video",frame)
    if cv2.waitKey(1) == 27: # if you press esc
        break
cap.release()
cv2.destroyAllWindows()