from pydantic import BaseModel, Field


class MentorSchema(BaseModel):
    id: int = Field(...)
    username: str = Field(...)
    specialization: str | None= Field()
    experience: int| None = Field()