import cv2
from rest_framework.decorators import api_view

from lib.opencv.bright import CheckBright
from api.apps import *
from lib.TGMT.TGMTmat import Base64ToMat

####################################################################################################

@api_view(["POST"])
def CheckBrightness(request):
    try:        
        _base64_image = request.POST.get("imageBase64")
        frame = Base64ToMat(_base64_image)   
        
        img_bright = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        result, mean = CheckBright(img_bright)


        return SuccessResponse(result + " {0:.3g}".format(mean))
    except Exception as e:
        printt(str(e))
        return ErrorResponse(str(e))
