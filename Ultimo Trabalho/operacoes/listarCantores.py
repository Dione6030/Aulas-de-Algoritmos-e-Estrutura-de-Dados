from rich.table import Table
from rich.console import Console

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def listarCantores():
    cursor.execute("select id, nome from cantor order by nome")
    cantores = cursor.fetchall()
    
    console = Console()
    tabela = Table(title="Cantores")
    
    tabela.add_column("Nome", style="cyan")
    tabela.add_column("Músicas", style="green")

    for cantor in cantores:
        cursor.execute("select nome from musica where cantor_id = %s", (cantor[0],))
        musicas = cursor.fetchone()
        
        tabela.add_row(
            cantor[1],
            musicas[0] if musicas else "Nenhuma"
        )
    
    console.print(tabela)