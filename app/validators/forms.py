from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, length, ValidationError

from app.libs.enums import ClientTypeEnum

from app.validators.baseForm import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[
        DataRequired(message='不允许为空'),
        Length(min=5, max=32)
    ])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    # 校验type字段, 如果存在，转化成枚举类型
    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):

    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    def validate_account(self, value):
        from app.models.user import User
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()


class BookSearchForm(Form):
    q = StringField(validators=[DataRequired()])


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])


# todolist 创建的表单
class ThingForm(Form):
    content = StringField(validators=[DataRequired()])


# todolist 更新的表单
class ThingUpdateForm(Form):
    content = StringField()
    complete_status = StringField(validators=[Length(min=2, max=2)])
