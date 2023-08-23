import requests
import os
from flask import Flask

INTERNAL_ENDPOINT=os.environ.get('INTERNAL_ENDPOINT')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "OK"

@app.route('/external', methods=['GET'])
def external():
    x = requests.get('https://ipecho.net/plain')
    return x.text

@app.route('/internal', methods=['GET'])
def internal():
    x = requests.get('http://'+INTERNAL_ENDPOINT)
    return x.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)