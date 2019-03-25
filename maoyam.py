import urllib.request
import urllib.parse
from lxml import etree
import time
import json

item_list = []

def handle_request(url, page):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
	}
	# 将url和page进行拼接
	url = url.format(page)
	# print(url)
	request = urllib.request.Request(url=url, headers=headers)
	return request

def parse_content(content):
	# print('haha')
	# 生成对象
	tree = etree.HTML(content)
	# 抓取内容
	div_list = tree.xpath('//div[@class="log cate10 auth1"]')
	# 遍历div列表
	for odiv in div_list:
		# print('lala')
		# 获取标题
		title = odiv.xpath('.//h3/a/text()')[0]
		# print(title)
		text_lt = odiv.xpath('.//div[@class="cont"]/p/text()')
		text = '\n'.join(text_lt)
		# print(text)
		# print('*' * 50)
		item = {
			'标题': title,
			'内容': text,
		}
		# 将内容添加到列表中
		item_list.append(item)

def main():
	url = 'http://www.haoduanzi.com/category-10_{}.html'
	for page in range(start_page, end_page + 1):
		request = handle_request(url, page)
		content = urllib.request.urlopen(request).read().decode()
		# 解析内容
		parse_content(content)
		time.sleep(2)

	# 写入到文件中
	# string = json.dumps(item_list, ensure_ascii=False)
	with open('duanzi.txt', 'w', encoding='utf8') as fp:
		fp.write(str(item_list))

if __name__ == '__main__':
	main()