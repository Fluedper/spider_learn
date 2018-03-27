import requests
import re
  
def get_one_page(url):
        header = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        response = requests.get(url,headers=header)
        if response.status_code == 200:
                return response.text
        return None

def get_info(html):
        pattern = re.compile(
                '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?</dd>',
                re.S)
        items = re.findall(pattern,html)
        print(items)
def main():
        url = "http://maoyan.com/board/4"
        html = get_one_page(url)
        get_info(html)
main()
