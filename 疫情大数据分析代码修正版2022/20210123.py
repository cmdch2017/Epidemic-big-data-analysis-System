import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import pymysql


filename = "China_area" + '.csv'


def get_data(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    # 找到所有class为md_td的td元素
    aaa = soup.find_all(name="td", attrs={"class": re.compile(r"md_td")})
    # 检查索引，以便于后面爬取工作
    # for n,i in enumerate(aaa):
    #    print(n,i.text)
    demo_list = []
    list1 = []
    list2 = []
    for i in aaa[4:128]:
        demo_list.append(i.text)
    while demo_list:
        list1.append(demo_list[0:4][1])
        list2.append(int(float(demo_list[0:4][2]) * 10000))
        del demo_list[0:4]
    return list1, list2


def save_csv(aname, people):
    result = pd.DataFrame()
    result['省份'] = aname
    result['人口'] = people
    result.to_csv("./" + filename, encoding='utf_8_sig', index=None)  # csv文件保存位置，自行更改
    print("中国人口数据保存csv成功")


def save_sql():
    # 本地将scv存入sql，本地/linux时需要修改路径
    data = pd.read_csv('./' + filename)  # scv文件读取位置，自行更改
    rows_nums = data.shape[0]
    db = pymysql.connect(host='localhost', user='root', password='123456', db='mydb',
                         charset='utf8')  # 数据库用户名、密码，自行更改
    cursor = db.cursor()
    try:
        cursor.execute("CREATE TABLE  if not exists china_people("
                       "name VARCHAR (100), "
                       "people VARCHAR (100)) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;")
        for i in range(rows_nums):
            sql = "INSERT INTO china_people(name,people) VALUES (%s,%s); "
            cursor.execute(sql, (
                str(data.iloc[i, 0]), str(data.iloc[i, 1])))
        cursor.close()
        db.commit()
        print("数据保存已保存到mysql")
    except:
        db.rollback()
        print("ERROR")
        cursor.close()
    finally:
        cursor.close()


if __name__ == '__main__':
    aname, people = get_data(url='http://www.china-10.com/news/488659.html')
    save_csv(aname, people)
    save_sql()
