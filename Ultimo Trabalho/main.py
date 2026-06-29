from rich.console import Console
from rich.panel import Panel
import os

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

sql_tabela1 = """
    CREATE TABLE IF NOT EXISTS cantor (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL
    )
"""

sql_tabela2 = """
    CREATE TABLE IF NOT EXISTS musica (
    id              SERIAL PRIMARY KEY,
    nome            VARCHAR(100) NOT NULL,
    cantor_id       INTEGER NOT NULL REFERENCES cantor(id),
    visualizacoes   DECIMAL(10,2),
    img_link        VARCHAR(200)
)"""
cursor.execute(sql_tabela1)
cursor.execute(sql_tabela2)
conexao.commit()

from operacoes.incluirMusica import incluirMusica
from operacoes.incluirCantor import incluirCantor
from operacoes.listarMusicas import listarMusicas
from operacoes.listarCantores import listarCantores
from operacoes.alterarMusica import alterarMusica
from operacoes.alterarCantor import alterarCantor
from operacoes.excluirMusica import excluirMusica
from operacoes.excluirCantor import excluirCantor
from operacoes.pesquisar import pesquisarMusica
from operacoes.grafico import gerarGrafico
from operacoes.gerarJSON import gerarJSON
from operacoes.geraHTML import gerarHTML

console = Console()

menu = ("""
1. Incluir Música
2. Incluir Cantor
3. Listar Músicas
4. Listar Cantores
5. Alterar Música
6. Alterar Cantor
7. Excluir Música
8. Excluir Cantor
9. Pesquisar Música
10. Finalizar
11. Gerar Gráfico de Quantidade de Músicas por Cantor
12. Gerar JSON com as Músicas e Cantores
13. Gerar Arquivo HTML com as Músicas e Cantores
""")

while True:
    #console.clear()
    os.system("cls")
    console.print(Panel.fit(menu, title="Menu Principal"))

    opcao = int(input("Opção: "))

    if opcao == 1:
        incluirMusica()
    elif opcao == 2:
        incluirCantor()
    elif opcao == 3:
        listarMusicas()
    elif opcao == 4:
        listarCantores()
    elif opcao == 5:
        alterarMusica()
    elif opcao == 6:
        alterarCantor()
    elif opcao == 7:
        excluirMusica()
    elif opcao == 8:
        excluirCantor()
    elif opcao == 9:
        pesquisarMusica()
    elif opcao == 10:
        console.print("[bold cyan]Fim do Programa[/bold cyan]")
        break
    elif opcao == 11:
        gerarGrafico()
    elif opcao == 12:
        gerarJSON()
    elif opcao == 13:
        gerarHTML()
    else:
        console.print("[bold red]Opção inválida[/bold red]")

    input("\nPressione Enter para continuar...")