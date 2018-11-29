# _*_ coding utf-8 _*_

import requests,re,json,os
from requests.exceptions import RequestException
# from requests.exceptions import RequestException
from multiprocessing import Pool

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

def getpages(url):
	try:
		res = requests.get(url,headers = headers)
		if res.status_code == 200:
			return res.text
		return None
	except RequestException:
		return None
def parsePage(html):
	pattern = re.compile('<img data-ks-lazyload=\"(.*?)\">.*?title="(.*?)">(.*?)</span>',re.S)
	# pattern = re.compile('<span class="title" title="(.*?)">(.*?)</span>',re.S)

	items = re.findall(pattern, html)
	print(items)
	for item in items:
		yield{
			"adressname":item[0],
			"name":item[1],
			"title":item[2],
		}

def createDir(path):
	if not os.path.exists(path):
		os.makedirs(path)
	else:
		os.mkdir(path)
# def saveImg(imagelist,path):
# 	createDir(path)
#     imgIndex = 1
#     for imgurl in imglist:
#        	splist = imgurl.split('.')
#        	filetype = splist[len(splist)-1]
#        	print "saving " + imgurl
#         try:
#             urllib.urlretrieve(imgurl , path + "/"+ str(imgIndex) + '.' + filetype )
#             imgIndex += 1
#             print "==> ok!"
#         except:
#             print "==> err!!!!!!"


def write_to_file(content):
	with open('ces.txt' ,'a' ,encoding="utf-8") as b:
		b.write(json.dumps(content, ensure_ascii = False)+',\n')
		b.close()

def main(offset):
	url = "https://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&keyword=%E5%A5%B3%E8%A3%85&clk1=aac126b3317f3be047668e8189d746b9&upsid=aac126b3317f3be047668e8189d746b9"+str(offset)
	html = getpages(url)
	for item in parsePage(html):
		write_to_file(item)
if __name__ == '__main__':
	p = Pool()
	p.map(main,[i for i in range(1)])