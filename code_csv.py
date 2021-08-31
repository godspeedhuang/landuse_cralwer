import json
import os
import pandas as pd

code = []
name = []
county = ['KHH', 'TNN', 'TXG', 'PIF']

for j in county:
    os.chdir('C:/Users/syuanbo/Desktop/landuse')
    os.chdir(j)
    with open(j + '.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i in data:
        code.append(i['計畫區代碼'])
        name.append(i['計畫區名稱'])


# print(code)
# print(name)
os.chdir('C:/Users/syuanbo/Desktop/landuse')
df = pd.DataFrame()
df['計畫區代碼'] = code
df['計畫區名稱'] = name
print(df)
df.to_csv('code_to_name.csv', encoding='utf-8')
