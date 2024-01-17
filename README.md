### hipy-ui 后端项目

##### 技术栈:  python|fastapi|redis|sqlachemy|postgresql|mysql|sqlite

[套装传送门:hipy-ui](https://github.com/hjdhnx/hipy-ui/)  
[巨人的肩膀](https://github.com/JohnDoe1996/fastAPI-vue)

## 项目部署

> 注意：
> 本源码中所有配置文件都使用 配置文件模板(.example)的形式上传, 目的是为了方便我自己的配置信息不被泄露。
> 部署项目时需要将[.example]后缀去掉才能使用。需要用到配置文件的地方均在后续说明有列出。

### FIRST

克隆项目主分支

```shell
git clone -b main https://github.com/hjdhnx/hipy-server.git
```

数据库中创建DB

```sql
CREATE
DATABASE hipy;  -- 仅供参考根据自己项目名和所用的数据库类型 修改SQL， 
```

运行脚本初始化数据库数据

```shell
cd ./hipy-server/app
python initial_data.py
```

### APP

1. 安装python3、virtualenv(pycharm自带)、Nginx、 supervisor

```shell
# 略
```

2. 安装必要第三方库

```shell
cd ./hipy-server/app   # 进入到后端程序代码的根目录

# 没有pycharm的注意下面两行代码，有的就跳过
python -m virtualenv venv     # 创建虚拟环境
source ./venv/bin/activate      # 进入虚拟环境

python -m pip install -i https://mirrors.cloud.tencent.com/pypi/simple --upgrade pip # 用腾讯源临时升级pip
pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple # 换源
pip install -r requirements.txt   # 安装库  可使用谷内源：  -i https://pypi.tuna.tsinghua.edu.cn/simple
```

3. 准备程序配置文件

```shell
cp ./configs/.env.example  ./configs/.env    # 复制配置模板

vim ./configs/.env     # 拷贝配置文件

# python main.py   # 测试项目是否成功运行，
```

> 根据需要修改.env的配置内容，配置所有的参数参考 ./core/config.py -> class Settings

4. 使用supervisor管理项目(生产环境)

```shell
cp ./configs/supervisor.conf.example  ./configs/supervisor.conf   # 拷贝配置文件

sudo ln -s /home/ubuntu/opt/hipy-server/app/configs/supervisor.conf /etc/supervisor/conf.d/hipy-server.conf   # 配置文件软链到supervisor的配置文件目录， 此处目录路径仅供参考

vim ./configs/supervisor.conf    # 编辑配置文件,已有参考配置，按需修改

sudo supervisorctl update     # 更新supervisor

sudo supervisorctl start hipy-server:   # 启动项目
```