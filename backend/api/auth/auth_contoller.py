from fastapi_restful.cbv import cbv
from fastapi import APIRouter, Depends
from ..global_funcs import exception_handler
from .auth_service import AuthService
from database.database import get_session_obj
from .auth_schemas import AuthAnswerSchema, LoginMentorSchema, RegisterMentorSchema
from sqlalchemy.ext.asyncio import AsyncSession

auth_controller = APIRouter()


@cbv(auth_controller)
class AuthContoller:

    def __init__(self, session: AsyncSession = Depends(get_session_obj)):
        self.session = session
        self.auth_service = AuthService(session=self.session)
    

    @auth_controller.post("/login", summary="Авторизация ментора")
    @exception_handler
    async def login(self, login_data: LoginMentorSchema) -> AuthAnswerSchema:
        tokens = await self.auth_service.login_mentor(login_data=login_data)
        return tokens

    @auth_controller.post("/register/mentor", summary="Регистрация нового ментора")
    @exception_handler
    async def register_mentor(self, register_data: RegisterMentorSchema) -> AuthAnswerSchema:
        tokens = await self.auth_service.register_mentor(register_data=register_data)
        return tokens
    
    @auth_controller.post("/refresh-token", summary="Выдача нового токена")
    @exception_handler
    async def get_new_access_token(self, refresh_token: str) -> str:
        token = await self.auth_service.get_new_access_token(refresh_token=refresh_token)
        return token
