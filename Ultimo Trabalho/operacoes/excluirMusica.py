from rich import print
from rich.table import Table
from rich.console import Console

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def excluirMusica():
    cursor.execute("SELECT id, nome, cantor_id FROM musica")
    musicas = cursor.fetchall()
    
    console = Console()
    tabela = Table(title="Músicas")
    
    tabela.add_column("ID", style="blue")
    tabela.add_column("Nome", style="cyan")
    tabela.add_column("Cantor", style="magenta")
    
    for musica in musicas:
        cursor.execute("SELECT nome FROM cantor WHERE id = %s", (musica[2],))
        cantor = cursor.fetchone()
        tabela.add_row(
            str(musica[0]), 
            musica[1], 
            cantor[0]
        )
    console.print(tabela)
    
    opcao = int(input("Digite o ID da música que deseja excluir: "))
    
    sql = "DELETE FROM musica WHERE id = %s"
    
    cursor.execute(sql, (opcao,))
    conexao.commit()
    
    print(f"[green]Música excluída com sucesso![/green]")