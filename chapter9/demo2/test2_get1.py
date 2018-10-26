import json
from pyquery import PyQuery as pq
from chapter9.demo2.utils import get_page


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(metaclass=ProxyMetaclass):
    def get_proxy(self, callback):
        proxies = []
        # 获取的代理是一个列表，获取这个列表的回调方法传入format，
        # 通过eval将字符串转化为了一个回调函数返回的列表，
        # 这样做的好处是可以通过这句话调用类中任意的函数，
        # 而不需要更改源代码，只需要传入函数名。这句代码
        # 相当于将字符串里面的内容当成python语句执行了
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili666(self, page_count=4):
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_kuaidaili(self, page_count=4):
        start_url = 'https://www.kuaidaili.com/free/inha/{}/'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('tbody tr').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_xici(self):
        start_url = 'http://www.xicidaili.com/'
        html = get_page(start_url)
        if html:
            doc = pq(html)
            trs = doc('tr.odd').items()
            for tr in trs:
                ip = tr.find('td:nth-child(2)').text()
                port = tr.find('td:nth-child(3)').text()
                yield ':'.join([ip, port])
