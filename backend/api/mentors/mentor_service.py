from sqlalchemy.ext.asyncio import AsyncSession
from .mentor_repository import MentorRepository


class MentorService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.mentor_repository = MentorRepository(session=self.session)
    

    async def get_mentors(self):
        return await self.mentor_repository.get_mentors() 

    async def add_mentor(self, mentor_data: dict):
        new_mentor_id = await self.mentor_repository.add_mentor(mentor_data=mentor_data)
        return new_mentor_id