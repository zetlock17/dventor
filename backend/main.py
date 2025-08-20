from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.database import create_tables
from fastapi.middleware.cors import CORSMiddleware
from api.api import api

@asynccontextmanager
async def lifespawn(app: FastAPI):
    await create_tables()
    yield
    
app = FastAPI(lifespan=lifespawn)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api)