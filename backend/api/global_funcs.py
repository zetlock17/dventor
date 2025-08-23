from functools import wraps
from fastapi import HTTPException
from sqlalchemy import select
from dotenv import load_dotenv
import os
import logging
from database.database import get_session_contextly
from database.models import User, UserType
from .exceptions import InternalServerErrorHttpException
from argon2 import PasswordHasher

load_dotenv()
ADMIN_LOGIN = os.getenv("ADMIN_LOGIN")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")




logger = logging.getLogger(__name__)

def exception_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            print(123)
            return await func(*args, **kwargs)
        except HTTPException as e:
            logger.error(f"Произошла ошибка в эндпоинте {func.__name__}: {e}", exc_info=True)
            raise e
        except Exception as e:
            logger.error(f"Произошла ошибка в эндпоинте {func.__name__}: {e}", exc_info=True)
            raise InternalServerErrorHttpException(msg=str(e))

    return wrapper

async def create_admin_user():

    password_hasher = PasswordHasher()
    hashed = password_hasher.hash(ADMIN_PASSWORD)
    admin_data = {
        "login" : ADMIN_LOGIN,
        "password" : hashed
    }
    
    async with get_session_contextly() as session:
        existing_admin = await session.execute(
            select(User).where(User.login == admin_data["login"])
        )
        if existing_admin.scalar_one_or_none():
            print(f"Админ с логином '{admin_data['login']}' уже существует.")
            return

        new_admin = User(
            type=UserType.ADMIN,
            **admin_data
        )
        
        session.add(new_admin)
        await session.commit()

    print("Админ успешно создан.")