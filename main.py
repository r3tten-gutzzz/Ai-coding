import cv2
import pytesseract
import os
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError("Image path does not exist ")
    image = cv2.imread(image_path)
    if image is None:
         raise ValueError("unsupported image format or coruppted image")
    return image

def processes_image(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _ , thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)
    return thresh

def extract_text(processed_image):
    config = "--psm 6"
    text = pytesseract.image_to_string(processed_image, config=config)
    return text.strip

def save_to_text_file(text, directory="output"):
    os.makedirs(directory,exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(directory, f"extracted_text_{timestamp}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
    return file_path

def main():
    try:
        image_path = input("Enter image path: ").strip
        image = load_image(image_path)
        processed_image = processes_image(image)
        text = extract_text(processed_image)

        if not text:
            print("No readable text detected.")
            return
        
        print("\n-------extracted text-------\n")
        print(text)
        print("\n----------------------------\n")

        choice = input("Save this text as a .txt file? (yes/no): ").lower().strip()
        if choice == "yes":
            file_path = save_to_text_file(text)
            print(f"text successfully saved at: {file_path}")
        else:
            print("text not saved")
        
    
    except Exception as e:
        print(f"Process failed: {e}")

if __name__ == "__main__":
    main()