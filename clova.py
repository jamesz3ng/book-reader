import requests
import uuid
import time
import base64
import json

api_url = "https://3wxndinkw0.apigw.ntruss.com/custom/v1/31984/e97996532a42c3787cca40289c421443d54d87c0147abbac99e3cee7064757f1/general"
secret_key = "VlBLd1ZNVFdEcENVRFdQbFBpVER5aFJYRVhGckdNclk="
image_file = "cam.jpg"
with open(image_file, "rb") as f:
    file_data = f.read()

request_json = {
    "images": [
        {
            "format": "jpg",
            "name": "demo",
            "data": base64.b64encode(file_data).decode(),
        }
    ],
    "requestId": str(uuid.uuid4()),
    "version": "V1",
    "timestamp": int(round(time.time() * 1000)),
}

payload = json.dumps(request_json).encode("UTF-8")
headers = {"X-OCR-SECRET": secret_key, "Content-Type": "application/json"}

response = requests.request("POST", api_url, headers=headers, data=payload)

# JSON 데이터 추출
data = response.json()

# 모든 inferText 값을 저장할 리스트
infer_texts = []

# images 아래의 모든 fields에서 inferText 값을 추출하여 리스트에 추가
for image in data["images"]:
    for field in image["fields"]:
        infer_texts.append(field["inferText"])

# 리스트에 있는 모든 inferText 값을 하나의 문자열로 합치기
result_text = " ".join(infer_texts)

# 결과 출력
print(result_text)
