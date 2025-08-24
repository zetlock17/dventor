from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Application, ApplicationStatus

application_storage = {}

class ApplicationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_applications(self) -> list[Application]:
        result = await self.session.execute(select(Application).where(Application.status == ApplicationStatus.PENDING))
        return result.scalars().all()

    async def save_application(self, application_uuid: str, application_data: dict):
        application_storage[application_uuid] = application_data

    async def check_and_get_application(self, telegram_data: dict):
        application_data = application_storage.get(telegram_data["application_uuid"])

        if not application_data:
            return None
        
        result = (await self.session.execute(select(Application).where(Application.telegram_id == telegram_data["telegram_id"], Application.status != ApplicationStatus.CANCELLED))).scalar()
        
        if result:
            return None
        
        return application_data
    
    async def create_application(self, application_data:dict):
        new_application = Application(**application_data)
        self.session.add(new_application)
        await self.session.flush()

    async def application_confirm(self, application_id: int):
        result = await self.session.execute(select(Application).where(Application.id == application_id))
        application = result.scalar()
        application.status = ApplicationStatus.CONFIRMED
        return application
        
    async def application_cancel(self, application_id: int):
        result = await self.session.execute(select(Application).where(Application.id == application_id))
        application = result.scalar()
        application.status = ApplicationStatus.CANCELLED
        return application
        