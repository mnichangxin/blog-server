import os, time
from concurrent.futures import ThreadPoolExecutor
from flask import Blueprint, jsonify

hooks = Blueprint('hooks', __name__)

def exec_sh():
    time.sleep(10)
    print(os.popen('cd / && ls').readlines())

@hooks.route('/payload', methods=['POST'])
def payload():
    executor = ThreadPoolExecutor(1)
    executor.submit(exec_sh)
    return jsonify({
        'version': '1.0'
    })