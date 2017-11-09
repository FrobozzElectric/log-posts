#!/usr/bin/env python3

import os
import time
import argparse
from flask import abort, Flask, json, request

app = Flask(__name__)
parser = argparse.ArgumentParser()
parser.add_argument('--log-dir')
parser.add_argument('--url-base')
args = parser.parse_args()

log_dir = args.log_dir
url_base = args.url_base


def json_test(data):
    try:
        json.loads(data)
        return True
    except:
        return False

def write_log(data, extension='.txt'):
    timestamp = time.strftime('%Y-%m-%d_%H:%M:%S')
    filename = timestamp + extension
    log_file = log_dir + filename
    with open(log_file, 'w') as log:
        log.write(str(data))
    return url_base + filename


@app.route('/post', methods=['POST'])
def log_post():
    if json_test(request.get_data()):
        data = json.dumps(request.get_json(force=True), indent=4)
        return write_log(data, '.json')
    else:
        data = request.get_data().decode('utf-8')
        return write_log(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True, threaded=True)
