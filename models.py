from sqlalchemy import Column, Integer, String, Text, DateTime

from database import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    nickname = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    join_dt = Column(DateTime(timezone=True), nullable=False)
    icon = Column(String, nullable=True)