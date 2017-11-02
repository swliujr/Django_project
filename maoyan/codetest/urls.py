from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^run/$',views.run, name='run'),
    url(r'^input_code/$', views.input_code, name='input_code'),

]