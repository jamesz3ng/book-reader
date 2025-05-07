from gtts import gTTS
import os
import easyocr
from paddleocr import PaddleOCR


reader = easyocr.Reader(["ko"])

korean_result = reader.readtext("korean_poetry.jpeg", detail = 0)
print(korean_result)

result_collated = ""
for line in korean_result:
    line = " " + line
    result_collated += line

print(result_collated)
# Korean text
korean_text = "안녕하세요. 저는 인공지능입니다."

# Convert text to speech
tts = gTTS(text=result_collated, lang='ko')

# Save the audio file
tts.save("result_collated.mp3")



os.system("afplay result_collated.mp3")  # For macOS
