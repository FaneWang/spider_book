# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
import sys

sys.path.append('..')
from ..items import UserItem, UserRelationItem, WeiboItem


class WeibocnSpider(scrapy.Spider):
    name = 'weibocn'
    allowed_domains = ['m.weibo.cn']
    user_url = 'https://m.weibo.cn/profile/info?uid={uid}'
    follow_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{followers}&page={page}'
    fan_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{fans}&since_id={since_id}'
    weibo_url = 'https://m.weibo.cn/api/container/getIndex?containerid=230413{containerid}_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page={page}'
    start_users = ['1594052081', '1319911982', '1885688010', '5974585848']

    def start_requests(self):
        for uid in self.start_users:
            yield Request(self.user_url.format(uid=uid), callback=self.parse_user)

    def parse_user(self, response):
        result = json.loads(response.text)
        user_info = result.get('data').get('user')
        user_item = UserItem()
        field_map = {
            'id': 'id', 'name': 'screen_name', 'avatar': 'profile_image_url', 'cover': 'cover_image_phone',
            'gender': 'gender', 'description': 'description', 'fans_count': 'followers_count',
            'follows_count': 'follow_count', 'weibos_count': 'statuses_count', 'verified': 'verified',
            'verified_reason': 'verified_reason', 'verified_type': 'verified_type'
        }
        for field, attr in field_map.items():
            user_item[field] = user_info.get(attr)
        yield user_item

        uid = user_info.get('id')
        yield Request(self.follow_url.format(followers=uid, page=1), callback=self.parse_follows,
                      meta={'page': 1, 'followers': uid})
        yield Request(self.fan_url.format(fans=uid, since_id=1), callback=self.parse_fans,
                      meta={'since_id': 1, 'fans': uid})
        yield Request(self.weibo_url.format(containerid=uid, page=1), callback=self.parse_weibos,
                      meta={'containerid': uid, 'page': 1})

    def parse_follows(self, response):
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards') and len(result.get('data').get('cards')) and \
                result.get('data').get('cards')[-1].get('card_group'):
            follows = result.get('data').get('cards')[-1].get('card_group')
            for follow in follows:
                if follow.get('user'):
                    uid = follow.get('user').get('id')
                    yield Request(self.user_url.format(uid=uid), callback=self.parse_user)
            uid = response.meta.get('uid')
            user_relation_item = UserRelationItem()
            follows = [{'id': follow.get('user').get('id'), 'name': follow.get('user').get('screen_name')} for follow in
                       follows]
            user_relation_item['id'] = uid
            user_relation_item['follows'] = follows
            user_relation_item['fans'] = []
            yield user_relation_item

            page = response.meta.get('page') + 1
            yield Request(self.follow_url.format(followers=uid, page=page), callback=self.parse_follows,
                          meta={'page': page, 'followers': uid})

    def parse_weibos(self, response):
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards'):
            weibos = result.get('data').get('cards')
            for weibo in weibos:
                mblog = weibo.get('mblog')
                if mblog:
                    weibo_item = WeiboItem()
                    field_map = {
                        'id': 'id', 'attitudes_count': 'attitudes_count', 'comments_count': 'comments_count',
                        'reposts_count': 'reposts_count', 'picture': 'original_pic', 'pictures': 'pics',
                        'created_at': 'created_at', 'source': 'source', 'text': 'text', 'raw_text': 'raw_text',
                        'thumbnail': 'thumbnail_pic',
                    }
                    for field, attr in field_map.items():
                        weibo_item[field] = mblog.get(attr)
                    weibo_item['user'] = response.meta.get('containerid')
                    yield weibo_item
            uid = response.meta.get('containerid')
            page = response.meta.get('page') + 1
            yield Request(self.weibo_url.format(containerid=uid, page=page), callback=self.parse_weibos,
                          meta={'containerid': uid, 'page': page})

    def parse_fans(self, response):
        """
        解析用户粉丝
        :param response: Response对象
        """
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards') and len(result.get('data').get('cards')) and \
                result.get('data').get('cards')[-1].get(
                    'card_group'):
            # 解析用户
            fans = result.get('data').get('cards')[-1].get('card_group')
            for fan in fans:
                if fan.get('user'):
                    uid = fan.get('user').get('id')
                    yield Request(self.user_url.format(uid=uid), callback=self.parse_user)

            uid = response.meta.get('fans')
            # 粉丝列表
            user_relation_item = UserRelationItem()
            fans = [{'id': fan.get('user').get('id'), 'name': fan.get('user').get('screen_name')} for fan in
                    fans]
            user_relation_item['id'] = uid
            user_relation_item['fans'] = fans
            user_relation_item['follows'] = []
            yield user_relation_item
            # 下一页粉丝
            page = response.meta.get('since_id') + 1
            yield Request(self.fan_url.format(fans=uid, since_id=page), callback=self.parse_fans,
                          meta={'since_id': page, 'fans': uid})
