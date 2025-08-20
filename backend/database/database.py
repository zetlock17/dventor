# database.py
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///database/dventor.db"


engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

async_session_maker = async_sessionmaker(
    engine, expire_on_commit=False
)

base = declarative_base()


async def get_session_obj() -> AsyncGenerator[AsyncSession, None]:
    session = async_session_maker()
    async with session.begin():
        yield session
    await session.close()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)