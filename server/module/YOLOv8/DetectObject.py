from ultralytics import YOLO
import cv2
import os
from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
print(CURRENT_DIR)

class DetectObject:
    def __init__(self):
        modelFile = os.path.join(CURRENT_DIR, "yolov8n.pt")
        if(os.path.exists(modelFile)):
            self.model = YOLO(modelFile)
        else:
            raise Exception("Missing model")
        

    def Detect(self, img):
        results = self.model.predict(img)
        for r in results:  
            annotator = Annotator(img)
            boxes = r.boxes
            for box in boxes:     
                b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
                c = box.cls
                annotator.box_label(b, self.model.names[int(c)])
        img = annotator.result()  
        return img

detectobj = DetectObject()

if __name__ == '__main__':
    img = cv2.imread('people.jpg')
    img = detectobj.Detect(img)
    cv2.imshow('YOLO V8 Detection', img)     
    cv2.waitKey(0)
