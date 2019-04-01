from selenium import webdriver
import time
import os


path = r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

url = 'https://dianying.taobao.com/cinemaList.htm?spm=a1z21.6646277.city.287.5eaf51f1Mwrh51&n_s=new&city=610100'


browser.get(url)
time.sleep(1)
# browser.save_screenshot(r'ceshi.png'))

browser.save_screenshot(r'test1.png')

# 让browser执行简单的js代码，模拟滚动滚动到底部
js = 'document.body.scrollTop=10000'
browser.execute_script(js)

time.sleep(1)

browser.save_screenshot(r'test2.png')

for i in range(11):
    button = browser.find_element_by_class_name('sortbar-more')
    button.click()
    time.sleep(1)


browser.save_screenshot(r'ceshi.png')

# 获取网页的代码，保存到文件中
html = browser.page_source
print(html)

with open(r'tppyuanma.html', 'w', encoding='utf8') as fp:
    fp.write(html)

browser.quit()
