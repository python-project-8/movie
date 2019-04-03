# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import os
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from meituan import settings


class MeituanPipeline(object):
    def process_item(self, item, spider):
        # 保存数据

        return item


class MvPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for img_url in item.get('image_urls'):

            # 将美女的name加入到info
            yield Request(img_url,
                          meta={'name': item.get('name')})

    def file_path(self, request, response=None, info=None):

        name = request.meta.get('name')  # 每一位的图片放在它自己的目录中

        mv_dir = os.path.join(settings.IMAGES_STORE, name)
        if not os.path.exists(mv_dir):
            os.mkdir(mv_dir)
            print('---->')

        url_filename = request.url.split('/')[-1]
        ext_name = os.path.splitext(url_filename)[-1]  # .jpg

        # 通过md5签名， 将文件名转成32位的md5编码格式
        md5_ = hashlib.md5()
        md5_.update(url_filename.encode())
        filename = md5_.hexdigest() + ext_name
        print('>>>'*10, name, filename)

        # 相对settings.IMAGES_STORE的子目录
        return '%s/%s' (name, filename)

    def item_completed(self, results, item, info):
        print('---item_completed-----')
        print(results)
        return item