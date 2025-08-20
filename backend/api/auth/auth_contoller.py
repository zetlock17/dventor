from fastapi_restful.cbv import cbv
from fastapi import APIRouter, Depends
from ..global_funcs import exception_handler
from .auth_service import AuthService
from database.database import get_session_obj
from .auth_schemas import AuthAnswerSchema, RegisterMentorSchema
from sqlalchemy.ext.asyncio import AsyncSession

auth_controller = APIRouter()


@cbv(auth_controller)
class AuthContoller:

    def __init__(self, session: AsyncSession = Depends(get_session_obj)):
        self.session = session
        self.auth_service = AuthService(session=self.session)
    

    @auth_controller.post("/login")
    @exception_handler
    async def login(self):
        pass

    @auth_controller.post("/register/mentor")
    @exception_handler
    async def register_mentor(self, register_data: RegisterMentorSchema) -> AuthAnswerSchema:
        tokens = await self.auth_service.register_mentor(register_data=register_data)
        return tokens
