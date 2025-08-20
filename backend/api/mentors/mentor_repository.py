from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Mentor


class MentorRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_mentors(self):
        result = await self.session.execute(select(Mentor))
        mentors = result.scalars().all()
        return mentors

    async def add_mentor(self, mentor_data: dict):
        new_mentor = Mentor(**mentor_data)
        self.session.add(new_mentor)
        await self.session.flush()
        return new_mentor.id
        