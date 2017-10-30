from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^poemers_search/$', views.poemers_search, name='poemers_search'),
    url(r'^poemers/$', views.poemers, name='poemers'),
    url(r'^all_word_cloud/$', views.poem_ajax, name='all_word_cloud'),
    url(r'^export_all_excel/$', views.export_all_excel, name='export_all_excel'),
    url(r'^export_per_excel/$', views.export_per_excel, name='export_per_excel'),
]
