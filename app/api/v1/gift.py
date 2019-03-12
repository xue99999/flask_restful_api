from flask import g

from app.libs.error_code import DuplicateGift, Success
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.book import Book
from app.models.gift import Gift

api = Redprint('gift')


@api.route('/<isbn>', methods=['POST'])
@auth.login_required
def create(isbn):
    uid = g.user.uid
    with db.auto_commit():
        # 先查询有没有这本书, 没有会自己返回错误
        Book.query.filter_by(isbn=isbn).first_or_404()
        # 再看是否有本同样的书正在赠送
        gift = Gift.query.filter_by(uid=uid, isbn=isbn).first()
        if gift:
            raise DuplicateGift()
        gift = Gift()
        gift.uid = uid
        gift.isbn = isbn
        db.session.add(gift)
    return Success()
