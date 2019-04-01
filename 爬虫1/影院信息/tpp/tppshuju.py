from lxml import etree
import json

# 创建自定义解析器
parser = etree.HTMLParser(encoding="utf-8")
page = etree.parse('tppyuanma.html', parser=parser)

cinema_name = page.xpath(
    "//div[@class='middle-hd']/h4/a/text()")
cinema_add = page.xpath(
    "//div[@class='middle-p-list'][1]/span/text()")
cinema_url = page.xpath(
    "//div[@class='middle-hd']/h4/a/@href")
print(len(cinema_name))
print(len(cinema_add))
print(len(cinema_url))
items = []
for name, add, url in zip(cinema_name, cinema_add, cinema_url):
    item = {
        '影院名称': name,
        '影院地址': add,
        '影院网址': url,
    }
    # print(len(item))
    items.append(item)
    # print(len(items))

    string = json.dumps(items, ensure_ascii=False)
    with open('tppshuju.txt', 'a', encoding='utf8') as fp:
        fp.write(string)

# # for name,add,url in zip(cinema_name,cinema_addm,cinema_url):

# print(len(cinema_name))
