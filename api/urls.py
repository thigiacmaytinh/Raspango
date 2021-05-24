from django.conf.urls import url

from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^user/login$', views.login, name='login'),
    url(r'^user/logout$', views.logout, name='logout'),    
    url(r'^user/changepassword$', views.ChangePassword, name='ChangePassword'),
    url(r'^user/register$', views.Register, name='Register'),
    url(r'^loginsession/get$', views.GetLoginSession, name='GetLoginSession'),
    url(r'^loginsession/verifyToken$', views.verifyToken, name='verifyToken'),
    url(r'^gpio/set$', views.SetValue),
    url(r'^webcam/stop$', views.StopWebcam),
    url(r'^opencv/detectface$', views.DetectFace),
]