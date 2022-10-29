from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.user import schemas
from apps.user.permissions import check_permission
from apps.user.views import create_user, get_users, get_user
from conf import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(check_permission)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.User)
async def user_create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return await create_user(db=db, user=user)


@router.get("/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return await get_users(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return await get_user(db, user_id=user_id)
