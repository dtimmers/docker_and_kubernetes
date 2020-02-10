from flask_table import Table, Col


class ValueTable(Table):
    index = Col('Index')
    value = Col('Value')


class Value(object):

    def __init__(self, index, value):
        self.index = index
        self.value = value


class IndexTable(Table):
    index = Col('Index')


class Index(object):

    def __init__(self, index):
        self.index = index
