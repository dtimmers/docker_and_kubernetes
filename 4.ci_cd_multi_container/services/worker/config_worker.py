import os


class RedisConfig:
    redis_host = os.environ['REDIS_HOST']
    redis_port = os.environ['REDIS_PORT']
    hash = 'values'
    channel = 'insert'
