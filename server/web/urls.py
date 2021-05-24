from django.conf.urls import url

from . import views
from django.contrib.sitemaps.views import sitemap
from server.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^404/$', views.notfound, name='notfound'),
    url(r'^relayshield/$', views.relayshield),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^user/$', views.user, name='create_user'), 
    url(r'^changepassword/$', views.changepassword, name='changepassword_manage'),
    url(r'^register/$', views.register, name='register'),
    url(r'^webcam/$', views.webcam, name='webcam'),
    url(r'^video_feed/$', views.video_feed, name='video_feed'),
    url(r'^stream/$', views.stream, name='stream'),
    url(r'^upload/$', views.upload),
]
handler404 = views.notfound
