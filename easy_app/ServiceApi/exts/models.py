from sqlalchemy import Column, String

from exts.config import Base, engine


class User(Base):
    __tablename__ = 'user'  # 数据库表名
    username = Column(String(255),primary_key=True, nullable=False)
    pwd = Column(String(255), nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
