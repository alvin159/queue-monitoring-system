from ultralytics import YOLO
import cv2
import cvzone
import math
import pyautogui
import requests
url = "http://localhost:5000/api/queues"
headers = {
    "Content-Type": "application/json"
}
id = "Helsinki"
company_id = "first_company"
store_id = "Kamppi"
# loading the YOLO model
model = YOLO('../YOLO_weights/yolov8n.pt')

# defining class names to detect
classNames = ["person"]

# defining the video capture source
cap = cv2.VideoCapture('Videos/video_1.mp4')

# defining displaying stuff
screen_width, screen_height = pyautogui.size()
display_width = math.ceil(640*1.5)
display_height = math.ceil(360*1.5)
x = (screen_width - display_width) // 2
y = (screen_height - display_height) // 2

# image loop
while cap.isOpened():

    # Capturing the image
    success, img = cap.read()

    # Resizing the image
    img = cv2.resize(img, (display_width, display_height))

    # Running the YOLO detection
    results = model(img)

    # counter for people
    people_count = 0
    confidence_count = float(0)

    for r in results:
        boxes = r.boxes
        for box in boxes:


            # Checking if the detected object is a person
            cls = int(box.cls[0])
            if cls != 0:
                continue

            # Increment the people counter
            people_count += 1

            # Calculating the rectangle
            x1, y1, x2, y2 = box.xyxy[0]
            w, h = x2 - x1, y2 - y1
            bbox = int(x1), int(y1), int(w), int(h)
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print(int(x1), int(y1), int(x2), int(y2))

            # Drawing the rectangle
            cvzone.cornerRect(img, bbox)
            conf = math.ceil(box.conf[0]*100)/100
            print(conf)

            # Drawing the confidence of the class detected
            cvzone.putTextRect(
                img,
                f'{classNames[cls]} {conf:.2f}',
                (max(0, x1), max(35, y1)),
                scale=1,  # Smaller text
                thickness=1,  # Thinner text stroke
                colorR=(0, 0, 0),  # Background color (optional)
                offset=5  # Padding inside the box (make this smaller too)
            )
            confidence_count += conf

    cvzone.putTextRect(
        img,
        f'People Count: {people_count}',
        (20, 30),
        thickness=2,
        colorR=(0, 0, 0),
        offset=10
    )
    if people_count > 0:
        total_confidence = round(confidence_count / people_count, 2)
    else:
        total_confidence = 0.0
    data = {
        "id": id,
        "company_id": company_id,
        "store_id": store_id,
        "queue_length": people_count,
        "confidence": total_confidence
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        print("POST response:", response.status_code, response.text)
    except Exception as e:
        print("Error sending data:", e)

    cv2.imshow("Image", img)
    cv2.moveWindow("Image", x, y)
    cv2.waitKey(1000)

