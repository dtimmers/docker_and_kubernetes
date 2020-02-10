import time

from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

from config_api import ConfigAPI
from redis_client import RedisClient

app = Flask(__name__)
config = ConfigAPI()

# add the postgres database
app.config['SQLALCHEMY_DATABASE_URI'] = config.postgres.get_url()
# silence the deprecation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import FibonacciIndex

# hacky way to solve problem that postgres is not running yet
database_ready = False
while not database_ready:
    try:
        db.create_all()
        db.session.commit()
        database_ready = True
    except OperationalError:
        time.sleep(1)

redis_client = RedisClient(config.redis)


@app.route('/')
def default():
    return "hi, there"


@app.route('/indices/insert', methods=['GET'])
def insert_index():
    index_fib = request.args.get(config.url_param_index)

    if index_fib is None:
        response = Response(
            'Missing required URL parameter "fib_index"',
            status=400,
            mimetype='application/json')
    else:
        try:
            index_fib = int(index_fib)
            if index_fib <= config.index_cutoff:
                try:
                    index_fib_db = FibonacciIndex(index=index_fib)
                    db.session.add(index_fib_db)
                    db.session.commit()
                    # insert index with a None value such that it can be picked up by the worker
                    redis_client.insert_value(key=index_fib, value='NA')
                    redis_client.publish_insert(index=index_fib)
                    response = {'index': index_fib}
                except Exception as e:
                    response = Response(
                        str(e),
                        status=400,
                        mimetype='application/json'
                    )
            else:
                response = Response(
                    f'The index can be at most {config.index_cutoff}',
                    status=400,
                    mimetype='application/json'
                )

        except ValueError:
            response = Response(
                'The URL parameter "fib_index" has to be integer-valued',
                status=400,
                mimetype='application/json')

    return response


@app.route('/indices/all', methods=['GET'])
def get_all_indices():
    """
    Endpoint /indices/all returns all possible indices stored in the SQL database
    :return: json object with a single key 'indices' which returns a list of all possible indices
    """
    try:
        indices = [fib_index.index for fib_index in FibonacciIndex.query.all()]
        response = {'indices': sorted(indices)}
    except Exception as e:
        response = Response(
            str(e),
            status=400,
            mimetype='application/json'
        )

    return response


@app.route('/values/all', methods=['GET'])
def get_all_values():
    """
    Endpoint /values/all returns all possible indices and their Fibonacci number that are stored in Redis
    :return: json object with a single key 'indices' which returns a list of all possible indices
    """
    try:
        values = redis_client.get_values()
        response = {'values': values}
    except Exception as e:
        response = Response(
            str(e),
            status=400,
            mimetype='application/json'
        )

    return response
