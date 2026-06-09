import requests

from rich.table import Table
from rich.console import Console

from config import API_URL_FILME, API_URL_PLATAFORMA

def listar():
    resposta_filmes = requests.get(API_URL_FILME)
    resposta_plataformas = requests.get(API_URL_PLATAFORMA)

    if resposta_filmes.status_code != 200:
        print("Erro ao consultar API")
        return

    filmes = resposta_filmes.json()     # Converte em uma lista de dicionários
    plataformas = resposta_plataformas.json()  # Converte em uma lista de dicionários

    mapa_plataformas = {plataforma["id"]: plataforma["nome"] for plataforma in plataformas}

    tabela = Table(title="Filmes Cadastrados")

    tabela.add_column("ID")
    tabela.add_column("Nome")
    tabela.add_column("Gênero")
    tabela.add_column("Duração")
    tabela.add_column("Sinopse")
    tabela.add_column("Plataformas")

    for item in filmes:
        nomes_plataformas = [mapa_plataformas.get(num, f"ID {num}") for num in item["plataformas"]]
        
        tabela.add_row(
            str(item["id"]),
            item["nome"],
            item["genero"],
            str(item["duracao"]),
            item["sinopse"],
            ", ".join(nomes_plataformas)
        )

    console = Console()
    console.print(tabela)