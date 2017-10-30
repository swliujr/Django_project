# #coding:utf8
import pymysql
import json

class Get_Mysql_data(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='admin2016', db='maoyan',charset='utf8', port=3306)
    def exesql(self,sql):
        conn = self.conn
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

    def fetch_data(self,sql):
        conn = self.conn
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            data=cursor.fetchall()
        return data



