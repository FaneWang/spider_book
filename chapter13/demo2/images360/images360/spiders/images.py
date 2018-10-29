# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import urlencode
import json
import sys

sys.path.append('..')
from ..items import Images360Item


class ImagesSpider(Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = Images360Item()
            item['id'] = image.get('imageid')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item

    def start_requests(self):
        data = {'ch': 'beauty', 'listtype': 'new'}
        bash_url = 'http://images.so.com/zj?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            print('参数：' + params)
            url = bash_url + params
            yield Request(url, self.parse)
