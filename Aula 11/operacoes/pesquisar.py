import requests

from rich.console import Console
from rich.panel import Panel

from config import API_URL_FILME, API_URL_PLATAFORMA

def pesquisar():
    id = input("ID do filme: ")

    resposta_filme = requests.get(f"{API_URL_FILME}/{id}")
    resposta_plataformas = requests.get(API_URL_PLATAFORMA)

    if resposta_filme.status_code != 200:
        print("Filme não encontrado")
        return

    filme = resposta_filme.json()
    plataformas = resposta_plataformas.json()
    console = Console()

    texto = (
        f"Nome: {filme['nome']}\n"
        f"Gênero: {filme['genero']}\n"
        f"Duração: {filme['duracao']} minutos\n"
        f"Sinopse: {filme['sinopse']}\n"
        f"Chance de Título: {filme['chanceTitulo']}%"
    )

    console.print(
        Panel(texto, title="Dados da Seleção")
    )