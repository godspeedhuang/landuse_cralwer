from pyproj import CRS
from pyproj.transformer import Transformer
import pyproj

# 方法一
# Step1，定義座標系統
TWD97 = pyproj.Proj(init='epsg:3826')
WGS84 = pyproj.Proj(init='epsg:4326')

# Step2，轉換座標，將WGS84轉成TWD97
lon, lat = TWD97(120.316135253, 22.7286904948)
print(lon, lat)

# Step2，轉換座標，將TWD97轉換成WGS84
lon, lat = pyproj.transform(TWD97, WGS84, 179754.960, 2514402.715)
print(lon, lat)


# 方法二(我覺得比較好用)

# Step1，初始化座標參考系統
# 台灣常用座標系統
crs_84 = CRS.from_epsg(4326)  # WGS84經緯度

crs_97_121 = CRS.from_epsg(3826)  # TWD97，中央經度121度，適用台灣本島
crs_97_191 = CRS.from_epsg(3825)  # TWD97，中央經度119度，適用澎湖金門馬祖

crs_67_121 = CRS.from_epsg(3828)  # TWD67，中央經度121度，適用台灣本島
crs_67_119 = CRS.from_epsg(3827)  # TWD67，中央經度1119度，適用澎湖金門馬祖

crs_mercator = CRS.from_epsg(3857)  # spherical mercator投影


# Step2，轉換座標，將WGS94轉換成TWD97
transformer = Transformer.from_crs(crs_84, crs_97_121)
trans = transformer.transform(
    22.728690494800002, 120.316135253)  # (lat緯度,lon經度)
print(trans)  # 印出WGS84

# Step2，轉換座標，將TWD97轉成WGS84
transformer = Transformer.from_crs(crs_97_121, crs_84)
trans = transformer.transform(
    179754.96003631147, 2514402.7149959356)  # (lat緯度,lon經度)
print(trans)  # 印出TWD97
