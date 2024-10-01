from ultralytics import YOLO
import cv2
import os
from ultralytics.utils.plotting import Annotator
import numpy as np
import matplotlib.pyplot as plt

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
print(CURRENT_DIR)

class DetectObject:
    def __init__(self):
        modelFile = os.path.join(CURRENT_DIR, "yolov8n.pt")
        if os.path.exists(modelFile):
            self.model = YOLO(modelFile)
        else:
            raise Exception("Missing model")

    def get_class_colors(self, num_classes):
        """Generate unique colors for each class using a colormap."""
        colors = plt.cm.get_cmap('tab20', num_classes)  #
        return [tuple([int(255 * c) for c in colors(i)[:3]]) for i in range(num_classes)]  # Convert to RGB format

    def Detect(self, img):
        results = self.model.predict(img)
        
        num_classes = len(self.model.names)
        class_colors = self.get_class_colors(num_classes)  
        
        for r in results:
            annotator = Annotator(img)
            boxes = r.boxes
            for box in boxes:
                b = box.xyxy[0]
                c = int(box.cls) 
                class_name = self.model.names[c]
                color = class_colors[c]  
                annotator.box_label(b, class_name, color=color)
        img = annotator.result()
        return img

detectobj = DetectObject()

if __name__ == '__main__':
    img = cv2.imread('people.jpg')
    img = detectobj.Detect(img)
    cv2.imshow('YOLO V8 Detection', img)
    cv2.waitKey(0)
