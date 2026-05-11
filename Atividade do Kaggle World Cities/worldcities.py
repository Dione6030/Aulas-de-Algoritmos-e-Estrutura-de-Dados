import csv
import os
import subprocess
import time

cidades = []

with open("worldcities.csv", "r", encoding="utf-8") as arq:
    dados = csv.DictReader(arq)
    for linha in dados:
        cidades.append(linha)

def limpar_tela():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

def titulo(text, traco="-"):
    print()
    print(text.upper())
    print(traco*40)

def top20_cidades_populosas():
    limpar_tela()
    titulo("As 20 Cidades mais Populosas")
    
    print("N. Cidades.......................: Países.............: População:")
    
    grupos = {}
    
    for linha in cidades:
        cidade = linha['city']
        pais = linha['country']
        populacao = linha['population']

while True:
    titulo("Menu Principal")
    print("1. As 20 Cidades mais Populosas")
    print("2. As 10 Cidades mais Populosas de Algum País")
    print("3. Top 10 Países com mais Cidades")
    print("4. Quantos Países estão representados")
    print("5. Mostra todos os estados de algum País")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        top20_cidades_populosas()