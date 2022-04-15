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
filename = '2021-06-09'+ '.csv'




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



if __name__ == '__main__':
    save_sql()
