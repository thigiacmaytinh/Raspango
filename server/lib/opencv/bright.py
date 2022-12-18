import cv2
import numpy as np
from numpy.linalg import norm
import mediapipe as mp
from api.apps import printt

THRESH1 = 170
THRESH2 = 100

def CheckBright(frame):
    #img = dtectface(frame)
    #cv2.imwrite('abc2.jpg',img)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
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
    return result, mean