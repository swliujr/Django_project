# #coding:utf8
import os
from os import path
import pymysql
import json




class Get_Mysql_data(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='admin2016', db='maoyan', charset='utf8',
                                    port=3306)

    def exesql(self, sql):
        conn = self.conn
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

    def fetch_data(self, sql):
        conn = self.conn
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            data = cursor.fetchall()
        return data

    def insert_data(self, sql, *args):
        conn = self.conn
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql, *args)
            conn.commit()
        alert_text = '数据保存成功!'
        return alert_text

    def export_excel(self, *args, **kwargs):
        workspace_path = kwargs['workspace_path']
        file_name = kwargs['file_name']
        BASE_DIR = kwargs['base_dir']
        par_path = path.join(BASE_DIR, workspace_path)
        os.chdir(par_path)

