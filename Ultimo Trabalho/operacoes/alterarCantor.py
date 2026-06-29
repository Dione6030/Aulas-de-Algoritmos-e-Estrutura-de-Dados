from rich import print
from rich.table import Table
from rich.console import Console

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def alterarCantor():
    cursor.execute("select id, nome from cantor order by nome")
    cantores = cursor.fetchall()
    
    console = Console()
    tabela = Table(title="Cantores")
    
    tabela.add_column("ID", style="yellow", justify="right")
    tabela.add_column("Nome", style="cyan")
    tabela.add_column("Músicas", style="green")

    for cantor in cantores:
        cursor.execute("select nome from musica where cantor_id = %s order by visualizacoes desc", (cantor[0],))
        musicas = cursor.fetchone()
        
        tabela.add_row(
            str(cantor[0]),
            cantor[1],
            musicas[0] if musicas else "Nenhuma"
        )
    
    console.print(tabela)
    
    opcao = int(input("Digite o ID do cantor que deseja alterar: "))
    
    nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
    
    sql= """
        update cantor
        set nome = coalesce(nullif(%s, ''), nome)
        where id = %s
        """
    
    cursor.execute(sql, (nome, opcao))
    conexao.commit()