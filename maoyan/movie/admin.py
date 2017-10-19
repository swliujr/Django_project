#coding:utf8
from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_name', 'movie_type', 'movie_time', 'movie_minutes')
    list_filter = ['movie_name']
    search_fields = ['movie_name']


admin.AdminSite.site_header = '猫眼电影后台'
admin.AdminSite.site_title = '猫眼电影'
admin.site.register(Movie, MovieBlogAdmin)