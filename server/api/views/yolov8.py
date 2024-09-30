from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import hashlib
import os
import datetime, time
from dateutil.parser import parse
from api.models import Level, User
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from api.apps import *
from django.db.models import Q
from api.views.loginsession import *
from lib.TGMT.TGMTutil import *
from django.conf import settings
from module.YOLOv8.DetectObject import detectobj
####################################################################################################

@api_view(["POST"])           
def DetectObject(request):
    try:
        dirName = "yolov8"
        _randFilename = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S") + "_" + GenerateRandomString() + ".jpg"
        uploaded_file_abs = os.path.join(settings.MEDIA_ROOT, dirName, _randFilename)
        hasNewImage = SaveImageFromRequest(request, dirName, _randFilename)

        if(not hasNewImage):
            return ErrorResponse("Ảnh không hợp lệ")

        startTime = time.time()

        img = cv2.imread(uploaded_file_abs)
        img = detectobj.Detect(img)

        elapsed = time.time() - startTime
        elapsed = round(elapsed, 2)

        retval, buffer = cv2.imencode('.jpg', img)
        strBase64 = base64.b64encode(buffer)
        
        return Response(
            {'image_base64': strBase64,
            'elapsed' : elapsed},
            status=SUCCESS_CODE,
            content_type="application/json")

    except Exception as e:
        return ErrorResponse("Có lỗi: " + str(e))
    

