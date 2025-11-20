import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()

    if filter_type == "original":
        return filtered_image
    
    elif filter_type == "red_tint":
        filtered_image[:, :,1] = 0
        filtered_image[:, :,0] = 0

    elif filter_type == "blue_tint":
        filtered_image[:, :,1] = 0
        filtered_image[:, :,2] = 0

    elif filter_type == "green_tint":
        filtered_image[:, :,0] = 0
        filtered_image[:, :,2] = 0

    return filtered_image


image_path = 'Example.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error:image not found!")
else:
    image = cv2.resize(image, (1200,800))
    filter_type = "Original"

    while True:
        filtered_image = apply_color_filter(image, filter_type)

        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('o'):
            filter_type = 'original'
        elif key == ord('r'):
            filter_type = 'red_tint'
        elif key == ord('b'):
            filter_type = 'blue_tint'
        elif key == ord('g'):
            filter_type = 'green_tint'
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key!")

    cv2.destroyAllWindows()
        
        
        



