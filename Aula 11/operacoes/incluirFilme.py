import requests
from rich import print
from config import API_URL_FILME

def incluirFilme():
    print("\n[bold green]Inclusão de Filme[/bold green]")

    nome = input("Nome...............: ")
    genero = input("Gênero.............: ")
    duracao = int(input("Duração (minutos)..: "))
    sinopse = input("Sinopse............: ")
    plataformas_str = input("ID da Plataforma(se mais de uma, colocar separado por vírgulas. Ex: 1,2,3): ")
    plataformas = [int(p.strip()) for p in plataformas_str.split(",")]

    dados = {
        "nome": nome,
        "genero": genero,
        "duracao": duracao,
        "sinopse": sinopse,
        "plataformas": plataformas
    }

    resposta = requests.post(API_URL_FILME, json=dados)

    if resposta.status_code in [200, 201]:
        print("[green]Filme cadastrado com sucesso![/green]")
    else:
        print(f"[red]Erro: {resposta.status_code}[/red]")