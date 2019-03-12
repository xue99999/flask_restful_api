from app import create_app
from app.models.base import db
from app.models.user import User
from app.models.book import Book

app = create_app()
with app.app_context():
    with db.auto_commit():
        user = User()
        user.email = 'admin123@qq.com'
        user.nickname = 'admin123'
        user.auth = 2
        user.password = '123456'
        db.session.add(user)


# app = create_app()
# with app.app_context():
#     with db.auto_commit():
#         book = Book()
#         book.title = '哈哈'
#         book.author = 'xuejun123'
#         book.binding = '精装'
#         book.publisher = 'xuejun123'
#         book.price = '22.00'
#         book.pages = '888'
#         book.pubdate = '1525874561'
#         book.isbn = '99996666'
#         book.summary = '这本书的简介'
#         book.image = 'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike272%2C5%2C5%2C272%2C90/sign=de65b2430424ab18f41be96554938da8/aec379310a55b31967c7d5104ea98226cffc179c.jpg'
#         db.session.add(book)
