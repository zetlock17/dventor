from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import User, UserType


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_id(self, user_id: int):
        result = await self.session.execute(select(User).where(User.id == user_id))
        user = result.scalar()
        return user
    
        