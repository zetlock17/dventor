from sqlalchemy import Column, ForeignKey, Integer, String
from database.database import base
from sqlalchemy.orm import relationship

class Mentor(base):
    __tablename__ = "mentors"

    id: int = Column(Integer, primary_key=True, auto_increment=True)
    username: str = Column(String, nullable=False)
    specialization: str = Column(String, nullable=True)
    experience: int = Column(Integer, nullable=True)


class AuthorizationMentor(base):
    __tablename__ = "authorization_mentors"

    id: int = Column(Integer, primary_key=True, auto_increment=True)
    login: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    mentor_id: int = Column(ForeignKey("mentors.id", ondelete="CASCADE"), nullable=False)

    mentor = relationship("Mentor")

    