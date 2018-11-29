# -*- coding: utf-8 -*-

import requests, re, json
from requests.exceptions import RequestException
from multiprocessing import Pool


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

def get_one_page(url):

	try:
		res = requests.get(url, headers=headers)
		if res.status_code == 200:
			return res.text
		return None
	except RequestException:
		return None

def parse_one_page(html):

	pattern2 = re.compile('<div class="cinema-info.*?<a href="(.*?)" class="cinema-name".*?}">(.*?)</a>.*?cinema-address">地址：(.*?)</p>.*?', re.S)
	items2 = re.findall(pattern2, html)
	print('相关数据匹配完成')
	for item in items2:
		yield {
			"影院名称": item[1],
			"跳转地址": item[0],
			"影院地址": item[2]

		}

def write_to_file(content):
	print('文件正在写入中，请稍等。。。')
	with open('电影院地址.txt', 'a', encoding="utf-8") as f:
		f.write(json.dumps(content, ensure_ascii=False) + '\n')
		f.close()

def main(offest):
	url = "http://maoyan.com/cinemas?brandId=102642"
	html = get_one_page(url)

	for item in parse_one_page(html):
		write_to_file(item)
	print('文件正在写入完成')

if __name__ == '__main__':
	p = Pool()
	p.map(main,[i*10 for i in range(1)])