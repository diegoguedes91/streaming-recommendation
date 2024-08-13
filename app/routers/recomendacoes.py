from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, recommendations
from app.database import get_db
from typing import List

router = APIRouter()

@router.get("/filmes/{usuario_id}/recomendacoes", response_model=List[schemas.Filme])
def read_recommendations(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud.get_usuario(db, usuario_id=usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    recomendacoes = recommendations.recommend_films_for_user(db, usuario)
    return recomendacoes
