from selenium import webdriver
import time
import os
from lxml import etree
import json

path = r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

url = "https://movie.douban.com/cinema/nowplaying/xian/"

browser.get(url)
time.sleep(1)

browser.save_screenshot(r'home.png')

button = browser.find_element_by_class_name('more')
button.click()
time.sleep(2)
browser.save_screenshot(r'test1.png')

html = browser.page_source
with open(r'yuanxian.html', 'w', encoding='utf-8') as fp:
    fp.write(html)

browser.quit()

# 解析保存好的html文件
parser = etree.HTMLParser(encoding='utf-8')
page = etree.parse('yuanxian.html', parser=parser)

movie_name = page.xpath(
    "//div[@id='nowplaying']/div/ul[@class='lists']/li/ul/li/a/@title")
movie_parse = page.xpath(
    "//div[@id='nowplaying']/div/ul[@class='lists']/li/@data-score")
movie_img = page.xpath(
    "//div[@id='nowplaying']/div/ul[@class='lists']/li/ul/li/a/img/@src")
items = []
for name, parse, img in zip(movie_name, movie_parse, movie_img):
    print(name)
    print(parse)
    print(img)
    item = {
        '电影名称': name,
        '电影评分': parse,
        '电影图片': img,
    }
    print(item)
    items.append(item)

    string = json.dumps(items, ensure_ascii=False)
    with open('yuanxian.txt', 'a', encoding='utf-8') as fp:
        fp.write(string)
