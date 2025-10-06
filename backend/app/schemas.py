from pydantic import BaseModel

class SurveyBase(BaseModel):
    firstName: str
    lastName: str
    email: str
    address: str
    city: str
    state: str
    zip: str
    telephone: str
    dateOfSurvey: str
    recommendation: str
    interest: str
    likings: str

class SurveyCreate(SurveyBase):
    pass

class Survey(SurveyBase):
    id: int

    class Config:
        orm_mode = True
