from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from rest_framework.views import APIView
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
from django.conf import settings as raspango
from lib.tensorflow.FaceMaskDetector import faceMask

####################################################################################################

@api_view(["POST"])           
def DetectFacemask(request):
    try:
        dirName = "facemask"
        _randFilename = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S") + "_" + GenerateRandomString() + ".jpg"
        uploaded_file_abs = os.path.join(raspango.MEDIA_ROOT, dirName, _randFilename)
        hasNewImage = SaveImageFromRequest(request, dirName, _randFilename)

        if(not hasNewImage):
            return ErrorResponse("Ảnh không hợp lệ")

        startTime = time.time()

        faceMask.drawText = False
        mat, arr = faceMask.DetectMaskFromImagePath(uploaded_file_abs)

        elapsed = time.time() - startTime
        elapsed = round(elapsed, 2)

        retval, buffer = cv2.imencode('.jpg', mat)
        strBase64 = base64.b64encode(buffer)
        
        return Response(
            {'image_base64': strBase64,
            'elapsed' : elapsed},
            status=SUCCESS_CODE,
            content_type="application/json")

    except Exception as e:
        return ErrorResponse("Có lỗi: " + str(e))

