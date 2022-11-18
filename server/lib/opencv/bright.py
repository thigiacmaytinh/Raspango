import cv2
import numpy as np
from numpy.linalg import norm
import mediapipe as mp
from api.apps import printt

THRESH1 = 170
THRESH2 = 100


def dtectface(img):
    cv2.imwrite('abc.jpg',img)
    # Detect face
        # Set up config:
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)
    results = face_detection.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if results.detections is not None:
    # print(results.detections)
        bound_box = results.detections[0].location_data.relative_bounding_box
        # print(bound_box)
        # Lay cac thong so bounding box
        x = int(np.abs(bound_box.xmin) * img.shape[0])
        y = int(np.abs(bound_box.ymin) * img.shape[1])
        w = int(np.abs(bound_box.width) * img.shape[0])
        h = int(np.abs(bound_box.height) * img.shape[1])
        # Crop image
        img = img[y:y + h, x:x + w, :]
    else:
        img = img

    return img



def CheckBright(frame):
    img = dtectface(frame)
    cv2.imwrite('abc2.jpg',img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Calculate Histogram of V channel
    hist = cv2.calcHist([hsv], [2], None, [256], [0, 256])
    # plt.plot(hist,color='b')
    # plt.show()

    # Calculate percent of dark region and bright region
    sum = np.sum(hist)
    dark = 0
    bright = 0
    for i in range(0, 65):
        dark += hist[i, 0]
    for i in range(230, 255):
        bright += hist[i, 0]
    dark_per = dark / sum
    bright_per = bright / sum

    # Compare to THRESHOLD
    if dark_per > 0.40:
        result = 'Dark'
        mean = dark_per
    elif bright_per > 0.40:
        result = 'Bright'
        mean = bright_per
    else:
        result = 'Ok'
        mean = dark_per
    print(dark_per)
    print(bright_per)
    return result, mean