from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError


# 为了让flask jsonify支持序列化模型而设计的
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, '__getitem__') and hasattr(o, 'keys'):
            # __dict__ 不能返回类变量，只能返回实例变量
            return dict(o)
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder


