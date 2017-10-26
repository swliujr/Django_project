from os import path
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread

def make_word_cloud_png(k):
    BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
    abs_path = path.dirname(__file__)
    #读取txt文件 同理也可以读取数据库
    mylist = list(open(path.join(abs_path,'{}.txt'.format(k))).readlines())
    word_list = [" ".join(jieba.cut(sentence)) for sentence in mylist]
    new_text = ' '.join(word_list)
    imagename = path.join(abs_path, "bg.png")  # 背景图片路径
    coloring = imread(imagename)             # 读取背景图片
    fontname=path.join(abs_path, "msyh.ttf")  # 使用的是微软雅黑字体
    wordcloud = WordCloud(mask=coloring,font_path=fontname,max_font_size=60).generate(new_text)
    plt.imshow(wordcloud)
    plt.axis("off")
    # 词云图片 存到到 django项目 static/wordImages文件夹内 文件名为 ***.png xxx 为传递的参数
    wordcloud_png_path = path.join(BASE_DIR, 'static/wordImages/{}'.format(k))
    wordcloud.to_file('{}.png'.format(wordcloud_png_path))
if __name__ == '__main__':
    k = '李白'
    make_word_cloud_png(k)