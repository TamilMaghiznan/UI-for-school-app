import pytesseract
from PIL import Image
from tkinter import Tk, filedialog

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set path to tesseract executable if needed (modify it based on your system setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to upload and recognize text from image
def upload_and_recognize_text():
    # Initialize tkinter for file dialog
    root = Tk()
    root.withdraw()  # Hide the main tkinter window

    # Open file dialog to select an image file
    image_path = filedialog.askopenfilename(title='Select an image', filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp')])

    if image_path:
        try:
            # Open the selected image
            img = Image.open(image_path)

            # Use Tesseract to do OCR on the image
            recognized_text = pytesseract.image_to_string(img)

            # Output the recognized text
            print("Recognized Text:")
            print(recognized_text)
        except Exception as e:
            print(f"Error recognizing text: {e}")
    else:
        print("No file selected.")

# Call the function to upload and recognize text
upload_and_recognize_text()
