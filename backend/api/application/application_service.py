from sqlalchemy.ext.asyncio import AsyncSession
from ..exceptions import ApplicationDuplicateErrorHttpException, ApplicationNotFoundErrorHttpException
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
        return await self.application_repository.get_applications()

    async def save_application(self, application: ApplicationCreateSchema):
        application_uuid = str(uuid.uuid4())
        application_data = application.model_dump()
        await self.application_repository.save_application(application_uuid=application_uuid, application_data=application_data)
        return application_uuid
    
    async def create_application(self, telegram_data: TelegramDataSchema):

        telegram_data_dict = telegram_data.model_dump()

        application_data = await self.application_repository.check_and_get_application(telegram_data=telegram_data_dict)

        if not application_data:
            raise ApplicationDuplicateErrorHttpException()

        application_data['telegram_id'] = telegram_data['telegram_id']

        application_data['telegram_username'] = telegram_data['telegram_username']

        await self.application_repository.create_application(application_data=application_data)

    async def application_confirmed(self, application_id: int):
        applciation = await self.application_repository.application_confirmed(application_id=application_id)
        if not applciation:
            raise ApplicationNotFoundErrorHttpException()

        register_data = {
            "login": applciation.login,
            "password": applciation.password,
            "username": applciation.username,
            "specialization": applciation.specialization,
            "experience": applciation.experience,
            "telegram_id": applciation.telegram_id,
            "telegram_username": applciation.telegram_username
        }

        await self.auth_service.register_mentor(register_data=register_data)

    async def application_cancell(self, application_id: int):
        self.application_repository.application_cancell(application_id=application_id)