from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import hashlib
import datetime
from dateutil.parser import parse
from api.models import User, LoginSession
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from api.apps import *
import api.auth
from django.db.models import Q
from lib.TGMT.TGMTemail import SendEmailInternal
from api.views.loginsession import *
from django.core import serializers
from django.conf import settings as djangoSettings

####################################################################################################

@api_view(["POST"])
def login(request):
    _email = request.POST.get('email').lower()
    _password = request.POST.get('password').lower()

    hashed_password = HashPassword(_password)

    try:
        _user = User.objects.get(email=_email, isDeleted=False)
        if(not djangoSettings.DEBUG and _user.password != hashed_password):
            return ErrorResponse("Không đúng email/password")
    except User.DoesNotExist:
        return ErrorResponse("Không đúng email/password")

    try:
        login_session = LoginSession(email = _email,
                                    fullname = _user.fullname,
                                    level = _user.level,                                    
                                    loginTime = datetime.datetime.utcnow()
                                    )
        login_session.save()
        payload = {
            'email': _email,
            'fullname' : _user.fullname,
            'level' : _user.level,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=365),
            'loginSession_pk' : str(login_session.pk)
        }

        jwt_token = api.auth.encode(payload)
        _user.password = ""
        _userJson = serializers.serialize('json', [_user])

        result = json.loads(_userJson)[0]
        result["token"] = jwt_token['token']

        return JsonObjResponse(result)
    except Exception as e:
        return ErrorResponse('Có lỗi: ' + str(e))

####################################################################################################

@api_view(["POST"])
def logout(request):
    try:
        _user_id = request.POST.get('user_id')
        _user_id = _user_id.lower()
        _image = request.POST.get('image')
        _token = request.POST.get('token')
        loginSession = LoginSession.objects.get(token = _token)
   
        if(_image != ""):
            _save_folder = "logout"
            _file_name = _user_id + "_"
            _imagePath = SaveBase64ToImg(_save_folder, _file_name, _image)
        else:
            _imagePath = ""
        loginSession.imageLogoutPath = _imagePath
        loginSession.logoutTime = datetime.datetime.utcnow()
        loginSession.save()

        return SuccessResponse('Logout thành công')

    except Exception as e:
        return ErrorResponse("Có lỗi: " + str(e))

####################################################################################################

def HashPassword(password):
    hash_routine = 5
    hashed_password = password
    while hash_routine != 0 :
       hashed_password = hashlib.sha224(hashed_password.encode('utf-8')).hexdigest()
       hash_routine = hash_routine - 1
    return hashed_password

####################################################################################################

@api_view(["POST"])
def GetUser(request):
    try:
        _token = request.POST.get('token')

        loginSession = FindLoginSession(_token)
        if(datetime.datetime.utcnow() > loginSession.validTo or loginSession.email != "admin"):
            return Response(
            {'Error': "Token hết hạn, vui lòng đăng nhập lại"},
            status=ERROR_CODE,
            content_type="application/json"
            )

        _username = request.POST.get('username')
        user = User.objects.get(username=_username, isDeleted=False)

        user.password = ""

        return Response(
            json.loads(user.to_json()),
            status=SUCCESS_CODE,
            content_type="application/json"
            )
    except Exception as e:
            return Response(
            {'Error': "Tìm thất bại: " + str(e)},
            status=ERROR_CODE,
            content_type="application/json"
            )


####################################################################################################

@api_view(["POST"])
def ChangePassword(request):
    try:
        _token = request.POST.get("token")
        if(len(_token) == 24):
            loginSession = LoginSession.objects.get(pk=_token, isDeleted=False)
            if(loginSession.purpose != "ResetPassword"):
                return ErrorResponse("Link không hợp lệ")       
        else:            
            loginSession = FindLoginSession(_token)
        

        _email = loginSession["email"]
        _password = request.POST.get('password')
        hashed_password = HashPassword(_password)
        _newPassword = request.POST.get('newPassword')

        user = User.objects.get(email=_email, isDeleted=False)
        if(len(_token) != 24):
            if(user.password != hashed_password):
                return ErrorResponse("Password cũ không đúng")
        
        hashed_newpassword = HashPassword(_newPassword)
        user.password = hashed_newpassword
        user.save()

        
        return SuccessResponse("Đổi mật khẩu thành công")
    except Exception as e:
        return ErrorResponse("Có lỗi: " + str(e))

####################################################################################################

@api_view(["POST"])
def ResetPassword(request):
    try:
        _username = request.POST.get('username')
        _password = _username
        try:
            user = User.objects.get(username=_username, isDeleted=False)
        except User.DoesNotExist:
            return Response(
                {'Error': "Không tìm thấy user: "+ _username},
                status=ERROR_CODE,
                content_type="application/json"
            )
        if user:
            hashed_newpassword = HashPassword(_password)
            user.password = hashed_newpassword
            user.isPasswordChanged = False
            user.save()
            return Response(
                {'Success': "Đổi mật khẩu thành công"},
                status=SUCCESS_CODE,
                content_type="application/json"
            )
    except Exception as e:
        return Response(
            {'Error': "Thông tin không đúng, lỗi: " + str(e)},
            status=ERROR_CODE,
            content_type="application/json"
            )


####################################################################################################

@api_view(["POST"])
def Register(request):
    try:
        _email = request.POST.get('email').lower()
        _name = request.POST.get('name')
        _position = request.POST.get('position')
        _password = request.POST.get('password').lower()    
        _phone = request.POST.get('phone')
        
        user = None
        try:
            user =  User.objects.get(email=_email, isDeleted=False)
            already_existed = True
        except User.MultipleObjectsReturned:
            already_existed = True
        except User.DoesNotExist:
            already_existed = False
        
        hashed_password = HashPassword(_password)
        
        if(user == None):
            user = User(email = _email)
        else:
            if(user.status != "Invited"):
                return ErrorResponse("Email này đã được đăng ký")

        user.fullname = _name
        user.password = hashed_password
        user.phone = _phone        
    
       
        user.timeUpdate = datetime.datetime.utcnow()

        if(_references != None and _references != ""):
            user.references = _references

        user.save()

        #create login session
        login_session = LoginSession(email = _email,
                                    fullname = user.fullname,
                                    level = user.level,
                                    purpose = "ConfirmEmail",
                                    loginTime = datetime.datetime.utcnow(),
                                    validTo = datetime.datetime.utcnow() + datetime.timedelta(days=7)
                                    )
        login_session.save()
        return SuccessResponse("Đăng ký thành công, vui lòng kiểm tra email để xác nhận")
    except Exception as e:
            return ErrorResponse("Có lỗi: " + str(e))
