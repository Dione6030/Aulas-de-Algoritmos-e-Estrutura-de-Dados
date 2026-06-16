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

# --------------------------------- Criação de Tabela

sql_tabela = """
    CREATE TABLE IF NOT EXISTS filmes (
    id      SERIAL PRIMARY KEY,
    titulo  VARCHAR(100) NOT NULL,
    genero  VARCHAR(50),
    ano     INTEGER,
    nota    NUMERIC(3,1)
)"""
cursor.execute(sql_tabela)
conexao.commit()
