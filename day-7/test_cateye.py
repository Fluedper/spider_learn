import requests

header = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
response = requests.get("http://maoyan.com/board/4",headers=header)

print(response.text)
