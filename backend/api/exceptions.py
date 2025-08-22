from fastapi import HTTPException


class LoginIsTakenErrorHttpException(HTTPException):
    def __init__(self):
        message = "Логин уже занят"
        super().__init__(status_code=500, detail=message)

class InvalidLoginErrorHttpException(HTTPException):
    def __init__(self):
        message = "Неверный логин"
        super().__init__(status_code=500, detail=message)

class InvalidPasswordErrorHttpException(HTTPException):
    def __init__(self):
        message = "Неверный пароль"
        super().__init__(status_code=500, detail=message)

class InvalidRefreshTokenErrorHttpException(HTTPException):
    def __init__(self):
        message = "Неверный рефреш-токен"
        super().__init__(status_code=500, detail=message)

class RefreshTokenExpiredErrorHttpException(HTTPException):
    def __init__(self):
        message = "Рефреш-токен истек"
        super().__init__(status_code=500, detail=message)

class ApplicationNotFoundErrorHttpException(HTTPException):
    def __init__(self):
        message = "Заявка не найдена"
        super().__init__(status_code=500, detail=message)

class ApplicationDuplicateErrorHttpException(HTTPException):
    def __init__(self):
        message = "Вы пытаетесь повторно отправить заявку или такой заявка не найдена"
        super().__init__(status_code=500, detail=message)

class InternalServerErrorHttpException(HTTPException):
    def __init__(
        self,
        msg: str = "",
    ):
        if msg in [None, ""]:
            msg = "internal server error"
        super().__init__(status_code=500, detail=msg)