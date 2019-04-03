# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meituan.items import MeituanItem


class MeishiSpider(CrawlSpider):
    name = 'meishi'
    allowed_domains = ['www.meinv.hk']
    start_urls = ['http://www.meinv.hk/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.meinv.hk/\?p=\d+?'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MeituanItem()
        item['name'] = response.xpath('//h1[@class="title"]/text()').get()  # 只提取一个元素
        item['image_urls'] = response.xpath('//div[@class="post-image"]/img/@src').extract()

        return item
