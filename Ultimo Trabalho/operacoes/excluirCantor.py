from rich import print
from rich.table import Table
from rich.console import Console

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def excluirCantor():
    cursor.execute("SELECT id, nome FROM cantor")
    cantores = cursor.fetchall()

    console = Console()
    tabela = Table(title="Cantores")

    tabela.add_column("ID", style="blue")
    tabela.add_column("Nome", style="cyan")

    for cantor in cantores:
        tabela.add_row(str(cantor[0]), cantor[1])

    console.print(tabela)

    opcao = int(input("Digite o ID do cantor que deseja excluir: "))

    sql = "DELETE FROM cantor WHERE id = %s"

    cursor.execute(sql, (opcao,))
    conexao.commit()

    print(f"[green]Cantor excluído com sucesso![/green]")