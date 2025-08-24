from sqlalchemy.ext.asyncio import AsyncSession
from .user_repository import UserRepository
from database.models import UserType


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.mentor_repository = UserRepository(session=self.session)
    
    async def get_user_by_id(self, user_id: int):
        return await self.mentor_repository.get_user_by_id(user_id=user_id) 
