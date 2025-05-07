from paddleocr import PaddleOCR
from gtts import gTTS, lang
from langdetect import detect
import os

# Initialize PaddleOCR with the Korean language model
ocr = PaddleOCR(use_angle_cls=True, lang="korean")

# Load an image for OCR
# img_path = 'korean_poetry.jpeg'
img_path = "english_test.png"

# Run OCR on the image
results = ocr.ocr(img_path, cls=True)

characters = [
    text
    for result in results
    for _, (text, _) in result
    if any("\u3131" <= char <= "\uD79D" for char in text)
]

print(f"Text: {characters}")

characters_combined = ""
for line in characters:
    line = " " + line
    characters_combined += line

print(characters_combined)

# Detect language
detected_lang = detect(characters[0])
print(f"The Detected Language: {detected_lang}")

try:
    if detected_lang != "ko" and detected_lang != "en":
        raise Exception("Language is not KOR and ENG")

    tts = gTTS(text=characters_combined, lang=detected_lang)
    tts.save("characters_combined.mp3")

    os.system("afplay characters_combined.mp3")
except Exception as e:
    print(f"ERROR: {e}")

# korean_characters = [text for _, (text, _) in results if any('\u3131' <= char <= '\uD79D' for char in text)]
