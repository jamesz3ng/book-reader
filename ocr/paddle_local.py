from paddleocr import PaddleOCR
from gtts import gTTS, lang
import os 


# Initialize PaddleOCR with the Korean language model
ocr = PaddleOCR(lang='korean')  

# Load an image for OCR
# img_path = 'korean_poetry.jpeg'
img_path = "english_test.png"

# Run OCR on the image
results = ocr.ocr(img_path, cls=False)


korean_characters = [text for result in results for _, (text, _) in result if any('\u3131' <= char <= '\uD79D' for char in text)]

print(korean_characters)

characters_combined = ""
for line in korean_characters:
    line = " " + line
    characters_combined += line

print(characters_combined)


# tts = gTTS(text =characters_combined, lang = "ko")
# tts.save("characters_combined.mp3")

# os.system("afplay characters_combined.mp3")


# korean_characters = [text for _, (text, _) in results if any('\u3131' <= char <= '\uD79D' for char in text)]

