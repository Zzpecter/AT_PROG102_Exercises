from flask import Flask
import redis

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Docker I finally got you lol!'


@app.route('/get/<key>', methods=["GET"])
def get_val(key):
    client = redis.Redis(host='localhost', port=6379)
    return client.get(key)


@app.route('/set/<key>/<value>', methods=["GET", "POST"])
def set_val(key, value):
    client = redis.Redis(host='localhost', port=6379)
    client.set(key, value)
    return 'Done!'



#set_val('1', 'test')
#get_val('1')