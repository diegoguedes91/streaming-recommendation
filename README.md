# Sistema de Recomendação de Filmes

## Descrição
Este projeto implementa um sistema de recomendação de filmes para uma plataforma de streaming, usando FastAPI e SQLite.

## Endpoints
- **/filmes/**: Retorna uma lista de todos os filmes disponíveis.
- **/filmes/{usuario_id}/recomendacoes**: Retorna recomendações de filmes personalizadas para o usuário.

## Como Executar
1. Instale as dependências com `pip install -r requirements.txt`.
2. Execute a aplicação com `uvicorn app.main:app --reload`.
3. Acesse `http://127.0.0.1:8000/docs` para visualizar a documentação Swagger.

## Requisitos
- Python 3.8+
- FastAPI
- SQLAlchemy
- SQLite
