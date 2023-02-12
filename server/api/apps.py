from django.apps import AppConfig
from rest_framework.response import Response
import json
from django.conf import settings
from django.core import serializers
import datetime

ERROR_CODE = 399
SUCCESS_CODE = 200

####################################################################################################

def QuerySetToJson(query_set):
    result = serializers.serialize('json', [query_set])
    result = json.loads(result)
    return result[0]

####################################################################################################

def ArrayQuerySetToJson(array_query_set):
    result = serializers.serialize('json', array_query_set)
    result = json.loads(result)
    return result

####################################################################################################

class ApiConfig(AppConfig):
    name = 'api'

####################################################################################################

class ErrorResponse(Response):
    def __init__(self, message):
        Response.__init__(self,
            {'Error': message},
            status=ERROR_CODE, content_type="application/json")

####################################################################################################

class SuccessResponse(Response):
    def __init__(self, message):
        Response.__init__(self,
            {'Success': message},
            status=SUCCESS_CODE, content_type="application/json")

####################################################################################################

class JsonResponse(Response):
    def __init__(self, jsonString):
        Response.__init__(self,
            json.loads(jsonString),
            status=SUCCESS_CODE, content_type="application/json")

####################################################################################################

class ObjResponse(Response):
    def __init__(self, jsonObj):
        Response.__init__(self,
            jsonObj,
            status=SUCCESS_CODE, content_type="application/json")

####################################################################################################

def GetVNTime():
    return utcnow().replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)

####################################################################################################

def utcnow():
    return datetime.datetime.utcnow()

####################################################################################################

def RequireParamExist(request, param, paramName):
    value = GetParam(request, param)
    if(value == None or value == ""):
        raise Exception("Thiếu tham số " + paramName)
    return True

####################################################################################################

def IsParamExist(request, param):
    value = GetParam(request, param)
    if(value == None or value == ""):
        return False
    return True

####################################################################################################

def RequireLevel(loginSession, levels):
    if(loginSession["level"] not in levels):
        raise Exception("Bạn phải đăng nhập để có thể thao tác")
    return True

####################################################################################################

def GetParam(request, param, defaultValue=""):
    params = request.POST
    if(len(params) == 0):
        params = request.data    
    if(param not in params):
        return defaultValue
    if(params[param] == None):
        return defaultValue
    return params[param]

####################################################################################################

def printt(msg):
    if(settings.DEBUG):
        print(">>>>" + str(msg))