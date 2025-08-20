from fastapi import HTTPException


class LoginIsTakenErrorHttpException(HTTPException):
    def __init__(self):
        message = "Логин уже занят"
        super().__init__(status_code=500, detail=message)


class InternalServerErrorHttpException(HTTPException):
    def __init__(
        self,
        msg: str = "",
    ):
        if msg in [None, ""]:
            msg = "internal server error"
        super().__init__(status_code=500, detail=msg)