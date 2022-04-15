import os

# 定义文件名为每日的日期
day = '18'
month = '05'
filename = '2021-' + month + '-' + day + '.csv'
print(filename)


# 上传至hdfs
def send_data_hdfs():
    # 这里是将其命名保存为当天的csv文件
    file_exist = os.system('ls ./Data | grep {filename}'.format(filename=filename))  # 0 表示存在
    if not file_exist:
        print("上传失败,原因："
              "404，File not Found")
    os.system("hdfs dfs -put file:///root/" + filename + " /Data")


if __name__ == '__main__':
    send_data_hdfs()
    print("代码执行成功")
