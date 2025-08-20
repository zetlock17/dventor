from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .auth_func import decode_refresh_token, make_access_token, make_refresh_token
from ..exceptions import InvalidLoginErrorHttpException, InvalidPasswordErrorHttpException, InvalidRefreshTokenErrorHttpException, LoginIsTakenErrorHttpException
from ..mentors.mentor_service import MentorService
from .auth_schemas import LoginMentorSchema, RegisterMentorSchema
from .auth_repository import AuthRepository
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError 

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

        print('fsdijofsdjkjfsdjkjsdklfdsjklfkljfsdjklfsdjkklfjklsdkfljsdkfjsdkl')

        return {
            "access_token": make_access_token(new_mentor_id),
            "refresh_token": make_refresh_token(new_mentor_id)
        }
    
    async def login_mentor(self, login_data: LoginMentorSchema):

        mentor = await self.auth_repository.get_auth_mentor_by_login(login=login_data.login)

        if not mentor:
            raise InvalidLoginErrorHttpException()

        try:
            self.password_hasher.verify(mentor.password, login_data.password)
        except VerifyMismatchError:
            raise InvalidPasswordErrorHttpException()

        return {
            "access_token": make_access_token(mentor.id),
            "refresh_token": make_refresh_token(mentor.id)
        }


    async def get_new_access_token(self, refresh_token: str):
        decode_token = decode_refresh_token(refresh_token=refresh_token)
        mentor_id = decode_token.get("mentor_id")

        if not mentor_id:
            raise InvalidRefreshTokenErrorHttpException()
        
        mentor = await self.mentor_service.get_mentor_by_id(mentor_id=mentor_id)

        if not mentor:
            raise InvalidRefreshTokenErrorHttpException()
        
        return make_access_token(mentor_id=mentor.id)
            