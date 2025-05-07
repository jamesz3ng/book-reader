import cv2
import numpy as np
import picamera

camera = picamera.Picamera()
camera.resolution = (640, 480)

file_number = 0


def save_img():
    camera.capture(f"/home/pi/Documents/pages/{file_number}")


def find_points(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    red_points = []
    for contour in contours:
        if cv2.contourArea(contour) > 100:  # 최소 면적 필터링
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                red_points.append((cX, cY))

    return red_points


def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


image_path = "demo.jpg"
image = cv2.imread(image_path)

points = find_points(image)

if len(points) >= 2:
    point1, point2 = points[0], points[1]
    distance = calculate_distance(point1, point2)
    print(f"Point 1: {point1}")
    print(f"Point 2: {point2}")
    print(f"Distance: {distance} pixels")
else:
    print("두 개 이상의 빨간 점을 찾을 수 없습니다.")
