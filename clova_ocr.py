from requests_toolbelt import MultipartEncoder
import requests
import time
import uuid

file_path = "cam.jpg"

url = "https://3wxndinkw0.apigw.ntruss.com/custom/v1/31405/3375378951a1435da08aa3c03c182bf1d14e87fbf3892a10d55bcabfbe53629c/general"

headers = {
    "X-OCR-SECRET": "a1NkVlBoeW12VXlud2JpbXRPT25mTWZQSkx2Q3RmTEM=",
    "Content-Type": "multipart/form-data",
}

message = {
    "version": "1.0",
    "requestId": str(uuid.uuid4),
    "timestamp": int(time.time() * 1000),
    "lang": "ko",
    "images": [{"format": "jpg", "name": "cam", "templateIds": [0]}],
}


with open(file_path, "rb") as file:
    files = {"file": (file.name, file, "image/jpeg")}
    m = MultipartEncoder(fields=files, encoding="utf-8")

    body = {"message": message, "file": m}

    response = requests.post(url, files=files, data=message)

    # 응답 출력
    print(response.status_code)
    print(response.text)

# import uuid
# import json
# import time

# image_file = "cam.jpg"

# request_json = {
#     "images": [{"format": "jpg", "name": "cam"}],
#     "requestId": str(uuid.uuid4()),
#     "version": "V2",
#     "timestamp": int(round(time.time() * 1000)),
# }

# payload = {"message": json.dumps(request_json).encode("UTF-8")}
# files = [("file", open(image_file, "rb"))]
# headers = {
#     "X-OCR-SECRET": "a1NkVlBoeW12VXlud2JpbXRPT25mTWZQSkx2Q3RmTEM",
#     "Content-Type": "multipart/form-data",
# }

# response = response = requests.request(
#     "POST", url, headers=headers, data=payload, files=files
# )

# if response.status_code == 200:
#     ocr_results = json.loads(response.text)
#     all_texts = []  # 모든 텍스트를 저장할 리스트
#     for image_result in ocr_results["images"]:
#         for field in image_result["fields"]:
#             text = field["inferText"]
#             all_texts.append(text)  # 텍스트 추가

#     # 모든 텍스트를 띄어쓰기로 연결하여 출력
#     full_text = " ".join(all_texts)
#     print(full_text)
# else:
#     print(f"OCR 결과를 받아오지 못했습니다. 상태 코드: {response.status_code}")
