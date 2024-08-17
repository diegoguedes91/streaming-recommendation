# Sistema de Recomendação de Filmes

## Descrição
Este projeto implementa um sistema de recomendação de filmes para uma plataforma de streaming, usando FastAPI e SQLite.

## Endpoints
- **/filmes/**: Retorna uma lista de todos os filmes disponíveis.
  - **Método**: GET
  - **Resposta**: Lista de filmes com detalhes como título, gênero, diretor e atores.
  
- **/filmes/{usuario_id}/recomendacoes**: Retorna recomendações de filmes personalizadas para o usuário.
  - **Método**: GET
  - **Parâmetros de URL**: `usuario_id` (ID do usuário para o qual as recomendações são solicitadas)
  - **Resposta**: Lista de filmes recomendados com base nas preferências e avaliações do usuário.

## Como Executar
1. Clone o repositório
2. Navegue para o diretório do projeto
3. Instale as dependências com `pip install -r requirements.txt`.
4. Execute a aplicação com `uvicorn app.main:app --reload`.
5. Acesse `http://127.0.0.1:8000/docs` para visualizar a documentação Swagger.

## Requisitos
- Python 3.8+
- FastAPI
- SQLAlchemy
- SQLite
- Pandas
