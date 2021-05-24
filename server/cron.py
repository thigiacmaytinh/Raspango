from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from api.models import Asset, AssetType, AssetChecklog, AssetStatus
import api.auth
import datetime
import json
from api.apps import *
# from api.views.patrol import GenerateTaskPatrol
# from api.views.asset import GenerateTaskCheckAsset
# from api.views.schedule import GenerateScheduleTask

####################################################################################################

def ScheduleJob():
    f = open("crontime.txt", "w")
    f.write(str(datetime.datetime.utcnow()))
    f.close()
    # GenerateTaskPatrol()
    # GenerateTaskCheckAsset()
    # GenerateScheduleTask()
