import csv
import os
import pandas as pd

import requests
from lxml import etree
from fake_useragent import UserAgent
from 淘票票.get_cities import TaoPP
from 淘票票.get_cinmal_length import *

class TaoPPCinemal(object):
    UA = UserAgent()

    def __init__(self):
        self.url2 = "https://dianying.taobao.com/ajaxCinemaList.htm?page={}&regionName=&cinemaName=&pageSize=10&pageLength={}&sortType=0&n_s=new&city={}"
        self.headers = {
            'User-Agent': self.UA.random,
        }

    def get_response(self, page_length, city_code):
        result_list = []
        for page in range(1, page_length+1):
            request_url = self.url2.format(page, page_length, city_code)
            r = requests.get(url=request_url, headers=self.headers)
            result_list.append(r.text)
        return result_list

    def get_msg_save(self, page_length, city_code):

        if not os.path.exists('cinmal_href.csv'):
            f = open('cinmal_href.csv', 'w')
            f.close()
        with open('cinmal_href.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['电影院名称', '电影院地址', '电影院电话', '电影院链接'])
            for r in self.get_response(page_length, city_code):
                try:
                    tree = etree.HTML(r)
                    city_cinema_name = tree.xpath("//li//h4/a/text()")
                    city_cinema_address = tree.xpath("//li/div[2]/div[2]/div/span/text()")
                    city_cinema_phone = tree.xpath("//li/div[2]/div[2]/div[2]/text()")
                    city_cinema_href = tree.xpath("//li//h4/a/@href")
                    for i in range(len(city_cinema_href)):
                        writer.writerow([city_cinema_name[i],
                                         city_cinema_address[i],
                                         city_cinema_phone[i],
                                         city_cinema_href[i]])
                    print("写入完成")
                except Exception as e:
                    print('有错')

                # 方法2
                # dataframe = pd.DataFrame({'电影院名称': city_cinema_name,
                #                           '电影院地址': city_cinema_address,
                #                           '电影院电话': city_cinema_phone,
                #                           '电影院链接': city_cinema_href, })
                # dataframe.to_csv('cinmal_href.csv',sep=',', index=False, mode='a')
                # print('写入完成')




