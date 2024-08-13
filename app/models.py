from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    favoritos = relationship("Filme", secondary="favoritos", back_populates="favoritado_por")
    avaliacoes = relationship("Avaliacao", back_populates="usuario")

class Filme(Base):
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    genero = Column(String, index=True)
    diretor = Column(String, index=True)
    atores = Column(String, index=True)
    favoritado_por = relationship("Usuario", secondary="favoritos", back_populates="favoritos")
    avaliacoes = relationship("Avaliacao", back_populates="filme")

class Avaliacao(Base):
    __tablename__ = "avaliacoes"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    filme_id = Column(Integer, ForeignKey("filmes.id"))
    nota = Column(Float)
    usuario = relationship("Usuario", back_populates="avaliacoes")
    filme = relationship("Filme", back_populates="avaliacoes")

favoritos = Table(
    "favoritos",
    Base.metadata,
    Column("usuario_id", ForeignKey("usuarios.id"), primary_key=True),
    Column("filme_id", ForeignKey("filmes.id"), primary_key=True),
)
