import cv2
import mediapipe as mp

drawing = mp.solutions.drawing_utils
objectron = mp.solutions.objectron

cap = cv2.VideoCapture(0)
with objectron.Objectron(
    static_image_mode = False,
    max_num_objects = 5,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.9,
    model_name = "Cup") as object_track:
    while True:
        success, image = cap.read()
        if not success:
            print("Empty camera Frame")
            continue
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False # to improve performance
        results = object_track.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.detected_objects:
            for result in results.detected_objects:
                drawing.draw_landmarks(image,result.landmarks_2d,objectron.BOX_CONNECTIONS)
                drawing.draw_axis(image,result.rotation,result.translation)
        cv2.imshow("Cup finder", image)
        if cv2.waitKey(1) == 27:
            break
cap.release()
cv2.destroyAllWindows()