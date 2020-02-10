import redis

from config_api import RedisConfig


class RedisClient:

    def __init__(self, redis_config: RedisConfig):
        # redis client used to query Redis
        self.client_query = redis.Redis(
            host=redis_config.host,
            port=redis_config.port,
            db=0,
            decode_responses=True
        )
        # redis client used to publish a message to the channel
        self.client_publish = redis.Redis(
            host=redis_config.host,
            port=redis_config.port,
            db=0
        )
        self.name = redis_config.hash
        self.channel = redis_config.channel

    def insert_value(self, key: int, value: int):
        """
        Insert a single key-value pair into the pre-configured hash name
        :param key: the key int
        :param value: the value int
        :return:
        """
        self.client_query.hset(self.name, key, value)

    def get_values(self):
        """
        Get all possible values from redis
        :return: dictionary in the form { <name>: {<key>: <value>}}
        """
        return self.client_query.hgetall(self.name)

    def publish_insert(self, index):
        """
        Publishes the index to Redis such that it can be picked up by a subscribed
        :param index: index to be published
        """
        self.client_publish.publish(self.channel, index)
