import random
import redis
from chapter10.demo2.settings import REDIS_PASSWORD, REDIS_PORT, REDIS_HOST


class RedisClient:
    def __init__(self, user_or_cookie, website, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
        self.user_or_cookie = user_or_cookie
        self.website = website

    def name(self):
        return "{user_or_cookie}:{website}".format(user_or_cookie=self.user_or_cookie, website=self.website)

    def set(self, username, value):
        return self.db.hset(self.name(), username, value)

    def get(self, username):
        return self.db.hget(self.name(), username)

    def delete(self, username):
        return self.db.hdel(self.name(), username)

    def count(self):
        return self.db.hlen(self.name())

    def random(self):
        return random.choice(self.db.hvals(self.name()))

    def usernames(self):
        return self.db.hkeys(self.name())

    def all(self):
        return self.db.hgetall(self.name())
