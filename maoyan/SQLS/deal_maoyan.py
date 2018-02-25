import pymysql

class MaoyanSpider(object):
    def __init__(self):
        self.movie_type_list = []
        self.MYSQL_CONFIG = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '密码',
            'db': 'maoyan',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**self.MYSQL_CONFIG)

    def fetch_data(self):
        conn = self.conn
        cursor = conn.cursor()
        sql = 'select movie_type from movie'
        cursor.execute(sql)
        datas = cursor.fetchall()
        for data in datas:
            types = data[0].split(',')
            for type in types:
                self.movie_type_list.append(type)
        return self.movie_type_list


if __name__ == '__main__':
    maoyan = MaoyanSpider()
    movie_type_list = maoyan.fetch_data()
    set_types = set(movie_type_list)
    print(movie_type_list)
    #统计 列表先set去重 使用列表count方法 结合字典统计
    item = {}
    for type in set_types:
        item[type] = movie_type_list.count(type)
    for k,v in item.items():
        print (k,v)
    sorted_type=sorted(item.items(),key=lambda x:x[1],reverse=True)[:10]
    print (sorted_type)
    #处理方法2  列表不去重 使用列表和字典及条件判断
    item2={}
    for type in movie_type_list:
        if type in  item2:
            item2[type]=item2[type]+1
        else:
            item2[type] = 1
    sorted_type = sorted(item2.items(), key=lambda x: x[1], reverse=True)[:10]
    print(sorted_type)


