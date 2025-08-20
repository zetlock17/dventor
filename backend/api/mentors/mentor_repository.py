from sqlalchemy.ext.asyncio import AsyncSession
from database.model import Mentor


class MentorRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_mentor(self, mentor_data: dict):
        new_mentor = Mentor(**mentor_data)
        self.session.add(new_mentor)
        await self.session.flush()
        return new_mentor.id
        