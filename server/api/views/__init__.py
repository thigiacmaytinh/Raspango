# we need to include new view here
from .user import login, logout, GetUser, ChangePassword, ResetPassword, Register
from .loginsession import GetLoginSession, verifyToken
from .gpio import SetValue
from .webcam import StopWebcam
from .opencv import DetectFace