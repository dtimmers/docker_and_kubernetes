import os


class RedisConfig:
    host = os.environ['REDIS_HOST']
    port = os.environ['REDIS_PORT']
    hash = 'values'
    channel = 'insert'


class PostgresConfig:

    def __init__(self):
        self.user = os.environ['PGUSER']
        self.host = os.environ['PGHOST']
        self.port = os.environ['PGPORT']
        self.db = os.environ['PGDATABASE']
        self.pw = os.environ['PGPASSWORD']

    def get_url(self) -> str:
        return f'postgresql+psycopg2://{self.user}:{self.pw}@{self.host}/{self.db}'


class ConfigAPI:

    def __init__(self):
        self.postgres = PostgresConfig()
        self.redis = RedisConfig()
        self.url_param_index = 'fib_index'
        self.index_cutoff = 50
