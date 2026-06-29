import plotly.express as px
import pandas as pd

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def gerarGrafico():
    sql = """
        select c.nome as cantor, count(m.id) as quantidade_musicas
        from cantor c
        left join musica m on c.id = m.cantor_id
        group by c.nome
        order by quantidade_musicas desc
    """

    dataframe = pd.read_sql_query(sql, conexao)

    fig = px.pie(
        dataframe,
        names='cantor',
        values='quantidade_musicas',
        title='Quantidade de Músicas por Cantor'
    )

    fig.show()