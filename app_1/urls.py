from django.conf.urls import url
from . import views


app_name = "app_1"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^liuyan', views.liuyan, name='liuyan'),
    url(r'^result', views.dayin, name='dayin'),
    url(r'^dayingaijin', views.dayingaijin, name='dayingaijin'),
    url(r'^uploadfile', views.upload_file, name='uploadfile'),
    url(r'^upload', views.upload, name='upload'),
    url(r'^downloadfile', views.downloadfile, name='downloadfile'),
    url(r'^comments_upload', views.comments_upload, name='comments_upload'),
    url(r'^welcome', views.welcome, name='welcome'),
]