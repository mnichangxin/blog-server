# from flask import jsonify
# from server.utils.common.redprint import Redprint
# # from server.api.v1.internal import internal
# # from server.api.v1.view import view

# from ...api import api

# api_v1 = Redprint(api, '/v1')

# # internal.register(api_v1)
# # view.register(api_v1)

# @api_v1.route('/')
# def api_v1_index():
#     return jsonify({
#         'version': '1.0'
#     })