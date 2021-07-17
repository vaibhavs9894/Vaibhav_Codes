import cv2
import mediapipe as mp

face_detection = mp.solutions.face_detection
drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with face_detection.FaceDetection(model_selection=0,min_detection_confidence = .5) as face_detector:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Empty camera Frame")
            continue
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #cv2.imshow("Camera", image)
        image.flags.writeable = False # to improve performance
        results = face_detector.process(image)
        image.flags.writeable = True
        if results.detections:
            for detection in results.detections:
                drawing.draw_detection(image,detection)
        cv2.imshow("Face Detection", image)
        if cv2.waitKey(1) == 27:
            break
cap.release()
cv2.destroyAllWindows()
