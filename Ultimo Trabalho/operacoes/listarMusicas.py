from rich.table import Table
from rich.console import Console

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def listarMusicas():
    cursor.execute("select nome, cantor_id, visualizacoes from musica order by nome")
    musicas = cursor.fetchall()
    
    console = Console()
    tabela = Table(title="Músicas")
    
    tabela.add_column("Nome", style="cyan")
    tabela.add_column("Cantor", style="magenta")
    tabela.add_column("Visualizações", style="green", justify="right")
    
    for musica in musicas:
        cursor.execute("select c.nome from cantor c where c.id = %s", (musica[1],))
        cantor = cursor.fetchone()
        tabela.add_row(
            musica[0], 
            cantor[0], 
            f"R$ {musica[2]:,}".replace(",", ".")
        )
    
    console.print(tabela)