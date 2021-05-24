from django.conf import settings
import jwt,json

def decode(token):
    try:        
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        return payload
    except jwt.ExpiredSignatureError as e:
        print(str(e))
        return None
    except Exception as e:
        print(str(e))
        return None

def encode(payload):
    jwt_token = {'token': jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')}
    return jwt_token