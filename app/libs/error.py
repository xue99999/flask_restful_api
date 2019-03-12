from flask import json, request
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we make a mistake ~'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if msg:
            self.msg = msg
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            # 'POST v1/client/register' 不要url参数后面的?号
            request=request.method + ' ' + self.get_url_no_param()
        )

        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

