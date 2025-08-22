from pydantic import Field, BaseModel


class LoginMentorSchema(BaseModel):
  login: str = Field(...)
  password: str = Field(..., min_length=8)

class RegisterMentorSchema(BaseModel):
    login: str = Field(...)
    password: str = Field(..., min_length=8)
    username: str = Field(...)
    specialization: str | None= Field()
    experience: int| None = Field()
    telegram_id: str = Field(...)
    telegram_username: str = Field(...)

class AuthAnswerSchema(BaseModel):
  access_token: str = Field(...)
  refresh_token: str = Field(...)
  