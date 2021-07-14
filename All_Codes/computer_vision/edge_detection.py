import cv2

cap = cv2.VideoCapture(r"C:\Users\Lenovo\Videos\a.mp4")
while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    edges = cv2.Canny(frame,100,200)
    if not ret:
        print("Can't receive frame")
        break
    cv2.imshow("video",frame)
    cv2.imshow("edges",edges)
    if cv2.waitKey(1) == 27: # if you press esc
        break
cap.release()
cv2.destroyAllWindows()