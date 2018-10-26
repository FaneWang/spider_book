import aiohttp
from aiohttp import ClientError
from aiohttp import ClientProxyConnectionError
import asyncio


async def test_proxy(proxy):
    conn = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            real_proxy = "https://" + proxy
            async with session.get('https://www.baidu.com', proxy=real_proxy, timeout=15) as response:
                if response.status == 200:
                    print('代理测试成功')
                else:
                    print('代理测试失败')
        except(ClientError, ClientProxyConnectionError):
            print('代理请求失败')


async def test_proxy_1(proxy):
    conn = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            real_proxy = 'http://' + proxy
            async with session.get('https://www.baidu.com', proxy=real_proxy, timeout=15) as response:
                if response.status == 200:
                    print('代理测试成功')
                else:
                    print('代理测试失败')
        except(ClientError, ClientProxyConnectionError):
            print('代理请求失败')


def run():
    try:
        loop = asyncio.get_event_loop()
        tasks = [test_proxy_1('125.70.13.77:8080')]
        loop.run_until_complete(asyncio.wait(tasks))
    except Exception as e:
        print('测试失败：' + e.args)


if __name__ == "__main__":
    run()
