from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import User, UserType


class MentorRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_mentors(self):
        result = await self.session.execute(select(User).where(User.type == UserType.MENTOR))
        mentors = result.scalars().all()
        return mentors
    
    async def get_mentor_by_id(self, mentor_id: int):
        result = await self.session.execute(select(User).where(User.id == mentor_id and User.status == UserType.MENTOR))
        mentor = result.scalar()
        return mentor
        
    async def add_mentor(self, mentor_data: dict):
        new_mentor = User(**mentor_data)
        self.session.add(new_mentor)
        await self.session.flush()
        return new_mentor.id
        