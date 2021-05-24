from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import hashlib
import datetime
from dateutil.parser import parse
from api.models import Level, User
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from api.apps import *
from django.db.models import Q
from api.views.loginsession import *
from lib.TGMT.TGMTemail import SendEmailInternal
from lib.TGMT.TGMTgpio import *

####################################################################################################

# create level
@api_view(["POST"])           
def SetValue(request):
    try:
        _token = request.POST.get("token")
        loginSession = FindLoginSession(_token)

        _gpio_pin = int(request.POST.get('gpio_pin'))
        _delay = int(request.POST.get('delay')) / 1000
        _triggerValue = int(request.POST.get('triggerValue'))
        
        newThread = TGMTgpio(_gpio_pin, _delay, _triggerValue)
        newThread.start()
        
        return SuccessResponse("Set giá trị thành công")
    except Exception as e:
        return ErrorResponse("Có lỗi: " + str(e))

####################################################################################################
