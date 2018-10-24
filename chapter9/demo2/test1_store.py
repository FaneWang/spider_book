MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = '192.168.1.101'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxy'

import redis
from random import choice

class RedisClient:
    