import json

import psycopg2
from conectar import conexao
cursor = conexao.cursor()


def gerarJSON():
    # Consulta SQL para obter os dados das músicas e cantores
    sql = """
        SELECT m.id, m.nome, c.nome AS cantor_nome, m.visualizacoes, m.img_link
        FROM musica m
        JOIN cantor c ON m.cantor_id = c.id
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()

    # Estrutura de dados para armazenar os resultados
    musicas = []
    for row in resultados:
        musica = {
            "id": row[0],
            "nome": row[1],
            "cantor": row[2],
            "visualizacoes": float(row[3]) if row[3] is not None else 0.0,
            "img_link": row[4]
        }
        musicas.append(musica)

    # Gerar o arquivo JSON
    with open("musicas.json", "w", encoding="utf-8") as json_file:
        json.dump(musicas, json_file, ensure_ascii=False, indent=4)

    print("Arquivo JSON gerado com sucesso!")