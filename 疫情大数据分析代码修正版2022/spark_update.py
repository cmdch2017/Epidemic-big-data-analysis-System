# 导入包
import os
import pymysql
import pandas as pd
from pyspark.sql import Row
from pyspark.sql.types import *
from datetime import datetime
import pyspark.sql.functions as func
from pyspark.sql import SparkSession
from sqlalchemy import create_engine
from pyspark import SparkConf, SparkContext

# 判断当前目录下是否存在Data文件夹，如果没有就新建
dir_exists = os.system('ls | grep Data')
if dir_exists:
    os.system('mkdir Data')

# 下载文件在本地
filename = datetime.now().strftime("%Y-%m-%d") + '.csv'
file_exist = os.system('ls ./Data | grep {filename}'.format(filename=filename))  # 0 表示存在
if not file_exist:
    os.system('rm -f ./Data/*')
# 将HDFS 中的文件下载到Linux系统本地目录
downloadfile = 'hdfs dfs -get hdfs://192.168.222.10:9000/Data/' + filename + ' ./Data'
downloadfile = downloadfile.format(date=datetime.now().strftime("%Y-%m-%d"))
status = os.system(downloadfile)

# 格式转换
data = pd.read_csv('./Data/{filename}'.format(filename=filename))
textname = datetime.now().strftime("%Y-%m-%d") + '.txt'
os.system('rm -f ./Data/{textname}'.format(textname=textname))
with open('./Data/' + textname, 'a+', encoding='utf-8') as f:
    for line in data.values:
        f.write(
            (str(line[0]) + ',' + str(line[1]) + '\n'))

# **************************************************
import pymysql

# 打开数据库连接
conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="mydb")
# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# 通过open（）方法以只读的方式打开文件，编码格式为UTF-8
file = open("./Data/"+textname, 'r', encoding='UTF-8')
# 通过readlines（）方法读取文件的每一行赋值给lines
lines = file.readlines()
# 如果lines为真，执行循环的内容
if lines:
    for line in lines:      # lines是一个列表，列表中的每隔元素就是txt文件中的一行数据
        print(line)         # 这一步是为了验证是否能如期获取到列表
        line = line.strip('\n').split(',')   # strip（）去掉字符串头尾的符号，通过","将每行数据拆分
        a = line[0]         # 我的txt文件中每行2个元素，所以将2个元素分别赋值给变量ab
        b = line[1]
        sql = "insert into epidemic values(%s,%s)"  # 数据库数据插入语句
        param = (a,b)                               # param参数是要输入的数据
        cursor.execute(sql, param)                  # cursor.execute(sql,param)方法执行插入语句
conn.commit()								        # 提交
file.close()                                        # 关闭所有的连接
cursor.close()
conn.close()


# **************************************************

# # 创建spark
# spark = SparkSession.builder.config(conf=SparkConf()).getOrCreate()
#
# # 创建模式
# fields = [StructField("cities", StringType(), False),
#           StructField("counts", IntegerType(), False), ]
#
# rdd0 = spark.sparkContext.textFile('file:///root/Data/{textname}'.format(textname=textname))
# rdd1 = rdd0.map(lambda x: x.split("\t")).map(
#     lambda p: Row(p[0], p[1]))
# schema = StructType(fields)
#
# # 注册 ncov_2020临时表
# shemaUsInfo = spark.createDataFrame(rdd1, schema)
# shemaUsInfo.createOrReplaceTempView("ncov_2020")
#
# # 查询各省市的情况并将结果写入mysql数据库中
# df1 = spark.sql(
#     "SELECT cities,counts FROM ncov_2020")
# df1 = df1.withColumnRenamed("cities", "counts")
# connect = create_engine('mysql+pymysql://root:root@192.168.222.10:3306/mydb?charset=utf8')
# prop = {'user': 'root', 'password': '123456', 'driver': 'com.mysql.jdbc.Driver'}
# df1.write.jdbc("jdbc:mysql://192.168.222.10/mydb", 'my_table', 'overwrite', prop)

# 删除 china_total_with_date中关于今天的数据
# db = pymysql.connect("192.168.222.10", "root", "123456", "mydb", charset='utf8')
# cursor = db.cursor()
# sql = "DELETE FROM ncov_2020"
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     print("execute sql failed")
# db.close()

# 将今天的情况追加到china_toal_with_date表中
# df2 = spark.sql(
#     "SELECT DATE,confirmed,suspected,cured,dead FROM ncov_2019")
# df2.write.jdbc("jdbc:mysql://49.235.47.70/mydb", 'ncov_2020', 'append', prop)
