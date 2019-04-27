import os, time
from concurrent.futures import ThreadPoolExecutor
from flask import Blueprint, request, jsonify

hooks = Blueprint('hooks', __name__)

def exec_sh():
    time.sleep(10)
    print(os.popen('cd / && ls').readlines())

@hooks.route('/payload', methods=['POST'])
def payload():
    print(request.get_json())
    # executor = ThreadPoolExecutor(1)
    # executor.submit(exec_sh)
    return jsonify({
        'version': '1.0'
    })