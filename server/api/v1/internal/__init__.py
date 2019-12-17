from flask import Blueprint, jsonify
from server.utils.common.redprint import Redprint
from .post import post

internal = Redprint('internal')

post.register(internal)