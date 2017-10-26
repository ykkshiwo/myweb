from django.conf.urls import url
from . import views


app_name = "app_1"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^liuyan/$', views.liuyan, name='liuyan'),
    url(r'^dd', views.dayin, name='dayin'),
]