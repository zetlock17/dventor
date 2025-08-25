from sqlalchemy.ext.asyncio import AsyncSession
from .application_func import bot_send_message
from ..exceptions import ApplicationDuplicateErrorHttpException, ApplicationNotFoundErrorHttpException, LoginIsTakenErrorHttpException
from .application_schemas import ApplicationCreateSchema, TelegramDataSchema
from .application_repository import ApplicationRepository
from ..auth.auth_service import AuthService
import uuid


class ApplicationService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.application_repository = ApplicationRepository(session=self.session)
        self.auth_service = AuthService(session=self.session)

    async def get_applications(self):
        applications =  await self.application_repository.get_applications()
        return applications

    async def save_application(self, application: ApplicationCreateSchema):

        if not await self.auth_service.auth_repository.login_free_check(login=application.login):
            raise LoginIsTakenErrorHttpException()

        application_uuid = str(uuid.uuid4())
        application_data = application.model_dump()
        await self.application_repository.save_application(application_uuid=application_uuid, application_data=application_data)

        return application_uuid
    
    async def create_application(self, telegram_data: TelegramDataSchema):

        telegram_data_dict = telegram_data.model_dump()

        application_data = await self.application_repository.check_and_get_application(telegram_data=telegram_data_dict)

        if not application_data:
            raise ApplicationDuplicateErrorHttpException()

        application_data['telegram_id'] = telegram_data.telegram_id

        application_data['telegram_username'] = telegram_data.telegram_username

        await self.application_repository.create_application(application_data=application_data)

    async def application_confirm(self, application_id: int):
        application = await self.application_repository.application_confirm(application_id=application_id)
        if not application:
            raise ApplicationNotFoundErrorHttpException()
        
        register_data = {
            "login": application.login,
            "password": application.password,
            "name": application.name,
            "surnmae": application.surname,
            "age": application.age,
            "city": application.city,
            "place_of_study": application.place_of_study,
            "experience": application.experience,
            "company": application.company,
            "post": application.post,
            "descriptiion": application.descriptiion,
            "specialization": application.specialization,
            "stack": application.stack,
            "telegram_id": application.telegram_id,
            "telegram_username": application.telegram_username
        }

        await self.auth_service.register_mentor(register_data=register_data)

        await bot_send_message(text=f"Ваша заявка была принята!\nЛогин: {application.login}\nПароль: {application.password}", chat_id=application.telegram_id)

    async def application_cancel(self, application_id: int):
        application = await self.application_repository.application_cancel(application_id=application_id)
        await bot_send_message(text=f"Ваша заявка была отклонена.", chat_id=application.telegram_id)