from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .auth_func import make_access_token, make_refresh_token
from ..exceptions import LoginIsTakenErrorHttpException
from ..mentors.mentor_service import MentorService
from .auth_schemas import RegisterMentorSchema
from .auth_repository import AuthRepository
from argon2 import PasswordHasher



class AuthService:
    def __init__(self, session: AsyncSession):
        self.password_hasher = PasswordHasher()
        self.session = session
        self.auth_repository = AuthRepository(session=self.session)
        self.mentor_service = MentorService(session=self.session)


    async def register_mentor(self, register_data: RegisterMentorSchema):

        mentor_data = {
            "username" : register_data.username
        }

        new_mentor_id = await self.mentor_service.add_mentor(mentor_data=mentor_data)

        hashed_password = self.password_hasher.hash(register_data.password)

        if not await self.auth_repository.login_free_check(login=register_data.login):
            raise LoginIsTakenErrorHttpException

        auth_mentor_data = {
            "login": register_data.login,
            "password": hashed_password,
            "mentor_id": new_mentor_id
        }
        
        await self.auth_repository.add_auth_mentor(auth_mentor_data=auth_mentor_data)

        return {
            "access_token": make_access_token(new_mentor_id),
            "refresh_token": make_refresh_token(new_mentor_id)
        }
