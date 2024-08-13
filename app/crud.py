from sqlalchemy.orm import Session
from app import models, schemas

def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def get_filme(db: Session, filme_id: int):
    return db.query(models.Filme).filter(models.Filme.id == filme_id).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(nome=usuario.nome)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def create_filme(db: Session, filme: schemas.FilmeCreate):
    db_filme = models.Filme(**filme.dict())
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme

def create_avaliacao(db: Session, avaliacao: schemas.AvaliacaoCreate, usuario_id: int, filme_id: int):
    db_avaliacao = models.Avaliacao(**avaliacao.dict(), usuario_id=usuario_id, filme_id=filme_id)
    db.add(db_avaliacao)
    db.commit()
    db.refresh(db_avaliacao)
    return db_avaliacao

def get_filmes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Filme).offset(skip).limit(limit).all()
