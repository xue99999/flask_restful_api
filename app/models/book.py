"""
 Created by 七月 on 2018/5/26.
"""
from sqlalchemy import Column, String, Integer, orm

from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'title', 'author', 'binding',
                       'publisher',
                       'price', 'pages', 'pubdate', 'isbn',
                       'summary',
                       'image']

    # 序列化模型的时候用到这个方法, 返回结果是可序列化对象就可以
    def keys(self):
        return self.fields

    # 隐藏 -- 返回给前端的字段
    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self
        # 这里必须return, 因为推导式返回的hide方法， 所以需要在hide方法里面把模型返回去

    # 添加 -- 返回给前端的字段
    def append(self, *keys):
        for key in keys:
            self.fields.append(key)
        return self
        # 这里必须return, 因为推导式返回的hide方法， 所以需要在hide方法里面把模型返回去

