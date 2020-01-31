from flask import Flask

app = Flask(__name__)


def get_message():
    """
    :return: the text from the text file services/message.txt
    """

    with open('message.txt', 'r') as file:
        msg = ""
        for line in file:
            msg = msg + line + '</br>'

    return msg


@app.route('/')
def hello_world():
    """
    Reads the text from a file which is assigned as a Docker volume.
    This is a contrived way to make Flask reactive to changes on the local file system.
    :return:
    """
    return get_message()

