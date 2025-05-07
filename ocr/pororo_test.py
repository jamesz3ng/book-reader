from pororo import Pororo

ocr = Pororo(task="ocr", lang="ko")
image_path = input("Enter image path: ")
text = ocr(image_path, debug=True)
print('Result :', text)
