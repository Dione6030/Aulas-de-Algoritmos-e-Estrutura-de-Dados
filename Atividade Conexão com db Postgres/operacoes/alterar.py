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
            str(aposta[0]), 
            aposta[1], 
            aposta[2],
            f"R$ {aposta[3]:.2f}"
        )
    console.print(tabela)
    
    opcao = int(input("Digite o ID da aposta que deseja alterar: "))
    
    nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
    selecao = input("Digite a nova seleção (ou pressione Enter para manter a atual): ")
    valor_texto = input("Digite o novo valor (ou pressione Enter para manter o atual): ")
    
    if valor_texto.strip() == "":
        valor = None
    else:
        valor = float(valor_texto)
        if valor < 10.00:
            print("[red]Valor deve ser no mínimo R$ 10.00[/red]")
            return
    
    sql= """
        update apostas
        set nome = coalesce(nullif(%s, ''), nome),
            selecao = coalesce(nullif(%s, ''), selecao),
            valor = coalesce(%s, valor)
        where id = %s
        """
    
    cursor.execute(sql, (nome, selecao, valor, opcao))
    conexao.commit()