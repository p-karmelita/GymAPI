from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, gt=1)
    surname = Column(String, index=True, gt=1)
    hashed_password = Column(String, lt=20)


class Exercise(Base):
    __tablename__ = 'exercise'
    name = Column(String)
    description = Column(String)
    series = Column(Integer)
    repetition = Column(Integer)
    muscle_group = Column(String)
