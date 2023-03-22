from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from database import get_db
from models import Category

router = APIRouter(
    prefix="/api/category",
)


@router.get("/list")
def category_list(db: Session = Depends(get_db)):
    _category_list = db.execute(select(Category)).scalars().all()
    return _category_list
