from fastapi import APIRouter
from api.auth.auth_contoller import auth_controller
from api.mentors.mentor_controller import mentor_controller
from api.application.application_contoller import application_controller

api = APIRouter()

api.include_router(auth_controller, prefix="/auth", tags=["Auth"])
api.include_router(mentor_controller, prefix="/mentors", tags=["Mentors"])
api.include_router(application_controller, prefix="/application", tags=["Applications"])