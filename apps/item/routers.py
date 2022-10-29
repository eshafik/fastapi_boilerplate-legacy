from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.item.schemas import ItemCreate
from apps.item.views import create_user_item, get_items
from apps.user import schemas
from apps.user.permissions import check_permission
from conf import get_db

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(check_permission)],
    responses={404: {"description": "Not found"}},
)


@router.post("/{user_id}/items/", response_model=schemas.Item)
async def create_item_for_user(
    user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    return await create_user_item(db=db, item=item, user_id=user_id)


@router.get("/", response_model=list[schemas.Item])
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return await get_items(db, skip=skip, limit=limit)
