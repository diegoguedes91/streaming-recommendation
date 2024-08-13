from pydantic import BaseModel
from typing import List, Optional

class AvaliacaoBase(BaseModel):
    nota: float

class AvaliacaoCreate(AvaliacaoBase):
    pass

class Avaliacao(AvaliacaoBase):
    id: int
    usuario_id: int
    filme_id: int

    class Config:
        orm_mode = True

class FilmeBase(BaseModel):
    titulo: str
    genero: str
    diretor: str
    atores: str

class FilmeCreate(FilmeBase):
    pass

class Filme(FilmeBase):
    id: int
    avaliacoes: List[Avaliacao] = []

    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    nome: str

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    favoritos: List[Filme] = []
    avaliacoes: List[Avaliacao] = []

    class Config:
        orm_mode = True
