from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.model import AuthorizationMentor


class AuthRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def login_free_check(self, login: str):
        result = (await self.session.execute(select(AuthorizationMentor).where(AuthorizationMentor.login==login))).first()
        return result is None

    async def add_auth_mentor(self, auth_mentor_data: dict):
        new_auth_mentor = AuthorizationMentor(**auth_mentor_data)
        self.session.add(new_auth_mentor)
        await self.session.flush()