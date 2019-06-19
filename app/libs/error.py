from werkzeug.exceptions import HTTPException

class APIException(HTTPException):
    msg = '系统错误'
    code = 500
    err_code = 900

    def __init__(self, msg=msg, code=code, err_code=err_code, headers=None):
        super(APIException, self).__init__(msg, None)
    
    '''
    Custom info return.
    '''
    # def __repr__(self):
    #     return '<APIException>: {}--{}'.format(self.code, self.msg)

    # def __str__(self):
    #     return '<APIException>: {}--{}'.format(self.code, self.msg)

class ServerException(APIException):
    msg = '系统未知错误'
    code = 500
    err_code = 999

    def __init__(self, msg=msg, code=code, err_code=err_code):
        super(ServerException, self).__init__(msg, code, err_code)