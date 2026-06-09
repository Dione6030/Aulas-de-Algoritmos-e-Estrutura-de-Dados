from rich.console import Console
from rich.panel import Panel
import os

from operacoes.incluirPlataforma import incluirPlataforma
from operacoes.incluirFilme import incluirFilme
from operacoes.listar import listar
from operacoes.alterarPlataforma import alterarPlataforma
from operacoes.alterarFilme import alterarFilme
from operacoes.excluirPlataforma import excluirPlataforma
from operacoes.excluirFilme import excluirFilme
from operacoes.pesquisar import pesquisar

console = Console()

menu = ("""
1. Incluir Plataforma
2. Incluir Filme
3. Listar Filmes
4. Pesquisar por ID
5. Alterar Plataforma
6. Alterar Filme
7. Excluir Plataforma
8. Excluir Filme
9. Finalizar
""")

while True:
    #console.clear()
    os.system("cls")
    console.print(Panel.fit(menu, title="Menu Principal"))

    opcao = int(input("Opção: "))

    if opcao == 1:
        incluirPlataforma()
    elif opcao == 2:
        incluirFilme()
    elif opcao == 3:
        listar()
    elif opcao == 4:
        pesquisar()
    elif opcao == 5:
        alterarPlataforma()
    elif opcao == 6:
        alterarFilme()
    elif opcao == 7:
        excluirPlataforma()
    elif opcao == 8:
        excluirFilme()
    elif opcao == 9:
        console.print("[bold cyan]Fim do Programa[/bold cyan]")
        break
    else:
        console.print("[bold red]Opção inválida[/bold red]")

    input("\nPressione Enter para continuar...")