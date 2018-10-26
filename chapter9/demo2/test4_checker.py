from chapter9.demo2.test1_store import RedisClient
import aiohttp

try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError
from aiohttp.client_exceptions import ClientConnectionError
import asyncio
import time
from chapter9.demo2.settings import VALID_STATUS_CODES, TEST_URL, BATCH_TEST_SIZE


class Checker:
    def __init__(self):
        self.redis = RedisClient()

    async def test_proxy(self, proxy):
        conn = aiohttp.TCPConnector(ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print('正在测试' + proxy)
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as res:
                    if res.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        print("代理可用", proxy)
                    else:
                        self.redis.decrease(proxy)
                        print("响应码不合法", proxy)
            except (ClientError, ClientConnectionError, asyncio.TimeoutError, AttributeError):
                self.redis.decrease(proxy)
                print("代理请求失败", proxy)

    def run(self):
        print('测试开始')
        try:
            count = self.redis.count()
            print('当前剩余', count, '个代理')
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                stop = min(i + BATCH_TEST_SIZE, count)
                print('正在测试第', start + 1, '-', stop, '个代理')
                test_proxies = self.redis.batch(start, stop)
                loop = asyncio.get_event_loop()
                tasks = [self.test_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误', e.args)

    # def run(self):
    #     print("测试开始")
    #     try:
    #         proxies = self.redis.all()
    #         loop = asyncio.get_event_loop()
    #         for i in range(0, len(proxies), BATCH_TEST_SIZE):
    #             test_proxies = proxies[i:i + BATCH_TEST_SIZE]
    #             tasks = [self.test_proxy(proxy) for proxy in test_proxies]
    #             loop.run_until_complete(tasks)
    #             time.sleep(5)
    #     except Exception as e:
    #         print('测试器发生错误')
    #         print(e)
