import requests

from rich import print

from config import API_URL_PLATAFORMA

def excluirPlataforma():
    id = input("ID da plataforma: ")

    resposta = requests.delete(f"{API_URL_PLATAFORMA}/{id}")

    if resposta.status_code in [200, 204]:
        print("[green]Registro excluído![/green]")
    else:
        print("[red]Erro ao excluir[/red]")