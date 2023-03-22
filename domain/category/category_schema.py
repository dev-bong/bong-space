from pydantic import BaseModel, Field


class Category(BaseModel):
    name: str = Field(default=..., title="카테고리 이름")
    description: str = Field(default=..., title="카테고리 설명")

    class Config:
        orm_mode = True
