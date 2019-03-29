from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


# 未知异常统一处理，装饰器，AOP(面向切面编程)
@app.errorhandler(Exception)
def error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        msg = e.description
        code = e.code
        error_code = 1007
        return APIException(msg, code, error_code)
    if isinstance(e, Exception):
        # 调试模式关闭不会打开堆栈信息，开发阶段为了快速定位问题，都打开了调试模式
        # log记录，后续对错误日子分析处理的
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
