import requests
import json
import time
import random
from fake_useragent import UserAgent
import os
import pandas as pd

# 處理防爬蟲技術
user_agent = UserAgent()
with open('ips.json', 'r') as file:
    cips = json.load(file)

# 抓出ISO碼
with open('taiwan_administrative_divisions.csv', 'r', encoding='utf-8') as file:
    data = pd.read_csv(file)

HRCIS = data['HRCIS'].tolist()
ISO = data['ISO'].tolist()
HRCIS.pop(0)
ISO.pop(0)

# 新增該縣市都計區範圍資料夾
for iso in ISO:
    os.chdir('C:/Users/syuanbo/Desktop/landuse')
    os.mkdir(iso+'_block')
    os.chdir('C:/Users/syuanbo/Desktop/landuse/Taiwan_district_code')

    # 抓出所有該縣市都計區的編號
    with open(iso+'.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
    data_plan = [i['計畫區代碼'] for i in data]

    os.chdir('C:/Users/syuanbo/Desktop/landuse/'+iso+'_block')
    for d in data_plan:

        # 該都計區各土地使用分區爬蟲
        headers_m = {
            'authority': 'luz.tcd.gov.tw',
            'method': 'POST',
            # 更改
            'path': '/web/ws_data.ashx?CMD=SEARCHURBANRANGE&TOKEN=U65yWjl1zDnIAUMdC3gzyuKCedGtDVZMYa5aw6sOY8GNirf1_GKHujtaNDhAcpjFFFpziwXLwblCvTQ9rxXtgQ..',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'content-length': '22',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 更改
            'cookie': '_ga=GA1.3.55520146.1629099145; _gid=GA1.3.967154037.1630226023; ASP.NET_SessionId=3cqvm420uoaovw0ws3imgzri; _gat_gtag_UA_164207323_1=1',
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
        }
        request_url = 'https://luz.tcd.gov.tw/web/ws_data.ashx?CMD=SEARCHURBANRANGE&TOKEN=U65yWjl1zDnIAUMdC3gzyuKCedGtDVZMYa5aw6sOY8GNirf1_GKHujtaNDhAcpjFFFpziwXLwblCvTQ9rxXtgQ..'
        response = requests.post(
            request_url, data=form_data, headers=headers_m, proxies={'https://': random.choice(cips), 'http://': random.choice(cips)})

        # 隨機更換ip位置
        raw_data = response.json()
        data_select = raw_data['features']

        # 建立該都計區geojson
        merge = dict()
        merge['type'] = 'FeatureCollection'
        merge['features'] = []
        for c in data_select:
            contain = {
                "type": "Feature",
                "properties": {
                    'planning_code': d,
                    'date': '2021/08/31'
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": c['geometry']['rings']
                }}
        merge['features'].append(contain)
        with open(str(d)+'_block.json', mode='w', encoding='utf-8') as file:
            json.dump(merge, file, ensure_ascii=False)

        print('success '+str(d))

        # 間隔
        time.sleep(random.randint(5, 10))
    print('=============================================')
    print('success'+str(iso))
    print('=============================================')
