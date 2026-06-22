from rich import print
from rich.table import Table
from rich.console import Console


import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def incluirCantor():
    print("\n[bold green]Inclusão de Cantor[/bold green]")
    
    nome = input("Nome do cantor: ")
    
    try:
        sql = """
        insert into cantor (nome) 
        values (%s)
        """
        
        cantor = (nome,)
        
        cursor.execute(sql, cantor)
        conexao.commit()
        print("[green]Cantor cadastrado com sucesso![/green]")
    except Exception as e:
        print(f"[red]Erro ao cadastrar cantor: {e}[/red]")
        conexao.rollback()