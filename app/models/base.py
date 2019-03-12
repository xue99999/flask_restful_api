from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, SmallInteger, Integer
from contextlib import contextmanager

from app.libs.error_code import NotFound


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


# 改写Query下的filter_by方法
class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            # status = 1代表数据没有被软删除
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        rv = self.get(ident)
        if rv is None:
            raise NotFound()
        return rv

    def first_or_404(self, msg=None):
        rv = self.first()
        if rv is None:
            raise NotFound(msg)
        return rv


# 重写SQLAlchemy的Query方法
db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    # 不让数据库创建这张表
    __abstract__ = True
    create_time = Column('create_time', Integer)
    # 软删除标识
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    # 序列化模型的时候，会用此方法获取属性值
    def __getitem__(self, item):
        return getattr(self, item)

    # 为模型统一赋值, 不能给id赋值
    def set_atrrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    # 把时间戳格式化
    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    # 所有模型的通用删除方法
    def delete(self):
        self.status = 0
