from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import User


class AuthRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def login_free_check(self, login: str):
        result = (await self.session.execute(select(User).where(User.login==login))).first()
        return result is None

    async def get_auth_mentor_by_login(self, login: str):
        result = await self.session.execute(select(User).where(User.login == login))
        mentor = result.scalar()
        return mentor

        