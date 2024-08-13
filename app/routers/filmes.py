from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db
from typing import List

router = APIRouter()

@router.get("/filmes/", response_model=List[schemas.Filme])
def read_filmes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    filmes = crud.get_filmes(db, skip=skip, limit=limit)
    return filmes
