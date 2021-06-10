import logging
from datetime import datetime
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.debug(debug_log('/'))
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.debug(debug_log('/status'))
    return jsonify({'result': 'OK - healthy'})

@app.route("/metrics")
def metrics():
    app.logger.debug(debug_log('/metrics'))
    return jsonify({'data': {'UserCount': 140, 'UserCountActive': 23}})

def debug_log(endpoint):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return '{0}, {1} endpoint was reached'.format(date_time, endpoint)

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
