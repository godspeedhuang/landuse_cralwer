import json
from pyproj import CRS
from pyproj.transformer import Transformer


with open('E0101_block.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

data_geo = data['features'][0]['geometry']['coordinates']

# 座標轉換
crs_97 = CRS.from_epsg(3826)
crs_mercator = CRS.from_epsg(3857)
transformer = Transformer.from_crs(crs_mercator, crs_97)

trans = []
geo = []
# print(data_geo[0][1])
for i in data_geo:
    for j in i:
        trans.append(list(transformer.transform(j[0], j[1])))  # (lat緯度,lon經度)
        # print(i)
    geo.append(trans)
    trans.clear()
    # print(trans)  # 印出WGS84

data['features'][0]['geometry']['coordinates'] = geo
print(data)

with open('E0101_block_97.json', 'w', encoding='utf-8') as file:
    json.dump(data, file)
