import requests

from rich import print

from config import API_URL_FILME

def excluirFilme():
    id = input("ID do filme: ")

    resposta = requests.delete(f"{API_URL_FILME}/{id}")

    if resposta.status_code in [200, 204]:
        print("[green]Registro excluído![/green]")
    else:
        print("[red]Erro ao excluir[/red]")