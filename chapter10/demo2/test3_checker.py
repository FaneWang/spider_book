import json
import requests
from requests.exceptions import ConnectionError
from chapter10.demo2.test1_store import RedisClient
from chapter10.demo2.settings import TEST_URL_MAP


class ValidChecker:
    def __init__(self, website='default'):
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)

    def check(self, username, cookies):
        raise NotImplementedError

    def run(self):
        cookies_groups = self.cookies_db.all()
        for username, cookies in cookies_groups.items():
            self.check(username, cookies)


class WeiboValidChecker(ValidChecker):
    def __init__(self, website='weibo'):
        ValidChecker.__init__(self, website)

    def check(self, username, cookies):
        print('正在测试Cookies', '用户名', username)
        try:
            cookies = json.loads(cookies)
        except TypeError:
            print('Cookies不合法', username)
            self.cookies_db.delete(username)
            print('删除Cookies', username)
            return
        try:
            test_url = TEST_URL_MAP[self.website]
            res = requests.get(test_url, cookies=cookies, timeout=5, allow_redirects=False)
            if res.status_code == 200:
                print('Cookies有效', username)
            else:
                print(res.status_code, res.headers)
                print('Cookies失效', username)
                self.cookies_db.delete(username)
                print('删除Cookies', username)
        except ConnectionError as e:
            print('发生异常', e.args)
