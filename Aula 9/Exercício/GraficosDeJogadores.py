import csv
import os
import subprocess
import time
import plotly.express as px

jogadores = []

with open("BRA_players.csv", "r", encoding="utf-8") as arq:
    dados = csv.DictReader(arq)
    for linha in dados:
        jogadores.append(linha)

def limpar_tela():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

def titulo(text, traco="-"):
    print()
    print(text.upper())
    print(traco*40)

def top_clubes_valiosos():
    limpar_tela()
    titulo("Top 10 Clubes mais Valiosos")
    
    print("Nº Clube................: Valor (Media)........:")
    
    grupo = {}
    for jogador in jogadores:
        clube = jogador['Team']
        valor = float(jogador['Market Value'])
        media = 0
        
        if clube in grupo:
            

while True:
    titulo("Menu Principal")
    print("1. Top 10 Clubes mais Valiosos")
    print("2. Top 10 Jogadores por Idade")
    print("3. Media de Idade entre dois clubes")
    print("4. Analisar Jogadores por Idade e quais clubes não possue Jogador com essa Idade")
    print("5. Quantidade de Jogadores por Posição (pizza)")
    print("6. Faixa etária dos Jogadores (Coluna)")
    print("7. Numero de Jogadores em cada Idade (Linha)")
    print("0. Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        top_clubes_valiosos()