import cv2

# 카메라 장치 열기 (0은 기본 카메라 장치 ID를 의미)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

# 카메라로부터 한 프레임 읽기
ret, frame = cap.read()
if ret:
    # 이미지를 'captured_image.jpg' 파일로 저장
    cv2.imwrite("captured_image.jpg", frame)
    print("이미지가 저장되었습니다.")
else:
    print("프레임을 읽을 수 없습니다.")

# 리소스 해제
cap.release()
