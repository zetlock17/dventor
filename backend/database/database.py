# database.py
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///database/dventor.db"


engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

async_session = async_sessionmaker(
    engine, expire_on_commit=False
)

base = declarative_base()

@asynccontextmanager
async def get_db():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)