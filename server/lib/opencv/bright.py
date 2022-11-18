import cv2
import numpy as np
from numpy.linalg import norm

from api.apps import printt

THRESH1 = 170
THRESH2 = 100

def CheckBright(frame):
    if len(frame.shape) == 3:
        # Colored RGB or BGR (*Do Not* use HSV images with this function)
        # create brightness with euclidean norm
        mean = np.average(norm(frame, axis=2)) / np.sqrt(3)
    else:
        # Grayscale
        mean = np.average(frame)


    printt(mean)
    result ='OK'
    if  mean > THRESH1:
        result = 'Light'
    elif mean < THRESH2:
        result = 'Dark'

    return result, mean