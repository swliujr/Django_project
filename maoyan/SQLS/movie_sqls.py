import json
from .get_mysql_data import Get_Mysql_data


class MovieTu(Get_Mysql_data):
    def __init__(self):
        super(MovieTu, self).__init__()
        # 各年份电影数量饼图
        self.movie_year_pie_sql = '''
select ifnull(movie_year,'无明确年份'),count(1) as count
from movie
where movie_year is not null
group by movie_year
'''
        # 各电影题材数量 柱状图
        self.movie_type_bar_sql = 'select movie_type from movie where movie_type is not null'
        self.movie_piaofang_top_sql = 'select movie_name,piaofang*1 from movie order by piaofang*1  desc limit 10'
        self.movie_tosee_top_sql= 'select movie_name,want_see_nums*1 from movie order by want_see_nums*1  desc limit 10'

    def movie_pie(self):
        datas = self.fetch_data(self.movie_year_pie_sql)
        series_data = [dict(name=x[0], value=str(x[1])) for x in datas]
        legend_data = [x[0] for x in datas]
        json_series_data = json.dumps(series_data)
        json_legend_data = json.dumps(legend_data)
        return json_legend_data, json_series_data

    def movie_type_bar(self):
        movie_type_list = []
        datas = self.fetch_data(self.movie_type_bar_sql)
        for data in datas:
            types = data[0].split(',')
            for type in types:
                movie_type_list.append(type)
        set_types = set(movie_type_list)
        # 统计 列表先set去重 使用列表count方法 结合字典统计
        item = {}
        for type in set_types:
            item[type] = movie_type_list.count(type)
        xAxis_data = [x[0] for x in sorted(item.items(), key=lambda x: x[1], reverse=True)]
        series_data = [x[1] for x in sorted(item.items(), key=lambda x: x[1], reverse=True)]
        bar_json_series_data = json.dumps(series_data)
        bar_json_xAxis_data = json.dumps(xAxis_data)
        return bar_json_xAxis_data, bar_json_series_data

    def movie_piaofang_top(self):
        # y轴电影列表 系列值为票房数据
        datas = self.fetch_data(self.movie_piaofang_top_sql)
        item={x[0]:x[1] for x in datas}
        sort_list=sorted(item.items(),key=lambda x:x[1],reverse=False)
        yAxis_data = [x[0] for x in sort_list]
        series_data = [x[1] for x in sort_list]
        piaofang_json_yAxis_data = json.dumps(yAxis_data)
        piaofang_json_series_data = json.dumps(series_data)
        return piaofang_json_yAxis_data,piaofang_json_series_data


    def movie_tosee_top(self):
        # y轴电影列表 系列值为票房数据
        datas = self.fetch_data(self.movie_tosee_top_sql)
        item = {x[0]: x[1] for x in datas}
        sort_list = sorted(item.items(), key=lambda x: x[1], reverse=False)
        yAxis_data = [x[0] for x in sort_list]
        series_data = [x[1] for x in sort_list]
        tosee_json_yAxis_data = json.dumps(yAxis_data)
        tosee_json_series_data = json.dumps(series_data)
        return tosee_json_yAxis_data, tosee_json_series_data
