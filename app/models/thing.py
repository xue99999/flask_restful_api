from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
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

    # 序列化模型的时候用到这个方法, 返回结果是可序列化对象就可以
    def keys(self):
        return ['id', 'content', 'complete_status', 'update_time']
