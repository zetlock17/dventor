import time
from fastapi import Header
from database.database import get_session_contextly
from database.models import User
from ..exceptions import InvalidTokenErrorHttpException, NotHaveAccessExceptionErrorHttpException, TokenExpiredErrorHttpException, UserNotFoundHttpExceptionErrorHttpException
from config import SECRET_KEY, ALGORITHM
import jwt
from datetime import datetime, timedelta
from ..global_funcs import exception_handler

def make_access_token(user_id: int):
    return  jwt.encode({
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=15)
    }, key=SECRET_KEY, algorithm=ALGORITHM)


def make_refresh_token(user_id: int):
    return  jwt.encode({
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(days=14)
    }, key=SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str):
    try:
        print(token)
        if token == "undefined":
            time.sleep(100)
        decode_token = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return decode_token
    except jwt.ExpiredSignatureError:
        raise TokenExpiredErrorHttpException()
    except jwt.InvalidTokenError:
        raise InvalidTokenErrorHttpException()
    
@exception_handler
async def type_required(
    type: str,
    token: str = Header(None)
):
    async with get_session_contextly() as session:

        data = decode_token(token=token)
        user = await session.get(User, data["user_id"])
        if user == None:
            raise UserNotFoundHttpExceptionErrorHttpException()

        if type != user.type.value:
            raise NotHaveAccessExceptionErrorHttpException()

        return user

async def admin_required(token: str = Header(None)):
    return await type_required(type="admin", token=token)