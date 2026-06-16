import psycopg2
conexao = psycopg2.connect(
    host="ep-shiny-block-acwws1ke-pooler.sa-east-1.aws.neon.tech",
    dbname="neondb",
    user="neondb_owner",
    password="npg_h2kwujroEi1W",
    port="5432"
)

print("Ok! Conectado com Sucesso")
cursor = conexao.cursor()

sql = """
    INSERT INTO filmes (titulo, genero, ano, nota)
    VALUES (%s, %s, %s, %s)
"""
filme = ("Duna", "Ficção Científica", 2021, 8.6)
filme2 = ("Toy Story 2", "Animação", 1999, 9.0)
filme3 = ("Todo Mundo em Pânico 6", "Comédia", 2026, 5.4)

cursor.execute(sql, filme)
cursor.execute(sql, filme2)
cursor.execute(sql, filme3)
conexao.commit()

print("Ok! 3 filmes inseridos")