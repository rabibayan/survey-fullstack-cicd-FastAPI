from sqlalchemy.orm import Session
from . import models, schemas

def create_survey(db: Session, survey: schemas.SurveyCreate):
    db_survey = models.Survey(**survey.dict())
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

def get_all_surveys(db: Session):
    return db.query(models.Survey).all()

def get_survey_by_id(db: Session, survey_id: int):
    return db.query(models.Survey).filter(models.Survey.id == survey_id).first()

def update_survey(db: Session, survey_id: int, survey_data: schemas.SurveyCreate):
    db_survey = get_survey_by_id(db, survey_id)
    if not db_survey:
        return None
    for field, value in survey_data.dict().items():
        setattr(db_survey, field, value)
    db.commit()
    db.refresh(db_survey)
    return db_survey

def delete_survey(db: Session, survey_id: int):
    db_survey = get_survey_by_id(db, survey_id)
    if db_survey:
        db.delete(db_survey)
        db.commit()
    return db_survey
