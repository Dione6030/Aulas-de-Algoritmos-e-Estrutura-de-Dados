from rich.console import Console
from rich.panel import Panel
import os

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

sql_tabela = """
    CREATE TABLE IF NOT EXISTS apostas (
    id       SERIAL PRIMARY KEY,
    nome     VARCHAR(100) NOT NULL,
    selecao  VARCHAR(50),
    valor    NUMERIC(10,2) check (valor >= 10.00)
)"""
cursor.execute(sql_tabela)
conexao.commit()

from operacoes.incluiraposta import incluiraposta
from operacoes.listar import listar
from operacoes.alterar import alterar
from operacoes.excluir import excluir
from operacoes.simulacao import simulacao

console = Console()

menu = ("""
1. Incluir Aposta
2. Listar Apostas
3. Alterar Apostas
4. Excluir Aposta
5. Simular Apostas
6. Finalizar
""")

while True:
    #console.clear()
    os.system("cls")
    console.print(Panel.fit(menu, title="Menu Principal"))

    opcao = int(input("Opção: "))

    if opcao == 1:
        incluiraposta()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        alterar()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        simulacao()
    elif opcao == 6:
        console.print("[bold cyan]Fim do Programa[/bold cyan]")
        break
    else:
        console.print("[bold red]Opção inválida[/bold red]")

    input("\nPressione Enter para continuar...")