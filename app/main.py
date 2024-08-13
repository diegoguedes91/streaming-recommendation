from fastapi import FastAPI
from app.routers import filmes, recomendacoes
from app.database import engine, Base

# Inicializa o banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclui os routers
app.include_router(filmes.router)
app.include_router(recomendacoes.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à plataforma de streaming!"}
