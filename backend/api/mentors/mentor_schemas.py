from pydantic import BaseModel, Field


class MentorSchema(BaseModel):
    id: int = Field(...)
    username: str = Field(...)
    specialization: str | None= Field()
    experience: int| None = Field()
    telegram_id: str = Field(...)
    telegram_username: str = Field(...)