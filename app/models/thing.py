from sqlalchemy import Column, Integer, ForeignKey, String, orm
from sqlalchemy.orm import relationship

from app.models.base import Base
# 完成状态
NO_COMPLETE = '01'
COMPLETE = '02'


class Thing(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    content = Column(String(15), nullable=False)
    complete_status = Column(String(2), default=NO_COMPLETE)
    update_time = Column(Integer, nullable=False)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'content', 'complete_status', 'update_time']

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
