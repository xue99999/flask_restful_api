from datetime import datetime

from flask import g, jsonify

from app.libs.error_code import Success, DeleteSuccess, ParameterException
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.thing import Thing
from app.validators.forms import ThingForm, ThingUpdateForm

api = Redprint('thing')

# 完成状态
NO_COMPLETE = '01'
COMPLETE = '02'


@api.route('', methods=['GET'])
@auth.login_required
def get_thing():
    uid = g.user.uid
    things = Thing.query.filter_by(uid=uid).all()
    r = {
        'error_code': 0,
        'msg': 'ok',
        'data': things
    }
    return jsonify(r)


@api.route('', methods=['POST'])
@auth.login_required
def create_thing():
    uid = g.user.uid
    form = ThingForm().validate_for_api()
    with db.auto_commit():
        thing = Thing()
        thing.uid = uid
        thing.content = form.content.data
        thing.update_time = int(datetime.now().timestamp())
        db.session.add(thing)

    return Success()


@api.route('/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_thing(id):
    uid = g.user.uid
    with db.auto_commit():
        thing = Thing.query.filter_by(uid=uid, id=id).first_or_404()
        thing.delete()
    return DeleteSuccess()


@api.route('/<int:id>', methods=['PUT', 'PATCH'])
@auth.login_required
def change_thing(id):
    uid = g.user.uid
    form = ThingUpdateForm().validate_for_api()
    with db.auto_commit():
        thing = Thing.query.filter_by(uid=uid, id=id).first_or_404()
        if form.content.data:
            thing.content = form.content.data
        status = form.complete_status.data
        if status == NO_COMPLETE or status == COMPLETE:
            thing.complete_status = form.complete_status.data
        else:
            return ParameterException(msg="complete_status 传值不对")
        thing.update_time = int(datetime.now().timestamp())

    thing = Thing.query.filter_by(uid=uid, id=id).first_or_404()

    r = {
        'error_code': 0,
        'msg': 'ok',
        'data': thing
    }
    return jsonify(r)
