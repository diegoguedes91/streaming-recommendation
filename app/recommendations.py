from sqlalchemy.orm import Session
from app import models

def recommend_films_for_user(db: Session, usuario: models.Usuario):
    filmes_recomendados = []
    for filme in db.query(models.Filme).all():
        if filme not in usuario.favoritos:
            filmes_recomendados.append(filme)
    return filmes_recomendados
