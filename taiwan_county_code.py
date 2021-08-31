import requests
import json
import pandas as pd

request_url = 'https://en.wikipedia.org/wiki/List_of_administrative_divisions_of_Taiwan'
res = requests.get(request_url)
elements = res.text

df = pd.read_html(elements)
data = df[0]

data.iloc[0, 0] = 'NWT'
data

data.to_csv('taiwan_administrative_divisions.csv')

data['HRCIS'].tolist()
