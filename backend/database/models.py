from sqlalchemy import JSON, Column, Integer, String, Enum
from database.database import base
from enum import Enum as PyEnum


class ApplicationStatus(PyEnum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class UserType(PyEnum):
    MENTOR = "mentor"
    ADMIN = "admin"


class User(base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True)
    type: UserType = Column(Enum(UserType), nullable=False)
    login: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    
    name: str = Column(String, nullable=True)
    surname: str = Column(String, nullable=True)
    age: int = Column(Integer, nullable=True)
    city: str = Column(String, nullable=True)
    place_of_study: str = Column(String, nullable=True)
    experience: int = Column(Integer, nullable=True)
    company: str = Column(String, nullable=True)
    post: str = Column(String, nullable=True)
    descriptiion: str = Column(String, nullable=True)
    specialization: str = Column(String, nullable=True)
    stack: list[str] = Column(JSON, nullable=True)

    telegram_id: str = Column(String, nullable=True)
    telegram_username: str = Column(String, nullable=True)
    
    

class Application(base):
    __tablename__ = "appllications"

    id: int = Column(Integer, primary_key=True)
    login: str = Column(String, nullable=False)
    password: str = Column(String, nullable=False)

    name: str = Column(String, nullable=True)
    surname: str = Column(String, nullable=True)
    age: int = Column(Integer, nullable=True)
    city: str = Column(String, nullable=True)
    place_of_study: str = Column(String, nullable=True)
    experience: int = Column(Integer, nullable=True)
    company: str = Column(String, nullable=True)
    post: str = Column(String, nullable=True)
    descriptiion: str = Column(String, nullable=True)
    specialization: str = Column(String, nullable=True)
    stack: list[str] = Column(JSON, nullable=True)

    telegram_id: str = Column(String, nullable=False)
    telegram_username: str = Column(String, nullable=False)
    status: ApplicationStatus = Column(Enum(ApplicationStatus), default=ApplicationStatus.PENDING, nullable=False)