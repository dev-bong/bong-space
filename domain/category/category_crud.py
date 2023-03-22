from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Category


def read_category_list(db: Session):
    return db.execute(select(Category)).scalars().all()
