import requests
from rich import print

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def incluiraposta():
    print("\n[bold green]Inclusão de Aposta[/bold green]")
    
    nome = input("Nome do apostador: ")
    selecao = input("Seleção apostada: ")
    valor = float(input("Valor da aposta: "))
    
    if valor < 10:
        print("[bold red]Valor mínimo para aposta é R$ 10,00[/bold red]")
        return
    
    try:
        sql = """
        insert into apostas (nome, selecao, valor) 
        values (%s, %s, %s)
        """
        
        aposta = (nome, selecao, valor)
        
        cursor.execute(sql, aposta)
        conexao.commit()
        print("[green]Aposta cadastrada com sucesso![/green]")
    except Exception as e:
        print(f"[red]Erro ao cadastrar aposta: {e}[/red]")
        conexao.rollback()