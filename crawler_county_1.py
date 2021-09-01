import requests
import json
import os
import pandas as pd
from fake_useragent import UserAgent
import time
import random
# 抓該縣市有哪些都計區


user_agent = UserAgent()
with open('ips.json', 'r') as file:
    cips = json.load(file)
# 建立該縣市資料夾(輸入縣市英文代碼)
with open('taiwan_administrative_divisions.csv', 'r', encoding='utf-8') as file:
    data = pd.read_csv(file)

HRCIS = data['HRCIS'].tolist()
ISO = data['ISO'].tolist()
HRCIS
ISO

# for h, i in zip(HRCIS, ISO):
headers_m = {
    'authority': 'luz.tcd.gov.tw',
    'method': 'POST',
    # 更換
    'path': '/web/ws_data.ashx?CMD=GETDATA&OBJ=URBANPLAN',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-length': '22',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 更換
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
    'FUNC': '0101',
    # 輸入縣市代碼
    'COUNTY': '09007'
}
request_url = 'https://luz.tcd.gov.tw/web/ws_data.ashx?CMD=GETDATA&OBJ=URBANPLAN'
response = requests.post(request_url, data=form_data, headers=headers_m, proxies={
                         'https://': random.choice(cips), 'http://': random.choice(cips)})
elements = response.json()
elements_list = [i for i in elements]
print(elements_list)

# 輸入資料夾名稱
os.chdir('C:/Users/syuanbo/Desktop/landuse/Taiwan_district_code')

# 建立該縣市都計區檔案
# 輸入縣市名稱
with open('LIE.json', mode='w', encoding='utf-8') as file:
    json.dump(elements_list, file, ensure_ascii=False)
# time.sleep(random.randint(2, 5))
