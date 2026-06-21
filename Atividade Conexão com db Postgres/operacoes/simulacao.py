from random import choice

from rich import print
from rich.table import Table
from rich.console import Console

from conectar import conexao

cursor = conexao.cursor()

def simulacao():
    cursor.execute("SELECT nome, selecao, valor FROM apostas")
    apostas = cursor.fetchall()

    if not apostas:
        print("[yellow]Não há apostas cadastradas para simulação.[/yellow]")
        return

    console = Console()

    totais_por_selecao = {}
    apostas_por_selecao = {}

    for nome, selecao, valor in apostas:
        valor = float(valor)

        totais_por_selecao[selecao] = totais_por_selecao.get(selecao, 0) + valor
        apostas_por_selecao.setdefault(selecao, []).append((nome, valor))

    selecao_vencedora = choice(list(totais_por_selecao.keys()))

    total_apostado = sum(float(aposta[2]) for aposta in apostas)
    taxa_casa = round(total_apostado * 0.10, 2)
    premio_distribuivel = round(total_apostado - taxa_casa, 2)

    total_na_selecao_vencedora = totais_por_selecao[selecao_vencedora]
    vencedores = apostas_por_selecao[selecao_vencedora]

    tabela_resumo = Table(title="Resumo das Seleções")
    tabela_resumo.add_column("Seleção", style="cyan")
    tabela_resumo.add_column("Total Apostado", style="green", justify="right")

    for selecao, total in totais_por_selecao.items():
        tabela_resumo.add_row(selecao, f"R$ {total:.2f}")

    console.print(tabela_resumo)

    tabela_final = Table(title="Resultado da Simulação")
    tabela_final.add_column("Time Vencedor", style="cyan")
    tabela_final.add_column("Total Apostado", style="green", justify="right")
    tabela_final.add_column("Casa", style="red", justify="right")
    tabela_final.add_column("Distribuído aos Apostadores", style="magenta", justify="right")

    tabela_final.add_row(
        selecao_vencedora,
        f"R$ {total_apostado:.2f}",
        f"R$ {taxa_casa:.2f}",
        f"R$ {premio_distribuivel:.2f}"
    )

    console.print(tabela_final)

    tabela_premios = Table(title=f"Rateio da Seleção Vencedora: {selecao_vencedora}")
    tabela_premios.add_column("Nome", style="cyan")
    tabela_premios.add_column("Apostado", style="green", justify="right")
    tabela_premios.add_column("Ganhou", style="yellow", justify="right")

    acumulado = 0.0

    for indice, (nome, valor_apostado) in enumerate(vencedores):
        if indice == len(vencedores) - 1:
            valor_ganho = round(premio_distribuivel - acumulado, 2)
        else:
            valor_ganho = round((valor_apostado / total_na_selecao_vencedora) * premio_distribuivel, 2)
            acumulado += valor_ganho

        tabela_premios.add_row(
            nome,
            f"R$ {valor_apostado:.2f}",
            f"R$ {valor_ganho:.2f}"
        )

    console.print(tabela_premios)