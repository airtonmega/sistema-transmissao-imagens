import cv2
import requests

video_url = "https://drive.google.com/uc?id=1iHHV0KNm1bWAphi9q0hAUxJbYww0XPcr&export=download"
cap = cv2.VideoCapture(video_url)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    _, img_encoded = cv2.imencode('.jpg', frame)
    response = requests.post(
        "http://S1:8000/detect/S3",
        files={"file": img_encoded.tobytes()},
    )

    print(response.json())
    
cap.release()
