import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error:- unable to access camera")
    exit()

print("Press SPACE to capture the image or ESC to exit")

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to get frame")
        break
    cv2.imshow("Camera-press SPACE to Capture",frame)

    key = cv2.waitKey(1)

    if key ==32:
        image_name = "captured_image.jpg"
        cv2.imwrite(image_name,frame)
        print(f"Image captured and saved as '{image_name}'")
        break
    elif key == 27:
        print("Capture Cancelled.")
        break


camera.release()
cv2.destroyAllWindows()  



