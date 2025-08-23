from fastapi_restful.cbv import cbv
from fastapi import APIRouter, Depends
from ..global_funcs import exception_handler
from .application_schemas import ApplicationCreateSchema, ApplicationGetSchema, ApplicationSchema, TelegramDataSchema
from .application_service import ApplicationService
from database.database import get_session_obj
from sqlalchemy.ext.asyncio import AsyncSession

application_controller = APIRouter()

@cbv(application_controller)
class ApplicationController:
    def __init__(self, session: AsyncSession = Depends(get_session_obj)):
        self.session = session
        self.application_service = ApplicationService(session=self.session)
    
    @application_controller.get("/", summary="Выдача всех заявок")
    @exception_handler
    async def get_applications(self) -> list[ApplicationGetSchema]:
        return await self.application_service.get_applications()

    @application_controller.post("/send", summary="Отправка заявки")
    @exception_handler
    async def take_application(self, application: ApplicationCreateSchema) -> str:
        application_uuid = await self.application_service.save_application(application=application)
        return application_uuid

    @application_controller.post("/create", summary="Создание заявки")
    @exception_handler
    async def create_application(self, telegram_data: TelegramDataSchema):
        await self.application_service.create_application(telegram_data=telegram_data)
    
    @application_controller.post("/confirm", summary="Подтверждение заявки")
    @exception_handler
    async def application_confirm(self, application_id: int):
        await self.application_service.application_confirm(application_id=application_id)


    @application_controller.post("/cancel", summary="Подтверждение заявки")
    @exception_handler
    async def application_cancel(self, application_id: int):
        await self.application_service.application_cancel(application_id=application_id)
