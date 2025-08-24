from sqlalchemy.ext.asyncio import AsyncSession
from .auth_func import decode_token, make_access_token, make_refresh_token
from ..exceptions import InvalidLoginErrorHttpException, InvalidPasswordErrorHttpException, LoginIsTakenErrorHttpException
from ..mentors.mentor_service import MentorService
from .auth_schemas import LoginMentorSchema
from .auth_repository import AuthRepository
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError 

class AuthService:
    def __init__(self, session: AsyncSession):
        self.password_hasher = PasswordHasher()
        self.session = session
        self.auth_repository = AuthRepository(session=self.session)
        self.mentor_service = MentorService(session=self.session)


    async def register_mentor(self, register_data: dict):
        if not await self.auth_repository.login_free_check(login=register_data['login']):
            raise LoginIsTakenErrorHttpException()
        
        register_data['password'] = self.password_hasher.hash(register_data['password'])

        await self.mentor_service.add_mentor(mentor_data=register_data)
        

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
        dec_token = decode_token(refresh_token=refresh_token)
        mentor_id = dec_token.get("mentor_id")

        if not mentor_id:
            raise InvalidRefreshTokenErrorHttpException()
        
        mentor = await self.mentor_service.get_mentor_by_id(mentor_id=mentor_id)

        if not mentor:
            raise InvalidRefreshTokenErrorHttpException()
        
        return make_access_token(mentor_id=mentor.id)
            