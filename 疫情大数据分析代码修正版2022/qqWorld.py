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
import time

# 定义文件名为每日的日期
filename = 'qqWorld' + datetime.now().strftime("%Y-%m-%d") + '.csv'


# 上传至hdfs
def send_data_hdfs():
    # 这里是将其命名保存为当天的csv文件
    file_exist = os.system('ls ./Data | grep {filename}'.format(filename=filename))  # 0 表示存在
    if not file_exist:
        os.system('rm -f ./Data/*')
        print("上传失败,原因："
              "404，File not Found")
    os.system("hdfs dfs -put file:///root/" + filename + " /Data")


# 请求数据
def get_data(url):
    headers_value = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.141 Safari/537.36"}  # 请求头，自行更改
    try:
        resp = requests.get(url, headers=headers_value, verify=False)
    except requests.exceptions.ConnectionError as e:
        print("请求错误", e)
        resp = None
    print("china数据请求成功")
    return resp


# 爬取数据
def parse_data(res):
    # 这里有字典呈现键值对模型，所以只能先将字典的value值取出再做分析，转化为str类型
    res_json = res.json()['data']  # dict;字典转str类型
    data = json.loads(res_json)  # 因为json.loads只能读取str类型的数据
    print(data)
    name = jsonpath.jsonpath(data, "$.foreignList[*].name")
    continent = jsonpath.jsonpath(data, "$.foreignList[*].continent")
    confirm = jsonpath.jsonpath(data, "$.foreignList[*].confirmAdd")
    date = jsonpath.jsonpath(data, "$.foreignList[*].date")
    year = jsonpath.jsonpath(data, "$.foreignList[*].y")
    confirm_all = jsonpath.jsonpath(data, "$.foreignList[*].confirm")
    dead = jsonpath.jsonpath(data, "$.foreignList[*].dead")
    heal = jsonpath.jsonpath(data, "$.foreignList[*].heal")
    isupdated = jsonpath.jsonpath(data, "$.foreignList[*].isUpdated")
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
        if date[i] is not None:
            date[i] = year[i] + "-" + (date[i]).replace(".", "-")

    print("world数据爬取成功");

    return name, continent, confirm, date, year, confirm_all, dead, heal, isupdated


# 数据储存csv
def save_csv(name, continent, confirm, update_date, year, confirm_all, dead, heal, isupdated):
    result = pd.DataFrame()
    result['国家'] = name
    result['洲'] = continent
    result['tx确诊人数'] = confirm
    result['tx日期'] = update_date
    result['年份'] = year
    result['tx所有确诊人数'] = confirm_all
    result['总计死亡'] = dead
    result['总计治愈'] = heal
    result['是否更新'] = isupdated
    result.to_csv("./" + filename, encoding='utf_8_sig', index=None)  # csv文件保存位置，自行更改
    print("new的世界数据保存csv成功")


# 数据存入mysql
def save_sql():
    # 本地将scv存入sql，本地/linux时需要修改路径
    data = pd.read_csv('./' + filename)  # scv文件读取位置，自行更改
    rows_nums = data.shape[0]
    db = pymysql.connect(host='localhost', user='root', password='123456', db='mydb',
                         charset='utf8')  # 数据库用户名、密码，自行更改
    cursor = db.cursor()
    try:
      #  cursor.execute("drop table if exists qq_world")
      #  cursor.execute("CREATE TABLE qq_world("
      #                 "name VARCHAR (100), "
      #                 "continent VARCHAR (100),"
      #                 "confirm VARCHAR (100),"
      #                 "update_date VARCHAR (100),"
      #                 "year VARCHAR (200),"
      #                 "confirm_all VARCHAR (200),"
      #                 "dead VARCHAR (200),"
      #                 "heal VARCHAR (200),"
      #                "isupdated VARCHAR (100)) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;")
        for i in range(rows_nums):
            sql = "INSERT INTO qq_world(name, continent, confirm, update_date, year, confirm_all, dead, heal, " \
                  "isupdated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s); "
            cursor.execute(sql, (
                str(data.iloc[i, 0]), str(data.iloc[i, 1]), str(data.iloc[i, 2]),
                str(data.iloc[i, 3]), str(data.iloc[i, 4]), str(data.iloc[i, 5]),
                str(data.iloc[i, 6]), str(data.iloc[i, 7]), str(data.iloc[i, 8])))
        cursor.close()
        db.commit()
        print("tx数据保存已保存到mysql")
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
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign"
    resp = get_data(url)
    name, continent, confirm, date, year, confirm_all, dead, heal, isupdated = parse_data(resp)
    save_csv(name, continent, confirm, date, year, confirm_all, dead, heal, isupdated)
    # add_date_csv()
    # 云服务器上运行此代码
    # send_data_hdfs()
    # download_data_hdfs()
    save_sql()
