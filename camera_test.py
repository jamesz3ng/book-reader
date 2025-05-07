import subprocess


def capture_image(output_path, width=None, height=None):
    try:
        command = ["libcamera-still", "-o", output_path]

        if width and height:
            command.extend(["--width", str(width), "--height", str(height)])

        # libcamera-still 명령어를 실행하여 사진을 캡처하고 파일로 저장
        subprocess.run(command, check=True)
        print(f"이미지가 저장되었습니다: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"이미지 캡처에 실패했습니다: {e}")


# 사진을 저장할 경로와 해상도
output_path = "captured_image.jpg"
width = 1920
height = 1080
capture_image(output_path, width, height)
