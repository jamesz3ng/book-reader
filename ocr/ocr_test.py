import easyocr

reader = easyocr.Reader(["en", "ko"])

result = reader.readtext("english_poetry.jpeg", detail = 0)
korean_result = reader.readtext("korean_poetry.jpeg", detail = 0)
hand_writing_test = reader.readtext("IMG_9161.jpeg", detail = 0)

korean_english_test = reader.readtext("korean_english.png", detail = 0)

for line in korean_english_test:
    print(line)

# print("Hand Writing Test")
# for line in hand_writing_test:
#     print(line)
# print("Handing writing test end")
# print("\n -------------")


# print("English Test")
# for line in result:
#     print(line)

# print("English Test end")
# print("\n -------------")


# print("Korean Test")
# for line in korean_result:
#     print(line)
# print("Korean Test End")



