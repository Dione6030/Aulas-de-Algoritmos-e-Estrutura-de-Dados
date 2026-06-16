import requests

from rich.table import Table
from rich.console import Console

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def listar():
    cursor.execute("select nome, selecao, valor from apostas order by nome")
    apostas = cursor.fetchall()
    
    console = Console()
    tabela = Table(title="Apostas")
    
    tabela.add_column("Nome", style="cyan")
    tabela.add_column("Seleção", style="magenta")
    tabela.add_column("Valor", style="green", justify="right")
    
    for aposta in apostas:
        tabela.add_row(
            aposta[0], 
            aposta[1], 
            f"R$ {aposta[2]:.2f}"
        )
    
    console.print(tabela)