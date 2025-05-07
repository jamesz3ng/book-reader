from numpy import character
import pytesseract
from PIL import Image, ImageOps
from gtts import gTTS, lang
import os
import cv2

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

# Preprocess the image
img = Image.open('scanned_book.jpg')
img = ImageOps.grayscale(img)
img = img.point(lambda x: 0 if x < 140 else 255, '1')
img.save('test_korean_preprocessed.png')

# Ensure the image has 300 DPI
img = Image.open('test_korean_preprocessed.png')
img.save('test_korean_300dpi.png', dpi=(300, 300))

# Perform OCR with custom configuration
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(Image.open('test_korean_300dpi.png'), lang='kor', config=custom_config)

# Display the results
print(text)

characters_combined = ""

for line in text:
    characters_combined += line


tts = gTTS(text =characters_combined, lang = "ko")
tts.save("characters_combined.mp3")

os.system("afplay characters_combined.mp3")
