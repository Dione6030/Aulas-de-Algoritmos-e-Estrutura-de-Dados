import requests

from rich.console import Console
from rich.panel import Panel

from config import API_URL_FILME

def pesquisar():
    id = input("ID do filme: ")

    resposta_filme = requests.get(f"{API_URL_FILME}/{id}")

    if resposta_filme.status_code != 200:
        print("Filme não encontrado")
        return

    selecao = resposta_filme.json()
    console = Console()

    texto = (
        f"Nome: {selecao['nome']}\n"
        f"Continente: {selecao['continente']}\n"
        f"Copas: {selecao['numCopas']}\n"
        f"Destaques: {selecao['destaques']}\n"
        f"Chance de Título: {selecao['chanceTitulo']}%"
    )

    console.print(
        Panel(texto, title="Dados da Seleção")
    )