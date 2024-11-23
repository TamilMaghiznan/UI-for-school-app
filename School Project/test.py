import cv2
import numpy as np
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('Model.h5')

# Function to preprocess and predict
def testing(img):
    img = cv2.bitwise_not(img)
    img = cv2.resize(img, (28, 28))  # Resize to match the model input size
    img = img.reshape(1, 28, 28, 1).astype('float32') / 255.0
    return model.predict(img)

# Mapping predictions to symbols
def num_to_sym(x):
    symbols = {10: '+', 11: '-', 12: '*', 13: '/', 14: '(', 15: ')', 16: '.'}
    return symbols.get(x, str(x))

# Solve the mathematical expression
def solve_exp(preds):
    expression = "".join([num_to_sym(ind) for ind, acc in preds])
    try:
        result = eval(expression)
        return f"{expression} = {result:.4f}"
    except Exception:
        return "Invalid expression"

# Ensure square aspect ratio for cropped digits
def make_square(image):
    h, w = image.shape[:2]
    if h == w:
        return image  # Already square
    size = max(h, w)
    delta_w = size - w
    delta_h = size - h
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)
    color = 255  # Padding color (white)
    return cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

# Process the uploaded image and predict
def process_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return "Error: Unable to read image."
    
    # Preprocess the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bw = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)[1]
    bw = cv2.bitwise_not(bw)

    # Find contours and sort by position
    contours, _ = cv2.findContours(bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

    preds = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cropped = gray[y:y + h, x:x + w]

        # Make the cropped region square
        cropped = make_square(cropped)

        # Resize to 28x28
        cropped = cv2.resize(cropped, (28, 28))

        # Predict
        pred = testing(cropped)
        ind = np.argmax(pred[0])
        acc = pred[0][ind] * 100
        preds.append((ind, acc))
    
    return solve_exp(preds)
    
image_path="saved_image/processed1_image.png"
    
result = process_image(image_path)
print("Result:", result)

