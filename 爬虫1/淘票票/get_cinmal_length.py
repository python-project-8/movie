import random
import time

import requests
from fake_useragent import UserAgent
from lxml import etree
from threading import Thread
from 淘票票.get_cities import TaoPP

class GetPageLen(object):

    UA = UserAgent()
    def __init__(self):

        self.url = "https://dianying.taobao.com/cinemaList.htm?n_s=new&city={}"
        self.headers = {
            'User-Agent': self.UA.random,
        }
    def get_response(self, city_code):
        request_url = self.url.format(city_code)
        r = requests.get(url=request_url, headers=self.headers)
        return r

    def get_page_len(self, city_code, city_name):
        tree = etree.HTML(self.get_response(city_code=city_code).text)
        page_length_str = tree.xpath("/html/body/div[4]/div[1]/div[2]/@data-param")

        if page_length_str:
            page_length = page_length_str[0].split("&")[4].split("=")[1]
            print("%s有%s页影院"%(city_name, page_length))
            return page_length
        else:
            page_length = 1
            print("%s只有1页影院"%city_name)
            return page_length

def run():
    page_length_list = []
    t = TaoPP()
    g = GetPageLen()
    cities = t.city_list()
    for city in cities:
        city_code = city["城市编码"]
        city_name = city["城市名称"]
        page_length = g.get_page_len(city_code, city_name)
        time.sleep(random.uniform(0,1))
        page_length_list.append(page_length)
    return page_length_list


