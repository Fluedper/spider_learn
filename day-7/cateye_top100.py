import requests
from requests.exceptions import RequestException
import re
import json
import time


def get_one_page(url):
	try:
		header = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
		}
		response = requests.get(url,headers=header)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def get_info(html):
        pattern = re.compile(
                '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?</dd>',
                re.S)
        items = re.findall(pattern,html)
        for item in items:
                yield{
                        'rank':item[0],
			'img':item[1],
			'name':item[2]
		}	
		
def write_to_file(content):
	with open('cateyetop100.txt','a',encoding='utf-8') as f:
		f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
	url = "http://maoyan.com/board/4?offset=" + str(offset)
	html = get_one_page(url)
	for item in get_info(html):
		print(item)
		write_to_file(item)
	
if __name__ == '__main__':
	for i in range(10):
		main(offset=i * 10)
		time.sleep(1)
