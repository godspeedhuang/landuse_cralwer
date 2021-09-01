import json
import os
import pandas as pd
county = []
code = []
name = []

with open('taiwan_administrative_divisions.csv', 'r', encoding='utf-8') as file:
    data = pd.read_csv(file)

HRCIS = data['HRCIS'].tolist()
ISO = data['ISO'].tolist()


for j in ISO:
    os.chdir('C:/Users/syuanbo/Desktop/landuse/Taiwan_district_code')
    with open(j + '.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i in data:
        county.append(j)
        code.append(i['計畫區代碼'])
        name.append(i['計畫區名稱'])


# print(code)
# print(name)
os.chdir('C:/Users/syuanbo/Desktop/landuse')
df = pd.DataFrame()
df['計畫區縣市'] = county
df['計畫區代碼'] = code
df['計畫區名稱'] = name
print(df)
df.to_csv('code_to_name.csv', encoding='utf-8')
