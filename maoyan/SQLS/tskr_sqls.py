import json
from .get_mysql_data import Get_Mysql_data


class TsKr(Get_Mysql_data):
    def __init__(self):
        super(TsKr, self).__init__()
        # 各年份电影数量饼图
        self.published_at_pie_sql = '''
select substr(published_at,1,4) as day,count(1) as count
from local_db.36kr
where published_at is not null and left(published_at,1)<>0
group by substr(published_at,1,4)
'''
        # 各电影题材数量 柱状图

        self.total_words_top_sql = 'select user_name,sum(total_words) from local_db.36kr group by user_name order by sum(total_words)   desc limit 10'
        self.favorite_top_sql= 'select user_name,sum(favorite) from  local_db.36kr group by user_name order by sum(favorite)  desc limit 10'
        self.title_pv_top_sql = 'select title,pv from  local_db.36kr  order by pv  desc limit 10'
    def kr_pie(self):
        datas = self.fetch_data(self.published_at_pie_sql)
        series_data = [dict(name=x[0], value=str(x[1])) for x in datas]
        legend_data = [x[0] for x in datas]
        json_series_data = json.dumps(series_data)
        json_legend_data = json.dumps(legend_data)
        return json_legend_data, json_series_data



    def total_words_top(self):
        # y轴电影列表 系列值为票房数据
        datas = self.fetch_data(self.total_words_top_sql)
        item={x[0]:x[1] for x in datas}
        sort_list=sorted(item.items(),key=lambda x:x[1],reverse=False)
        yAxis_data = [x[0] for x in sort_list]
        series_data = [x[1] for x in sort_list]
        total_words_json_yAxis_data = json.dumps(yAxis_data)
        total_words_json_series_data = json.dumps(series_data)
        return total_words_json_yAxis_data,total_words_json_series_data


    def favorite_top(self):
        # y轴电影列表 系列值为票房数据
        datas = self.fetch_data(self.favorite_top_sql)
        item = {x[0]: x[1] for x in datas}
        sort_list = sorted(item.items(), key=lambda x: x[1], reverse=False)
        yAxis_data = [x[0] for x in sort_list]
        series_data = [x[1] for x in sort_list]
        favorite_json_yAxis_data = json.dumps(yAxis_data)
        favorite_json_series_data = json.dumps(series_data)
        return favorite_json_yAxis_data, favorite_json_series_data

    def title_pv_top(self):
        # y轴电影列表 系列值为票房数据
        datas = self.fetch_data(self.title_pv_top_sql)
        item = {x[0]: x[1] for x in datas}
        sort_list = sorted(item.items(), key=lambda x: x[1], reverse=False)
        yAxis_data = [x[0] for x in sort_list]
        series_data = [x[1] for x in sort_list]
        title_pv_json_yAxis_data = json.dumps(yAxis_data)
        title_pv_json_series_data = json.dumps(series_data)
        return title_pv_json_yAxis_data, title_pv_json_series_data

