# -*- coding: utf-8 -*-

import requests, json
url = "http://192.168.31.98:8040/access/records"
payload = {
    'len': 50,
    'active': 1
}
headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJhZG1pbiIsImF0dGVuZGFuY2UiOiJhZG1pbiIsImNvcmUiOiJhZG1pbiIsImVudGVycHJpc2UiOiJhZG1pbiIsImV4YW0iOiJhZG1pbiIsImV4cCI6MTU0MzY2NjA1MywiaWQiOiI5NDU1ZDUwZC1mODFhLTExZTYtOTliMS0wMjQyYWMxMzAwMGUiLCJvcmlnX2lhdCI6MTU0MzQwNjg1MywicGF5bWVudCI6ImFkbWluIiwicmVtb3Rlc2l0ZSI6ImFkbWluIiwidmlzaXRvciI6ImFkbWluIn0.64UTweZEwbCRJBz_RwgqajM2pR13ZYP4pNNXpx7byJ0','Content-Type': 'application/json; charset=utf-8'}

def writepage(content):
    with open('圣点数据.txt', 'a', encoding="utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

r = requests.get(url, params=payload, headers=headers)
print(r.status_code)
print(r.status_code)
print(r.history)
writepage(r.json())

# 发送一个post 请求
url2 = ''
payload = {}
r1 = requests.post(url2, params=payload, headers=headers)



