import os
from flask import Flask

app = Flask(__name__)


@app.route('/about', methods=['GET'])
def about():
    version = os.environ.get('APP_VERSION')
    return {'version': version}, 200
