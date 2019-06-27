from werkzeug.exceptions import HTTPException

class APIException(HTTPException):
    def __init__(self, msg='客户端错误', code=400, err_code=900, headers=None):
        self.msg = msg
        self.code = code
        self.err_code = err_code
        super(APIException, self).__init__(msg, None)
    
    '''
    Custom info return.
    '''
    # def __repr__(self):
    #     return '<APIException>: {}--{}'.format(self.code, self.msg)

    # def __str__(self):
    #     return '<APIException>: {}--{}'.format(self.code, self.msg)

class ServerException(APIException):
    def __init__(self, msg='服务端错误', code=500, err_code=999):
        self.msg = msg
        self.code = code
        self.err_code = err_code
        super(ServerException, self).__init__(msg, code, err_code, None)