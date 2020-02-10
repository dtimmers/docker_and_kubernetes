import threading

import redis

from config_worker import RedisConfig


class Listener(threading.Thread):

    def __init__(self, redis_config: RedisConfig):
        super(Listener, self).__init__()
        # Redis client for inserting new Fibonacci values
        self.client_query = redis.Redis(
            host=redis_config.redis_host,
            port=redis_config.redis_port,
            socket_keepalive=True,
            retry_on_timeout=True,
            db=0)

        # Redis client for listening to new inserts
        redis_subscribe = redis.Redis(
            host=redis_config.redis_host,
            port=redis_config.redis_port,
            socket_keepalive=True,
            retry_on_timeout=True,
            db=0)
        self.client_subscribe = redis_subscribe.pubsub()
        self.client_subscribe.subscribe(redis_config.channel)
        self.name = redis_config.hash

    def run(self):
        for message in self.client_subscribe.listen():
            try:
                if message['type'] == 'message':
                    index_fib = int(message['data'])
                    value = fibonacci(index_fib)
                    print(f'computed Fibonacci number {index_fib}: {value}')
                    self.client_query.hset(self.name, key=index_fib, value=value)
                    print('inserted Fibonacci into Redis.')
            except Exception as e:
                print(f'Failed to write to redis with error {e}')


def fibonacci(index: int):
    if index < 2:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)


if __name__ == '__main__':
    redis_config = RedisConfig()
    listener = Listener(redis_config)
    listener.start()
