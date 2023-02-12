from rest_framework.decorators import api_view
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
from django.conf import settings
import cv2
import threading

####################################################################################################

@api_view(["POST"])           
def StopWebcam(request):
    try:
        

        

        settings.PLAY_WEBCAM = False

        return SuccessResponse("Stop thành công")
    except Exception as e:
        return ErrorResponse("Có lỗi: " + str(e))

