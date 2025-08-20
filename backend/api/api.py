from fastapi import APIRouter
from api.auth.auth_contoller import auth_controller
from api.mentors.mentor_controller import mentor_controller

api = APIRouter()

api.include_router(auth_controller, prefix="/auth", tags=["auth"])
api.include_router(mentor_controller, prefix="/mentors", tags=["Mentors"])