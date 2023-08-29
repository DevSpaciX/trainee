from sqlalchemy import Column, Integer, String

from db.engine import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, index=True,primary_key=True)
    name = Column(String(255),nullable=False)
    surname = Column(String(255),nullable=False)
    login = Column(String(255),nullable=False)
    password = Column(String(255),nullable=False)
