from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^add_report/$', views.add_report, name='add_report'),
    url(r'^delete_report/$', views.delete_report, name='delete_report'),
    url(r'^update_report/$', views.update_report, name='update_report'),
    url(r'^export_all_excel/$', views.export_all_excel, name='export_all_excel'),
]
