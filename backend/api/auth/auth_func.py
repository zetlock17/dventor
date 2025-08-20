from ..exceptions import InvalidRefreshTokenErrorHttpException, RefreshTokenExpiredErrorHttpException
from config import SECRET_KEY, ALGORITHM
import jwt
from datetime import datetime, timedelta


def make_access_token(mentor_id: int):
    return  jwt.encode({
        "mentor_id": mentor_id,
        "exp": datetime.now() + timedelta(minutes=30)
    }, key=SECRET_KEY, algorithm=ALGORITHM)


def make_refresh_token(mentor_id: int):
    return  jwt.encode({
        "mentor_id": mentor_id,
        "exp": datetime.now() + timedelta(days=14)
    }, key=SECRET_KEY, algorithm=ALGORITHM)

def decode_refresh_token(refresh_token: str):
    try:
        decode_refresh_token = jwt.decode(refresh_token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return decode_refresh_token
    except jwt.ExpiredSignatureError:
        raise RefreshTokenExpiredErrorHttpException()
    except jwt.InvalidTokenError:
        raise InvalidRefreshTokenErrorHttpException()