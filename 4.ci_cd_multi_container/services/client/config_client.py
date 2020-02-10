import os


class RedisConfig:
    host = os.environ['REDIS_HOST']
    port = os.environ['REDIS_PORT']


class PostgresConfig:
    user = os.environ['PGUSER']
    host = os.environ['PGHOST']
    port = os.environ['PGPORT']
    database = os.environ['PGDATABASE']
    password = os.environ['PGPASSWORD']
