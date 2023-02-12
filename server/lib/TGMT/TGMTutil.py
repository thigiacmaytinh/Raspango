from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import hashlib
import datetime
from dateutil.parser import parse
from api.apps import *
from django.conf import settings
import time
from django.core.files.storage import FileSystemStorage
from PIL import Image
from django.core.paginator import Paginator
from lib.TGMT.TGMTfile import *
from lib.TGMT.TGMTimage import *
from lib.TGMT.TGMTwebcam import cascade
from api.util import *
from api.views.loginsession import *
import shutil
import cv2
import django

####################################################################################################
       
def GetSystemInfo():
    result = {}
    try:        
        total, used, free = shutil.disk_usage("/")

        result = {
            "totalDiskSize" : (total // (2**30)),
            "usedDiskSize" : (used // (2**30)),
            "freeDiskSize" : (free // (2**30)),
            "opencv_version" : cv2.__version__,
            "django_version" : django.VERSION,
            "cascade_loaded" : not cascade.empty()
        }
    
        return result
    except Exception as e:
        result = {
            "error" : str(e)
        }

    return result

