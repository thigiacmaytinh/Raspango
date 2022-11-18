import numpy as np
import cv2
import base64
import threading
from api.apps import printt

def Base64ToMat(base64Str):
    nparr = np.fromstring(base64.b64decode(base64Str), np.uint8)
    mat = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return mat

####################################################################################################

def MatToBase64(mat):
    retval, buffer = cv2.imencode('.jpg', mat)
    strBase64 = base64.b64encode(buffer)
    return strBase64.decode("utf8")

####################################################################################################

def WriteMatAsync(imgPath, mat):    
    if(np.shape(mat) == ()):
        raise Exception("mat empty in WriteMatAsync")
    t = threading.Thread(target=cv2.imwrite, args=(imgPath, mat.copy()))
    t.start()

####################################################################################################

def IsMatEmpty(mat):
    [im_height, im_width] = mat.shape[:2]
    if(im_height == 0 or im_width == 0):
        printt("width or height = 0")
        return True

    if(mat.any() == None):
        printt("mat face is none")
        return True

    if(np.shape(mat) == ()):
        printt("mat shape is empty")
        return True

    if np.sum(mat) == 0:
        printt("sum mat = 0")
        return True
        
    return False

####################################################################################################

def ConvertRectToSquare(mat, rects):
    [im_height, im_width] = mat.shape[:2]

    for index, r in enumerate(rects):
        (left, top, w, h) = r    
        bottom = top + h
        right = left + w    
        
        if(w > h):            
            marginTop = int((w - h)/2)         
            top = max(top - marginTop, 0)
            bottom = min(im_height, bottom + marginTop)
            h = bottom - top
        elif(h > w):
            marginLeft = int((h - w)/2)
            left = max(left - marginLeft, 0)
            right = min(im_width, right + marginLeft)
            w = right - left
        
        rects[index] = (left, top, w, h)

    return rects

####################################################################################################

def CropFaceSquare(mat, rects):
    croppedMats = []
    [im_height, im_width] = mat.shape[:2]

    squares = ConvertRectToSquare(mat, rects)

    for r in squares:
        (left, top, w, h) = r    
        bottom = top + h
        right = left + w 

        croppedMat = mat[top:bottom, left:right]
        croppedMats.append(croppedMat)

    return croppedMats