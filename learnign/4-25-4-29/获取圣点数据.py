# -*- coding: utf-8 -*-

import requests, json
# url = "http://192.168.31.98:8040/access/records"
# payload = {
#     'len': 50,
#     'active': 1
# }
# headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJhZG1pbiIsImF0dGVuZGFuY2UiOiJhZG1pbiIsImNvcmUiOiJhZG1pbiIsImVudGVycHJpc2UiOiJhZG1pbiIsImV4YW0iOiJhZG1pbiIsImV4cCI6MTU0MzY2NjA1MywiaWQiOiI5NDU1ZDUwZC1mODFhLTExZTYtOTliMS0wMjQyYWMxMzAwMGUiLCJvcmlnX2lhdCI6MTU0MzQwNjg1MywicGF5bWVudCI6ImFkbWluIiwicmVtb3Rlc2l0ZSI6ImFkbWluIiwidmlzaXRvciI6ImFkbWluIn0.64UTweZEwbCRJBz_RwgqajM2pR13ZYP4pNNXpx7byJ0','Content-Type': 'application/json; charset=utf-8'}
#
# def writepage(content):
#     with open('圣点数据.txt', 'a', encoding="utf-8") as f:
#         f.write(json.dumps(content, ensure_ascii=False) + '\n')
#         f.close()
#
# r = requests.get(url, params=payload, headers=headers)
# print(r.status_code)
# print(r.history)
# writepage(r.json())

# # 发送一个post 请求
# url2 = 'http://192.168.35.52:9000/op/accounts'
headers2 = {'X-Access-Token': 'c08a674c20c744f48fa790b5ba018f97',
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
            }
#
# payload2 = {'name': 'sqqtest', 'password': '12345678', 'company_name': '这是一条测试的数据', 'sign_years': 2}
# r1 = requests.post(url2, data=json.dumps(payload2), headers=headers2)
# print(r1.status_code)
# print(r1.text)
# print(r1.headers)
# print(r1.json())

url3 = 'http://192.168.35.52:9000/op/operators?page=1&page_size=20'

r3 = requests.get(url3, headers=headers2)
print(r3.status_code)
print(r3.text)
print(r3.headers['X-Total-Count'])



