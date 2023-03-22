from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.category import category_schema, category_crud

router = APIRouter(
    prefix="/api/category",
)


@router.get(
    "/list",
    response_model=list[category_schema.Category],
    summary="카테고리 목록 조회",
    description="",
)
def get_category_list(db: Session = Depends(get_db)):
    return category_crud.read_category_list(db)
