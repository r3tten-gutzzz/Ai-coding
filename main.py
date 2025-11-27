import cv2
import numpy as np

# ---------------------------
#  Settings
# ---------------------------
USE_WEBCAM = True   # Set to False to load an image: path below
IMAGE_PATH = "your_image.jpg"
# ---------------------------


# Tint function
def apply_tint(frame, r, g, b, alpha):
    tint = np.full(frame.shape, (b, g, r), dtype=np.uint8)
    return cv2.addWeighted(frame, 1 - alpha, tint, alpha, 0)


# Trackbar callback (unused)
def nothing(x):
    pass


cv2.namedWindow("Tint Filter", cv2.WINDOW_AUTOSIZE)

# Create trackbars
cv2.createTrackbar("Red", "Tint Filter", 0, 255, nothing)
cv2.createTrackbar("Green", "Tint Filter", 0, 255, nothing)
cv2.createTrackbar("Blue", "Tint Filter", 0, 255, nothing)
cv2.createTrackbar("Opacity (%)", "Tint Filter", 0, 100, nothing)

# Load webcam or image
if USE_WEBCAM:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera error!")
        exit()
else:
    frame = cv2.imread(IMAGE_PATH)
    if frame is None:
        print("Image not found!")
        exit()

while True:

    if USE_WEBCAM:
        ret, frame = cap.read()
        if not ret:
            break
    else:
        frame = frame.copy()

    # Get trackbar values
    r = cv2.getTrackbarPos("Red", "Tint Filter")
    g = cv2.getTrackbarPos("Green", "Tint Filter")
    b = cv2.getTrackbarPos("Blue", "Tint Filter")
    alpha = cv2.getTrackbarPos("Opacity (%)", "Tint Filter") / 100.0

    # Apply tint
    tinted = apply_tint(frame, r, g, b, alpha)

    cv2.imshow("Tint Filter", tinted)

    key = cv2.waitKey(1)
    if key == 27:  # ESC to exit
        break

if USE_WEBCAM:
    cap.release()

cv2.destroyAllWindows()
