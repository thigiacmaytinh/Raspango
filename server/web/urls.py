from django.conf.urls import url

from . import views
from django.contrib.sitemaps.views import sitemap
from raspango.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^404/$', views.notfound, name='notfound'),
    url(r'^relayshield/$', views.relayshield),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^user/$', views.user), 
    url(r'^changepassword/$', views.changepassword),
    url(r'^register/$', views.register),
    url(r'^camera/$', views.camera),
    url(r'^webcam/$', views.webcam),
    url(r'^facemask/$', views.facemask),
    url(r'^video_feed/$', views.video_feed),
    url(r'^stream/$', views.stream),
    url(r'^upload/$', views.upload),
]
handler404 = views.notfound
