
import os
from os import path
from maoyan.settings import BASE_DIR

class CodeTest(object):
    def check_code_run(self,input_code):
        par_path = path.join(BASE_DIR,'static')
        os.chdir(par_path)
        pyfile = path.join(par_path,'index.py')
        relust_file =  path.join(par_path,'code_result.txt')
        #生成index.py
        with open(pyfile,'w',encoding='utf8') as fw:
            fw.write(input_code)
        with open(pyfile,'r',encoding='utf8') as py:
            pycode=py.read()
        # 交互模式执行 生成结果文件
        execute_code = 'python {} 2>&1 |tee code_result.txt'.format(pyfile)
        os.system(execute_code)
        #读取结果文件
        with open(relust_file,'r',encoding='utf8') as fr:
            contents = fr.readlines()
            code_run_result = '\n'.join(contents).replace('/Users/chengxinyao/django_project/maoyan/static/','')
        os.remove(relust_file)
        #返回代码运行结果
        return pyfile,pycode,code_run_result




