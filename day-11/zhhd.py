import requests
from pyquery import PyQuery as pq


url = "https://www.zhihu.com/explore"
headers = {
	'User-Agent':'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

html = requests.get(url,headers=headers).text

doc = pq(html)

items = doc('.explore-tab .feed-item').items()
for item in items:
	question = item.find('h2').text()
	author = item.find('.author-link-line').text()
	answer = pq(item.find('.content').html()).text()
	file = open('explore-1.txt','a',encoding='utf-8')
	file.write('\n'.join([question,author,answer]))
	file.write('\n'+'='*80 + '\n')
	file.close()

