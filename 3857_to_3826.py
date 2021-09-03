import json
from pyproj import CRS
from pyproj.transformer import Transformer
import pandas as pd
import os
import time

with open('taiwan_administrative_divisions.csv', 'r', encoding='utf-8') as file:
    data = pd.read_csv(file)
HRCIS = data['HRCIS'].tolist()
ISO = data['ISO'].tolist()

# 座標轉換
crs_97 = CRS.from_epsg(3826)
crs_mercator = CRS.from_epsg(3857)
transformer = Transformer.from_crs(crs_mercator, crs_97)


# 轉換中
for iso in ISO:
    path = 'C:/Users/syuanbo/Desktop/landuse'
    os.chdir(os.path.join(path, 'Taiwan_district_code'))
    with open(iso+'.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    # print(data)
    os.chdir(os.path.join(path, iso+'_block'))
    for d in data:
        with open(d['計畫區代碼']+'_block.json', 'r', encoding='utf-8') as file:
            block_data = json.load(file)
        data_geo = block_data['features'][0]['geometry']['coordinates']
        trans = []
        geo = []
        time.sleep(1)
        for i in data_geo:
            trans.clear()
            for j in i:
                # (lat緯度,lon經度)
                trans.append(list(transformer.transform(j[0], j[1])))
            geo.append(trans)

            # print(trans)  # 印出WGS84
        block_data['features'][0]['geometry']['coordinates'] = geo

        with open(d['計畫區代碼']+'_block_97.json', 'w', encoding='utf-8') as file:
            json.dump(block_data, file)
