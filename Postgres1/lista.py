import psycopg2
from psycopg2.extras import RealDictCursor
conexao = psycopg2.connect(
    host="ep-shiny-block-acwws1ke-pooler.sa-east-1.aws.neon.tech",
    dbname="neondb",
    user="neondb_owner",
    password="npg_h2kwujroEi1W",
    port="5432"
)

print("Ok! Conectado com Sucesso")

cursor = conexao.cursor(cursor_factory=RealDictCursor)

cursor.execute("SELECT * FROM filmes")
filmes = cursor.fetchall()
for filme in filmes:
    print(filme)
    print(filme["titulo"], "-", filme["ano"])