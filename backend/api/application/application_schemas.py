from pydantic import BaseModel, Field, ConfigDict
from database.models import ApplicationStatus

class ApplicationGetSchema(BaseModel):
    id: int = Field(...)
    
    name: str = Field(...)
    surname: str = Field(...)
    age: int = Field(...)
    city: str = Field(...)
    place_of_study: str = Field(...)
    experience: int = Field(...)
    company: str = Field(...)
    post: str = Field(...)
    descriptiion: str = Field(...)
    specialization: str = Field(...)
    stack: list[str] = Field(...)
    telegram_username: str = Field(...)
    status: ApplicationStatus = Field(...)

    class Config:
        from_attributes = True

class ApplicationSchema(BaseModel):
    id: int = Field(...)
    login: str = Field(...)
    password: str = Field(..., min_length=8)

    name: str = Field(...)
    surname: str = Field(...)
    age: int = Field(...)
    city: str = Field(...)
    place_of_study: str = Field(...)
    experience: int = Field(...)
    company: str = Field(...)
    post: str = Field(...)
    descriptiion: str = Field(...)
    specialization: str = Field(...)
    stack: list[str] = Field(...)

    specialization: str | None= Field()
    experience: int| None = Field()

    telegram_id: str = Field(...)
    telegram_username: str = Field(...)
    status: ApplicationStatus = Field(...)


class ApplicationCreateSchema(BaseModel):
    login: str = Field(...)
    password: str = Field(..., min_length=8)

    name: str = Field(...)
    surname: str = Field(...)
    age: int = Field(...)
    city: str = Field(...)
    place_of_study: str = Field(...)
    experience: int = Field(...)
    company: str = Field(...)
    post: str = Field(...)
    descriptiion: str = Field(...)
    specialization: str = Field(...)
    stack: list[str] = Field(...)

    specialization: str | None= Field()
    experience: int| None = Field()

class TelegramDataSchema(BaseModel):
    telegram_username: str = Field(...)
    telegram_id: str = Field(...)
    application_uuid: str = Field(...)