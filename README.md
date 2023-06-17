# welcome to use my project
# 欢迎使用我的项目
## *使用前* __必读__
```
项目作者：YELLOWZAN
IDE: Pycharm Professional、VScode、
Python version ：3.9.13
Database:Mysql version-5.8
其它工具：phpmyadmin
```
本项目所需依赖环境已在requirements.txt文件中

**使用前请先创建虚拟环境!**
然后在虚拟环境内安装requirements.txt的依赖，运行命令：
```shell
pip install -r requirements.txt
```
建议使用pycharm专业版运行项目 

可视化流程大致如下：

1.寻找数据，收集数据并处理好数据。

2.对数据进行分析，以做出合理的图表。

3.先对数据生成图表页面，存放在**templates**文件夹

4.在app.py文件中对设定文件进行文件路由调用以及负载均衡（**如果需要**）

# 所需技术栈

__HTML、Python、JavaScript、Mysql、flask__


**本项目为可视化课程项目设计，分为几大模块：**

## 1.数据爬取
数据爬取文件夹位于项目根目录下的.\pa_chong\

主程序文件为spider-demo.py，在运行前需要对所爬取的网页进行网页结构分析，对所需数据进行xpath定位或者re正则定位，提取我们所需要的数据。

然后，分析服务器是否存在反爬虫，比如字体反爬、ip封锁、验证码等，定制化相应的措施

爬虫文件我本人手写，反爬程序为定制化反爬，禁止用于非法用途

## 2.数据处理

数据处理比较常规，主要流程有清理空缺值，检查是否存在异常值等等，部分字段用到编码的手段，以方便后期的数据建模
处理完成的数据存放于./data_clear/clean_data/目录下

## 3.数据存储

这一部分为将数据放入数据库存储，由于时间关系我们尚未设计完成

## 4.静态页面生成

使用pyecharts代码整合我们所爬取到的数据进行生成静态页面，注意，echarts与pyecharts是两种不同的玩意！

## 5.前后端交互

项目运行方法：

```shell
cd ./  #项目根目录
python app.py  #启动flask并调用所需文件
```

需要注意的是，如果后期需要添加其它页面，请先在templates目录下生成所需的HTML页面文件，然后修改index.html以达到JS调用

修改方法如下：
```shell
cd ./templates  # 进入html页面目录

```

然后使用编辑器修改index.html代码
所需修改位置为（xpath地址）：/html/body/div/div[1]/ul
```html
        <li>
           <a href="#" onclick="showContent('出勤频率分布.html')">  # showContent函数内引号内容修改为所调用的文件
             <i class="fas fa-cloud"></i> 出勤频率分布   # 将此处修改为所显示的链接名称
           </a>
        </li>
```
