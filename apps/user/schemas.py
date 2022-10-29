from typing import Union

from pydantic import BaseModel

from apps.item.schemas import Item


class UserBase(BaseModel):
    email: str
    real_age: Union[int, None] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
