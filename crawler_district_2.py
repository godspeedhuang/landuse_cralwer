import requests
import json
import os
# 抓該縣市都計區有哪些土地使用分區

# 進入該縣市資料夾
os.chdir('C:/Users/syuanbo/Desktop/landuse/TNN')

# 讀取該縣市都計區
with open('TNN.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
plnning_code = [i['計畫區代碼'] for i in data]

for i in plnning_code:
    headers_m = {
        'authority': 'luz.tcd.gov.tw',
        'method': 'POST',
        # 更換
        'path': '/web/ws_data.ashx?CMD=GETDATA&OBJ=URBANPLANS',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-length': '22',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 更換
        'cookie': '_ga=GA1.3.55520146.1629099145; _gid=GA1.3.967154037.1630226023; ASP.NET_SessionId=iigmb0dtq0qf4a5y1sk154xi',
        'origin': 'https://luz.tcd.gov.tw',
        'referer': 'https://luz.tcd.gov.tw/web/default.aspx',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73',
        'x-requested-with': 'XMLHttpRequest'
    }
    form_data = {
        'FUNC': '0101',
        # 輸入縣市代碼
        'VAL1': i
    }
    request_url = 'https://luz.tcd.gov.tw/web/ws_data.ashx?CMD=GETDATA&OBJ=URBANPLANS'
    response = requests.post(request_url, data=form_data, headers=headers_m)
    elements = response.json()

    # 建立json
    with open(i+'_code.json', mode='w', encoding='utf-8') as file:
        json.dump(elements, file, ensure_ascii=False)
