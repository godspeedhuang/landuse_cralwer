import requests
# 正規表達法
import re
import json


request_url = 'https://free-proxy-list.net/'
response = requests.get(request_url)
# print(response.text)
# 用正規表達法找符合的字元(即IP)
m = re.findall('\d+\.\d+\.+\d+\.\d+:\d+', response.text)
# print(m)
validips = []
for ip in m:
    try:
        response = requests.get(
            'https://api.ipify.org?format=json', proxies={'http': ip, 'https:': ip}, timeout=5)
        validips.append(ip)
        print('success', ip)
    except:
        print('Fail', ip)
print(validips)

with open('ips.json', 'w') as file:
    json.dump(validips, file)
