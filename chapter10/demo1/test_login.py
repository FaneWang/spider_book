import requests
from lxml import etree


class Login:
    def __init__(self):
        self.headers = {
            'Referrer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Host': 'github.com'
        }

        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        res = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(res.text)
        token = selector.xpath('//div/form/input[2]/@value')[0]
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }

        # res = self.session.post(self.post_url, data=post_data, headers=self.headers)
        # if res.status_code == 200:
        #     self.dynamics(res.text)

        res = self.session.get(self.logined_url, headers=self.headers)
        if res.status_code == 200:
            self.profile(res.text)

    # def dynamics(self, html):
    #     selector = etree.HTML(html)
    #     dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
    #     for item in dynamics:
    #         dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
    #         print(dynamic)

    def profile(self, html):
        # selector = etree.HTML(html)
        # # name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        # email = selector.xpath('//span[@class="css-truncate-target"]/text()')
        print(html)


if __name__ == "__main__":
    login = Login()
    login.login(email='2079409377@qq.com', password='password')
