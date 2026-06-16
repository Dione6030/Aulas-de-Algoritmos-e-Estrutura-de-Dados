import requests

from rich import print
from rich.table import Table
from rich.console import Console

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def alterar():
    cursor.execute("SELECT * FROM apostas")
    apostas = cursor.fetchall()
    
    console = Console()
    tabela = Table(title="Apostas")
    
    tabela.add_column("ID", style="blue")
    tabela.add_column("Nome", style="cyan")
    tabela.add_column("Seleção", style="magenta")
    tabela.add_column("Valor", style="green", justify="right")
    
    for aposta in apostas:
        tabela.add_row(
            aposta[0], 
            aposta[1], 
            aposta[2],
            f"R$ {aposta[3]:.2f}"
        )
    console.print(tabela)