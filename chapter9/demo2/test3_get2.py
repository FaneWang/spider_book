from chapter9.demo2.test1_store import RedisClient
from chapter9.demo2.test2_get1 import Crawler

POOL_UPPER_THRESHOLD = 10000

class Getter:
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                proxies = self.crawler.get_proxy(callback)
                for proxy in proxies:
                    # 将获取的代理添加到redis中，初始分数设置默认值100
                    self.redis.add(proxy)




