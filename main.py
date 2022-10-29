from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.user.permissions import get_query_token
from conf import get_db, engine, Base
from apps.user.routers import router as user_router
from apps.item.routers import router as item_router

Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(get_query_token)])
# app = FastAPI()
app.include_router(user_router)
app.include_router(item_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    # for redis
    # app.state.redis = await aioredis.create_redis_pool('redis://redis')
    pass


@app.on_event("shutdown")
async def shutdown():
    pass
