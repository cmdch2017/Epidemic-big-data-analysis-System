import os
import json
import pandas as pd
import pymysql
import requests
import jsonpath


from datetime import datetime


# 定义文件名为每日的日期
filename = datetime.now().strftime("%Y-%m-%d") + '.csv'



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



# 数据存入mysql
def save_sql():

    data = pd.read_csv('./' + filename)  # scv文件读取位置，自行更改
    rows_nums = data.shape[0]
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='mydb',
                         charset='utf8')  # 数据库用户名、密码，自行更改
    cursor = db.cursor()
    try:
        cursor.execute("drop table if exists now_Crawling")
        cursor.execute("CREATE TABLE now_Crawling("
                             "name VARCHAR (100), "
                             "confirm VARCHAR (100),"
                             "confirm_all VARCHAR (100),"
                             "dead VARCHAR (100),"
                             "heal VARCHAR (200),"
                             "last_update_time VARCHAR (100));")
        for i in range(rows_nums):
            sql = "INSERT INTO now_Crawling(name, confirm,confirm_all,dead,heal,last_update_time) VALUES (%s,%s,%s,%s,%s,%s);"
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
    url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=318268778643"  # 网易提供的疫情数据网址
    resp = get_data(url)
    name, confirm, confirm_all, dead, heal,last_update_time = parse_data(resp)

    save_csv(name, confirm, confirm_all, dead, heal,last_update_time)

    save_sql()
