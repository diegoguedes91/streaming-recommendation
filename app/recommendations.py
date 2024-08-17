import pandas as pd
from sqlalchemy.orm import Session
from app import models

def recommend_films_for_user(db: Session, usuario: models.Usuario):
    # Extrair os dados dos filmes e avaliações
    filmes = db.query(models.Filme).all()
    avaliacoes = db.query(models.Avaliacao).filter_by(usuario_id=usuario.id).all()

    # Converter os dados para DataFrames do Pandas
    filmes_df = pd.DataFrame([{
        'id': filme.id,
        'titulo': filme.titulo,
        'genero': filme.genero,
        'diretor': filme.diretor,
        'atores': filme.atores
    } for filme in filmes])

    avaliacoes_df = pd.DataFrame([{
        'filme_id': avaliacao.filme_id,
        'nota': avaliacao.nota
    } for avaliacao in avaliacoes])

    # Associar avaliações aos filmes
    filmes_avaliados = filmes_df.merge(avaliacoes_df, left_on='id', right_on='filme_id', how='left')

    # Considerar as preferências do usuário
    def calcular_pontuacao(filme):
        pontuacao = 0
        # Considerar gênero
        if filme['genero'] in [f.genero for f in usuario.favoritos]:
            pontuacao += 1
        # Considerar diretor
        if filme['diretor'] in [f.diretor for f in usuario.favoritos]:
            pontuacao += 1
        # Considerar atores
        atores_usuario = [ator for f in usuario.favoritos for ator in f.atores.split(", ")]
        if any(ator in filme['atores'].split(", ") for ator in atores_usuario):
            pontuacao += 1
        # Considerar avaliações
        if pd.notnull(filme['nota']):
            pontuacao += filme['nota']
        return pontuacao

    # Calcular a pontuação para cada filme
    filmes_avaliados['pontuacao'] = filmes_avaliados.apply(calcular_pontuacao, axis=1)

    # Ordenar os filmes pela pontuação e recomendar os melhores
    filmes_recomendados = filmes_avaliados.sort_values(by='pontuacao', ascending=False)

    # Filtrar para recomendar apenas filmes que o usuário ainda não assistiu
    filmes_recomendados = filmes_recomendados[~filmes_recomendados['id'].isin([f.id for f in usuario.favoritos])]

    # Retornar os filmes recomendados
    return filmes_recomendados[['id', 'titulo', 'genero', 'diretor', 'atores']].to_dict(orient='records')
