from django.apps import AppConfig
from rest_framework.response import Response
import json
from django.conf import settings as djangoSettings
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

class JsonObjResponse(Response):
    def __init__(self, jsonObj):
        Response.__init__(self,
            jsonObj,
            status=SUCCESS_CODE, content_type="application/json")

####################################################################################################

def GetVNTime():
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)