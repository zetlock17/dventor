from fastapi_restful.cbv import cbv
from fastapi import APIRouter, Depends, Response

from config import CACHED
from .mentor_service import MentorService
from ..global_funcs import exception_handler
from database.database import get_session_obj
from .mentor_schemas import MentorSchema
from sqlalchemy.ext.asyncio import AsyncSession


mentor_controller = APIRouter()

@cbv(mentor_controller)
class MentorController:

    def __init__(self, session: AsyncSession = Depends(get_session_obj)):
        self.session = session
        self.mentor_service = MentorService(session= self.session)

    @mentor_controller.get("/", summary="Выдает список всех менторов")
    @exception_handler
    async def get_mentors(self, response: Response) -> list[MentorSchema]:
        if CACHED:
            response.headers["Cache-Control"] = "public, max-age=3600"
        return await self.mentor_service.get_mentors()