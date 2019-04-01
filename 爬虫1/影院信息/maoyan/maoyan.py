import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from lxml import etree
import json
import time

# http://sou.zhaopin.com/jobs/searchresult.ashx


class maoYanSpider(object):
    # url中不变的内容，要和参数进行拼接组成完整的url
    url = 'https://maoyan.com/cinemas?'

    def __init__(self, start_page, end_page):
        # 将上面的参数都保存为自己的成员属性
        self.start_page = start_page
        self.end_page = end_page
        # 定义一个空列表，用来存放所有的工作信息
        self.items = []

    # 根据page拼接指定的url，然后生成请求对象
    def handle_request(self, page):
        data = {
            'offset': (page - 1) * 12
        }
        url_now = self.url + urllib.parse.urlencode(data)
        # 构建请求对象
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
        request = urllib.request.Request(url=url_now, headers=headers)
        print(url_now)
        return request

    # 解析内容函数
    def parse_content(self, content):
        # 生成对象
        tree = etree.HTML(content)
        # 思路：
        cinema_name = tree.xpath("//div/a[@class='cinema-name']/text()")
        # print(cinema_name)
        cinema_address = tree.xpath("//div/p[@class='cinema-address']/text()")
        # print(cinema_address)
        cinema_url = tree.xpath("//div/a[@class='cinema-name']/@href")
        # print(cinema_url)
        url2 = "https://maoyan.com"
        for name, address, url in zip(cinema_name, cinema_address, cinema_url):
            item = {
                '影院名称': name,
                '影院地址': address,
                '影院网址': url2 + url,
            }
            print(item)
        # 再存放到列表中
        self.items.append(item)

    # 爬取程序
    def run(self):
        # 搞个循环，循环爬取每一页数据
        for page in range(self.start_page, self.end_page + 1):
            print('开始爬取第%s页' % page)
            request = self.handle_request(page)
            # 发送请求，获取内容
            content = urllib.request.urlopen(request).read().decode()
            # 解析内容
            self.parse_content(content)
            print('结束爬取第%s页' % page)
            time.sleep(2)

            # 将列表数据保存到文件中
            string = json.dumps(self.items, ensure_ascii=False)
            with open('maoyan.txt', 'a', encoding='utf8') as fp:
                fp.write(string)


def main():
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))

    # 创建对象，启动爬取程序
    spider = maoYanSpider(start_page, end_page)
    spider.run()

if __name__ == '__main__':
    main()
