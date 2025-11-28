import cv2
from ultralytics import YOLO
import math
import numpy as np
import cvzone

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

ClassName = ["john"]
model = YOLO("Pro-1(car counter)/best (3).pt")

while True:
    Success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            #cv2.rectangle(img, (x1, y1), (x2, y2), (255,255,0), 2)
            conf = math.ceil((box.conf[0]*100))/100
            cls = int(box.cls[0])
            currentClass = ClassName[cls]
            if currentClass == "john":
                cvzone.cornerRect(img, (x1, y1, w, h), l=15, rt=0)
                cvzone.putTextRect(img, f' {int(currentClass)}', (max(0, x1), max(40, y1)),
                                   scale=1, thickness=1, offset=5)

        cv2.imshow("Ace", img)
        cv2.waitKey(0)

