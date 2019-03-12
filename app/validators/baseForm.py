from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

# 重写父类方法有2种:
# 第一种新建Base类，覆盖原有方法
# 第二种是新建Base类，重新写一个新的方法


class BaseForm(Form):
    def __init__(self):
        # 所有的表单数据在这里统一拿，调用起来非常方便
        data = request.get_json(silent=True)
        # 注意args字典的传递方式 **args
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate(self):
        pass

    def validate_for_api(self):
        # 调用父类的验证方法
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
