from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^show_movie/$',views.show_movie, name='show_movie'),
    url(r'^tu/$', views.tu, name='tu')

]
