# import soup as soup
from fontTools.ttLib import TTFont
import requests
import re
from bs4 import BeautifulSoup as bs

headers = {

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

    "Accept-Encoding": "gzip, deflate, br",

    "Accept-Language": "zh-CN,zh;q=0.8",

    "Cache-Control": "max-age=0",

    "Connection": "keep-alive",

    "Upgrade-Insecure-Requests": "1",

    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"

}


# 这个是爬出整个网页
def body():
    # 这里是抓取网页信息
    font_url = 'http://maoyan.com/cinemas'
    font_content = requests.get(font_url, headers=headers).content
    return font_content.decode('utf-8')


# 这个是爬出字体
def fontfun(html):
    # 这个是读取本地的字体文件
    # 这个文件是对应软件用眼睛查看出来的
    def readdata():
        # 这里是读取第一次我们存储下来的数据
        font1 = TTFont('qidian.woff')
        qidianlist = ['glyph00000', 'x', 'uniF53F', 'uniF5B4', 'uniE549', 'uniE9B7', 'uniF384', 'uniE7FA', 'uniE4E3',
                      'uniF453',
                      'uniE4CC', 'uniF8AF']
        qidiannumber = [' ', '.', '4', '2', '7',
                        '5', '8', '0', '3', '6', '9', '1']
        # 从这里提取出来是一个列表接下来进行比对
        # ['glyph00000', 'x', 'uniF53F', 'uniF5B4', 'uniE549',
        #  'uniE9B7', 'uniF384', 'uniE7FA', 'uniE4E3', 'uniF453', 'uniE4CC', 'uniF8AF']
        font1data = font1['cmap'].tables[0].ttFont.getGlyphOrder()
        # 这里把数据全部提取出来,这样不会重复for循环,节约时间.
        # 这是列表推导式
        font1alldata = [font1['glyf'][x] for x in font1data]
        return font1, qidianlist, qidiannumber, font1data, font1alldata

    font1, qidianlist, qidiannumber, font1data, font1alldata = readdata()
    pattern = re.compile(",\n           url\('(//.*.woff)'\) format\('woff'\)")
    # ([\s\S]*?)
    url = re.findall(pattern, html)
    print('url', url)

    # 问:为什么每次都要进行网址抓取
    # 答:因为每次刷新网页uni码跟数字都会改变
    # font_url = 'http://vfile.meituan.net/colorstone/139b11f6872ff93197a7dab5a60640182080.woff'
    font_url = "http:" + url[0]
    print('font_url', font_url)
    font_content = requests.get(font_url, headers=headers).content
    # 这里保存起来,方便TTFont读取,和等一下进行数据对照
    with open('maoyan.woff', 'wb') as f:
        f.write(font_content)
    font2 = TTFont('maoyan.woff')
    font2data = font2['cmap'].tables[0].ttFont.getGlyphOrder()
    # 这里把数据全部提取出来,这样不会重复for循环,节约时间.
    # 这是列表推导式
    font2alldata = [font2['glyf'][x] for x in font2data]

    # 这里存储数据对应的数字
    font2number = [qidiannumber[font1alldata.index(
        font2alldata[x])] for x in range(2, 12)]
    font2data = [eval('"' + r"\u" + x[3:] + '"').encode('utf-8')
                 for x in font2data[2:]]
    print('font2number', font2number)
    print('font2data', font2data)

    soup = bs(html.encode('utf-8'), "html.parser")
    tag = soup.find_all('span', {'class': 'stonefont'})
    tag = [tag[x].get_text().encode('utf-8') for x in range(len(tag))]

    span = soup.find_all('span', {'class': 'stonefont'})
    span = [span[x].get_text().encode('utf-8') for x in range(len(span))]
    print('span', span)
    # 这里没办法用推导式了~^~
    # span = [span[i].replace(font2data[i], font2number[i]) for i in range(len(font2data))]
    price = []
    for i in range(len(span)):
        value = ''
        for j in range(len(font2number)):
            if font2data[j] == span[i][:3]:
                value += font2number[j]
        for j in range(len(font2number)):
            if font2data[j] == span[i][3:]:
                value += font2number[j]
                # 输出结果为一个列表
        price.append(value)
    print(price)

if __name__ == '__main__':
    html = body()
    fontfun(html)
