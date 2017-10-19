# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    movie_url = models.CharField(max_length=255, blank=True, null=True,verbose_name='电影url')
    movie_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='电影名称')
    ename = models.CharField(max_length=255, blank=True, null=True,verbose_name='电影别名')
    movie_desc = models.TextField(blank=True, null=True,verbose_name='剧情描述')
    infos = models.CharField(max_length=255, blank=True, null=True,verbose_name='综合信息')
    celebritys = models.CharField(max_length=255, blank=True, null=True,verbose_name='导员')
    actors = models.TextField(blank=True, null=True,verbose_name='演员')
    req_url = models.CharField(max_length=255, blank=True, null=True,verbose_name='请求url')
    movie_type = models.CharField(max_length=255, blank=True, null=True,verbose_name='电影题材')
    movie_area = models.CharField(max_length=255, blank=True, null=True,verbose_name='放映区域')
    movie_minutes = models.CharField(max_length=255, blank=True, null=True,verbose_name='时长')
    piaofang = models.CharField(max_length=255, blank=True, null=True, verbose_name='票房')
    want_see_nums = models.CharField(max_length=255, blank=True, null=True, verbose_name='想看的人数')
    movie_year = models.CharField(max_length=255, blank=True, null=True,verbose_name='年份')
    movie_time = models.CharField(max_length=255, blank=True, null=True,verbose_name='上映时间')
    player_type = models.CharField(max_length=255, blank=True, null=True,verbose_name='上映类型')

    class Meta:
        db_table = 'movie'
        verbose_name = '猫眼电影数据库数据'
        verbose_name_plural = verbose_name
