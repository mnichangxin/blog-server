class Error(Exception):
    def __init__(self, message, errcode=500, detail=None, msg_en=None):
        self.message = message
        self.errcode = errcode
        self.detail = detail
        self.msg_en = msg_en
    
    def __repr__(self):
        return '{}--{}'.format(self.message, self.detail)

    def __str__(self):
        return '{}--{}'.format(self.message, self.detail)
