from flask import current_app
from werkzeug.exceptions import HTTPException
from .error import APIException, ServerException

@current_app.errorhandler(Exception)
def handle_error(e):
    current_app.logger.info('<Exception logger>: {}'.format(e))
    if isinstance(e, APIException):
        return e
    elif isinstance(e, HTTPException):
        return APIException(e.code, e.description, 1007)
    else:
        return ServerException()