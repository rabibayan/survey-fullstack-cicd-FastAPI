from sqlalchemy import Column, Integer, String
from .database import Base

class Survey(Base):
    __tablename__ = "survey"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(255))
    city = Column(String(255))
    dateOfSurvey = Column("date_of_survey", String(255))
    email = Column(String(255))
    firstName = Column("first_name", String(255))
    interest = Column(String(255))
    lastName = Column("last_name", String(255))
    likings = Column(String(255))
    recommendation = Column(String(255))
    state = Column(String(255))
    telephone = Column(String(255))
    zip = Column(String(255))
