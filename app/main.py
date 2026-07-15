from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Weather App Backend",
    description="Technical assessment backend: CRUD + weather API integration",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/about")
def about():
    return {
        "developer": "Jawaria Hassan",
        "pm_accelerator_description": (
            "The Product Manager Accelerator Program is designed to support PM professionals "
            "through every stage of their careers. From students looking for entry-level jobs "
            "to Directors looking to take on a leadership role, our program has helped over "
            "hundreds of students fulfill their career aspirations. Our Product Manager "
            "Accelerator community are ambitious and committed. Through our program they have "
            "learnt, honed and developed new PM and leadership skills, giving them a strong "
            "foundation for their future endeavors. Learn more at https://www.pmaccelerator.io/"
        ),
    }


@app.post("/searches", response_model=schemas.SearchResponse, status_code=201)
def create_search(payload: schemas.SearchCreate, db: Session = Depends(get_db)):
    return crud.create_search(db, payload.location_query)


@app.get("/searches", response_model=list[schemas.SearchResponse])
def list_searches(db: Session = Depends(get_db)):
    return crud.get_all_searches(db)


@app.get("/searches/{search_id}", response_model=schemas.SearchResponse)
def read_search(search_id: int, db: Session = Depends(get_db)):
    result = crud.get_search(db, search_id)
    if not result:
        raise HTTPException(status_code=404, detail=f"No search found with id {search_id}")
    return result


@app.put("/searches/{search_id}", response_model=schemas.SearchResponse)
def update_search(search_id: int, payload: schemas.SearchUpdate, db: Session = Depends(get_db)):
    result = crud.update_search(db, search_id, payload.location_query)
    if not result:
        raise HTTPException(status_code=404, detail=f"No search found with id {search_id}")
    return result


@app.delete("/searches/{search_id}", status_code=204)
def delete_search(search_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_search(db, search_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"No search found with id {search_id}")
    return None