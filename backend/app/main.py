from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/v1.0/surveys", response_model=schemas.Survey)
def create_survey(survey: schemas.SurveyCreate, db: Session = Depends(get_db)):
    return crud.create_survey(db, survey)

@app.get("/api/v1.0/surveys", response_model=list[schemas.Survey])
def get_all_surveys(db: Session = Depends(get_db)):
    return crud.get_all_surveys(db)

@app.get("/api/v1.0/surveys/{survey_id}", response_model=schemas.Survey)
def get_survey(survey_id: int, db: Session = Depends(get_db)):
    survey = crud.get_survey_by_id(db, survey_id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey

@app.put("/api/v1.0/surveys/{survey_id}", response_model=schemas.Survey)
def update_survey(survey_id: int, updated: schemas.SurveyCreate, db: Session = Depends(get_db)):
    result = crud.update_survey(db, survey_id, updated)
    if not result:
        raise HTTPException(status_code=404, detail="Survey not found")
    return result

@app.delete("/api/v1.0/surveys/{survey_id}")
def delete_survey(survey_id: int, db: Session = Depends(get_db)):
    result = crud.delete_survey(db, survey_id)
    if not result:
        raise HTTPException(status_code=404, detail="Survey not found")
    return {"ok": True}
