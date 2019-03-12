from app.libs.error import APIException


class ServerError(APIException):
    code = 500
    msg = 'sorry, we make a mistake ~'
    error_code = 999


class ClientTypeError(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    # error_code 告诉客户端，删除成功, rest正常删除返回204，因为204么有内容
    error_code = 1


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not scope'


class DuplicateGift(APIException):
    code = 400
    error_code = 2001
    msg = '重复赠送此书'

