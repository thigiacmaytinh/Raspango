from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import hashlib
import datetime, time
from dateutil.parser import parse
from api.models import Level, User
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from api.apps import *
from django.db.models import Q
from api.views.loginsession import *
from lib.TGMT.TGMTemail import SendEmailInternal
from lib.TGMT.TGMTsound import PlaySound
from lib.TGMT.TGMTwebcam import *
from lib.TGMT.TGMTimage import *
from django.conf import settings as djangoSettings
import cv2
import threading

####################################################################################################

@api_view(["POST"])           
def DetectFace(request):
    try:
        folder = "uploaded_image"
        _randFilename = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S") + "_" + GenerateRandomString() + ".jpg"
        uploaded_file_abs = os.path.join(djangoSettings.MEDIA_ROOT, folder, _randFilename)

        SaveImageFromRequest(request, folder, _randFilename)

        startTime = time.time()

        mat = cv2.imread(uploaded_file_abs)
        mat, rects = DetectFaceByCascade(mat)

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

