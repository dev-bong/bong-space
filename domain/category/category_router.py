from fastapi import APIRouter

from database import SessionLocal
from models import Category

router = APIRouter(
    prefix="/api/category",
)


@router.get("/list")
def category_list():
    db = SessionLocal()
    _question_list = db.query(Category).all()
    db.close()
    return _question_list
