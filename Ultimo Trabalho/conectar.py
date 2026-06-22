import psycopg2
import config
conexao = psycopg2.connect(
    host=config.HOST,
    dbname=config.DBNAME,
    user=config.USER,
    password=config.PASSWORD,
    port=config.PORT
)