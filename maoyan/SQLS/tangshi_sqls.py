
import os
from os import path
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread
from maoyan.settings import BASE_DIR
from .get_mysql_data import Get_Mysql_data

class TangShi(Get_Mysql_data):
    def __init__(self):
        super(TangShi,self).__init__()
        self.tangshi_word_clound_sql='''
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
        self.all_poemers_sql='''
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
    #制作 词云图片 存放到    static/wordImages目录
    def make_poemer_word_clound(self,poemer):
        wordcloud_png_path = path.join(BASE_DIR, 'static/wordImages/{}'.format(poemer))
        par_path = path.dirname(__file__)
        datas = [x[1] for x in self.fetch_data(self.tangshi_word_clound_sql.format(poemer))]
        word_list = [" ".join(jieba.cut(sentence)) for sentence in datas]
        new_text = ' '.join(word_list)
        imagename = path.join(par_path, "bg.png")  # 背景图片路径
        coloring = imread(imagename)  # 读取背景图片
        fontname = path.join(par_path, "msyh.ttf")  # 使用的是微软雅黑字体
        wordcloud = WordCloud(mask=coloring, font_path=fontname,max_font_size=40).generate(new_text)
        plt.imshow(wordcloud)
        plt.axis("off")
        wordcloud.to_file('{}.png'.format(wordcloud_png_path))

    def per_poemer_data(self,poemer):
        poemer_data = []
        datas = self.fetch_data(self.poemer_sql.format(poemer))
        fields = ['id', 'chaodai', 'poemer', 'zuopins_total', 'poemer_url']
        for data in datas:
            item = {}
            for i in range(len(data)):
                if i ==0 or i==3:
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
                if i ==0 or i==3:
                    item[fields[i]] = int(data[i])
                else:
                    item[fields[i]] = data[i]
            all_poemers_datas.append(item)
        return all_poemers_datas

    def make_all_word_cloud(self):
        all_poemers = [{'id':int(x[0]),'poemer':x[2]} for x in self.fetch_data(self.all_poemers_sql)]
        for item in all_poemers:
            if self.check_word_cloud(item['poemer']):
                continue
            else:
                self.make_poemer_word_clound(item['poemer'])
        return all_poemers

    def check_word_cloud(self,poemer):
        par_path = path.join(BASE_DIR, 'static/wordImages')
        os.chdir(par_path)
        for root, dirs, files in os.walk(".", topdown=True):
            if poemer in [file.replace('.png', '') for file in files]:
                return True
            else:
                return False









