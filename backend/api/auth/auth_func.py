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