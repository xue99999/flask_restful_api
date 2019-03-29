from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AuthFailed
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, TokenForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    # form.type.data 已经转化为枚举类型了
    identity = promise[form.type.data](
        form.account.data,
        form.secret.data
    )
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'], expiration)

    t = {
        'error_code': 0,
        'msg': 'ok',
        'data': {
            'token': token.decode('ascii')
        }
    }
    return jsonify(t), 201


@api.route('/secret', methods=['POST'])
def get_token_info():
    form = TokenForm().validate_for_api()
    token = form.token.data

    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        # return_header=True 把框架自带的token过期时间和创建时间返回去，格式为tuple
        # ({'uid': 5, 'scope': 'UserScope', 'ac_type': 100}, {'alg': 'HS512', 'iat': 1552396311, 'exp': 1554988311})
        data = s.loads(token, return_header=True)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)

    r = {
        'uid': data[0]['uid'],
        'scope': data[0]['scope'],
        'expire_in': data[1]['exp'],
        'create_at': data[1]['iat'],
    }
    return jsonify(r)


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'scope': scope,
        # ac_type后面要加value属性，因为他是formData的值
        'ac_type': ac_type.value
    })
