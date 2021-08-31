import json
import os
import pandas as pd

counties = ['KHH', 'TNN', 'TXG', 'PIF']
for i in counties:
    os.chdir('./'+i)
    with open(i+'.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    code = pd.DataFrame(list(data.items()), columns=['計畫區代碼', '計畫區名稱'])
