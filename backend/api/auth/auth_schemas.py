from pydantic import Field, BaseModel


class LoginMentorSchema(BaseModel):
  login: str = Field(...)
  password: str = Field(..., min_length=8)

class RegisterMentorSchema(BaseModel):
  username: str = Field(...)
  login: str = Field(...)
  password: str = Field(..., min_length=8)

class AuthAnswerSchema(BaseModel):
  access_token: str = Field(...)
  refresh_token: str = Field(...)
  