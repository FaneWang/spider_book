import json
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from chapter10.demo2.test1_store import RedisClient
from chapter10.demo2.settings import BROWSER_TYPE


class CookiesGenerator:
    def __init__(self, website='default'):
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)
        self.init_browser()

    def __del__(self):
        self.close()

    def init_browser(self):
        if BROWSER_TYPE == 'PhantomJS':
            caps = DesiredCapabilities.PHANTOMJS
            caps[
                'phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
            self.browser = webdriver.PhantomJS(desired_capabilities=caps)
            self.browser.set_window_size(1400, 500)
        elif BROWSER_TYPE == 'Chrome':
            self.browser = webdriver.Chrome()

    def new_cookies(self, username, password):
        raise NotImplementedError

    def process_cookies(self, cookies):
        # cookie的结构
        # [{'domain': '.baidu.com', 'httpOnly': False, 'name': 'H_PS_PSSID', 'path': '/', 'secure': False, 'value': '26524_1446_21096_18559_27401_26350'},
        # {'domain': '.baidu.com', 'httpOnly': False, 'name': 'delPer', 'path': '/', 'secure': False, 'value': '0'}]
        dict_cookies = {}
        for cookie in cookies:
            dict_cookies[cookie['name']] = cookie['value']
        return dict_cookies

    def run(self):
        accounts_usernames = self.accounts_db.usernames()
        cookies_usernames = self.cookies_db.usernames()
        for username in accounts_usernames:
            if not username in cookies_usernames:
                password = self.accounts_db.get(username)
                print('正在生成Cookies', '账号', username, '密码', password)
                result = self.new_cookies(username, password)

                if result.get('status') == 1:
                    cookies = self.process_cookies(result.get('content'))
                    print('成功获取到Cookies', cookies)
                    if self.cookies_db.set(username, json.dumps(cookies)):
                        print('成功保存Cookies')
                elif result.get('status') == 2:
                    print(result.get('content'))
                    if self.accounts_db.delete(username):
                        print('成功删除账号')
                else:
                    print(result.get('content'))
            else:
                print('所有账号都已经成功获取Cookies')

    def close(self):
        try:
            print('Closing Browser')
            self.browser.close()
            del self.browser
        except TypeError:
            print('Browser not opened')


class WeiboCookiesGenerator(CookiesGenerator):
    def __init__(self, website='weibo'):
        CookiesGenerator.__init__(self, website)
        self.website = website

    def new_cookies(self, username, password):
        pass
