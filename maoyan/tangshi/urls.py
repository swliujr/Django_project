from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^poemers_search/$', views.poemers_search, name='poemers_search'),
    url(r'^poemers/$', views.poemers, name='poemers'),
    url(r'^all_word_cloud/$', views.all_word_cloud, name='all_word_cloud'),


]
