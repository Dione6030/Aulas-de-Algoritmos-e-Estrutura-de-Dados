import requests

from rich import print

from config import API_URL_PLATAFORMA

def alterarPlataforma():
    id = input("ID da plataforma: ")

    consulta = requests.get(f"{API_URL_PLATAFORMA}/{id}")

    if consulta.status_code != 200:
        print("[red]Plataforma não encontrada[/red]")
        return

    selecao = consulta.json()

    print("\n[bold yellow]Alteração[/bold yellow]")

    nome = input(f"Nome [{selecao['nome']}]: ") \
        or selecao["nome"]

    continente = input(
        f"Continente [{selecao['continente']}]: "
    ) or selecao["continente"]

    numCopas = input(
        f"Copas [{selecao['numCopas']}]: "
    )

    destaques = input(
        f"Destaques [{selecao['destaques']}]: "
    ) or selecao["destaques"]

    chance = input(
        f"Chance [{selecao['chanceTitulo']}]: "
    )

    dados = {
        "nome": nome,
        "continente": continente,
        "numCopas": int(numCopas) if numCopas else selecao["numCopas"],
        "destaques": destaques,
        "chanceTitulo": float(chance) if chance else selecao["chanceTitulo"]
    }

    resposta = requests.put(
        f"{API_URL_PLATAFORMA}/{id}",
        json=dados
    )

    if resposta.status_code == 200:
        print("[green]Registro alterado![/green]")
    else:
        print("[red]Erro na alteração[/red]")