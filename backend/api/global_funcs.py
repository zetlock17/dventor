from functools import wraps
from fastapi import HTTPException
from .exceptions import InternalServerErrorHttpException


def exception_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, HTTPException):
                print(e)
                raise e
            print(e)
            raise InternalServerErrorHttpException(msg=str(e))

    return wrapper