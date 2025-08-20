from fastapi import APIRouter
from api.auth.auth_contoller import auth_controller

api = APIRouter()

api.include_router(auth_controller, prefix="/auth", tags=["auth"])