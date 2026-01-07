from fastapi import FastAPI
from app.routers import posts_router
from app.database import create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(title="Social App API", lifespan=lifespan)

app.include_router(posts_router)

@app.get('/healthcheck')
def healthcheck():
    return {'status': 'ok'}
