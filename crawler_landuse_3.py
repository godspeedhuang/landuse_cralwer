import requests
import json
import time
import random
from fake_useragent import UserAgent
import os

# 處理防爬蟲技術
user_agent = UserAgent()
with open('ips.json', 'r') as file:
    cips = json.load(file)
# 進入該縣市資料夾
os.chdir('C:/Users/syuanbo/Desktop/landuse/KHH')

# 抓出所有該縣市的都計區
with open('KHH_2.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)
data_plan = [i['計畫區代碼'] for i in data]


for d in data_plan:
    # 抓出該都計區有的土地使用分區類別
    with open(d+'_code.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
    landuse_code = [k['分區代碼'] for k in data]

    # 建立該都計區geojson
    merge = dict()
    merge['type'] = 'FeatureCollection'
    merge['features'] = []

    # 該都計區各土地使用分區爬蟲
    for i in landuse_code:
        headers_m = {
            'authority': 'luz.tcd.gov.tw',
            'method': 'POST',
            # 更改
            'path': '/web/ws_data.ashx?CMD=SEARCHURBANLANDUSE&TOKEN=U65yWjl1zDnIAUMdC3gzyuMG0pUR0h_UvdjLBpEvF5V-Jc2ZCnBV23UDyyOL3n7bC-XCeKGv41-DsF22rSTifw..',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'content-length': '22',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 更改
            'cookie': '_ga=GA1.3.55520146.1629099145; _gid=GA1.3.967154037.1630226023; ASP.NET_SessionId=iigmb0dtq0qf4a5y1sk154xi',
            'origin': 'https://luz.tcd.gov.tw',
            'referer': 'https://luz.tcd.gov.tw/web/default.aspx',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user_agent.random,
            'x-requested-with': 'XMLHttpRequest'
        }
        form_data = {
            'VAL1': d,
            'VAL2': i
        }
        request_url = 'https://luz.tcd.gov.tw/web/ws_data.ashx?CMD=SEARCHURBANLANDUSE&TOKEN=U65yWjl1zDnIAUMdC3gzyuMG0pUR0h_UvdjLBpEvF5V-Jc2ZCnBV23UDyyOL3n7bC-XCeKGv41-DsF22rSTifw..'
        response = requests.post(
            request_url, data=form_data, headers=headers_m, proxies={'https://': random.choice(cips), 'http://': random.choice(cips)})
        # 隨機更換ip位置
        raw_data = response.json()
        data_select = raw_data['features']

        # append進geojson裡面
        for c in data_select:
            contain = {
                "type": "Feature",
                "properties": {
                    'planning_code': d,
                    'landuse_code': i,
                    'date': '2021/08/30'
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": c['geometry']['rings']
                }}
            merge['features'].append(contain)
        print('success '+str(i))

        # 間隔
        time.sleep(random.randint(5, 10))
    with open(str(d)+'.json', mode='w', encoding='utf-8') as file:
        json.dump(merge, file, ensure_ascii=False)
    print('=============================================')
    print('success '+str(d))
    print('=============================================')
