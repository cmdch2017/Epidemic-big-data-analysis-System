import os

from pyecharts.charts import Map
from pyecharts import options as opts
import requests
import pandas as pd
from datetime import datetime

# &callback=jQuery35109954929483789403_1605576147763&_=1605576147764
res = requests.get('https://i.snssdk.com/toutiao/normandy/pneumonia_trending/city_dist/?activeWidget=1')

res_json = res.json()['data']
res_name = res_json["list"]

res_sj = {}
for i in res_name:
    res_sj[i["name"]] = i["total"]

data = [list(i) for i in zip(res_sj.keys(), res_sj.values())]
# data = [("广东", 10430.03), ("山东", 9579.31), ("河南", 9402.36), ("四川", 8041.82), ("江苏", 7865.99), ("河北", 7185.42),
#         ("湖南", 6568.37), ("安徽", 5950.1), ("浙江", 5442), ("湖北", 5723.77), ("广西", 4602.66), ("云南", 4596.6),
#         ("江西", 4456.74), ("辽宁", 4374.63), ("黑龙江", 3831.22), ("陕西", 3732.74), ("山西", 3571.21), ("福建", 3552),
#         ("重庆", 2884), ("贵州", 3476.65), ("吉林", 2746.22), ("甘肃", 2557.53), ("内蒙古", 2470.63), ("上海", 2301.391),
#         ("台湾", 2316.2), ("新疆", 2181.33), ("北京", 1961.2), ("天津", 1293.82), ("海南", 867.15), ("香港", 709.76),
#         ("青海", 562.67), ("宁夏", 630.14), ("西藏", 300.21), ("澳门", 55.23)]
print(data)

# list = [[1, '肖申克的救赎', '犯罪 剧情', '9.7'],
#         [2, '霸王别姬', '剧情 爱情', '9.5'],
#         [3, '阿甘正传', '爱情', '9.5'],
#         [4, '这个杀手不太冷', '剧情 动作 犯罪', '9.4'],
#         [5, '美丽人生', '喜剧 爱情 战争', '9.5']]
# name = ['豆瓣排名', '电影名称', '类别', '评分']
name = ['城市', '数量']
test = pd.DataFrame(columns=name, data=data)
print(test)

# **************************************************************
# 这里是将其命名保存为当天的csv文件
filename = datetime.now().strftime("%Y-%m-%d") + '.csv'
file_exist = os.system('ls ./Data | grep {filename}'.format(filename=filename))  # 0 表示存在
if not file_exist:
    os.system('rm -f ./Data/*')
test.to_csv('./Data/'+filename, index=False)
os.system("hdfs dfs -put file:///root/Data/"+filename+" /Data")
# **************************************************************

coronavirusMap = (
    Map().add("", data, "china")
        .set_global_opts(
        title_opts=opts.TitleOpts(title="疫情地图", subtitle="数据来源：字节跳动", pos_right="center", pos_top="5%"),
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True,

                                          pieces=[
                                              {"min": 1, "max": 9, "label": "1-9人", "color": "#FFF68F"},
                                              {"min": 10, "max": 99, "label": "10-99人", "color": "#7CFC00"},
                                              {"min": 100, "max": 999, "label": "100-999人", "color": "red"},
                                              {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CD0000"},
                                              {"min": 10000, "label": "10000人以上", "color": "#9d2933"}
                                          ]),
    )
)

coronavirusMap.render("testMap.html")
