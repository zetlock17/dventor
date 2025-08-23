from pydantic import BaseModel, Field, ConfigDict
from database.models import ApplicationStatus

class ApplicationGetSchema(BaseModel):
    id: int = Field(...)
    username: str = Field(...)
    specialization: str | None= Field()
    experience: int| None = Field()
    telegram_id: str = Field(...)
    telegram_username: str = Field(...)
    status: ApplicationStatus = Field(...)

    class Config:
        from_attributes = True

class ApplicationSchema(BaseModel):
    id: int = Field(...)
    login: str = Field(...)
    password: str = Field(..., min_length=8)
    username: str = Field(...)
    specialization: str | None= Field()
    experience: int| None = Field()
    telegram_id: str = Field(...)
    telegram_username: str = Field(...)
    status: ApplicationStatus = Field(...)

class ApplicationCreateSchema(BaseModel):
    username: str = Field(...)
    login: str = Field(...)
    password: str = Field(..., min_length=8)
    specialization: str | None= Field()
    experience: int| None = Field()

class TelegramDataSchema(BaseModel):
    telegram_username: str = Field(...)
    telegram_id: str = Field(...)
    application_uuid: str = Field(...)