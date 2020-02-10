from flask import Flask, render_template, request, Response
from wtforms import Form, StringField
from wtforms.validators import DataRequired

from api_client import APIClient, APIConfig
from tables import Value, ValueTable, Index, IndexTable

app = Flask(__name__)

api_config = APIConfig()
api_client = APIClient(api_config)


class FibIndexForm(Form):
    fib_index = StringField('Enter Fibonacci index: ', validators=[DataRequired()])

    @app.route('/', methods=['GET'])
    def render_fib_template():
        index_form = FibIndexForm(request.args)

        if index_form.validate():
            api_client.insert_index(request.args)

        values_dict = api_client.get_all_values()
        indices_dict = api_client.get_all_indices()

        return render_template('index.html',
                               table_indices=parse_indices(indices_dict),
                               table_values=parse_values(values_dict),
                               index_form=index_form
                               )


def parse_values(values_dict):
    values = [Value(index, value) for index, value in values_dict['values'].items()]
    values = sorted(values, key=lambda value: int(value.index))

    return ValueTable(values)


def parse_indices(indices_dict):
    indices = [Index(index) for index in sorted(indices_dict['indices'])]

    return IndexTable(indices)