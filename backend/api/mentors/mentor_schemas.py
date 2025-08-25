from pydantic import BaseModel, Field


class MentorSchema(BaseModel):
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

    specialization: str | None= Field()
    experience: int| None = Field()

    class Config:
        from_attributes = True