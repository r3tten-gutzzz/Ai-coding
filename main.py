import cv2
import time
from fer import FER

# Load emotion detector
detector = FER()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error! failed to open camera")
    exit()

time.sleep(1)

# Filter toggles
blue_tint = False
red_tint = False
green_tint = False

while True:
    ret, frame = cap.read()

    if not ret:
       print("ERROR:- failed to capture image")
       break

    # ----------------- COLOR FILTERS -----------------
    if blue_tint:
        layer = frame.copy()
        layer[:, :, 0] = cv2.add(layer[:, :, 0], 80)   # Blue channel
        frame = layer

    if red_tint:
        layer = frame.copy()
        layer[:, :, 2] = cv2.add(layer[:, :, 2], 80)   # Red channel
        frame = layer

    if green_tint:
        layer = frame.copy()
        layer[:, :, 1] = cv2.add(layer[:, :, 1], 80)   # Green channel
        frame = layer
    # --------------------------------------------------

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face_region = frame[y:y+h, x:x+w]
        emotion = detector.top_emotion(face_region)

        if emotion is not None:
            emotion_name, emotion_score = emotion
            cv2.putText(frame, f"{emotion_name} ({emotion_score:.2f})",
                        (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 255, 0), 2)

    cv2.imshow("Filters: B=Blue | R=Red | G=Green | Q=Quit", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    # Toggle blue
    elif key == ord('b'):
        blue_tint = not blue_tint
        red_tint = False
        green_tint = False

    # Toggle red
    elif key == ord('r'):
        red_tint = not red_tint
        blue_tint = False
        green_tint = False

    # Toggle green
    elif key == ord('g'):
        green_tint = not green_tint
        red_tint = False
        blue_tint = False

cap.release()
cv2.destroyAllWindows()
