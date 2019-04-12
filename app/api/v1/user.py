from flask import jsonify, g

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')

# class Qiyue():
#     name = 'xuejun'
#     age = '23'
#
#     def keys(self):
#         return ('name', 'age')
#
#     def __getitem__(self, item):
#         return getattr(self, item)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # 管理员访问
    user = User.query.filter_by(id=uid).first_or_404()

    r = {
        'error_code': 0,
        'msg': 'ok',
        'data': user
    }
    return jsonify(r)


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()

    r = {
        'error_code': 0,
        'msg': 'ok',
        'data': user
    }
    return jsonify(r)


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
    # 管理员访问
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    # 2个用户同时调用山粗接口，会有问题吗？
    # 不会， 因为g是线程隔离
    # g.user.uid 为什么可以这样用? 因为验证token通过，
    # 把userinfo 存成了namedtuple结构， 可以通过.来访问属性
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()
