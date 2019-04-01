from selenium import webdriver
import time
import os


path = r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

url = 'http://dianying.nuomi.com/cinema?cityId=233'


browser.get(url)
time.sleep(1)

browser.save_screenshot(r'test1.png')

# 让browser执行简单的js代码，模拟滚动滚动到底部
js = 'document.body.scrollTop=10000'
browser.execute_script(js)

time.sleep(1)

browser.save_screenshot(r'test2.png')

for i in range(20):
    button = browser.find_element_by_id('moreCinema')
    button.click()
    time.sleep(1)
    print(i)


browser.save_screenshot(r'ceshi.png')

# 获取网页的代码，保存到文件中
html = browser.page_source
print(html)

with open(r'nuomi.html', 'w', encoding='utf8') as fp:
    fp.write(html)

browser.quit()
