**一.安装前准备 mysql服务 建库**
```
#在哪台机器安装airflow 需要在这台机器本地开启mysql服务(非root账户则需要拥有建库建表权限)
mysql  -u root -p 
输入密码
#注意命令后的分号
mysql>create database airflow;
```

![创建airflow数据库](https://www.showdoc.cc/home/common/visitfile/sign/6042622b77e696b3519b1dd394d74256?showdoc=.jpg)

**二.安装**
```
#2.1 使用pip安装 安装完之后会在root文件夹下生成airflow文件夹
export AIRFLOW_HOME=~/.airflow
pip install airflow
#上面执行完 输入airflow会显示其相关的命令 backfill test run 等 说明安装成功 已经添加进环境变量
```
```
#2.2 安装python链接mysql的驱动
pip install pymysql
```
```
#2.3 安装密码验证模块 web登录
pip install airflow[password]
```
```
#2.4 进入airflow文件夹 修改配置文件
cd airflow
vim airflow.cfg

```
```
#2.5 修改执行器
#执行器 LocalExecutor是调用本地进程执行
executor = LocalExecutor
```
```
#2.6 修改默认链接为mysql airflow数据库 pymysql是驱动模块
sql_alchemy_conn = mysql+pymysql://root:密码@localhost:3306/airflow
```
![修改数据库和执行器](https://www.showdoc.cc/home/common/visitfile/sign/727d9ab5d9ff238c8c5e06ee54cd0f82?showdoc=.jpg)
```

#2.7 修改webserver 开启密码验证
authenticate = true
auth_backend = airflow.contrib.auth.backends.password_auth
```
![开启密码验证](https://www.showdoc.cc/home/common/visitfile/sign/a0aaa97ae49c2b12a2922d507c5c5420?showdoc=.jpg)

```
#2.8创建存放python脚本的目录 /data/airflow_jobs  data目录下创建 airflow_jobs
cd /data
mkdir airflow_jobs
```

```
#2.9编辑web登录用户脚本
cd airflow_jobs
vim create_user.py

#输入以下代码
import sys
import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
user_name = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]
print('user_name:---->:',user_name)
print('email:---->:',email)
pwd_len = len(password)
pwd = password[:1] +'*'*(pwd_len-3)+password[-1]
print('password:---->:',pwd)
user = PasswordUser(models.User())
user.username = user_name
user.email = email
user.password = password
session = settings.Session()
session.add(user)
session.commit()
session.close()
print('user:---->{}   created success'.format(user_name))

```
```
2.10 创建用户  airflow_jobs目录下执行下面命令
#参数不可更换顺序 依次为用户名  邮箱 密码
python create_user.py 用户名 邮箱 密码
```
![创建用户](https://www.showdoc.cc/home/common/visitfile/sign/cc0891b07b3ff325b6596c664a659f36?showdoc=.jpg)

![airflow数据库 user表记录](https://www.showdoc.cc/home/common/visitfile/sign/b5a01dcfabd2134f40fead1fbf86918e?showdoc=.jpg)


```
#2.11 修改邮箱设置 smtp
#发件邮箱服务器 金服邮箱
smtp_host = mail.galaxyf.com
smtp_starttls = True
smtp_ssl = False
#用户
smtp_user = xinyaocheng@galaxyf.com
#端口
smtp_port = 25
#用户密码
smtp_password = 密码(不用加引号)
smtp_mail_from = xinyaocheng@galaxyf.com
```
![修改smtp](https://www.showdoc.cc/home/common/visitfile/sign/2e35ef98c95b5f6dba87fd8df28595b0?showdoc=.jpg)
```
#2.12 airflow初始化数据库 会在本地mysql数据库airflow下创建表
airflow initdb;
```

```
#2.13 创建 dags目录 用于存放任务python脚本 airflow会自动识别这个路径下的文件
mkdir dags
```

![创建dags目录](https://www.showdoc.cc/home/common/visitfile/sign/ef88a9326617dec13a68e981eb66e126?showdoc=.jpg)
```
#启动web服务 在windows的服务器上输入 本地http://localhost:8080 弹出登录页面 外网用http://公网ip:8080 访问
airflow webserver -p 8080
#输入创建的用户名和密码即可

```
![web页面任务调度](https://www.showdoc.cc/home/common/visitfile/sign/14b9f8ed00d03efd1b5d3b8bcb09d286?showdoc=.jpg)

