import requests
from rich import print
from config import API_URL_PLATAFORMA

def incluirPlataforma():
    print("\n[bold green]Inclusão de Plataforma[/bold green]")

    nome = input("Nome...............: ")
    mensalidade = float(input("Mensalidade em R$..: "))

    dados = {
        "nome": nome,
        "mensalidade": mensalidade
    }

    resposta = requests.post(API_URL_PLATAFORMA, json=dados)

    if resposta.status_code in [200, 201]:
        print("[green]Plataforma cadastrada com sucesso![/green]")
    else:
        print(f"[red]Erro: {resposta.status_code}[/red]")