import os
from threading import Thread, Lock
import cv2
from django.conf import settings as raspango
import threading
import time, datetime

cascade = cv2.CascadeClassifier(os.path.join(raspango.BASE_DIR, "lib", "data", "lbpcascade_face_viscom.xml"))
if(cascade.empty()):
    print("cascade empty")

####################################################################################################

def DetectFaceByCascade(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    rects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20),
                                     flags=cv2.CASCADE_SCALE_IMAGE)

    if(len(rects) > 0):
        rects[:,2:] += rects[:,:2]

        for x1, y1, x2, y2 in rects:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return frame, rects

####################################################################################################

def streamwebcam():
    raspango.PLAY_WEBCAM = True
    cam = cv2.VideoCapture(0)

    while raspango.PLAY_WEBCAM:
        raspango.WEBCAM_CONNECTED, frame = cam.read()

        frame, rects = DetectFaceByCascade(frame)
        raspango.NUM_FACE = len(rects)

        (flag, encodedImage) = cv2.imencode(".jpg", frame)

        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
