import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import screen_brightness_control as sbc

cap = cv2.VideoCapture(0) 
detector = HandDetector(maxHands=1, detectionCon=0.7)

prev_y = None
brightness = sbc.get_brightness()[0]

while True:
    sucess, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        finger = hand["ImList"][8]
        x , y , z = finger

        if prev_y is not None:
            diff = prev_y - y
            
            if diff > 20:
                brightness = min(brightness + 5, 100)
                sbc.set_brightness(brightness)

            elif  diff < -20:
                brightness = max(brightness - 5, 0)
                sbc.set_brightness(brightness)


        prev_y = y 

        cv2.putText(img, f"Brightness: {brightness}%", (30,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv2.imshow("Brightness Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



