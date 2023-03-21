from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    join_date = Column(DateTime(timezone=True), nullable=False)
    icon = Column(String, nullable=True)


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime(timezone=True), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="user_posts")
    category_name = Column(String, ForeignKey("category.name"), nullable=True)
    category = relationship("Category", backref="category_posts")


class Category(Base):
    __tablename__ = "category"

    name = Column(String, primary_key=True)
    description = Column(Text, nullable=False)
