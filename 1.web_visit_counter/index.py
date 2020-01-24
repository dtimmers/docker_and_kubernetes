from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.Redis(host='redis-server', port=6379, db=0)
redis_key = 'num_visit'
redis_client.set(redis_key, 0)


def retrieve_num_visit():
    """
    Return the number of visits by first querying Redis.
    If successful, it returns the number stored in Redis otherwise it will return 0.
    :return:
    """
    num_visit_redis = redis_client.get(redis_key)
    if num_visit_redis is None:
        return 0
    else:
        return int(num_visit_redis)


@app.route('/')
def hello_world():
    # we don't consider failures but hey it's a docker/kubernetes course
    num_visit = retrieve_num_visit() + 1
    redis_client.set(redis_key, num_visit)
    return f'Number of visits: {num_visit}'
