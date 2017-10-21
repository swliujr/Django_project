from django.conf.urls import url
from . import views


urlpatterns = [


    url(r'^tu/$', views.tskr_tu, name='tskr_tu')

]