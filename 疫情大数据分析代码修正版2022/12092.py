import os
import json
import jsonpath
import pandas as pd
import pymysql
import requests
from pyecharts import options as opts
from pyecharts.charts import Map
import matplotlib.pyplot as plt
from pyecharts.faker import Faker
from datetime import datetime


# 定义文件名为每日的日期
filename = datetime.now().strftime("%Y-%m-%d") + '.csv'


# 上传至hdfs
def send_data_hdfs():
    # 这里是将其命名保存为当天的csv文件
    file_exist = os.system('ls ./Data | grep {filename}'.format(filename=filename))  # 0 表示存在
    if not file_exist:
        os.system('rm -f ./Data/*')
    os.system("hdfs dfs -put file:///root/" + filename + " /Data")


# 请求数据
def get_data(url):
    headers_value = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.61 Safari/537.36"}  # 请求头，自行更改
    try:
        resp = requests.get(url, headers=headers_value)
    except requests.exceptions.ConnectionError as e:
        print("请求错误", e)
        resp = None
    print("china数据请求成功")
    return resp


# 爬取数据
def parse_data(resp):
    data = json.loads(resp.text)
    name = jsonpath.jsonpath(data, "$.data.areaTree[2].children[*].name")  # 省份名
    confirm = jsonpath.jsonpath(data, "$.data.areaTree[2].children[*].today.confirm")  # 现有确诊
    confirm_all = jsonpath.jsonpath(data, "$.data.areaTree[2].children[*].total.confirm")  # 累计确诊
    dead = jsonpath.jsonpath(data, "$.data.areaTree[2].children[*].total.dead")  # 累计死亡
    heal = jsonpath.jsonpath(data, "$.data.areaTree[2].children[*].total.heal")  # 累计治愈
    last_update_time = jsonpath.jsonpath(data, "$.data.areaTree[2].children[*].lastUpdateTime")#更新时间
    # 数据处理,空值设置为0
    for i in range(len(confirm)):
        if confirm[i] == None:
            confirm[i] = 0
        elif confirm_all[i] == None:
            confirm_all[i] = 0
        elif dead[i] == None:
            dead[i] == 0
        elif heal[i] == None:
            heal[i] = 0
        elif last_update_time[i]:
            print(last_update_time[i])
            arr = str(last_update_time[i]).split(" ")
            last_update_time[i] = arr[0]
    print("china 数据爬取成功！")
    print("name:", name)
    print("confirm:", confirm)
    print("confirm_all:", confirm_all)
    print("dead:", dead)
    print("heal:", heal)
    print("last_update_time", last_update_time)
    return name, confirm, confirm_all, dead, heal,last_update_time


# 数据储存csv
def save_csv(name, confirm, confirm_all, dead, heal,last_update_time):
    result = pd.DataFrame()
    result['省份'] = name
    result['新增确诊'] = confirm
    result['累计确诊'] = confirm_all
    result['死亡'] = dead
    result['治愈'] = heal
    result['更新日期'] = last_update_time
    result.to_csv("./" + filename, encoding='utf_8_sig', index=None)  # csv文件保存位置，自行更改
    print("中国数据保存csv成功")


# PyechartsMap 地图
def plt_data(name, confirm_all):
    data_list = list(zip(name, confirm_all))
    map = Map(opts.InitOpts(width='1600px', height='600px')).add(series_name='累计确诊',
                                                                 data_pair=data_list,
                                                                 maptype="china",
                                                                 is_map_symbol_show=False)
    map.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    map.set_global_opts(title_opts=opts.TitleOpts("中国疫情"),
                        visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color, max_=1000))  # 图例显示
    map.render("./Data/中国疫情分布图.html")  # 疫情地图保存位置，自行更改
    plt.rcParams['font.sans-serif'] = ['FangSong']
    plt.bar(range(len(confirm_all)), confirm_all, tick_label=name)
    plt.xticks(rotation=270)
    plt.savefig("./Data/中国疫情柱状图")  # 柱状图保存位置，自行更改。
    print("中国数据可视化成功，文件名：中国疫情分布图.html、中国疫情柱状图.png")


# 数据存入mysql
def save_sql():
#这里如果能够从hdfs读取文件的话会存入Data文件夹下，如果你hdfs配置了，运行下面第一句话，如果你没有配置，则运行第二句话，跳过hdfs
#*********************************************************************************
#    data = pd.read_csv('./Data/' + filename)  # scv文件读取位置，自行更改
#*********************************************************************************
    data = pd.read_csv('./' + filename)  # scv文件读取位置，自行更改
    rows_nums = data.shape[0]
    db = pymysql.connect(host='localhost', user='root', password='123456', db='mydb',
                         charset='utf8')  # 数据库用户名、密码，自行更改
    cursor = db.cursor()
    try:
      #  cursor.execute("drop table if exists data_china")
      #  cursor.execute("CREATE TABLE data_china("
      #                       "name VARCHAR (100), "
      #                       "confirm VARCHAR (100),"
      #                       "confirm_all VARCHAR (100),"
      #                       "dead VARCHAR (100),"
      #                       "heal VARCHAR (200),"
      #                       "last_update_time VARCHAR (100));")
        for i in range(rows_nums):
            sql = "INSERT INTO data_china(name, confirm,confirm_all,dead,heal,last_update_time) VALUES (%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql, (
                (str)(data.iloc[i, 0]), (str)(data.iloc[i, 1]), (str)(data.iloc[i, 2]), (str)(data.iloc[i, 3]),
                (str)(data.iloc[i, 4]),(str)(data.iloc[i, 5])))
        cursor.close()
        db.commit()
        print("中国数据保存已保存到mysql")
    except:
        db.rollback()
        print("ERROR")
        cursor.close()
    finally:
        cursor.close()


def download_data_hdfs():
    # 将HDFS 中的文件下载到Linux系统本地目录的Data目录下
    os.system('hdfs dfs -get hdfs://192.168.222.10:9000/Data/' + filename + ' ./Data')


if __name__ == '__main__':
    url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=318268778643"  # 网易提供的疫情数据网址
    resp = get_data(url)
    name, confirm, confirm_all, dead, heal,last_update_time = parse_data(resp)

    save_csv(name, confirm, confirm_all, dead, heal,last_update_time)
    # 云服务器上运行此代码
    send_data_hdfs()
    download_data_hdfs()
    save_sql()
#    plt_data(name, confirm_all)
'''
#效果图如下
![csv文件截图.png](https://upload-images.jianshu.io/upload_images/19102738-28b2f15a3a801571.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![中国地图.png](https://upload-images.jianshu.io/upload_images/19102738-77b57d2763917618.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![柱状图.png](https://upload-images.jianshu.io/upload_images/19102738-1b25cd73b869d7ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
'''
