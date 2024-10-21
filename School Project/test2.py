import keras_ocr
import matplotlib.pyplot as plt

# 1. Initialize the Keras-OCR pipeline
pipeline = keras_ocr.pipeline.Pipeline()

# 2. Load an image (your handwritten number image)
# Replace 'path_to_image.jpg' with the path to your image
image_path = 'saved_image/cv_image.png'
image = keras_ocr.tools.read(image_path)

# 3. Use the pipeline to recognize text
prediction_groups = pipeline.recognize([image])

# 4. Display the image and the detected text
# Plot the image with the recognized text
keras_ocr.tools.drawAnnotations(image=image, predictions=prediction_groups[0])

plt.imshow(image)
plt.axis('off')  # Hide axis
plt.show()

# 5. Print the recognized text
for text, box in prediction_groups[0]:
    print(f'Text: {text}, Bounding Box: {box}')
