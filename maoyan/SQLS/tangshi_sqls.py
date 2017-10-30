import os
from os import path
import time
import datetime
import xlsxwriter
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread
from maoyan.settings import BASE_DIR
from .get_mysql_data import Get_Mysql_data


class TangShi(Get_Mysql_data):
    def __init__(self):
        super(TangShi, self).__init__()
        self.tangshi_word_clound_sql = '''
select b.poemer,a.zuopin_content
from (
    select poemer_url,zuopin_content
    from local_db.poem_zuopin
    where poemer='{}' and zuopin_words<>0
    group by poemer_url,zuopin_content
    order by poemer_url
) as a 
left join local_db.poemers as b on a.poemer_url=b.poemer_url
'''
        self.all_poemers_sql = '''
select @i:=@i+1 as id,a.chaodai,a.poemer,a.zuopins_total*1,a.poemer_url
from (
	select id as id1,chaodai,poemer,zuopins_total,poemer_url 
	from local_db.poemers 
	order by zuopins_total*1 desc
) as a,(select @i:=0) as it
'''
        self.poemer_sql = '''
select b.*
from (
        select @i:=@i+1 as id,a.chaodai,a.poemer,a.zuopins_total*1,a.poemer_url
        from (
        	select id as id1,chaodai,poemer,zuopins_total,poemer_url 
        	from local_db.poemers 
        	order by zuopins_total*1 desc
        ) as a,(select @i:=0) as it
) as b
where poemer='{}'
        '''

    # 制作 词云图片 存放到    static/wordImages目录
    def make_poemer_word_clound(self, poemer):
        wordcloud_png_path = path.join(BASE_DIR, 'static/wordImages/{}'.format(poemer))
        par_path = path.dirname(__file__)
        datas = [x[1] for x in self.fetch_data(self.tangshi_word_clound_sql.format(poemer))]
        word_list = [" ".join(jieba.cut(sentence)) for sentence in datas]
        new_text = ' '.join(word_list)
        imagename = path.join(par_path, "bg.png")  # 背景图片路径
        coloring = imread(imagename)  # 读取背景图片
        fontname = path.join(par_path, "msyh.ttf")  # 使用的是微软雅黑字体
        wordcloud = WordCloud(mask=coloring, font_path=fontname, max_font_size=40).generate(new_text)
        plt.imshow(wordcloud)
        plt.axis("off")
        wordcloud.to_file('{}.png'.format(wordcloud_png_path))

    def per_poemer_data(self, poemer):
        poemer_data = []
        datas = self.fetch_data(self.poemer_sql.format(poemer))
        fields = ['id', 'chaodai', 'poemer', 'zuopins_total', 'poemer_url']
        for data in datas:
            item = {}
            for i in range(len(data)):
                if i == 0 or i == 3:
                    item[fields[i]] = int(data[i])
                else:
                    item[fields[i]] = data[i]
            poemer_data.append(item)
        return poemer_data

    def all_poemers_data(self):
        all_poemers_datas = []
        datas = self.fetch_data(self.all_poemers_sql)
        fields = ['id', 'chaodai', 'poemer', 'zuopins_total', 'poemer_url']
        for data in datas:
            item = {}
            for i in range(len(data)):
                if i == 0 or i == 3:
                    item[fields[i]] = int(data[i])
                else:
                    item[fields[i]] = data[i]
            all_poemers_datas.append(item)
        return all_poemers_datas

    def make_all_word_cloud(self):
        all_poemers = [{'id': int(x[0]), 'poemer': x[2], 'poemer_url': x[4]} for x in
                       self.fetch_data(self.all_poemers_sql)]
        for item in all_poemers:
            if self.check_word_cloud(item['poemer']):
                continue
            else:
                self.make_poemer_word_clound(item['poemer'])
        return all_poemers

    def check_word_cloud(self, poemer):
        par_path = path.join(BASE_DIR, 'static/wordImages')
        os.chdir(par_path)
        for root, dirs, files in os.walk(".", topdown=True):
            if poemer in [file.replace('.png', '') for file in files]:
                return True
            else:
                return False

    def export_excel(self,poemer):
        par_path = path.join(BASE_DIR, 'static/xlsxfiles')
        os.chdir(par_path)
        if poemer:
            file = poemer + '.xlsx'
            # 删除昨日执行文件
            if os.path.isfile(file):
                os.remove(file)
            data = self.per_poemer_data(poemer)
        else:
            file ='all_poemers.xlsx'
            if os.path.isfile(file):
                os.remove(file)
            data = self.all_poemers_data()
        if data:
            fields = ['id', 'chaodai', 'poemer', 'zuopins_total', 'poemer_url']
            workbook = xlsxwriter.Workbook(file)
            worksheet = workbook.add_worksheet('data')
            # 表头格式
            format1 = workbook.add_format(
                {'bold': True, 'font_color': 'black', 'font_size': 13, 'align': 'left', 'font_name': u'宋体'})
            # 除日期A列外数值区域
            format2 = workbook.add_format({'font_color': 'black', 'font_size': 9, 'align': 'left', 'font_name': u'宋体'})
            # A列列宽设置能更好的显示
            worksheet.set_column("A:A", 9)
            # 插入第一行表头标题
            for i in range(0, len(fields)):
                field = fields[i]
                worksheet.write(0, i, field, format1)
            for i in range(len(data)):
                item = data[i]
                for j in range(len(fields)):
                    field = fields[j]
                    worksheet.write(i+1, j, item[field], format2)
            workbook.close()
            alert_text = '导出%s条数据到excel成功' % len(data)
        else:
            alert_text = '无数据 导出失败'
        return alert_text

