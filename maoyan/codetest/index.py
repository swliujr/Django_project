import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='admin2016', db='maoyan', charset='utf8', port=3306)
with conn:
      cursor = conn.cursor()
      sql = 'select * from movie'
      cursor.execute(sql)
      data = cursor.fetchall()
      print(data)
      


