import pytesseract
from PIL import Image, ImageOps
from gtts import gTTS
import os
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

import cv2
import numpy as np

def preprocess_image(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Increase contrast
    alpha = 1.5 # Contrast control (1.0-3.0)
    beta = 0    # Brightness control (0-100)
    contrasted = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(contrasted, (5, 5), 0)

    # Apply adaptive thresholding
    binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Remove noise
    kernel = np.ones((1, 1), np.uint8)
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    # Deskew the image
    coords = np.column_stack(np.where(binary > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = binary.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    binary = cv2.warpAffine(binary, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # Save the preprocessed image
    preprocessed_image_path = 'test_korean_preprocessed.png'
    cv2.imwrite(preprocessed_image_path, binary)

    return preprocessed_image_path

# Preprocess the image
preprocessed_image_path = preprocess_image('scanned_book.jpg')

# Ensure the image has 300 DPI
img = Image.open(preprocessed_image_path)
img.save('test_korean_300dpi.png', dpi=(300, 300))

# Perform OCR with custom configuration
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(Image.open('test_korean_300dpi.png'), lang='kor', config=custom_config)

# Display the results
print(text)

# Combine text into a single string
characters_combined = "".join(text)

# Convert text to speech
tts = gTTS(text=characters_combined, lang='ko')
tts.save("characters_combined.mp3")

# Play the mp3 file
os.system("afplay characters_combined.mp3")
