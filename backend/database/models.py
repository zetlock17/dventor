from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from database.database import base
from sqlalchemy.orm import relationship
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
    username: str = Column(String, nullable=True)
    telegram_id: str = Column(String, nullable=True)
    telegram_username: str = Column(String, nullable=True)
    specialization: str = Column(String, nullable=True)
    experience: int = Column(Integer, nullable=True)


class AuthorizationMentor(base):
    __tablename__ = "authorization_mentors"

    id: int = Column(Integer, primary_key=True)
    login: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    mentor_id: int = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    mentor = relationship("User")


class Application(base):
    __tablename__ = "appllications"

    id: int = Column(Integer, primary_key=True)
    login: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    username: str = Column(String, nullable=False)
    specialization: str = Column(String, nullable=True)
    experience: int = Column(Integer, nullable=True)
    telegram_id: str = Column(String, nullable=False)
    telegram_username: str = Column(String, nullable=False)
    status: ApplicationStatus = Column(Enum(ApplicationStatus), default=ApplicationStatus.PENDING, nullable=False)