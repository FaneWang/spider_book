# 存储模块
REDIS_HOST = '192.168.1.101'
REDIS_PORT = 6379
REDIS_PASSWORD = None
# 生成模块
BROWSER_TYPE = 'Chrome'
# 检测模块
TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/'
}
# 接口模块
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}
# 调度模块
CYCLE = 20
TESTER_MAP = {
    'weibo': 'WeiboValidChecker'
}

GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}

API_HOST = '127.0.0.1'
API_PORT = 6868
API_PROCESS = True
GENERATOR_PROCESS = False
VALID_PROCESS = False
