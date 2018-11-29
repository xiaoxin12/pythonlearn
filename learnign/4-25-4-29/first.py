# -*- coding: utf-8 -*-

import requests, re, json
from requests.exceptions import RequestException
from multiprocessing import Pool

# 如果下次不能够爬取东西了记得查看是不是这里除了问题了
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

def get_one_page(url):

	try:
		res = requests.get(url, headers=headers)
		print(res)
		if res.status_code == 200:
			return res.text
		print('顺利今人这里',res.status_code)
		return None
	except RequestException:
		return None

def parse_one_page(html):
	pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
	items = re.findall(pattern , html)
	for item in items:
		yield{
			"index":item[0],
			"image":item[1],
			"title": item[2],
			"actor": item[3].strip()[3:],
			"time": item[4].strip()[4:],
			"score": item[5]+item[6]
		}


def write_to_file(content):
	with open('result.txt', 'a', encoding="utf-8") as f:
		f.write(json.dumps(content, ensure_ascii=False) + '\n' )
		f.close()

def main(offest):
	url = "http://maoyan.com/board/4?offset=" + str(offest)

	html = get_one_page(url)
	for item in parse_one_page(html):
		print(item)
		write_to_file(item)

if __name__ == '__main__':
	p = Pool()
	p.map(main,[i*10 for i in range(10)])