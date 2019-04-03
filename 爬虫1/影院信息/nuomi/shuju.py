from lxml import etree
import json

# 创建自定义解析器
parser = etree.HTMLParser(encoding="utf-8")
page = etree.parse('nuomi.html', parser=parser)

cinema_name = page.xpath(
    "//div[@id='cinemaCinemalist']/ul//span[@class='name']/text()")
cinema_add = page.xpath(
    "//div[@id='cinemaCinemalist']/ul//span[@class='fl text']/text()")
cinema_url = page.xpath(
    "//div[@class='btns fr single']/p[@class='clearfix']/a/@data-data")
url2 = "http://dianying.nuomi.com/cinema/cinemadetail?cityId=233&"
items = []
for name, add, url in zip(cinema_name, cinema_add, cinema_url):
    a = (url[2:10] + '=')
    b = (url[12:-1])
    url_now = url2 + a + b
    # print(name)
    # print(add)
    # print(url)
    item = {
        'nm_name': name,
        'nm_add': add,
        'nm_url': url_now,
    }
    print(item)
    items.append(item)

    string = json.dumps(items, ensure_ascii=False)
    with open('nuomi.txt', 'a', encoding='utf8') as fp:
        fp.write(string)

# for name,add,url in zip(cinema_name,cinema_addm,cinema_url):

print(len(cinema_name))
