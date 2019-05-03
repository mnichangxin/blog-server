from werkzeug.exceptions import HTTPException

class APIException(HTTPException):
    msg = 'make a mistake'
    code = 500
    err_code = 900

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if msg:
            self.msg = msg
        if code:
            self.code = code
        if error_code:
            self.err_code = error_code
        super(APIException, self).__init__(msg, None)
    
    '''
    Custom info return.
    '''
    # def __repr__(self):
    #     return '<APIException>: {}--{}'.format(self.code, self.msg)

    # def __str__(self):
    #     return '<APIException>: {}--{}'.format(self.code, self.msg)

class ServerException(APIException):
    msg = 'make a mistake'
    code = 500
    err_code = 999